#讀取檔案
proudcts = []
with open('proudcts.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品,價格' in line:#過讀取'商品,價格'字串
            continue#跳到下一迴
        name, price = line.strip().split(',')
        proudcts.append([name, price])
print(proudcts)#檢查上面有沒有coding對

#讓使用者輸入
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入商品價格： ')

    proudcts.append([name, price]) 
print(proudcts)

#印出所有購買記錄
for p in proudcts:
    print(p[0],'的價格是', p[1])

#寫入檔案
with open('proudcts.csv', 'w', encoding='utf-8') as f: 

    f.write('商品,價格\n') 
    for p in proudcts:
        f.write(p[0] + ',' + p[1] + '\n')
