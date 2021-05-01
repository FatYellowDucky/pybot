def find_error(error):
    if error == IndexError:
        return 'error: null value'
    elif error == ZeroDivisionError:
        return 'error: zero division'
    else:
        return 'error: error-error inputed error not an error'
def info(code):
    info=str(code).split('!')
    print('?bot/>'+str('?')+'language : '+str(info[1]))
    print('?bot/>'+str('?')+'$version : '+str(info[2]))
def ory(con1, con2):
    if con1:
        return True
    elif con2:
        return True
    else:
        return False