import sys
from support import block, start, intout, fin

with open(input("Введи имя файла кода (python) для преобразования в блоксхему (в формате txt)")) as fl:
    start()
    sp = fl.readlines()
    for i in range(len(sp)):
        lin = sp[i].strip()
        if "input" in lin:
            z = lin.split("=")
            a = intout(20, i+1, "Ввод " + z[0])
        elif "print" in lin:
            z = lin.split("(")
            a = intout(20, i + 1, "Вывод " + z[1][:-1])
        else:
            a = block(20, i+1, lin)
    a = fin(20, len(sp) + 1)
    print(fl.readline())
    a.show()

