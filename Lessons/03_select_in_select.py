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

        # Problem 9
        print(f"Problem 9:\n{prob9(cur)}\n")

        # Problem 10
        print(f"Problem 10:\n{prob10(cur)}\n")

    finally:
        conn.close()

def prob1(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List each country name where the population is larger than that of
    'Russia'.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT name
                FROM world
                WHERE population > (SELECT population
                FROM world
                WHERE name = 'Russia');""")

    return pd.DataFrame(cur.fetchall(), columns=['name'])

def prob2(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the countries in Europe with a per capita GDP greater than
    'United Kingdom'.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT name
                FROM world
                WHERE continent = 'Europe' AND gdp/population > (SELECT gdp/population
                FROM world
                WHERE name = 'United Kingdom');""")

    return pd.DataFrame(cur.fetchall(), columns=['name'])

def prob3(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List the name and continent of countries in the continents containing
    either Argentina or Australia. Order by name of the country.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT name, continent
                FROM world
                WHERE continent IN (SELECT continent
                FROM world
                WHERE name IN ('Argentina', 'Australia'))
                ORDER BY name;""")

    return pd.DataFrame(cur.fetchall(), columns=['name', 'continent'])

def prob4(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Which country has a population that is more than Canada but less than
    Poland? Show the name and the population.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT name, population
                FROM world
                WHERE population > (SELECT population
                FROM world
                WHERE name = 'Canada') AND population < (SELECT population
                FROM world
                WHERE name = 'Poland');""")

    return pd.DataFrame(cur.fetchall(), columns=['name', 'population'])

def prob5(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the name and the population of each country in Europe. Show the
    population as a percentage of the population of Germany.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    # The SQLite solution differs slightly from the MySQL solution I used on
    # the website due to not having FORMAT and how CONCAT works as ||.
    cur.execute("""SELECT name, (CAST(100*population/(SELECT population
                FROM world
                WHERE name = 'Germany') AS TEXT) || '%') AS percentage
                FROM world
                WHERE continent = 'Europe';""")

    return pd.DataFrame(cur.fetchall(), columns=['name', 'percentage'])

def prob6(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Which countries have a GDP greater than every country in Europe?
    [Give the name only.] (Some countries may have NULL gdp values)
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT name
                FROM world
                WHERE gdp > (SELECT MAX(gdp)
                FROM world
                WHERE gdp > 0 AND continent = 'Europe');""")

    return pd.DataFrame(cur.fetchall(), columns=['name'])

def prob7(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Find the largest country (by area) in each continent, show the
    continent, the name and the area:
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT continent, name, area
                FROM world AS w_outer
                WHERE area >= (SELECT MAX(area)
                FROM world AS w_inner
                WHERE w_outer.continent = w_inner.continent);""")

    return pd.DataFrame(cur.fetchall(), columns=['continent', 'name', 'area'])

def prob8(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List each continent and the name of the country that comes first
    alphabetically.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT continent, name
                FROM world AS w_outer
                WHERE name <= (SELECT MIN(name)
                FROM world as w_inner
                WHERE w_outer.continent = w_inner.continent);""")

    return pd.DataFrame(cur.fetchall(), columns=['name', 'continent'])

def prob9(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Find the continents where all countries have a population <= 25000000.
    Then find the names of the countries associated with these continents.
    Show name, continent and population.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT name, continent, population
                FROM world AS out_world
                WHERE 25000000 >= (SELECT MAX(population)
                FROM world AS in_world
                WHERE out_world.continent = in_world.continent);""")

    return pd.DataFrame(cur.fetchall(), columns=['name', 'continent', 'population'])

def prob10(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Some countries have populations more than three times that of any of
    their neighbours (in the same continent). Give the countries and
    continents.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT name, continent
                FROM world AS out_world
                WHERE population >=(SELECT MAX(population*3)
                FROM world as in_world
                WHERE out_world.continent = in_world.continent AND out_world.name <> in_world.name);""")

    return pd.DataFrame(cur.fetchall(), columns=['name', 'continent'])

if __name__ == "__main__":
    main()