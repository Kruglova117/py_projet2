try:
    number_1 = float(input('Довжина однієї діагоналі: '))
    number_2 = int(input('Довжина другої діагоналі: '))
    print( 'Площа ромба: ', number_1 * number_2 / 2)


except Exception as e:
    print(e)