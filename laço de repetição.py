while True:
    num = (int(input('digite um numero: ')))
    if num <= 0:
        break
    for cont in range (1, 10):
    print ('{} X {} = {}'.format(num,cont,num*cont))
