'''
rò chơi đoán số
o Mô tả: Xây dựng một trò chơi đoán số với số ngẫu nhiên.
o Áp dụng: Kỹ năng sử dụng vòng lặp, thư viện random, và lưu kết quả chơi
vào file CSV.
'''
import json
import  random
def run():
    while True:
        arr = []
        n = int(input("mời bạn nhập vào số: "))
        for i in range(5):
            ngauNhien = random.randint(1, 10)
            arr.append(ngauNhien)
            if ngauNhien == n:
                print('chọn đúng')
        print('các số đã radom đc là : ',arr)
        try:
            with open('./gio_hang.json',mode='w') as f:
                json.dump(arr,f)
        except FileNotFoundError:
            print(FileNotFoundError)
        if n == -1:
                return
run()