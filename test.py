def convert():
    number = 0
    symbol = ''
    value = 0
    while True:
        converter = input("npr to usd(n), usd to npr(u): ").lower()
        if converter == 'n' or converter == 'u':
            break
        else:
            continue
    while True:
        try:
            number = float(input("write the number: "))
            break
        except:
            continue
    if converter == 'n':
        value = number / 132.43
        symbol = '$'
    else:
        value = number * 132.43
        symbol = 'Rs'
    print(f"the price is {symbol}{value}")
convert()