

def timer(func):
    """
    Decorator to measure the execution time of a function.
    """
    import time

    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result

    return wrapper