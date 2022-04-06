# 1. Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# - если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# Если я передаю число, то смотрим:
# - произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

class StringOrNumber:

    def __init__(self):
        self.gl = []
        self.glas = 0
        self.sogl = []
        self.soglas = 0
        self.sum = 0

    def reshenie(self, a):
        if type(a) is str:
            for i in a:
                if i in 'eyuioa':
                    self.gl.append(i)
                    self.glas += 1
                else:
                    self.sogl.append(i)
                    self.soglas += 1
            if self.glas * self.soglas <= self.dlina(a):
                print(f'Все гласные в слове: {self.gl}')
            else:
                print(f'Все согласные в слове: {self.sogl}')
        elif type(a) is int:
            for i in str(a):
                i = int(i)
                if i % 2 == 0:
                    self.sum += i
            print(f'Произведение суммы чётных цифр на длину числа равно: {self.sum * self.dlina(a)}')

    def dlina(self, a):
        return len(str(a))


str_or_num = StringOrNumber()
b = input('Введите слово на английском языке или число: ')

if b.isalpha():
    str_or_num.reshenie(b)
elif b.isdigit():
    str_or_num.reshenie(int(b))
