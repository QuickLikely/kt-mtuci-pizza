# Составьте программу вычисления количества элементов матрицы B (N, N),
# сумма цифр которых кратная 3. Матрица записана в файле

'''
3
125 121 137
67 12 13
51 114 15
'''


def summ(i):
    #сумма цифр
    s=0
    while i>0:
        i, g = divmod(i, 10)
        s+=g
    return (s)
c=open("dhbfh.txt", "r")
c.readline()
k=0
K=int(input("K= "))
for i in c.read().split():
    if summ(int(i))%K==0:
        k+=1
if k>0:
    print(k)
else: print ("Нет таких")