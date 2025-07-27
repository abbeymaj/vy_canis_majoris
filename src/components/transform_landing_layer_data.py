# Importing packages
import sys
import pandas as pd
from src.utils import create_dataframe
from src.utils import clean_magnitude_feature
from src.utils import clean_error_feature
from src.utils import create_adjusted_magnitude
from src.utils import extract_date_feature
from src.exception import CustomException


# Creating a class to transform the data for the landing layer
class TransformLandingLayerData():
    '''
    This class transforms the data fetched from the AAVSO website and prepares
    it for loading into the landing layer. 
    '''
    # Creating the constructor for the TransformLandingLayerData class
    def __init__(self, rows:list, cols:list):
        '''
        This is the constructor for the TransformLandingLayerDat class.
        '''
        self.rows = rows
        self.cols = cols
    
    # Creating a method to make the calendar date feature into a Datetime
    # object.
    def convert_calendar_date_to_datetime(self, df):
        '''
        This method converts the calendar date to a datetime object.
        =================================================================================
        ---------------
        Parameters:
        ---------------
        df : pandas dataframe -> This is the pandas dataframe with the date feature.
        
        ---------------
        Returns:
        ---------------
        df : pandas dataframe -> This is the pandas dataframe with the date feature
        converted to a datetime object.
        =================================================================================
        '''
        try:
            # Extracting the date from the Calendar Date feature
            df['Date'] = df['Calendar_Date'].apply(lambda x: extract_date_feature(x))
            
            # Covnerting the Date feature into a DateTime feature
            df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
            
            # Sorting the dataframe by the Date feature and dropping duplicates
            df = df.sort_values(by='Date').drop_duplicates(['Date'], keep='last')
            
            return df
        
        except Exception as e:
            raise CustomException(e, sys)
        
    
    
    # Creating a method to convert the data into a pandas dataframe
    def transform_landing_data(self):
        '''
        This method cleans the data and prepares the data to be loaded into the 
        landing layer.
        ================================================================================
        ---------------
        Returns:
        ---------------
        df : pandas dataframe -> This is returns a pandas dataframe with clean data.
        ================================================================================
        '''
        try:
            # Creating a pandas dataframe from the rows and columns data
            df = create_dataframe(self.rows, self.cols)
            
            # Cleaning the Magnitude feature
            df['Magnitude'] = df['Magnitude'].apply(lambda x: clean_magnitude_feature(x))
            
            # Cleaning the Error feature
            df = clean_error_feature(df)
            
            # Creating the Adjusted Magnitude feature
            df = create_adjusted_magnitude(df)
            
            # Renaming the Calendar Date feature to Date
            df = df.rename(columns={'Calendar Date': 'Calendar_Date'})
            
            # Extracting the date feature and converting it to a datetime object
            df = self.convert_calendar_date_to_datetime(df)
            
            # Taking the Date and Adjusted Magnitude features and creating a new dataframe
            sub_df = df[['Date', 'Magnitude_Adj']]
            
            return sub_df
        
        except Exception as e:
            raise CustomException(e, sys)
