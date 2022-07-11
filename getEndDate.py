import datetime

def getEndDate():

    try:

        inputEndDate = input("Please enter the end date of the data in YYYY-MM-DD format: ")

        endDate = datetime.datetime.strptime(endingDate, "%Y-%m-%d").date()

    except DateError:

            if endDate <= begin_date:

                print("The ending date must not be before the beginning date.")

    else:
    
            return endDate
    
getEndDate();
