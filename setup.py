from setuptools import setup, find_packages
from typing import List




# Declaring variables for set up functions

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Gracy"
DESCRIPTION="ML project to predict the house prices"
REQUIREMENTS_FILE_NAME = "requirements.txt"


#reading the requirements.txt and returns a list of strings
def get_requirements_list()->List[str]:
    """
    Description: This function will return the list 
    of requirements in requirements.txt file
    
    return type: Returns the list of libraries mentioned in the requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME)  as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name = PROJECT_NAME,
version= VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()

)
