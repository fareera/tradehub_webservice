'''系统错误码'''


class LogicError(Exception):
    '''逻辑错误基类'''


code = None


def gen_logic_error(name, code):
    '''创建一个逻辑错误'''

    return type(name, (LogicError,), {'code': code})


OK = gen_logic_error("ok.", 0)
HASERROR = gen_logic_error("has error", 1001)
FILETYPEERROR = gen_logic_error("文件类型错误",1002)
PARAMSERROR = gen_logic_error("参数有误",1003)