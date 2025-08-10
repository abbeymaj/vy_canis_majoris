# Importing packages
import sys
import pandas as pd
import sqlite3
from src.components.config_entity import DataBaseConfig
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
        self.db = DataBaseConfig()
    
    
    # Creating a method to load the data into a SQLite database
    def load_landing_layer(self, df:pd.DataFrame):
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
            # Creating the connection
            conn = sqlite3.connect(self.db.db_path)
            
            # Creating the cursor
            cursor = conn.cursor()
            
            # Inserting the data into the database
            for _, row in df.iterrows():
                cursor.execute(
                    '''
                    INSERT INTO lnd_cma (Date, Magnitude)
                    VALUES (
                        ?,
                        ?
                    )
                    ON CONFLICT (Date) DO UPDATE SET
                    Magnitude = excluded.Magnitude
                    WHERE true
                    ''', (row['Date'], row['Magnitude_Adj'])
                )
            
            # Committing the transaction
            conn.commit()
            
            # Closing the connection
            conn.close()        
        
        except Exception as e:
            raise CustomException(e, sys)