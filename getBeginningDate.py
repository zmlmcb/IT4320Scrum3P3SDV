import datetime


def get_beginning_date():
    beginning_date = input("What is the beginning date of the data you want? (Use YYYY-MM-DD format)")
    begin_date = datetime.datetime.strptime(beginning_date, "%Y/%m/%d").date()

    return begin_date
