def infinityloop():
    a = int(input("введите цифру a:"))
    b = int(input("введите цифру b:"))
    c = int(input("введите цифру c:"))
    results = [a, a + c, b]
    if a < b:
        print('щось сумне')
        a += c
    if a < b is True:
        while a < b:
            a += c
            print('щось сумне')
            break
    if a >= b:
        print('щось дуже радісне', results)
    if __name__ == '__main__':
        infinityloop()


































































