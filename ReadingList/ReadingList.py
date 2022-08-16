'''
    Method to return int input from user

    @param message: string message
    @return: int input
'''
def inputNumber(message):
    return int(input(message))


'''
    Method to return message used in int input from user

    @return: string message
'''
def messageInputNumber():
    return "Input a number: "


'''
    Method to show list

    @param list: list
    @return: void
'''
def showList(list):
    for i in range(len(list)):
        print(i, ':', list[i])


'''
    Method to show error message

    @return: void
'''
def errorMessage():
    print("Invalid input")
    exit()


'''
    Method to reading list

    @param list: list
    @return: void
    @throws: exception
'''
def readingList(list):
    index = 0
    try:
        list.append(inputNumber(messageInputNumber()))
        while int(list[index]) > -1:
            list.append(inputNumber(messageInputNumber()))
            index += 1
        list.pop()
        showList(list)
    except:
        messageInputNumber()


'''
    Method to move index list

    @param list: list
    @return: void
    @throws: exception
'''
def moveIndexList(list):
    originIndex = inputNumber("Input the origin: ")
    finalIndex = inputNumber("Input the final: ")
    try:
        origin = list[originIndex]
        list.remove(list[originIndex])
        list.insert(finalIndex, origin)
        showList(list)
    except:
        messageInputNumber()


# variable list
list = []

# call method reading list
readingList(list)

# call method move index list
moveIndexList(list)
