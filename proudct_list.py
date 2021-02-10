
proudcts = []
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入商品價格： ')
    p = []
    p.append('商品：' + name)
    p.append('價格：' + price + '元') 
    proudcts.append(p)#建立雙重清單(二維清單)


print(proudcts)