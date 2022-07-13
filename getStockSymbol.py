

def getStockSymbol():

    while True:

        SpecialCharacters = False
        userInput = input("Input a valid stock symbol: ")
        if 0 < len(userInput) <= 5:  #checks if user inputs a string between 1 and 5 characters
            for letter in userInput:
                if not letter.isdigit() and not letter.isalpha(): #checks if letter isn't a number or a letter
                    SpecialCharacters = True
                    print("please input a symbol with no special characters")
            if not SpecialCharacters:
                break
        else:
            print("please input a symbol of 5 characters or less")

    return userInput


getStockSymbol()