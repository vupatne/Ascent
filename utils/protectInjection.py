import constants.appconstants as constants

def checkInjection(data):
    flag=True
    return False

    #condition 1: check for special chars
    for item in data:
        strr = data[item]
        strr = replacesomechars(strr)
        #returns True is string is not alphanumber
        flag = any(not c.isalnum() for c in strr)
        if flag:
            break
    if flag:
        return flag

    #condition 2: check for special words
    innerbreaked =False
    for item in data:
        if innerbreaked:
            break
        strr = data[item]
        strr = replacesomechars(strr)
        strr = strr.lower()
        for ele in constants.injectionWords:
            if strr.find(ele.lower()) == -1:
                flag=False
            else:
                flag=True
                innerbreaked=True
                break

    if flag:
        return flag

    #add further condition here

    return flag

def replacesomechars(strr):
    char_to_replace = {'@': '',
                       ' ': '',
                       '-': '',
                       '.': '',
                       'sys': '',
                       'or': ''}
    for key, value in char_to_replace.items():
        # Replace key character with value character in string
        strr = strr.replace(key, value)

    return strr