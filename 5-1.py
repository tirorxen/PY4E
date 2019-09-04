#題目說需要的是總和、輸入數、平均值的一個程式
num = 0
total = 0.0
while True:
    inpt = input('Enter a number: ')
    if inpt == 'done' :
        break
    try:
        floatinpt = float(inpt)
    except:
        print('Invalid input')
        continue
    num = num + 1
    total = total + floatinpt
print('total:',total,'number counts:',num,'average:',total/num)
