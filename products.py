import os # operating system

products = [] # 寫在最初是為了無論找不找的到檔案，都要執行
if os.path.isfile('products.csv'):  # 作業系統中的模組path中其中一個功能isfile，檢查檔案在不在
    print('找到檔案了！') # 找完檔案要開始讀取檔案！！
    with open('products.csv', 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue # 跳過它，繼續
            s = line.strip().split(',') # split變成一塊一塊的東西，s為清單
            name = s[0]
            price = s[1]
            # 6～7進階，直接把name, price取代4的s
            products.append([name, price])
    print(products)

else:
    print('找不到檔案Q_Q')

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入商品價格： ')
    price = int(price)
    products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
    print(p[0], '的價格', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')    