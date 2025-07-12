from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .' # This is a special case for editable installs. To remove it from requirements getting executed by setup.py.
def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        requirements = [req for req in requirements if req]  # Remove empty lines
        requirements = [req for req in requirements if not req.startswith('#')]  # Remove comments
        if '-e .' in requirements:
            requirements.remove('-e .') # Remove editable install if present        
        
    return requirements

setup(
    name='house_price_prediction_regression',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[get_requirements('requirements.txt')],
    author='Sandeep',author_email='sandeep.singh91291@gmail.com',
    description='A Flask application for house price prediction using regression models.')
# This setup.py file is used to package the Flask application for house price prediction.
# It includes the necessary dependencies and metadata for the application.