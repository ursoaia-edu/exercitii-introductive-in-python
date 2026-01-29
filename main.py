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

valoarea_maxima = -9999999

for i in a:
    if valoarea_maxima < i:
        valoarea_maxima = i

print(valoarea_maxima)




