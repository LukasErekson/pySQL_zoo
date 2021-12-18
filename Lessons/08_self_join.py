import sqlite3
import pandas as pd

def main():
    """Runs and prints the results of the queries required a given SQL Zoo
    lesson.
    """
    try:
        conn = sqlite3.connect('databases/self_join.db')
        cur = conn.cursor()

        # Problem 1
        print(f"Problem 1:\n{prob1(cur)}\n")

        # Problem 2
        print(f"Problem 2:\n{prob2(cur)}\n")

        # Problem 3
        print(f"Problem 3:\n{prob3(cur)}\n")

        # Problem 4
        print(f"Problem 4:\n{prob4(cur)}\n")

        # Problem 5
        print(f"Problem 5:\n{prob5(cur)}\n")

        # Problem 6
        print(f"Problem 6:\n{prob6(cur)}\n")

        # Problem 7
        print(f"Problem 7:\n{prob7(cur)}\n")

        # Problem 8
        print(f"Problem 8:\n{prob8(cur)}\n")

        # Problem 9
        print(f"Problem 9:\n{prob9(cur)}\n")

        # Problem 10
        print(f"Problem 10:\n{prob10(cur)}\n")

    finally:
        conn.close()

def prob1(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List how many stops are in the database.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("SELECT COUNT(*) FROM stops;")

    return pd.DataFrame(cur.fetchall())

def prob2(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Find the id value for the stop 'Craiglockhart.'
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT stops.id 
                FROM stops
                WHERE stops.name = 'Craiglockhart';
                """)

    return pd.DataFrame(cur.fetchall())

def prob3(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Give the id and the name for the stops on the '4' 'LRT' service.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT stops.id, stops.name
                FROM route 
                JOIN stops ON stops.id = route.stop
                WHERE route.num = 4 AND route.company = 'LRT';""")

    return pd.DataFrame(cur.fetchall())

def prob4(cur: sqlite3.Cursor) -> pd.DataFrame:
    """The query given gives the number of routes that visit either London Road
    (149) or Craiglockhart (53). Run the query and notice the two services that
    link these stops have a count of 2. Add a HAVING clause to restrict the
    output to these two routes.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT company, num, COUNT(*)
                FROM route 
                WHERE stop=149 OR stop=53
                GROUP BY company, num HAVING COUNT(*) = 2;
                """)

    return pd.DataFrame(cur.fetchall())

def prob5(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Execute the self join shown and observe that b.stop gives all the places
    you can get to from Craiglockhart, without changing routes. Change the
    query so that it shows the services from Craiglockhart to London Road.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT a.company, a.num, a.stop, b.stop
                FROM route a 
                JOIN route b ON (a.company=b.company AND a.num=b.num)
                WHERE a.stop=53
                AND b.stop = (SELECT id FROM stops WHERE name = 'London Road');
                """)

    return pd.DataFrame(cur.fetchall())

def prob6(cur: sqlite3.Cursor) -> pd.DataFrame:
    """The query given is similar to the previous one, however by joining two
    copies of the stops table we can refer to stops by name rather than by
    number. Change the query so that the services between 'Craiglockhart' and
    'London Road' are shown. If you are tired of these places try
    'Fairmilehead' against 'Tollcross'
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT a.company, a.num, stopa.name, stopb.name
                FROM route a 
                JOIN route b ON (a.company=b.company AND a.num=b.num)
                JOIN stops stopa ON (a.stop=stopa.id)
                JOIN stops stopb ON (b.stop=stopb.id)
                WHERE stopa.name='Craiglockhart' AND stopb.name='London Road';
                """)

    return pd.DataFrame(cur.fetchall())

def prob7(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Give a list of all the services which connect stops 115 and 137
    ('Haymarket' and 'Leith').
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT DISTINCT r1.company, r1.num
                FROM route AS r1 
                JOIN route AS r2 ON (r1.company = r2.company AND r1.num = r2.num)
                WHERE r1.stop = 115 AND r2.stop = 137;
                """)

    return pd.DataFrame(cur.fetchall())

def prob8(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Give a list of the services which connect the stops 'Craiglockhart' and
    'Tollcross'.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT DISTINCT r1.company, r1.num
                FROM route AS r1 
                JOIN route AS r2 ON (r1.company = r2.company AND r1.num = r2.num)
                JOIN stops AS stops1 ON stops1.id = r1.stop
                JOIN stops as stops2 ON stops2.id = r2.stop
                WHERE stops1.name = 'Craiglockhart'
                AND stops2.name = 'Tollcross';
                """)

    return pd.DataFrame(cur.fetchall())

def prob9(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Give a distinct list of the stops which may be reached from
    'Craiglockhart' by taking one bus, including 'Craiglockhart' itself,
    offered by the LRT company. Include the company and bus no. of the relevant
    services.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT DISTINCT stops1.name, r1.company, r1.num
                FROM route AS r1 
                JOIN route AS r2 ON (r1.company = r2.company AND r1.num = r2.num)
                JOIN stops AS stops1 ON (stops1.id = r1.stop)
                JOIN stops AS stops2 ON (stops2.id = r2.stop)
                WHERE r1.company = 'LRT' AND stops2.name = 'Craiglockhart'
                ORDER BY r1.num, stops1.name;
                """)

    return pd.DataFrame(cur.fetchall())

def prob10(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Find the routes involving two buses that can go from Craiglockhart to
    Lochend. Show the bus no. and company for the first bus, the name of the
    stop for the transfer, and the bus no. and company for the second bus.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT DISTINCT r1.num, r1.company, stops2.name, r4.num, r4.company
                FROM route AS r1 
                JOIN route AS r2 ON (r1.company = r2.company AND r1.num = r2.num)
                JOIN stops AS stops1 ON (stops1.id = r1.stop)
                JOIN stops AS stops2 ON (stops2.id = r2.stop)
                JOIN route AS r3 ON (r3.stop = stops2.id)
                JOIN route AS r4 ON (r3.company = r4.company AND r3.num = r4.num)
                JOIN stops AS stops3 ON (stops3.id = r3.stop)
                JOIN stops AS stops4 ON (stops4.id = r4.stop)
                WHERE stops1.name = 'Craiglockhart'
                AND stops4.name = 'Lochend'
                ORDER BY LENGTH(r1.num), r1.num, LENGTH(r3.num), r3.num, stops2.name;
                """)

    return pd.DataFrame(cur.fetchall())


if __name__ == "__main__":
    main()