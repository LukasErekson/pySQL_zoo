import sqlite3
import pandas as pd

def main():
    """Runs and prints the results of the queries required in the first lesson
    of the SQL Zoo, Select basics.
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

    finally:
        conn.close()

def prob1(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Use a query to find the population of Germany.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the population of Germany according to 
        the world table in world.db.
    """
    cur.execute("""SELECT population
                FROM world
                WHERE name = "Germany";""")

    return pd.DataFrame(data=cur.fetchall(), columns=['population'])

def prob2(cur: sqlite3.Cursor) ->  pd.DataFrame:
    """Show the name and the population for 'Sweden', 'Norway' and 'Denmark'.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table of (name, population) for 'Sweden', 'Norway' 
        and 'Denmark' according to the world table in world.db.

    """
    cur.execute("""SELECT name, population
                FROM world
                WHERE name IN ("Sweden", "Norway", "Denmark");""")

    return pd.DataFrame(data=cur.fetchall(), columns=['name', 'population'])

def prob3(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the country and the area for countries with an area between
    200,000 and 250,000.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table of (name, area) for for countries with an area
        between 200,000 and 250,000. according to the world table in world.db.
    """
    cur.execute("""SELECT name, area
                FROM world
                WHERE area BETWEEN 200000 AND 250000;""")

    return pd.DataFrame(data=cur.fetchall(), columns=['name', 'area'])

if __name__ == "__main__":
    main()