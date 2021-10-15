stars = input('Введите строку из пробелов, начиная и заканчивая символом * : ')
strs = 0
for i in range(0,len(stars)):
    strs = '*' + i*' ' + '*'
    print(strs)
