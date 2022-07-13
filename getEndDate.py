import datetime

def getEndDate(begin_date):
   
    inputEndDate = input("Enter the end date (YYYY-MM-DD): ")
    try:
        endDate = datetime.datetime.strptime(inputEndDate, "%Y-%m-%d").date()
    except:
      
        print("Please enter a end date with the format YYYY-MM-DD: ")
        return getEndDate(begin_date)

   
    if endDate <= begin_date:
        print("Error: Start date cannot be later than end date. Please enter the dates again.")
        return getEndDate(begin_date)
    else:
        return endDate

getEndDate(datetime.date(2020, 8, 1))
