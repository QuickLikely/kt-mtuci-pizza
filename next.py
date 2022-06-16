'''
Задача №14
Создайте файл numbers.txt и запишите в него натуральные числа, из массива которые имеют такую же сумму цифр что и максимальное число.

Входные данные:

122 121 131 67     12  13 500  14    5
результат 122 131 500 14 5

2      3      11    115
781 1000  235  7
95    5       16   25
125 19       21    11
Результат: Нет таких


'''


def summ(i):
    #сумма цифр
    s=0
    while i>0:
        i, g = divmod(i, 10)
        s+=g
    return (s)

c=open("numbers.txt", "w")
l=list(map(int, input("Введите числа").split()))
m=summ(max(l))
for i in l:
    pass
print(*l)
print(m)

