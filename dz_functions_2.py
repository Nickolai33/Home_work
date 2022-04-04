# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Если число – кол-во нечётных цифр.
# Если строка – кол-во букв.
# Сделать проверку со всеми этими случаями.

def func(a):
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    if type(a) is tuple:
        for i in a:
            b = len(i)
            c += b
        return f'Длина всех слов кортежа равна: {c}'
    elif type(a) is list:
        for i in a:
            if type(i) is int:
                d += 1
            elif type(i) is str:
                for j in i:
                    if j.isalpha():
                        e += 1
        return f'В этом списке количество букв - {e}, а чисел - {d}'
    elif type(a) is int:
        for i in str(a):
            i = int(i)
            if i % 2 != 0:
                f += 1
        return f'Количество нечётных цифр: {f}'
    elif type(a) is str:
        for i in a:
            if i.isalpha():
                g += 1
        return f'Количество букв: {g}'


print(func(('bohemian', 'rhapsody')))
print(func(['dog', 55, 'wow', 952, 'queen']))
print(func(6549865168))
print(func('Is this the real life?'))
