def initialWarning():
    print("Quit the program, input a number outside the interval of 0.0 to 10.0")


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


def reportNotes(cont, notes, minNotes):
    if (cont >= minNotes):
        HigherNote(notes)
        LowerNote(notes)
        return
    print("The min number notes is: ", minNotes)


def HigherNote(notes):
    print("Higher note: ", max(notes))


def LowerNote(notes):
    print("Lower note: ", min(notes))


initialWarning()

response = inputNote()
reportNotes(response[0]["cont"], response[0]["notes"], 2)
