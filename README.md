## End to end ML project
### created an enviroment venv using
'''

conda create -p venv python==3.11

'''

Install all necessary libs

'''

pip install -r requirements.txt 

'''

create setup.py to make folders into packages

create src folder (entire ML lifecycle)

src-->__init__.py(this will also be a package and we should be able to import this package to others.Python recognizes it as a package, allowing you to organize related modules and functions into a structured and importable unit. Without it, a directory is just a collection of files, and you cannot import modules from it using standard package import syntax. )
src--> utils.py for generic functionalities. These are reusable, general-purpose functions or methods that perform common tasks and are not specific to a particular domain or feature of the application.

It typically contains functions for tasks such as:
File I/O operations (reading/writing files, handling paths)
String manipulation
Date and time handling
Data conversions or formatting
Validation routines
Simple mathematical calculations


src/components/data ingestion file for data cleaning and data ingestion and model trainer for training and evaluation

src/pipepline/__ini__.py