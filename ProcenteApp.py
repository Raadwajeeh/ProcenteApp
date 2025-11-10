print("Welkom bij de Procente App!")

print("Welk type procentsom wil je oplossen; maak je keuze:")
print("[1] Hoeveel is x% van y?")
print("[2] Hoeveel % is x van y?")
print("[3] x neemt toe met y%; hoeveel heb je nu?")
print("[4] x neemt af met y%; hoeveel heb je nu?")
print("[5] x neemt toe van oud → nieuw; met hoeveel %?")
print("[6] x neemt af van oud → nieuw; met hoeveel %?")
print("[7] Terugrekenen na toename (nieuw bekend, oud onbekend)")
print("[8] Terugrekenen na afname (nieuw bekend, oud onbekend)")
print("[0] Stoppen")

choice = input("Welke optie kies je? ")

match choice:

    case "1":
        x = float(input("Wat is x (% getal)? "))
        y = float(input("Wat is y (basis)? "))
        answer = x / 100 * y
        print(f"De vraag is: hoeveel is {x}% van {y}?")
        print(f"Het antwoord is: {answer:.2f}")
        print(f"De berekening is: {x}% = {x/100} en {x/100} x {y} = {answer:.2f}")

    
    case "2":
        x = float(input("Wat is x? "))
        y = float(input("Wat is y? "))
        if y == 0:
            print("Let op: je kunt niet delen door 0.")
        else:
            answer = x / y * 100
            print(f"De vraag is: hoeveel % is {x} van {y}?")
            print(f"Het antwoord is: {answer:.2f}%")
            print(f"De berekening is: {x} : {y} = {x/y:.4f}; {x/y:.4f} x 100 = {answer:.2f}%")

    
    case "3":
        x = float(input("Wat is de basiswaarde? "))
        y = float(input("Met hoeveel % neemt het toe? "))
        factor = 1 + y / 100
        answer = x * factor
        print(f"De vraag is: {x} neemt toe met {y}%; hoeveel is het nu?")
        print(f"Het antwoord is: {answer:.2f}")
        print(f"De berekening is: 1 + {y/100} = {factor}; {factor} x {x} = {answer:.2f}")

    
    case "4":
        x = float(input("Wat is de basiswaarde? "))
        y = float(input("Met hoeveel % neemt het af? "))
        factor = 1 - y / 100
        answer = x * factor
        print(f"De vraag is: {x} neemt af met {y}%; hoeveel is het nu?")
        print(f"Het antwoord is: {answer:.2f}")
        print(f"De berekening is: 1 - {y/100} = {factor}; {factor} x {x} = {answer:.2f}")

    
    case "5":
        oud = float(input("Wat was de oude waarde? "))
        nieuw = float(input("Wat is de nieuwe waarde? "))
        if oud == 0:
            print("Let op: oude waarde mag niet 0 zijn.")
        else:
            factor = nieuw / oud
            perc = (factor - 1) * 100
            print(f"De vraag is: van {oud} naar {nieuw}, hoeveel % toename?")
            print(f"Het antwoord is: {perc:.2f}%")
            print(f"De berekening is: {nieuw} : {oud} = {factor:.4f}; ( {factor:.4f} - 1 ) x 100 = {perc:.2f}%")

    
    case "6":
        oud = float(input("Wat was de oude waarde? "))
        nieuw = float(input("Wat is de nieuwe waarde? "))
        if oud == 0:
            print("Let op: oude waarde mag niet 0 zijn.")
        else:
            factor = nieuw / oud
            perc = (1 - factor) * 100
            print(f"De vraag is: van {oud} naar {nieuw}, hoeveel % afname?")
            print(f"Het antwoord is: {perc:.2f}%")
            print(f"De berekening is: {nieuw} : {oud} = {factor:.4f}; (1 - {factor:.4f}) x 100 = {perc:.2f}%")

    
    case "7":
        nieuw = float(input("Wat is de nieuwe waarde (na toename)? "))
        p = float(input("Met hoeveel % is het toegenomen? "))
        factor = 1 + p / 100
        oud = nieuw / factor
        print(f"De vraag is: nieuw = {nieuw} na toename van {p}%; wat was oud?")
        print(f"Het antwoord is: {oud:.2f}")
        print(f"De berekening is: oud = nieuw / (1 + {p/100}) = {nieuw} / {factor} = {oud:.2f}")

    
    case "8":
        nieuw = float(input("Wat is de nieuwe waarde (na afname)? "))
        p = float(input("Met hoeveel % is het afgenomen? "))
        factor = 1 - p / 100
        if factor == 0:
            print("Let op: afname 100% betekent dat de oude waarde oneindig groot zou zijn!")
        else:
            oud = nieuw / factor
            print(f"De vraag is: nieuw = {nieuw} na afname van {p}%; wat was oud?")
            print(f"Het antwoord is: {oud:.2f}")
            print(f"De berekening is: oud = nieuw / (1 - {p/100}) = {nieuw} / {factor} = {oud:.2f}")

    case "0":
        print("Programma beëindigd. Tot ziens!")
    case _:
        print("Onbekende keuze. Probeer opnieuw.")
