# Importing packages
import sys
import pandas as pd
import sqlite3
from src.exception import CustomException

# Creating a class to load the data into a SQLite database
class LoadLandingLayer():
    '''
    This class loads the data, which has been scraped from the AAVSO website,
    into a landing layer within the sqlite database.
    '''
    # Creating the constructor for the class
    def __init__(self):
        '''
        This is the constructor for the LoadLandingLayer class.
        '''
        self.db_path = 'db/landing/stg_vycma.db'
    
    
    # Creating a method to load the data into a SQLite database
    def load_landing_layer(self, rows:list):
        '''
        This method loads the data into the landing layer.
        ================================================================================
        ---------------
        Parameters:
        ---------------
        cols : list -> This is the list of columns for the scraped data.
        rows : list -> This is the list of rows for the scraped data.
        
        ---------------
        Returns:
        ---------------
        None
        ================================================================================
        '''
        try:
            # Connecting to the database
            conn = sqlite3.connect(self.db_path)
            
            # Creating a cursor
            cursor = conn.cursor()
            
            # Creating the landing layer table if it does not exist 
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS landing_tbl(
                Star TEXT,
                JD TEXT,
                Calend_Dt TEXT,
                Magnitude TEXT,
                Error TEXT,
                Filter TEXT,
                Observer TEXT
                '''
            )
            
            # Loading the data into the landing layer
            for row in rows:
                cursor.execute(
                    '''
                    SELECT * 
                    FROM landing_tbl 
                    WHERE Star=? 
                    AND JD=? 
                    AND Calend_Dt=? 
                    AND Magnitude=? 
                    AND Error=? 
                    AND Filter=? 
                    AND Observer=?
                    ''',
                    (row)
                )
                result = cursor.fetchone()
                if result is None:
                    cursor.execute(
                        '''
                        INSERT INTO landing_tbl()
                        VALUES(?,?,?,?,?,?,?)
                        ''',
                        (row)
                    )
            
            # Committing the changes to the database
            conn.commit()
            
            # Closing the connection to the database
            conn.close()
            
        
        except Exception as e:
            raise CustomException(e, sys)