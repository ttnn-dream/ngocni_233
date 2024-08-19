# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:02:56 2024

@author: TranThiNgocNi
"""
gio=int(input("Nhập giờ: "))
phut=int(input("Nhập phút: "))
giay=int(input("Nhập giây: "))
 
if (0<=gio<=23) and (0<=phut<=59) and (0<=phut<=59):
    tonggiay= gio*3600+phut*60+giay
    print("Tổng giây", tonggiay)
    
