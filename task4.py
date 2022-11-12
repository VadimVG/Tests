import sys
var=sys.argv[1]
try:
    f=open(var, 'r')
    l=[]
    for i in f:
        l.append(int(i.strip()))

    total_lst = sorted(l)[len(l) // 2]
    print(sum(abs(item - total_lst) for item in l))
except UnicodeError:
    print('Необходимо передать txt файл')
































