'''
    Method to add values rows and columns in list

    @param list: array
    @return: void
'''
def addValuesList(list):
    rows = int(input("Rows: "))
    columns = int(input("Columns: "))

    for i in range(rows):
        row = []
        list.append(row)
        for x in range(columns):
            list[i].append(int(input("Input a number: ")))


'''
    Method to read value in list

    @param list: array
    @return: void
'''
def readValueList(list):
    for i in range(len(list)):
        print(list[i])


'''
    Method to sum values in list

    @param list: array
    @return: void
'''
def sumValues(list):
    for i in range(len(list)):
        for x in range(len(list[i])):
            if x == len(list[i])-1:
                list[i].append(sum(list[i]))


'''
    Method to add new row in list

    @param list: array
    @return: void
'''
def newRow(list):
    sumList = 0
    for i in range(len(list)+1):
        if i == len(list):
            row = []
            list.append(row)
    for x in range(len(list)):
        if x == len(list)-1:
            for y in range(len(list)-1):
                for z in range(len(list)-1):
                    sumList += list[z][y]
                list[x].append(sumList)
                sumList = 0


list = []
addValuesList(list)
readValueList(list)
sumValues(list)
readValueList(list)
newRow(list)
readValueList(list)
