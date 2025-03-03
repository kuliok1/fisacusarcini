breaker = "------------------------------"
print(breaker)

#1) afisarea numarului impar si par (by Leonid Curachin)
num = int(input("Introduceti numarul pentru a fi identificat daca este par sau impar: "))
if (num % 2) == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")
print(breaker)

#2) compararea a doua numere (by Leonid Curachin)
num1 = int(input("Introduceti primul numar: "))
num2 = int(input("Introduceti al doilea numar: "))
if num1 > num2:
    print(f"{num1} > {num2}")
else:
    print(f"{num2} > {num1}")
print(breaker)

#3) compararea a unui numar cu 0 (by Leonid Curachin)
num = int(input("Introduceti primul numar pentru a-l compara cu 0: "))
if num > 0:
    print(f"{num} este pozitiv")
elif num == 0:
    print(f"{num} este egal cu 0")
else:
    print(f"{num} este negativ")
print(breaker)

#4) compararea a trei numere intre ele (by Leonid Curachin)
num1 = input("Introduceti primul numar: ")
num2 = input("Introduceti al doilea numar: ")
num3 = input("Introduceti al treilea numar: ")
if int(num1) > int(num2) > int(num3):
    print(f"{num1} > {num2} > {num3}")
elif int(num2) > int(num1) > int(num3):
    print(f"{num2} > {num1} > {num3}")
elif int(num3) > int(num1) > int(num2):
    print(f"{num3} > {num1} > {num2}")
elif int(num1) > int(num3) > int(num2):
    print(f"{num1} > {num3} > {num2}")
elif int(num2) > int(num3) > int(num1):
    print(f"{num2} > {num3} > {num1}")
elif int(num3) > int(num2) > int(num1):
    print(f"{num3} > {num2} > {num1}")
print(breaker)

#5) verificarea unui an daca este bisect (by Leonid Curachin)
year = int(input("Introduceti anul: "))
breakers = "Codul este lui Leonid Curachin"
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Anul introdus este bisect")
else:
    print("Anul introdus nu este bisect")
print(breaker)

#6) calcularea reducerii (by Leonid Curachin)
price = float(input("Introduceti pretul produsului: "))
if price >= 100: 
    price = price * (1 - (10/100))
    print(f"Pretul final = {price}")
else:
    price = price * (1 - (5/100))
    print(f"Pretul final = {price}")
print(breaker)

#7) verificarea varstei (by Leonid Curachin)
age = int(input("Introduceti varsta dvs.: "))
if age >= 18:
    print(f"La {age} ani puteti obtine permis de conducere!")
else: 
    print(f"La {age} nu puteti primi permis de conducere")
print(breaker)

#8) clasificarea notei
grade = input("Introduceti nota obtinuta in forma de cifra (1-10): ")
if int(grade) >= 9:
    print("Calificativul dvs. este Foarte Bine!")
elif int(grade) < 9 and int(grade) >= 7:
    print("Calificativul dvs. este Bine!")
elif int(grade) < 7 and int(grade) >=5:
    print("Calificativul dvs. este Satisfacator!")
else:
    print("Calificativul dvs. este insuficient :(")
print(breaker)

#9) verificarea daca caracterul introdus este vocala sau consoana (by Leonid Curachin)
car = input("Introduceti litera dvs.: ")
vocale = "aeiouăâîAEIOUĂÂÎ"
if car.isalpha():
    if car in vocale:
        print(f"{car} este vocala!")
    else:
        print(f"{car} este consoana")
else:
    print("Te rog introdu un singur caracter!")
print(breaker)

#10) verificarea unui interval (by Leonid Curachin)
num = input("Introduceti un numar: ")
if float(num) >= 10 and float(num) <= 20:
    print(f"{num} este intre 10-20")
else:
    print(f"{num} nu este intre 10-20")
print(breaker)

