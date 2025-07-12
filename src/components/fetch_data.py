# Importing packages
import numpy as np
import sys
import pandas as pd
from random import randint
from time import sleep
from bs4 import BeautifulSoup as bs
import requests
from src.exception import CustomException


# Creating a class to fetch and load the magnitude data from the AAVSO website
class FetchData():
    '''
    This class fetches the magnitude data from the AAVSO website.
    '''
    # Creating the constructor for the class
    def __init__(self):
        '''
        This is the constructor for the FetchData class.
        '''
        self.url = 'https://app.aavso.org/webobs/results/?star=VY+Canis+Majoris&num_results=200&obs_types=vis&page='
        
    
    # Creating a method to fetch the magnitude data from the AAVSO website
    def fetch_data(self):
        '''
        This method fetches the magnitude data from the AAVSO website. The method uses
        webscraping to obtain the data. 
        ==================================================================================
        ---------------
        Returns:
        ---------------
        col_ls : list -> This is a list of the column names for the magnitude data.
        row_ls : list -> This is a list of the data rows for the magnitude data.
        ==================================================================================
        '''
        try:
            # Defining the number of pages to scrape
            pages = np.arange(0,3,1)
            
            # Creating empty lists to store the column names and data rows
            col_ls = []
            row_ls = []
            
            # Scraping the data from the AAVSO website
            for i in pages:
                url = self.url+str(i)
                res = requests.get(url)
                text = res.text
                data = bs(text, 'html.parser')
                tbl = data.select('table.observations')[0]
                if i == 1:
                    cols = tbl.find('thead').find_all('th')
                    for col in cols[1:-1]:
                        col_ls.append(col.string)
                else:
                    rows = tbl.find('tbody').find_all('tr', attrs={'class': ['obs tr-even', 'obs tr-odd']})
                    for row in rows:
                        td = row.find_all('td')
                        td_row = tuple(str(tr.get_text().strip()) for tr in td[1:-1])
                        row_ls.append(td_row)
                sleep(randint(3,10))
        
            return col_ls, row_ls
        
        except Exception as e:
            raise CustomException(e, sys)
    
    