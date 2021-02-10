
import os # os = operating system
# 讀取檔案
def read_file(filename):
    proudcts = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            proudcts.append([name, price])
    return proudcts # 回傳清單(proudcts = [])

# 讓使用者輸入
def user_input(proudcts):
    while True:
        name = input('請輸入商品名稱： ')
        price = input('請輸入商品價格： ')
        proudcts.append([name, price]) 

        c = input('要繼續輸入？(q:離開)')
        if c == 'q':
            break
    print(proudcts)
    return proudcts # 回傳參數(proudcts[]) 

# 印出所有購買記錄
def print_products(proudcts):
    for p in proudcts:
        print(p[0],'的價格是', p[1])

# 寫入檔案
def write_file(filename, proudcts):
    with open(filename, 'w', encoding='utf-8') as f: 
        f.write('商品,價格\n') 
        for p in proudcts:
            f.write(p[0] + ',' + p[1] + '\n')

def main():
    filename = 'proudcts.csv'
    if os.path.isfile(filename):# 檢查檔案在不在
        print('有此檔案')
        proudcts = read_file(filename)
    else:
        print('沒有此檔案...')

    proudcts = user_input(proudcts)
    print_products(proudcts)# 檢查輸入有沒有對
    write_file('proudcts.csv', proudcts)

main()