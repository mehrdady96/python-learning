import time


def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        leng = len(result)
        end = time.time()
        final_time = end - start
        print(f"Prosses ended and it toke {final_time} to count {leng} numbers")
        return result
    return wrapper



@timer
def my_list():
    numbers = list(range(1,201))
    return numbers




my_list()