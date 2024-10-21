import sys
import os



def error_handler(err,error_detail:sys):
    _,_,exec_tb=error_detail.exc_info()
    file_name=exec_tb.tb_frame.f_code.co_filename
    err_msg=f"error occured in the file {file_name} in the line {exec_tb.tb_lineno} and the error is {str(err)}"
    return err_msg
class CustomException(Exception):
    def __init__(self,err,error_detail:sys):
        super().__init__(err)
        self.err=error_handler(err=err,error_detail=error_detail)
        
    def __str__(self):
        return self.err
  
  
'''
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
 
        #logging.info("this is exception log divude by zero")
        raise CustomException(e,sys)

'''  
