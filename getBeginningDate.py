import datetime

def get_beginning_date():
    beginning_date = input("What is the beginning date of the data you want? (Use YYYY-MM-DD format): ")
    try:
        begin_date = datetime.datetime.strptime(beginning_date, "%Y-%m-%d").date()
    except:
        print("Invalid date. Please try again.")
        return get_beginning_date()

    return begin_date

get_beginning_date()