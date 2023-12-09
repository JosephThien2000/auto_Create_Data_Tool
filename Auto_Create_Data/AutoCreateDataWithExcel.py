# Thêm vào các thư viện cần thiết
import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile
import random
import tkinter.messagebox as mbox
from xlsxwriter import *

# gán các biến và các giá trị của chúng
user_list = ['Nhà cung cấp', 'Khách']
state_list = ['HỦY', 'KHÔNG HỦY']
user = []
state= []
value = []
coin = []
point = []
voucher = []
voucher_percent = []
sale_amount = []

# Hàm tạo dữ liệu tự động và lưu lại ở dạng file excel
def auto_Create_Data(num):
    # Số dòng dữ liệu muốn tạo
    for i in range(int(num)):
        sale_amount_rand = random.randint(100,1000)
        coin_rand = sale_amount_rand * 0.1
        voucher_rand = sale_amount_rand * 0.3
        point_rand = random.choice([sale_amount_rand*0.9, sale_amount_rand])
        user_rand = random.choice(user_list)
        state_rand = random.choice(state_list)
        # coin_rand = random.randint(1,100)
        # point_rand = random.randint(1,10)
        # voucher_rand = random.randint(1,5)
        voucher_percent_rand = f"{random.randint(1,5)}%" # ???
        # sale_amount_rand = random.randint(100,10000)
        # user_rand = random.choice(user_list)
        # state_rand = random.choice(state_list)

        value_rand = 0

        if user_rand == 'Khách' and state_rand == 'HỦY':
            value_rand = random.randint(100, 1000)

        user.append(user_rand)
        state.append(state_rand)
        value.append(value_rand)
        coin.append(coin_rand)
        point.append(point_rand)
        voucher.append(voucher_rand)
        voucher_percent.append(voucher_percent_rand)
        sale_amount.append(sale_amount_rand)

    df = pd.DataFrame(
        {
            'XU': coin,
            'POINT': point,
            'VOUCHER': voucher,
            'VOUCHER(%)': voucher_percent,
            'GIÁ TRỊ ĐƠN HÀNG($)': sale_amount,
            'USER': user
            , 'STATE': state
            , 'VALUE': value
        }
    )

    writer = ExcelWriter('data.xlsx')
    df.to_excel(writer, 'Sheet1', index=False)
    writer.close() # The save() method has been deprecated and removed in Pandas. You should use close() instead.
    mbox.showinfo("Information", "Create successfully!")