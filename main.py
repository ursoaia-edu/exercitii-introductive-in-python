'''Realizați un program care citește de la tastatură un șir 
de caractere și 
afișează de câte ori apare litera "a" în text.'''


text = input('Introdu textul: ')

count = text.count('a')

print(f'Simbolul a apare de: {count} ori')


'''Calculează aria unui dreptunghi folosind 
lățimea și lungimea introduse de utilizator.'''

lungimea = int(input('Introdu lungimea: '))
latimea = int(input('Introdu latimea: '))

aria = lungimea * latimea

print(f'Aria dreptunghiului este: {aria}')


'''Transformă temperatura din Celsius în Fahrenheit'''

# înmulțiți temperatura în Celsius cu 1,8 și adăugați 32

celsiu = 13

fahrenheit = celsiu * 1.8 + 32

print(f'{celsiu} grade celsius sunt egale cu {fahrenheit} Fahrenheit')



'''Afișează primul și ultimul caracter dintr-un șir 
introdus de utilizator'''

text = input('Introdu textul: ')

print(text)
print(f'primul caracter este: {text[0]}, iar ultimul caracter este: {text[-1]}')


'''Calculează media a trei numere'''

a = int(input('introdu primul numar: '))
b = int(input('introdu al doilea numar: '))
c = int(input('introdu al treilea numar: '))


media =(a + b + c) // 3

print(f'Media numerelor {a}, {b} si {c} este {media}')


'''Determină cea mai mare valoare dintre trei numere.'''

a = [-1, -12, -10]

valoarea_maxima = None

for i in a:
    if valoarea_maxima == None:
        valoarea_maxima = i
    elif valoarea_maxima < i:
        valoarea_maxima = i

print(valoarea_maxima)

'''Scrie un program care calculează suma 
valorilor pare dintr-o listă.'''

lista = []

while True:
    element = input('Introdu un element: ')
    if element == 'x':
        break
    lista.append(int(element))
    
suma = 0

for i in lista:
    if i % 2 == 0:
        suma = suma + i

print(f'Suma elementelor pare este: {suma}')


'''Creează o listă cu 10 numere și 
afișează doar cele mai mari decât 5'''

lista = []

while True:
    element = input('Introdu un element: ')
    if len(lista) == 10:
        break
    lista.append(int(element))

elemente_mai_mari_ca_5 = []

for i in lista:
    if i > 5:
        elemente_mai_mari_ca_5.append(i)

print(f'Lista initiala: {lista}')
print(f'Lista finala: {elemente_mai_mari_ca_5}')


'''Folosește o expresie condițională pentru a decide 
dacă un elev a promovat.'''

nota = int(input('Introdu nota elevului: '))

if nota < 0 or nota > 10:
    print('Eroare')
else:
    if nota >= 5:
        print('Elevul este promovat')
    else:
        print('Elevul nu este promovat')


'''Creează un program care calculează vârsta pe 
baza anului de naștere.'''

anul_curent = 2026

anul_nasterii = int(input('Introdu anul nasterii: '))

virsta = anul_curent - anul_nasterii

print(f'Virsta este: {virsta}')




