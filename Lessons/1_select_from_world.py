import sqlite3
import pandas as pd

def main():
    """Runs and prints the results of the queries required in the second lesson
    of the SQL Zoo, SELECT from world.
    """
    try:
        conn = sqlite3.connect('databases/world.db')
        cur = conn.cursor()

        # Problem 1
        print(f"Problem 1:\n\{prob1(cur)}\n")

        # Problem 2
        print(f"Problem 2:\n\{prob2(cur)}\n")

        # Problem 3
        print(f"Problem 3:\n\{prob3(cur)}\n")

        # Problem 4
        print(f"Problem 4:\n\{prob4(cur)}\n")

        # Problem 5
        print(f"Problem 5:\n\{prob5(cur)}\n")

        # Problem 6
        print(f"Problem 6:\n\{prob6(cur)}\n")

        # Problem 7
        print(f"Problem 7:\n\{prob7(cur)}\n")

        # Problem 8
        print(f"Problem 8:\n\{prob8(cur)}\n")

        # Problem 9
        print(f"Problem 9:\n\{prob9(cur)}\n")

        # Problem 10
        print(f"Problem 10:\n\{prob10(cur)}\n")

        # Problem 11
        print(f"Problem 11:\n\{prob11(cur)}\n")

        # Problem 12
        print(f"Problem 12:\n\{prob12(cur)}\n")

        # Problem 13
        print(f"Problem 13:\n\{prob13(cur)}\n")

    finally:
        conn.close()

def prob1(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Observe the result of running this SQL command to show the name, 
    continent and population of all countries.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the name, continent and population of all 
        countries in the world table.
    """
    cur.execute('SELECT name, continent, population FROM world WHERE name = "Germany";')

    return pd.DataFrame(data=cur.fetchall(), columns=['name', 'continent', 'population'])

def prob2(cur: sqlite3.Cursor) ->  pd.DataFrame:
    """Show the name for the countries that have a population of at least 200
    million. 200 million is 200000000, there are eight zeros.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table of the name for the countries that have a 
        population of at least 200 million in world.db.

    """
    cur.execute('SELECT name FROM world WHERE population > 200e6;')

    return pd.DataFrame(data=cur.fetchall(), columns=['name'])

def prob3(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Give the name and the per capita GDP for those countries with a
    population of at least 200 million.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table of the name and the per capita GDP for those 
        countries with a population of at least 200 million in world.db.
    """
    cur.execute('SELECT name, gdp/population AS per_capita_gdp FROM world WHERE population > 2e8;')

    return pd.DataFrame(data=cur.fetchall(), columns=['name', 'per_capita_gdp'])

def prob4(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the name and population in millions for the countries of the
    continent 'South America'. Divide the population by 1000000 to get
    population in millions.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table of the name and population in millions for the
        countries of the continent 'South America' in world.db.
    """
    cur.execute('SELECT name, population/1e6 FROM world WHERE continent = "South America";')

    return pd.DataFrame(data=cur.fetchall(), columns=['name', 'population'])

def prob5(cur: sqlite3.Cursor) -> pd.DataFrame:
    pass

def prob6(cur: sqlite3.Cursor) -> pd.DataFrame:
    pass

def prob7(cur: sqlite3.Cursor) -> pd.DataFrame:
    pass

def prob8(cur: sqlite3.Cursor) -> pd.DataFrame:
    pass

def prob9(cur: sqlite3.Cursor) -> pd.DataFrame:
    pass

def prob10(cur: sqlite3.Cursor) -> pd.DataFrame:
    pass

def prob11(cur: sqlite3.Cursor) -> pd.DataFrame:
    pass

def prob12(cur: sqlite3.Cursor) -> pd.DataFrame:
    pass

def prob13(cur: sqlite3.Cursor) -> pd.DataFrame:
    pass

if __name__ == "__main__":
    main()