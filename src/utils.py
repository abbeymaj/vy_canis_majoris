# Importing packages
import sys


# Creating a function to fetch the error message from the sys module
def fetch_error_message(error, error_detail:sys):
    '''
    This function fetches the error information from the sys module.
    ====================================================================
    ------------------
    Parameters:
    ------------------
    error - str : This is the error message.
    error_detail: This is the error detail from the sys module.
    
    ------------------
    Returns:
    ------------------
    error_message - This is the error message from the sys module.
    =====================================================================
    '''
    _, _, exc_tbl = error_detail.exc_info()
    file_name = exc_tbl.tb_frame.f_code.co_filename
    line_no = exc_tbl.tb_lineno
    error_message = f"Error occurred in script name [{file_name}], line_number [{line_no}], with error message [{str(error)}]"
    return error_message