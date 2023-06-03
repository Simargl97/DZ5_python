a = int(input("Введите первое неотрицительное число "))
b = int(input("Введите второе неотрицательно число "))


def rec_sum(a, b):
    if a == 0:
        return b
    else:
        return rec_sum(a - 1, b + 1)


print(rec_sum(a, b))