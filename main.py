import datetime

def check_time():
    print("current time: ",datetime.datetime.now())

def main():
    print("Hello, Jenkins!")
    check_time()

if __name__ == "__main__":
    main()
