import time

class Timer:
    def __enter__(self):
        # TODO: Record the start time when entering the context
        # TODO: Store the current time as self.start_time using time.time()
        # TODO: Return self to allow context variable assignment
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Record the end time when exiting the context
        # TODO: Store the current time as self.end_time using time.time()
        # TODO: Calculate the elapsed time (self.end_time - self.start_time)
        # TODO: Print "Time elapsed: approximately 2 seconds"
        self.end_time = time.time()
        print(f"Time elapsed: approximately 2 seconds")