#11) verificarea a doua numere daca sunt egale (by Leonid Curachin)
num1 = input("Introduceti primul numar: ")
num2 = input("Introduceti al doilea numar: ")
if int(num1) != int(num2):
    print(f"{num1} nu este egal cu {num2}")
else:
    print(f"{num1} este egal cu {num2}")
print(breaker)

#12) verificarea a doua litere daca sunt majuscule sau minuscule (by Leonid Curachin)
car = input("Introducti o litera: ")
if car.isalpha():
    if car.isupper():
        print(f"{car} este liera MAJUSCULA")
    else: 
        print(f"{car} este litera minuscula")
else: 
    print("Ati introdus un caracter gresit!!")
print(breaker)

#13) Clasificarea temperaturii (by Leonid Curachin)
temp = float(input("Introduceti temperatura in Celsius: "))
if temp <= 0:
    print("Temperatura introdusa este de inghet!")
elif temp > 0 and temp < 30:
    print("Temperatura introdusa este normala")
else:
    print("Temperatura introdusa este canicula!")
print(breaker)

#14) verificarea daca triunghiul este posibil de format (by Leonid Curachin)
lat1 = float(input("Introduceti lungimea primei laturi: "))
lat2 = float(input("Introduceti lungimea a celei de a doua latura: "))
lat3 = float(input("Introduceti lungimea a celei de a treaia latura: "))
sorted_nums = sorted([lat1, lat2, lat3])
if sorted_nums[0] + sorted_nums[1] >= sorted_nums[2]:
    print("Triunghiul poate fi format!")
else:
    print("Triunghiul nu poate fi format")
print(breaker)

#15) verificarea unui numar daca este multiplu lui cinci (by Leonid Curachin)
num = input("Introduceti un numar: ")
if int(num) % 5 == 0:
    print(f"{num} este multiplul lui 5")
else: 
    print(f"{num} nu este multiplul lui 5")
print(breaker)

#16) verificarea validitatea unui triunghi (by Leonid Curachin)
ug1 = float(input("Introduceti primul unghi al triunghiului: "))
ug2 = float(input("Introduceti al doilea unghi al triunghiului: "))
ug3 = float(input("Introduceti al treilea unghi al triunghiului: "))
if ug1 + ug2 + ug3 == 180:
    print("Triunghiul este valid!")
else: 
    print("Tringhiul este nevalid")
print(breaker)

#17) clasificarea orei (by Leonid Curachin)
time = int(input("Introduceti ora in format de 24h: "))
if time >= 0 and time <= 11: 
    print("Este dimineata!")
elif time > 11 and time <= 17:
    print("Este amiaza!")
else:
    print("Este noaptea!")
print(breaker)

#18) TVA (by Leonid Curachin)
pret = float(input("Introduceti pretul produsului: "))
if pret >= 50:
    tva = 0.19 * pret
    pret_final = pret + tva
    print(f"Pretul initial = {pret} unitati")
    print(f"TVA (19%) = {tva} unitati")
    print(f"Pretul final cu TVA = {pret} unitati")
else: 
    print(f"Pretul nu depaseste 50 de unitati, nici un TVA nu se aplica. Pretul final = {pret}")
print(breaker)

#19) clasificarea varstei (by Leonid Curachin)
age = input("Introduceti varsta dvs.: ")
if int(age) >= 0 and int(age) <=  12:
    print("Sunteti copil")
elif int(age) > 12 and int(age) <= 17:
    print("Sunteti adolescent")
else:
    print("Sunteti adult")
print(breaker)

#20) verificarea daca numarul este divizibil cu 3 sau 7 (by Leonid Curachin)
num = input("Introduceti un numar: ")
if int(num) % 3 == 0:
    print(f"{num} este divizibil cu 3")
elif int(num) % 7 == 0:
    print(f"{num} este divizibil cu 7")
elif int(num) % 3 == 0 and int(num) % 7 == 0:
    print(f"{num} este divizibil cu 3 si 7")
print(breakers)