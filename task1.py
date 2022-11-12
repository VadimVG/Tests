import sys
try:
    var1=sys.argv[1]
    var2=sys.argv[2]
    n=int(var1)
    m=int(var2)
    if (n < 0 or n > 2147483647) or (m < 0 or m > 2147483647):
        print('Введите число от 0 до 2 147 483 647')
    else:
        i = 1
        while True:
            print(i, end="")
            i = 1+(i+m-2) % n
            if i == 1:
                break
except (IndexError, ValueError):
    print('Неверное кол-во аргументов или тип данных')








































