# Importing packages
import sys
from src.utils import fetch_error_message

# Creating a custom class to display exceptions thrown by the system.
# This custom class will inherit from the Python Exception class.

class CustomException(Exception):
    '''
    The CustomException class is a custom class to display system exceptions. 
    This class inherits from the Python Exception class.
    The class contains two methods - The constructor and a method to display the error message.
    '''
    # Defining the constructor for the class
    def __init__(self, error_message, error_detail:sys):
        '''
        This is the constructor for the CustomException class.
        The constructor takes two arguments - The error message and the error detail.
        '''
        super().__init__(error_message)
        self.error_message = fetch_error_message(error_message, error_detail=error_detail)
    
    # Defining the method to display the error message
    def __str__(self):
        '''
        This method displays the error message.
        '''
        return self.error_message