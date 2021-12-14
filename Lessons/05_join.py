import sqlite3
import pandas as pd

def main():
    """Runs and prints the results of the queries required a given SQL Zoo
    lesson.
    """
    try:
        conn = sqlite3.connect('databases/sport.db')
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
    """ show the matchid and player name for all goals scored by Germany. 
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("SELECT matchid, player FROM goal WHERE teamid = 'GER';")

    return pd.DataFrame(cur.fetchall(), columns=['matchid', 'player'])

def prob2(cur: sqlite3.Cursor) -> pd.DataFrame:
    """
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob3(cur: sqlite3.Cursor) -> pd.DataFrame:
    """
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob4(cur: sqlite3.Cursor) -> pd.DataFrame:
    """
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob5(cur: sqlite3.Cursor) -> pd.DataFrame:
    """
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob6(cur: sqlite3.Cursor) -> pd.DataFrame:
    """
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob7(cur: sqlite3.Cursor) -> pd.DataFrame:
    """
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob8(cur: sqlite3.Cursor) -> pd.DataFrame:
    """
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob9(cur: sqlite3.Cursor) -> pd.DataFrame:
    """
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob10(cur: sqlite3.Cursor) -> pd.DataFrame:
    """
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob11(cur: sqlite3.Cursor) -> pd.DataFrame:
    """
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob12(cur: sqlite3.Cursor) -> pd.DataFrame:
    """
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob13(cur: sqlite3.Cursor) -> pd.DataFrame:
    """
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

def prob14(cur: sqlite3.Cursor) -> pd.DataFrame:
    """
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("")

    return pd.DataFrame(cur.fetchall(), columns=['yr', 'subject', 'winner'])

if __name__ == "__main__":
    main()