import time


def exec_time(func):
    def decorator(*args, **kwargs):
        # Start the timer
        start = time.time()

        # Execute the function
        func(*args, **kwargs)

        # Stop the timer
        end = time.time()

        # Return execution time
        return end - start

    return decorator


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 100000000))
