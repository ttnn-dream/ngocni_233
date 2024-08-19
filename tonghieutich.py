# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:41:12 2024

@author: TranThiNgocNi
"""

a= int(input("Nhập a: "))
b= int(input("Nhập b: "))

tong= a+b
print("Tổng = ", tong)
hieu= a-b
print("Hiệu = ", hieu)
tich= a*b
print("Tich = ", tich)
thuong= a/b
tron2chuso= round(thuong,2)
tron3chuso= round(thuong,3)
print("Thương 2 chữ số", tron2chuso)
print("Thương 3 chữ số", tron3chuso)
cld= a%b
print("Chia lấy dư =", cld)
cln= a//b
print("Chia lấy nguyên=",cln)
