import sqlite3
import pandas as pd

def main():
    """Runs and prints the results of the queries required a given SQL Zoo
    lesson.
    """
    try:
        conn = sqlite3.connect('databases/null_lesson.db')
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
    """List the teachers who have NULL for their department.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT name from teacher WHERE teacher.dept IS NULL;""")

    return pd.DataFrame(cur.fetchall())

def prob2(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Note the INNER JOIN misses the teachers with no department and the
    departments with no teacher.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT teacher.name, dept.name
                FROM teacher INNER JOIN dept
                ON (teacher.dept=dept.id);""")

    return pd.DataFrame(cur.fetchall())

def prob3(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Use a different JOIN so that all teachers are listed.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT teacher.name, dept.name
                FROM teacher
                LEFT JOIN dept ON teacher.dept = dept.id;""")

    return pd.DataFrame(cur.fetchall())

def prob4(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Use a different JOIN so that all departments are listed.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    # I would use a RIGHT JOIN here, but they ar enot currently supported by
    # sqlite3.
    cur.execute("""SELECT teacher.name, dept.name
                FROM teacher
                JOIN dept ON teacher.dept = dept.id;""")
                #RIGHT JOIN dept ON teacher.dept = dept.id;""")

    return pd.DataFrame(cur.fetchall())

def prob5(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Use COALESCE to print the mobile number. Use the number '07986 444 2266'
    if there is no number given. Show teacher name and mobile number or '07986
    444 2266'.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT teacher.name,
                COALESCE(teacher.mobile, '07986 444 2266') AS mobile
                FROM teacher;""")

    return pd.DataFrame(cur.fetchall())

def prob6(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Use the COALESCE function and a LEFT JOIN to print the teacher name and
    department name. Use the string 'None' where there is no department.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT teacher.name,
                COALESCE(dept.name, 'None') AS department
                FROM teacher
                LEFT JOIN dept ON teacher.dept = dept.id;""")

    return pd.DataFrame(cur.fetchall())

def prob7(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Use COUNT to show the number of teachers and the number of mobile phones.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT COUNT(teacher.name) as num_teachers,
                SUM(CASE WHEN mobile IS NOT NULL THEN 1 ELSE 0 END) AS num_mobile
                FROM teacher;""")

    return pd.DataFrame(cur.fetchall())

def prob8(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Use COUNT and GROUP BY dept.name to show each department and the number
    of staff. Use a RIGHT JOIN to ensure that the Engineering department is
    listed.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    # I would use a RIGHT JOIN here, but they ar enot currently supported by
    # sqlite3.
    cur.execute("""SELECT dept.name, COUNT(teacher.name) AS num_staff
                FROM teacher
                JOIN dept ON teacher.dept = dept.id
                GROUP BY dept.name;""")

    return pd.DataFrame(cur.fetchall())

def prob9(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Use CASE to show the name of each teacher followed by 'Sci' if the
    teacher is in dept 1 or 2 and 'Art' otherwise.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT teacher.name,
                (CASE WHEN teacher.dept IN (1, 2) THEN 'Sci' ELSE 'Art' END) 
                    AS dept_type 
                FROM teacher;""")

    return pd.DataFrame(cur.fetchall())

def prob10(cur: sqlite3.Cursor) -> pd.DataFrame:
    """Use CASE to show the name of each teacher followed by 'Sci' if the
    teacher is in dept 1 or 2, show 'Art' if the teacher's dept is 3 and 'None'
    otherwise.
    
    Parameters
    ----------
        cur (sqlite3.Cursor) : The cursor for the database we're accessing.

    Returns
    -------
        (pd.DataFrame) : Table with the solution.
    """
    cur.execute("""SELECT teacher.name,
                (CASE WHEN teacher.dept IN (1, 2) THEN 'Sci' WHEN teacher.dept = 3 THEN 'Art' ELSE 'None' END)
                AS dept_type
                FROM teacher;""")

    return pd.DataFrame(cur.fetchall())


if __name__ == "__main__":
    main()