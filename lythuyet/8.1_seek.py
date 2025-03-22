with open ("tuan.txt","w+") as f :
    f.write('Helooo , my name is Tuan')
    f.seek(0)
    a = f.read()
    print(a)
with open ("tuannn.txt","w+") as f :
    f.write('Helooo , my name is Tuan')
    f.seek(0,2)
    a = f.read()
    print(a)   # do con trỏ đã di chuyển đến cuối file nên khi đọc sẽ ra khoảng trắng.
with open ("tuanbeo.txt","w+") as f :
    f.write('Helooo,my name is Tuan')
    f.seek(8)
    a = f.read()
    print(a) # lúc này con trỏ sẽ di chuyển đến vị trí thứ 8 , bắt đầu từ 0 từ trái qua phải


    
    
    
