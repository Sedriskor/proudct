
proudcts = []
x = 0
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入商品價格： ')
    # p = [] #小清單
    # p.append('商品：' + name) 
    # p.append('價格：' + price + '元') 
    # proudcts.append(p)#建立雙重清單(二維清單)
    proudcts.append(['商品：' + name, '價格：' + price + '元']) #簡寫
    x = x + 1

# print(x)
# print(proudcts)
# print(proudcts[0]) 
# #大清單的第一格內容(名稱＋價錢)
# print(proudcts[0][0])
# #大清單的第一格裡小清單的第一格內容(價錢)

for p in proudcts:#for loop
    print(p) #印出大清單
    print(p[0]) ##印出小清單

