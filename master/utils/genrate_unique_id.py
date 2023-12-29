import string
import random 

def genrate_password(digits=8):
    """
    This function will genrate unique password with given digits

    Bydefault will generate 8 digits password
    """
    chs = string.ascii_letters + string.digits + '@_$.'
    password_ = ''
    for d in range(0, digits):
        password_ +=  chs[random.randint(0, len(chs) - 1)]
    return password_