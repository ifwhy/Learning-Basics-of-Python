import random, string, time

def init_pk(panjang:int)->str:
    pk = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(panjang))
    return pk

def init_tgl_ditambahkan()->str:
    return time.strftime("%Y-%m-%d | %H:%M:%S%z", time.gmtime())
    