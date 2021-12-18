import sqlite3
import pandas as pd

def main():
    """Runs and prints the results of the queries required a given SQL Zoo
    lesson.
    """
    try:
        conn = sqlite3.connect('databases/more_join.db')
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

        # Problem 15
        print(f"Problem 15:\n{prob15(cur)}\n")

    finally:
        conn.close()

def prob1(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List the films where the yr is 1962 [Show id, title].
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("SELECT id, title FROM movie WHERE yr=1962;")

    return pd.DataFrame(cur.fetchall())

def prob2(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Give year of 'Citizen Kane'.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("SELECT yr FROM movie WHERE title = 'Citizen Kane';")

    return pd.DataFrame(cur.fetchall())

def prob3(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List all of the Star Trek movies, include the id, title and yr 
    (all of these movies include the words Star Trek in the title).
    Order results by year.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT id, title, yr
                FROM movie 
                WHERE title LIKE '%Star Trek%'
                ORDER BY yr;
                """)

    return pd.DataFrame(cur.fetchall())

def prob4(cur: sqlite3.Cursor) -> pd.DataFrame:
    """What id number does the actor 'Glenn Close' have?
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("SELECT id FROM actor WHERE name = 'Glenn Close';")

    return pd.DataFrame(cur.fetchall())

def prob5(cur: sqlite3.Cursor) -> pd.DataFrame:
    """What is the id of the film 'Casablanca'?
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("SELECT id FROM movie WHERE title = 'Casablanca';")

    return pd.DataFrame(cur.fetchall())

def prob6(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Obtain the cast list for 'Casablanca'.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT actor.name
                FROM casting 
                JOIN actor ON actor.id = casting.actorid 
                WHERE movieid = (SELECT id FROM movie WHERE title = 'Casablanca');
                """)

    return pd.DataFrame(cur.fetchall())

def prob7(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Obtain the cast list for the film 'Alien'.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT name FROM actor
                JOIN casting ON actor.id = casting.actorid
                WHERE casting.movieid = (SELECT id FROM movie WHERE title = 'Alien');
                """)

    return pd.DataFrame(cur.fetchall())

def prob8(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List the films in which 'Harrison Ford' has appeared.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT title
                FROM movie 
                JOIN casting ON movie.id = casting.movieid
                WHERE casting.actorid = (SELECT id FROM actor WHERE name = 'Harrison Ford');""")

    return pd.DataFrame(cur.fetchall())

def prob9(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List the films where 'Harrison Ford' has appeared - but not in the
    starring role.
    [Note: the ord field of casting gives the position of the actor. If ord=1
    then this actor is in the starring role]
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT title FROM movie
                JOIN casting ON movie.id = casting.movieid
                WHERE casting.actorid = (SELECT id FROM actor WHERE name = 'Harrison Ford') 
                AND casting.ord != 1;
                """)

    return pd.DataFrame(cur.fetchall())

def prob10(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List the films together with the leading star for all 1962 films.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT movie.title, actor.name FROM casting
                JOIN actor ON actor.id = casting.actorid
                JOIN movie ON movie.id = casting.movieid
                WHERE casting.ord = 1 AND movie.yr = 1962;
                """)

    return pd.DataFrame(cur.fetchall())

def prob11(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Which were the busiest years for 'Rock Hudson', show the year and the
    number of movies he made each year for any year in which he made more than
    2 movies.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT yr,COUNT(title) FROM movie 
                JOIN casting ON movie.id=movieid
                JOIN actor   ON actorid=actor.id
                WHERE name='Rock Hudson'
                GROUP BY yr
                HAVING COUNT(title) > 2;
                """)

    return pd.DataFrame(cur.fetchall())

def prob12(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List the film title and the leading actor for all of the films 'Julie 
    Andrews' played in.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT movie.title, actor.name
                FROM casting
                JOIN movie ON casting.movieid = movie.id 
                JOIN actor ON casting.actorid = actor.id 
                WHERE movie.id IN (SELECT DISTINCT movieid FROM casting
                WHERE actorid IN (
                    SELECT id FROM actor
                    WHERE name='Julie Andrews'))
                AND casting.ord = 1;
                """)

    return pd.DataFrame(cur.fetchall())

def prob13(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Obtain a list, in alphabetical order, of actors who've had at least 15
    starring roles.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT actor.name FROM casting
                JOIN actor ON actor.id = casting.actorid 
                GROUP BY actor.name 
                HAVING SUM(CASE WHEN casting.ord = 1 THEN 1 ELSE 0 END) >= 15;
                """)

    return pd.DataFrame(cur.fetchall())

def prob14(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List the films released in the year 1978 ordered by the number of actors
    in the cast, then by title.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT movie.title, COUNT(casting.actorid) AS num_actors 
                FROM movie
                JOIN casting ON movie.id = casting.movieid 
                WHERE movie.yr = 1978
                GROUP BY movie.title 
                ORDER BY num_actors DESC, movie.title;
                """)

    return pd.DataFrame(cur.fetchall())


def prob15(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List all the people who have worked with 'Art Garfunkel'.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT actor.name FROM actor
                JOIN casting ON actor.id = casting.actorid
                WHERE casting.movieid IN 
                    (SELECT casting.movieid FROM casting
                    WHERE casting.actorid = (SELECT actor.id FROM actor
                    WHERE actor.name = 'Art Garfunkel'))
                AND actor.name <> 'Art Garfunkel';
                """)

    return pd.DataFrame(cur.fetchall())

if __name__ == "__main__":
    main()