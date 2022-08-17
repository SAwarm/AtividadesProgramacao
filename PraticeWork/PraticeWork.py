# Variable list of situations/options
option = [
    {
        "amount": 0,
        "name": "Defective mice on ball",
    }, {
        "amount": 0,
        "name": "Mice need cleaning",
    }, {
        "amount": 0,
        "name": "Mice need to change the cable connector",
    }, {
        "amount": 0,
        "name": "Broken or unused Mice"
    }
]

'''
    Method to get option array variable

    @return: array
'''
def getOptionArray():
    return option


'''
    Method to validate input number

    @param input: int input
    @return: boolean
'''
def validInput(input):
    return input != 0


'''
    Method to show report

    @param array: array
    @return: void
'''
def report(array):
    for i in range(len(array)):
        print(array[i]["amount"],
              "mouses with", array[i]["name"])


'''
    Method to read situation and push into array

    @param inputDigit: int input
    @return: void
'''
def inputSituation(inputDigit):
    while (validInput(inputDigit)):
        inputDigit = int(
            input("Input the situation: (input the number zero for quit of program) "))
        try:
            if (validInput(inputDigit)):
                getOptionArray()[inputDigit -
                                 1]["amount"] += int(input("Input the quantity of mice: "))
                continue
            print("\n")
        except Exception as e:
            print(e)


'''
    Method to read situation specific and show option array

    @param inputDigit: int input
    @return: void
'''
def whatSituation(inputDigit):
    while (validInput(inputDigit)):
        inputDigit = int(input(
            "What a situation you want search? (input the number zero for quit of program and show report) \n"))
        try:
            if (validInput(inputDigit)):
                print(getOptionArray()[inputDigit - 1]["amount"], "mouses with",
                      getOptionArray()[inputDigit - 1]["name"], "\n")
                continue
            print("\n")
        except Exception as e:
            print(e)


# inputSituation(1) read situation and push into array
inputDigit = 1
inputSituation(inputDigit)

# whatSituation(1) read situation specific and show option array
inputDigit = 1
whatSituation(inputDigit)

# report(option) show report all situations
report(getOptionArray())
