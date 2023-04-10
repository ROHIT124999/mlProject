"""import sys # The sys library provide functionalities tha are used to manipulate different parts of python runtime environment
import logging

def error_message_details(error, error_detail:sys):
    _,_,exec_tb = error_detail.exe_info()
    file_name= exec_tb.tb_frame.f_code.co_filename
    error_message = "Error Occured in python script name [{0}] line number [{1}] error message [{2}]".formatt(file_name, exec_tb.tb_lineno,str(error) )
    return error_message


class customException(Exception):
    def __init__(self, error_message,error_display:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        a=10/0
    except Exception as e:
        logging.info("Divide By Zero error")
        raise customException(e,sys)"""
import sys
from logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message


"""if __name__ == "__main__":
    try:
        a=10/0
    except Exception as e:
        logging.info("Divide By Zero error")
        raise CustomException(e,sys)"""