import sqlite3
import pandas as pd

def main():
    """Runs and prints the results of the queries required a given SQL Zoo
    lesson.
    """
    try:
        conn = sqlite3.connect('databases/world.db')
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

    finally:
        conn.close()

def prob1(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the total population of the world.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT SUM(population)
                FROM world;""")

    return pd.DataFrame(cur.fetchall(), columns=['SUM(population)'])

def prob2(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List all the continents - just once each.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT DISTINCT continent
                FROM world;""")

    return pd.DataFrame(cur.fetchall(), columns=['continent'])

def prob3(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Give the total GDP of Africa.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT SUM(gdp)
                FROM world 
                WHERE continent = 'Africa';""")

    return pd.DataFrame(cur.fetchall(), columns=['SUM(gdp)'])

def prob4(cur: sqlite3.Cursor) -> pd.DataFrame:
    """How many countries have an area of at least 1000000.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT COUNT(name)
                FROM world
                WHERE area >= 1e6;""")

    return pd.DataFrame(cur.fetchall(), columns=['COUNT(name)'])

def prob5(cur: sqlite3.Cursor) -> pd.DataFrame:
    """What is the total population of ('Estonia', 'Latvia', 'Lithuania').
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT SUM(population)
                FROM world 
                WHERE name in ('Estonia', 'Latvia', 'Lithuania');""")

    return pd.DataFrame(cur.fetchall(), columns=['SUM(population)'])

def prob6(cur: sqlite3.Cursor) -> pd.DataFrame:
    """For each continent show the continent and number of countries.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT DISTINCT continent, COUNT(name)
                FROM world
                GROUP BY continent;""")

    return pd.DataFrame(cur.fetchall(), columns=['continent', 'COUNT(name)'])

def prob7(cur: sqlite3.Cursor) -> pd.DataFrame:
    """For each continent show the continent and number of countries with
    populations of at least 10 million.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT continent, COUNT(name) 
                FROM world WHERE population >= 10e6
                GROUP BY continent;""")

    return pd.DataFrame(cur.fetchall(), columns=['continent', 'COUNT(name)'])

def prob8(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List the continents that have a total population of at least 100 million.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT continent
                FROM world
                GROUP BY continent
                HAVING SUM(population) >= 100e6;""")

    return pd.DataFrame(cur.fetchall(), columns=['continent'])

if __name__ == "__main__":
    main()