salary = []
numberChildrens = []


def readData(salary, numberChildrens):
    salary.append(int(input("What's your salary? ")))
    numberChildrens.append(int(input("How many children do you have? ")))
    index = 0
    while salary[index] != -1 and numberChildrens[index] != -1:
        salary.append(int(input("What's your salary? ")))
        numberChildrens.append(int(input("How many children do you have? ")))
        index += 1
    if salary[index] == -1 or numberChildrens[index]:
        salary.pop()
        numberChildrens.pop()
    return True


def averageValue(list):
    average = sum(list)/len(list)
    print("Average: ", average)


def maxValue(list):
    print("Max value", max(list))


def percentagePeopleSalary(list, n):
    countPeople = 0
    for i in range(len(list)):
        if (list[i] <= n):
            countPeople += 1
    percentage = (countPeople*100)/len(list)
    print("Percentage of people with the lower room than", n, ':', percentage, "%")


def report(list, name):
    for i in range(len(list)):
        print(name, ":", list[i])


readData(salary, numberChildrens)
averageValue(salary)
averageValue(numberChildrens)
maxValue(salary)
percentagePeopleSalary(salary, 350)
report(salary, "Salary")
report(numberChildrens, "Number of childrens")
