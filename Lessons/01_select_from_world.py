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

        # Problem 11
        print(f"Problem 11:\n{prob11(cur)}\n")

        # Problem 12
        print(f"Problem 12:\n{prob12(cur)}\n")

        # Problem 13
        print(f"Problem 13:\n{prob13(cur)}\n")

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
    cur.execute("""SELECT name, continent, population
                FROM world
                WHERE name = "Germany";""")

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
    cur.execute("""SELECT name
                FROM world
                WHERE population > 200e6;""")

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
    cur.execute("""SELECT name, gdp/population AS per_capita_gdp
                FROM world
                WHERE population > 2e8;""")

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
    cur.execute("""SELECT name, population/1e6
                FROM world
                WHERE continent = "South America";""")

    return pd.DataFrame(data=cur.fetchall(), columns=['name', 'population'])

def prob5(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the name and population for France, Germany, and Italy.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table of the name and population for France,
        Germany, and Italy.
    """
    cur.execute("""SELECT name, population
                FROM world
                WHERE name IN ('France', 'Germany', 'Italy');""")

    return pd.DataFrame(data=cur.fetchall(), columns=['name', 'population'])

def prob6(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the countries which have a name that includes the word 'United'
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table of the names where 'United' is
        somewhere in the name.
    """
    cur.execute("""SELECT name
                FROM world
                WHERE name LIKE '%United%';""")

    return pd.DataFrame(data=cur.fetchall(), columns=['name'])

def prob7(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the countries that are big by area or big by population.
    Show name, population and area. A country is big if it has an 
    area of more than 3 million sq km or it has a population of more
    than 250 million.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table of the names, populations, and areas
        of "big" contries.
    """
    cur.execute("""SELECT name, population, area
                FROM world
                WHERE area > 3e6
                OR population > 250e6;""")

    return pd.DataFrame(data=cur.fetchall(), columns=['name', 'population', 'area'])

def prob8(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the countries that are big by area (more than 3 million)
    or big by population (more than 250 million) but not both. Show
    name, population and area.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table of the names, populations, and areas
        of "big" contries that only satisfy one of the criteria
        listed in prob7.
    """
    # Sqlite doesn't support the XOR like MySQL, so a work-around is
    # needed.
    cur.execute("""SELECT name, population, area
                FROM world
                WHERE (area > 3e6 AND population < 250e6)
                OR (area < 3e6 AND population > 250e6);""")

    return pd.DataFrame(data=cur.fetchall(), columns=['name', 'population', 'area'])

def prob9(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the name and population in millions and the GDP in
    billions for the countries of the continent 'South America'.
    Use the ROUND function to show the values to two decimal places.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table of the names, populations, and GDP for
        countries in South America.
    """
    cur.execute("""SELECT name, ROUND(population / 1e6, 2) AS population_in_mil, ROUND(gdp / 1e9, 2) AS gdp_in_bil
                FROM world
                WHERE continent = 'South America';""")

    return pd.DataFrame(data=cur.fetchall(), columns=['name', 'population_in_mil', 'gdp_in_bil'])

def prob10(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the name and per-capita GDP for those countries with a
    GDP of at least one trillion (1000000000000; that is 12 zeros).
    Round this value to the nearest 1000.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table of the name and per-capita GDP for
        those countries with a GDP of at least one trillion
        rounded to the nearest 1000.
    """
    cur.execute("""SELECT name, ROUND(gdp/population, -3) AS per_capita_gdp
                FROM world
                WHERE gdp > 1e12;""")

    return pd.DataFrame(data=cur.fetchall(), columns=['name', 'per_capita_gdp'])

def prob11(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the name and capital where the name and the capital have
    the same number of characters.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table of the name and capital where the name
        and the capital have the same number of characters.
    """
    cur.execute("""SELECT name, capital
                FROM world
                WHERE LENGTH(name) = LENGTH(capital);""")

    return pd.DataFrame(data=cur.fetchall(), columns=['name', 'capital'])

def prob12(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the name and the capital where the first letters of each
    match. Don't include countries where the name and the capital are
    the same word.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table of the name and the capital where the
        first letters of each match but they are not the same value.
    """
    # Sqlite doesn't support the LEFT keyword, so use substr instead.
    cur.execute("""SELECT name, capital
                FROM world
                WHERE substr(name, 1, 1) = substr(capital, 1, 1) AND name <> capital;""")

    return pd.DataFrame(data=cur.fetchall(), columns=['name', 'capital'])

def prob13(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Find the country that has all the vowels and no spaces in its
    name.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table of the name of the country that has 
        all the vowels and no spaces in its name.
    """
    cur.execute("""SELECT name
                FROM world
                WHERE name LIKE '%a%' AND name LIKE '%e%' AND name LIKE '%i%' AND name LIKE '%o%' AND name LIKE '%u%' AND name NOT LIKE '% %';""")

    return pd.DataFrame(data=cur.fetchall(), columns=['name'])

if __name__ == "__main__":
    main()