from datetime import datetime
import time

def dec(func):
    def wrapper():
        start = datetime.now()
        results = func()
        end = datetime.now()
        print("execution time in seconds : ", (end-start).total_seconds())
        return results
    return wrapper

@dec
def main():
    time.sleep(0.5)
    print("function execution completed")
    
if __name__ == "__main__":
    main()
