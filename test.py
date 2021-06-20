from texttojson import text_to_json
from texttoarray import text_to_array


texto1 = """"e-mail","texto","Name", "Team", "Position", "Height(inches)", "Weight(lbs)", "Age"
"Adam@teste.com","texto longo","Adam Donachie", "BAL", "Catcher", 74, 180, 22.99
"Paul@teste.com","texto longo","Paul Bako", "BAL", "Catcher", 74, 215, 34.69
"Ramon@teste.com","texto longo","Ramon Hernandez", "BAL", "Catcher", 72, 210, 30.78
"Kevin@teste.com","texto longo","Kevin Millar", "BAL", "First Baseman", 72, 210, 35.43
"Chris@teste.com","texto longo","Chris Gomez", "BAL", "First Baseman", 73, 188,
"Brian@teste.com","texto longo","Brian Roberts", "BAL", "Second Baseman", 69, 176, 29.39
"Miguel@teste.com","texto longo","Miguel Tejada", "BAL", "Shortstop", 69, 209, 30.77
"Melvin@teste.com","textox
 longo aqui","Melvin Mora", "BAL", "Third Baseman", 71, 200, 35.07
 valor
"Aubrey@teste.com", "texto \"muito\" longo","Aubrey Huff", "BAL", "Third Baseman", 76, 231, 30.19

"Adam@teste.com","texto\\",longo,","Adam Stern", "BAL", "Outfielder",,,, campo extra
"Jeff@teste.com",",texto longo","Jeff\\ Fiorentino",, "Outfielder", 188, 23.88,
 

"""

texto2 = """"e-mail","texto"
"Adam@teste.com","texto, longo"
"Paul@teste.com","texto longo",campo extra 
"""

r, e = text_to_json(text=texto2)
print('Susses = ', len(r) == 1)
print(r[0]['e-mail'])
print("Fail: ", e[0])

r = text_to_array(text=texto1)
print('\nSusses = ', len(r) == 16)
print(r[2][0])

