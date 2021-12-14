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

    finally:
        conn.close()

def prob1(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the matchid and player name for all goals scored by Germany.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT matchid, player
                FROM goal
                WHERE teamid = 'GER';""")

    return pd.DataFrame(cur.fetchall())

def prob2(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show id, stadium, team1, team2 for just game 1012.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT id, stadium, team1, team2
                FROM game
                WHERE id = 1012;""")

    return pd.DataFrame(cur.fetchall())

def prob3(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Modify it to show the player, teamid, stadium and mdate for every German
    goal.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT goal.player, goal.teamid, game.stadium, game.mdate
                FROM goal JOIN game
                ON (game.id = goal.matchid) WHERE goal.teamid = 'GER';""")

    return pd.DataFrame(cur.fetchall())

def prob4(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the team1, team2 and player for every goal scored by a player
    called Mario using player LIKE 'Mario%'.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT game.team1, game.team2, goal.player
                FROM goal JOIN game
                ON (game.id = goal.matchid) WHERE goal.player LIKE 'Mario%';""")

    return pd.DataFrame(cur.fetchall())

def prob5(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show player, teamid, coach, gtime for all goals scored in the first 10
    minutes gtime<=10.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT player, teamid, coach, gtime
                FROM goal JOIN eteam
                ON goal.teamid = eteam.id
                WHERE goal.gtime <= 10;""")

    return pd.DataFrame(cur.fetchall())

def prob6(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List the dates of the matches and the name of the team in which
    'Fernando Santos' was the team1 coach.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT game.mdate, eteam.teamname
                FROM game JOIN eteam
                ON (eteam.id = game.team1)
                WHERE eteam.coach = 'Fernando Santos';""")

    return pd.DataFrame(cur.fetchall())

def prob7(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List the player for every goal scored in a game where the stadium was
    'National Stadium, Warsaw'.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT goal.player
                FROM goal JOIN game
                ON (goal.matchid = game.id)
                WHERE game.stadium = 'National Stadium, Warsaw';""")

    return pd.DataFrame(cur.fetchall())

def prob8(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the name of all players who scored a goal against Germany.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT DISTINCT player
                FROM game
                JOIN goal ON game.id = goal.matchid
                WHERE (team1 = 'GER' OR team2 = 'GER')
                AND goal.teamid <> 'GER';""")

    return pd.DataFrame(cur.fetchall())

def prob9(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show teamname and the total number of goals scored.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.
    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT eteam.teamname, COUNT(goal.player) AS goal_count
                FROM eteam
                JOIN goal ON eteam.id = goal.teamid
                GROUP BY eteam.teamname;""")

    return pd.DataFrame(cur.fetchall())

def prob10(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Show the stadium and the number of goals scored in each stadium.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT game.stadium, COUNT(goal.player) AS total_goals
                    FROM game
                    JOIN goal ON game.id = goal.matchid
                    GROUP BY game.stadium;""")

    return pd.DataFrame(cur.fetchall())

def prob11(cur: sqlite3.Cursor) -> pd.DataFrame:
    """For every match involving 'POL', show the matchid, date and the number
    of goals scored.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT DISTINCT goal.matchid, game.mdate,
                COUNT(goal.player) AS goals
                FROM game
                JOIN goal ON game.id = goal.matchid
                WHERE game.team1 = 'POL' OR game.team2 = 'POL'
                GROUP BY goal.matchid, game.mdate;""")

    return pd.DataFrame(cur.fetchall())

def prob12(cur: sqlite3.Cursor) -> pd.DataFrame:
    """For every match where 'GER' scored, show matchid, match date and the
    number of goals scored by 'GER'.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT goal.matchid, game.mdate,
                COUNT(goal.player) AS goals_scored
                FROM goal JOIN game ON goal.matchid = game.id
                WHERE goal.teamid = 'GER'
                GROUP BY goal.matchid, game.mdate;""")

    return pd.DataFrame(cur.fetchall())

def prob13(cur: sqlite3.Cursor) -> pd.DataFrame:
    """List every match with the goals scored by each team as shown. This will
    use "CASE WHEN" which has not been explained in any previous exercises.

    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT game.mdate,
                game.team1,
                SUM(CASE WHEN teamid = team1 THEN 1 ELSE 0 END) AS score1,
                game.team2,
                SUM(CASE WHEN teamid = team2 THEN 1 ELSE 0 END) AS score2
                FROM game
                LEFT JOIN goal ON goal.matchid = game.id
                GROUP BY mdate, team1, team2
                ORDER BY game.mdate, goal.matchid, game.team1, game.team2;""")

    return pd.DataFrame(cur.fetchall())

if __name__ == "__main__":
    main()