# imports
import requests


# api_call
def api_call(ss, ct, ts, bd, ed):
    tsf = ""
    if ts == 1:
        tsf = "TIME_SERIES_INTRADAY"
    elif ts == 2:
        tsf = "TIME_SERIES_DAILY"
    elif ts == 4:
        tsf = "TIME_SERIES_WEEKLY"
    else:
        tsf = "TIME_SERIES_MONTHLY"
    url = 'https://www.alphavantage.co/query?function=' + tsf + '&symbol=' + ss + '&interval=5min&apikey=2C4AFL520Q27QCZ9'
    print(url)
    r = requests.get(url)
    data = r.json()

    print(data)

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
        time_series = "2"
        begin_date = "1994-08-01"
        end_date = "1994-08-31'"

        api_call(stock_symbol, chart_type, time_series, begin_date, end_date)
        if exit_prompt() == 0:
            break

