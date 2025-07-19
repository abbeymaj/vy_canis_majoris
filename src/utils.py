# Importing packages
import sys
import re
import numpy as np
import pandas as pd
from src.exception import CustomException


# Creating a function to create a Pandas dataframe from the rows and columns data
def create_dataframe(rows:list, cols:list):
    '''
    This function converts the row and column data into a pandas dataframe.
    ================================================================================
    ---------------
    Returns:
    ---------------
    df : pandas dataframe -> This is returns a pandas dataframe with the row and
    column data.
    ================================================================================
    '''
    try:
        df = pd.DataFrame(rows, columns=cols)
        return df
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function to clean the Magnitude feature
def clean_magnitude_feature(row):
    '''
    This function removes any non-numeric characters from the Magnitude feature.
    ==================================================================================
    ---------------
    Parameters:
    ---------------
    row -> This is each row in the dataset
    
    ---------------
    Returns:
    ---------------
    row -> This is each row after all non-numeric characters have been removed.
    ==================================================================================
    '''
    try:
        x = re.sub('<', '', row).strip()
        return x
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function to clean the Error feature
def clean_error_feature(df):
    '''
    This function removes any non-numeric characters from the Error feature and 
    replaces them with a zero (0).
    ==================================================================================
   ---------------
    Parameters:
    ---------------
    df : pandas dataframe -> This is the pandas dataframe with the Error feature.
    
    ---------------
    Returns:
    ---------------
    df : pandas dataframe -> This is the pandas dataframe with the clean Error
    feature.
    ==================================================================================
    '''
    try:
        df['Error_clean'] = df['Error'].replace(["—","None"], 0).infer_objects(copy=False)
        return df
    
    except Exception as e:
        raise CustomException(e, sys)


# Creating a function to create an adjusted Magnitude feature
def create_adjusted_magnitude(df):
    '''
    This function takes the Magnitude feature and adjusts it for any errors, using the
    Error feature.
    ====================================================================================
    ---------------
    Parameters:
    ---------------
    df : pandas dataframe -> This is the pandas dataframe with the Magnitude feature.
    
    ---------------
    Returns:
    ---------------
    df : pandas dataframe -> This is the pandas dataframe with the Adjusted Magnitude
    feature.
    ====================================================================================
    '''
    try:
        # Converting the Magnitude and Error features into a numeric feature
        df['Error_float'] = pd.to_numeric(df['Error_clean'], errors='coerce')
        df['Magnitude_float'] = pd.to_numeric(df['Magnitude'], errors='coerce')
        
        # Converting the Magnitude and Error features into float16 feature
        df['Error_float'] = df['Error_float'].astype(np.float16)
        df['Magnitude_float'] = df['Magnitude_float'].astype(np.float16)
        
        # Creating the Adjusted Magnitude feature
        df['Magnitude_Adj'] = df['Magnitude_float'] + df['Error_float']
        
        return df
    
    except Exception as e:
        raise CustomException(e, sys)
    