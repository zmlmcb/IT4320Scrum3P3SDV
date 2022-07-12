# api_call
import json

import requests
import datetime
import pandas as pd


def retrieve_date_range(data, bd, ed):
    if bd == 0 and ed == 0:
        return data
    else:
        data_ranged = data.loc[bd: ed]
        return data_ranged


def graph_data(data, ct, bd, ed):
    data = retrieve_date_range(data, bd, ed)
    print(data)


def api_call(ss, ct, ts, bd, ed):
    if ts == "1":
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ss + \
              '&interval=5min&outputsize=compact&apikey=2C4AFL520Q27QCZ9'
        record_path = "Time Series (5min)"
    elif ts == "2":
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ss + \
              '&outputsize=full&apikey=2C4AFL520Q27QCZ9'
        record_path = "Time Series (Daily)"
    elif ts == "3":
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=' + ss + '&apikey=2C4AFL520Q27QCZ9'
        record_path = "Weekly Time Series"
    else:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + ss + '&apikey=2C4AFL520Q27QCZ9'
        record_path = "Monthly Time Series"
    print(url)
    r = requests.get(url)
    data = r.json()

    if 'Error Message' in data:
        print("There was an error in your request, please try again.")
        return 1

    json_str = json.dumps(data[record_path])
    data_df = pd.read_json(json_str)
    data_df = data_df.T
    data_df.sort_index(inplace=True, ascending=True)

    graph_data(data_df, ct, bd, ed)

    return 0


# exit_prompt
def exit_prompt():
    x = input("\nWould you like to view more stock data? Enter 'y' to continue, or 'n' to exit:   ")
    if x == 'n':
        print("Thank you and Goodbye!\n")
        return 0
    elif x == 'y':
        return 1
    else:
        print("Invalid Value: please pick either 'y' or 'n'")
        exit_prompt()


if __name__ == "__main__":

    while 1:
        stock_symbol = "GOOGL"
        chart_type = "2"
        time_series = "1"
        if time_series != "1":
            begin_date = datetime.date(2020, 8, 1)
            end_date = datetime.date(2020, 10, 31)
        else:
            print('intraday does not support a specified date range, the last two months of intraday values will be'
                  ' displayed')
            begin_date = 0
            end_date = 0

        ec = api_call(stock_symbol, chart_type, time_series, begin_date, end_date)
        if ec == 0:
            if exit_prompt() == 0:
                break
        else:
            print("This is a testing point, normally loop but dont want to lock")
            if exit_prompt() == 0:
                break


