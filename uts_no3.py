import datetime

def main():
    days = int(input("Enter a number of days: "))

    future_date = datetime.datetime.now() + datetime.timedelta(days=days)

    formatted_date = future_date.strftime("%A on %d %B %Y")

    print(formatted_date)

if __name__ == "__main__":
    main()
