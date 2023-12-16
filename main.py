try:
    number_1 = int(input('Введіть зарплату за місяць: '))
    number_2 = int(input('Введіть платіж за кредит: '))
    number_3 = int(input(' Введіть платіж за комунальні послуги: '))
    print( 'Залишок заробітньої плати: ', number_1 - number_2 -number_3)


except Exception as e:
    print(e)