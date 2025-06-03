# Importing packages
from typing import List
from setuptools import setup, find_packages

# Setting hyphen e dot as a global variable
HYPHEN_E_DOT = "-e ."

# Creating a function to fetch all packages from the 
# requirements.txt file.
def get_requirements(filepath:str)->List[str]:
    '''
    This function fetches all packages from requirements.txt.
    =============================================================================================
    ----------------
    Parameters:
    ----------------
    filepath : str -> This is the filepath of the requirements.txt file. 
    This must be a string.
    
    ----------------
    Returns:
    ----------------
    List of packages : str -> This is a list of the packages from the requirements.txt file.
    =============================================================================================
    ''' 
    requirements = []
    
    # Opening and reading the requirements.txt file.
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        
        # Removing any line breaks  
        requirements = [req.replace('\n', "") for req in requirements]
        
        # Remove the "-e ." line if present in the requirements.txt file
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

# Using the setup function from setuptools to install all packages listed in requirements.txt
setup(
    name='vy_canis_majoris',
    version='0.0.1',
    author='Abhijit Majumdar',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)