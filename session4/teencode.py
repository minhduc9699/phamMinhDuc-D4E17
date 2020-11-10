teencode = {
    'hc': 'học',
    'vk': 'vợ',
    'ck': 'chồng',
}

while True:
    for key in teencode:
        print(key, end='\t')
    print()
    print('*'*20)

    your_code = input('your code?')
    if your_code in teencode:
        print('its mean: ', teencode[your_code])
    else:
        choice = input('not found, do you want to contribute this word? (Y/N) ').lower()
        if choice == 'y':
            meaning = input('Enter your trans: ')
            teencode[your_code] = meaning
        else:
            print('thank you')
            break