stars = input('Введите строку из пробелов, начиная и заканчивая символом * : ')
strs = 0
for i in range(0, len(stars)-1):
    strs = '*' + i*' ' + '*'
    print(strs)
