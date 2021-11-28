import sqlite3

def main():
    """Runs and prints the results of the queries required in the first lesson
    of the SQL Zoo, Select basics.
    """
    conn = sqlite3.connect('databases/world.db')
    cur = conn.cursor()

    # Problem 1
    print(f"The population of Germany is {prob1(cur)}.")

    # Problem 2
    print(prob2(cur))

    # Problem 3
    print(prob3(cur))

    conn.close()

def prob1(cur: sqlite3.Cursor) -> int:
    """Use a query to find the population of Germany.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (int) : Population of Germany according to the world table in world.db.
    """
    cur.execute('SELECT population FROM world WHERE name = "Germany";')
    
    return cur.fetchall()[0][0]

def prob2(cur: sqlite3.Cursor) -> list:
    """Show the name and the population for 'Sweden', 'Norway' and 'Denmark'.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (list of tuples) : List of (name, population) for 'Sweden', 'Norway' 
        and 'Denmark' according to the world table in world.db.

    """
    cur.execute('SELECT name, population FROM world WHERE name IN ("Sweden", "Norway", "Denmark");')

    return cur.fetchall()

def prob3(cur: sqlite3.Cursor) -> int:
    """Show the country and the area for countries with an area between
    200,000 and 250,000.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (list of tuples) : List of (name, area) for for countries with an area
        between 200,000 and 250,000. according to the world table in world.db.
    """
    cur.execute('SELECT name, area FROM world WHERE area BETWEEN 200000 AND 250000;')

    return cur.fetchall()

if __name__ == "__main__":
    main()