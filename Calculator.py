# coding=utf-8

import Funktionen

print("Willkommen bei Deinem persönlichen Taschenrechner.")

a = 0
b = 0
operator = None
bedingung = True

while bedingung:

	operator = raw_input(
		"Welche Rechenart möchtest du durchführen? (' + ' - ' / ' * ' quadrat ' log ' wurzel') ").strip()

	if operator in ["+", "-", "/", "*"]:

		try:
			a = int(raw_input("Wie lautet die erste Zahl? ").strip())
			b = int(raw_input("Wie lautet die zweite Zahl? ").strip())
		except:
			print("\n")
			print("Es ist ein Fehler aufgetreten! Bitte überprüfe deine Eingaben")


	elif operator in ["log", "wurzel", "quadrat"]:

		try:
			a = int(raw_input("Wie lautet Ihre Zahl: ").strip())
		except Exception as error:
			print("Es ist ein Fehler aufgetreten! Bitte überprüfe deine Eingabe.")
			continue

	if operator == "+":
		result = Funktionen.addition(a, b)
		print("Ergebnis: " + str(result))

	elif operator == "-":
		result = Funktionen.subtraktion(a, b)
		print("Ergebnis: " + str(result))

	elif operator == "/":
		result = Funktionen.division(a, b)
		print("Ergebnis: " + str(result))

	elif operator == "*":
		result = Funktionen.multiplikation(a, b)
		print("Ergebnis: " + str(result))

	elif operator == "log":
		result = Funktionen.logarithmus(a)
		print("Ergebnis: " + str(result))

	elif operator == "quadrat":
		result = Funktionen.quadrat(a)
		print("Ergebnis: " + str(result))

	elif operator == "wurzel":
		result = Funktionen.wurzel(a)
		print("Ergebnis: " + str(result))

	decision = raw_input("Möchten Sie es erneut versuchen? Antworten Sie mit Ja oder Nein: ").strip()
	if decision == "Nein":
		bedingung = False