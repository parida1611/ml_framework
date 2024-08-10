import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message =  "Error occoured in file : [{0}] at line number [{1}] with error message [{2}]".format(file_name, line_no, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail:sys):
        super().__init__(error)
        self.error = error_message_detail(error, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error
    
