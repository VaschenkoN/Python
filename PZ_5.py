x = int(input ("Введите выручку: "))
y = int(input ('Введите издержки: '))
if x > y:
    print ('Прибыль')
else:
    print ("Убыток")
a = x - y
if x > y:
    print (a)
z = int(input ("Введите количество сотрудников: "))
b = a / z
print ("Прибыль одного сотрудника:" , b)

