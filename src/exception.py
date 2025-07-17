import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info() # Get the traceback object 
    file_name = exc_tb.tb_frame.f_code.co_filename # Get the file name where the error occurred
    error_message = f"Error occurred in script: {file_name} at line number: {exc_tb.tb_lineno} - {str(error)}" # Create a detailed error message
    return error_message

class CustomException(Exception): # Custom exception class to handle errors with detailed messages
    def __init__(self, error, error_detail: sys): # Initialize with error and error detail
        super().__init__(error) # Call the parent class constructor
        self.error_message = error_message_detail(error, error_detail) # Get the detailed error message
    
    def __str__(self): # String representation of the exception
        return self.error_message # Return the error message
    
    def __repr__(self): # Representation of the exception
        # Return the class name and the error message   
        return CustomException.__name__.str() + f"({self.error_message})"
    
    #logging.error(f"Error occurred in script: {file_name} at line number: {exc_tb.tb_lineno} - {str(error)}") # Log the error message   
'''  
if __name__ == "__main__":
    
    logging.info("Logging has started. Custom exception module loaded")  # Log that the custom exception module is loaded
    try:
        a=1/0  # Example to raise a division by zero error
        #raise Exception("This is a test exception")  # Example to raise an exception
    except Exception as e:
        logging.INFO(f"An error occurred: {e}")  # Log the error
        raise CustomException(e, sys)  # Raise the custom exception with detailed error information
        
        '''