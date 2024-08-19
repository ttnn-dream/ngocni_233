# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:53:47 2024

@author: TranThiNgocNi
"""

N= int(input("Nhập vào số nguyên dương N có hai chữ số: "))

if 10<= N<=99:
    hangchuc= N//10
    hangdonvi= N%10
    tong= hangchuc+ hangdonvi
print("Tổng các chữ số của N: ", tong)
