import sys
import sqlite3
from typing import List
import pandas as pd


def main(arguments: list):
    """Generates an SQL database from a CSV file using Pandas.

    Parameters
    ----------
        arguments (list) : The arguments passed in by the user running the
            script.
    
    Raises
    ------
        ValueError if there aren't enough arguments.
    """
    csv_filename, db_filename = get_filenames(arguments)

    try:
        connection = sqlite3.connect(db_filename)
        csv_data = pd.read_csv(csv_filename)

        csv_data.to_sql('world', connection, if_exists='replace', index=False)

    finally:
        connection.close()


def get_filenames(arguments: list) -> tuple:
    """Extracts the filenames from the arguments as strings.
    
    Parameters
    ----------
        arguments (list) : The arguments passed in by the user running the
            script.
    
    Returns
    -------
        tuple (str, str) : The names of the csv and database files respectively.
    
    Raises
    ------
        ValueError if there aren't enough arguments.
    """
    if len(arguments) == 2:
        csv_filename = correct_extension(arguments[1], '.csv')
        db_filename = correct_extension(arguments[1], '.db')
    elif len(arguments) > 2:
        csv_filename = correct_extension(arguments[1], '.csv')
        db_filename = correct_extension(arguments[2], '.db')
    else:
        raise ValueError('Please input the filename of the csv file to convert.')

    return (csv_filename, db_filename)

def correct_extension(filename: str, extension: str ='.csv') -> str:
    """Ensures that the passed in filename has the correct extension. Defaults
    to csv.
    
    Parameters
    ----------
        filename (str) : The filename to verify whether it has the extension.
        extension (str) : The extension that the filename should have.
    
    Returns
    -------
        (str) : The filename with the proper extension attached to it.
    """
    if filename[-len(extension):] != extension:
        # If it has another extension, remove it
        if '.' in filename:
            filename = filename[:filename.find('.')]
        
        filename += extension
    
    return filename

if __name__ == "__main__":
    main(sys.argv)