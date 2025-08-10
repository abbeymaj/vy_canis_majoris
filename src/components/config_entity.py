# Importing packages
import os
from dataclasses import dataclass

# Creating a class to store the path to the database
@dataclass
class DataBaseConfig():
    '''
    This class stores the path to the database.
    '''
    db_path : str = os.path.join('db', 'canis_majoris.db')