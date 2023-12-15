import time
def calc_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return {"time": end-start, "result": result}