import sqlite3
import pandas as pd

def main():
    """Runs and prints the results of the queries required a given SQL Zoo
    lesson.
    """
    try:
        conn = sqlite3.connect('databases/nobel.db')
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

        # Problem 14
        print(f"Problem 14:\n{prob14(cur)}\n")

    finally:
        conn.close()

def prob1(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Display the nobel prizes for 1950.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT *
                FROM nobel
                WHERE yr = 1950;""")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob2(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show who won the 1962 prize for Literature.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT winner
                FROM nobel
                WHERE yr = 1962 AND subject = 'Literature';""")

    return pd.DataFrame(cur.fetchall(), columns=['winner'])

def prob3(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the year and subject that won 'Albert Einstein' his prize.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT yr, subject
                FROM nobel
                WHERE winner = 'Albert Einstein';""")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject'])

def prob4(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Give the name of the 'Peace' winners since the year 2000, including 2000.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT winner
                FROM nobel
                WHERE subject = 'Peace' AND yr >= 2000;""")

    return pd.DataFrame(cur.fetchall(), columns=['winner'])

def prob5(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show all details (yr, subject, winner) of the Literature prize winners
    for 1980 to 1989 inclusive.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT *
                FROM nobel
                WHERE subject = 'Literature' AND yr BETWEEN 1980 AND 1989;""")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob6(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show all details of the presidential winners:

    - Theodore Roosevelt
    - Woodrow Wilson
    - Jimmy Carter
    - Barack Obama
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT *
                FROM nobel
                WHERE winner IN ('Theodore Roosevelt', 'Woodrow
                Wilson', 'Jimmy Carter', 'Barack
                Obama');""")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob7(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the winners with first name John.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT winner
                FROM nobel
                WHERE winner LIKE 'John %';""")

    return pd.DataFrame(cur.fetchall(), columns=['winner'])

def prob8(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the year, subject, and name of Physics winners for 1980 together
    with the Chemistry winners for 1984.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT *
                FROM nobel
                WHERE (yr = 1980 AND subject = 'Physics')
                OR (subject = 'Chemistry' AND yr = 1984);""")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob9(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the year, subject, and name of winners for 1980 excluding Chemistry
    and Medicine.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT *
                FROM nobel
                WHERE yr = 1980 AND subject NOT IN ('Chemistry', 'Medicine');""")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob10(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show year, subject, and name of people who won a 'Medicine' prize in an
    early year (before 1910, not including 1910) together with winners of a
    'Literature' prize in a later year (after 2004, including 2004).
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT *
                FROM nobel
                WHERE (subject = 'Medicine' AND yr < 1910)
                OR (subject = 'Literature' AND yr >= 2004);""")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob11(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Find all details of the prize won by PETER GRÜNBERG.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT *
                FROM nobel
                WHERE winner = 'Peter Grünberg';""")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob12(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Find all details of the prize won by EUGENE O'NEILL.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT *
                FROM nobel
                WHERE winner = "Eugene
                O\'Neill";""")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob13(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List the winners, year and subject where the winner starts with Sir. Show the the most recent first, then by name order.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT winner, yr, subject
                FROM nobel
                WHERE winner LIKE 'Sir%'
                ORDER BY yr DESC;""")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob14(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the 1984 winners and subject ordered by subject and winner name;
    but list Chemistry and Physics last.

    The expression subject IN ('Chemistry','Physics') can be used as a value -
    it will be 0 or 1.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT winner, subject
                FROM nobel
                WHERE yr = 1984
                ORDER BY subject IN ('Chemistry', 'Physics'), subject, winner;""")

    return pd.DataFrame(cur.fetchall(), columns=['subject', 'winner'])

if __name__ == "__main__":
    main()