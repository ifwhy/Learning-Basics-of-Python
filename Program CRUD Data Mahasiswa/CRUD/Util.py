import random, string, time

def random_pk(panjang:int)->str:
    pk = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(panjang))
    return pk

def get_current_time()->str:
    return time.strftime("%Y-%m-%d | %H:%M:%S%z", time.gmtime())