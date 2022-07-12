# api_call
import requests


def retrieve_date_range(data, bd, ed):
    data_ranged = data
    return data_ranged


def graph_json_data(data, ct, bd, ed):
    data_range = retrieve_date_range(data, bd, ed)


def api_call(ss, ct, ts, bd, ed):
    if ts == "1":
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ss + \
              '&interval=5min&apikey=2C4AFL520Q27QCZ9'
    elif ts == "2":
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ss + \
              '&outputsize=full&apikey=2C4AFL520Q27QCZ9'
    elif ts == "3":
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=' + ss + '&apikey=2C4AFL520Q27QCZ9'
    else:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + ss + '&apikey=2C4AFL520Q27QCZ9'
    print(url)
    r = requests.get(url)
    data = r.json()
    if 'Error Message' in data:
        print("There was an error in your request, please try again.")
        return 1

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
        time_series = "2"
        begin_date = "1994-08-01"
        end_date = "1994-08-31'"

        ec = api_call(stock_symbol, chart_type, time_series, begin_date, end_date)
        if ec == 0:
            if exit_prompt() == 0:
                break
        else:
            print("This is a testing point, normally loop but dont want to lock")
            if exit_prompt() == 0:
                break


