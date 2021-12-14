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
    csv_filenames, db_filename, delimiter = get_filenames(arguments)

    try:
        connection = sqlite3.connect(db_filename)
        for csv_file in csv_filenames:
            # Extract table name from the CSV file name
            table_name = csv_file.split('/')[-1][:-4]

            # Write the table to the database
            csv_data = pd.read_csv(csv_file, delimiter=delimiter)
            csv_data.to_sql(table_name, connection, if_exists='replace', index=False)

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
        list : The names of the csv files that make up the tables in the
            database.
        str : The name of the database file.
        str : The delimiter to use.
    
    Raises
    ------
        ValueError if there aren't enough arguments.
    """
    # Set the default csv extension
    csv_extension = '.csv'
    
    if len(arguments) == 2:
        db_filename = correct_extension(arguments[1], '.db')
    elif len(arguments) > 2:
        db_filename = correct_extension(arguments[2], '.db')

        if len(arguments) == 4:
            csv_extension = '.tsv'
    else:
        raise ValueError('Please input the filename of the csv file to convert.')

    csv_names = arguments[1].split(',')

    csv_filenames = [correct_extension(name, csv_extension) for name in csv_names]

    if len(arguments) == 4:
        delimiter = arguments[3]
    else:
        delimiter = ','

    return csv_filenames, db_filename, delimiter

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