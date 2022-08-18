'''
    Method to show warning

    @return void
'''
def initialWarning():
    print("Quit the program, input a number outside the interval of 0.0 to 10.0")


'''
    Method to received notes of user

    @return: array
'''
def inputNote():
    cont = 0
    notes = []
    while (1):
        try:
            note = float(input("Digite a nota do aluno: "))
            if (note <= 10 and note >= 0):
                notes.append(note)
                cont += 1
                continue
            break
        except Exception as e:
            print(e)
            continue
    return [
        {
            "notes": notes,
            "cont": cont
        }
    ]


'''
    Method to show report

    @param totalNotes: int
    @param notes: array
    @param minNotes: int
    @return: void
'''
def reportNotes(totalNotes, notes, minNotes):
    if (totalNotes >= minNotes):
        HigherNote(notes)
        LowerNote(notes)
        return
    print("The min number notes is: ", minNotes)


'''
    Method to show Higher note

    @param notes: array
    @return: void
'''
def HigherNote(notes):
    print("Higher note: ", max(notes))


'''
    Method to show lower note

    @param notes: array
    @return: void
'''
def LowerNote(notes):
    print("Lower note: ", min(notes))


# Initial warning
initialWarning()

# Input notes array and show Higher and Lower note
response = inputNote()
reportNotes(response[0]["cont"], response[0]["notes"], 2)
