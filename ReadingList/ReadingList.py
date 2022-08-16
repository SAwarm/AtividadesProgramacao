def inputNumber(message):
    return int(input(message))


def messageInputNumber():
    return "Input a number: "


def errorMessage():
    print("Invalid input")
    exit()


def showList(list):
    for i in range(len(list)):
        print(i, ':', list[i])


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


list = []
readingList(list)
moveIndexList(list)
