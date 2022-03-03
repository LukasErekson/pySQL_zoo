<img src="Sql_zoo.png" width="50%" alt="SQL Zoo"/>

# pySQL Zoo
A way to showcase my solutions going through the [SQL Zoo](https://sqlzoo.net/wiki/SQL_Tutorial) using the <code>sqlite3</code> package in Python.

As I worked through 9 lessons of the [SQL Zoo Tutorial](https://sqlzoo.net/wiki/SQL_Tutorial), I wanted a way to showcase the different queries and SQL commands that I learned. I settled on converting the different queries to SQLite commands in Python.

All of these solutions and scripts are my own work.

The databases on which these exercises are based were obtained "manually" by querying the SQL Zoo databases for the relevant information and placing that information into the relevant .tsv files. SQL Zoo has a limit of showing only up to 50 rows of a query at a time. In the case of Lesson 6, the casting table has around 120,000 entries, so the solution is split into two files: the raw SQL queries in <code>06_more_join.sql</code> and also the Python implementation in <code>06_more_join.py</code>.

To avoid excessive copy/pasting, I wrote a simple Python script to scrape a lot of the data using the <code>pynput</code> package. The script is not included in this repository as its values are specific for my monitor configuration.

<br />
<br />

## Showcased Skills
___
- ### SQL Queries: Executing SQL queries accurately and in a way that is readable to someone reviewing the queires later.
- ### Scripting: Creating SQLite Databases from csv/tsv files using Python and Pandas.
- ### Documentation: Clean, standardized documentation for my scripts and solutions.


<br />
<br />

This project was done as part of [The Odin Project](https://www.TheOdinProject.com), which is why not all of the tutorials and lesosns available on SQL Zoo are included.
