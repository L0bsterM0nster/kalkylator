tal1 = float(input("Skriv in ett tal: "))
tal2 = float(input("Skriv in ett annat tal: "))
operator = input("vad vill du göra? +, -, *, /: ")

def addera(tal1, tal2):
    return tal1 + tal2

def subtrahera(tal1, tal2):
    return tal1 - tal2

def multiplicera(tal1, tal2):
    return tal1 * tal2

def dividera(tal1, tal2):
    return tal1 / tal2

if operator == "+":
    resultat = (addera(tal1, tal2))
elif operator == "-":
    resultat = (subtrahera(tal1, tal2))
elif operator == "*":
    resultat = (multiplicera(tal1, tal2))
elif operator == "/":
    if tal2 == 0:
        print("Går inte att dividera med 0")
    else:
        resultat = (dividera(tal1, tal2))
else:
    print("Ogiltig operator")

print("Resultat:",resultat)