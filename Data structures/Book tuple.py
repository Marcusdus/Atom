# Tuple are list that don`t change(immutable) and use blackets instead of squares

Kigali = ('Kicukiro', 'Rugende', 'Kabuga', 'Gacingiro') # creating tuple
print(Kigali)
print(Kigali[2])
print(Kigali[3])

for i in Kigali:
    print(i)

# Quiz 5

Buffet = ('Ibishyimbo', 'Ibirayi', 'Ifiriti', 'Umureti', 'Inyama')

for w in Buffet:
    print(w)

Buffet = ('Ibishyimbo', 'Ibijumba', 'Ifiriti', 'Umuceri', 'Inyama') # overwriting a Tuple.

for a in Buffet:
    print(a)

lyon1 = {'color': 'green', 'points' : 5}
lyon2 = {'colori': 'greeni', 'pointsi' : 6}
lyons3 = {colore': 'greene', 'pointse' : 8}

lyon = [lyon1, lyon2, lyon3]  # list of dictionaries

for w in lyon:
    print(w)
sisters = []

for Ynumber in range(30):
    Ynumber = {'color': 'green', 'points' : 5, 'speed': 'slow'}
    sisters.append(Ynumber)

for z in sisters[:5]:
    print(z)

print("...")

football = {
 'champions' : ['real', 'barca'],
 'worldcup' : ['C'],
 'premier' : ['Arsenal','Man united'],
}

print(football)
