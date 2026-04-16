import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {end - start:.6f} seconds")
        return result
    return wrapper


@log_execution_time
def calculate_sum(n):
    return sum(range(1, n + 1))


print(calculate_sum(1000000))