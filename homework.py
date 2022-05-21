def my_function():
  a = ('Python популярный язык програмирования.')
  b = ('Он был создан Гвидо ван Россумом.')
  age = ('выпущен в 1991 году.')
  print((a) + (b) + str(age))
  a = int(input("введите цифру a:"))
  b = int(input("введите цифру b:"))
  c = int(input("введите цифру c:"))
  if a > b:
    print('грустный текст')
  elif b > a and b > c:
    print('безгранично happy text')
  elif a == b:
    print('равные цифры')
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
my_function()



























































































































































































