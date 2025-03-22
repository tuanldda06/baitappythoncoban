# Mở , đọc file , ghi file text
#with open("file.txt","r") as f :
    #content = f.read()
    #print(content)
#Ghi file
with open("file.txt","w") as f :
    f.write('Heloo , my name is Tuann')
# áp dụng để đọc file :
with open ("file.txt","r") as f :
    print(f.read())
# Dùng pandas để đọc/ghi file CSV
import pandas as pd
df = pd.read_csv("data.csv")  # Đọc file CSV
df.to_csv("output.csv", index=False)  # Ghi file CSV
#Đọc file Excel
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
#Xử lý file JSON (hay dùng cho API, dữ liệu web)
import json
with open("data.json", "r") as f:
    data = json.load(f)  # Đọc JSON thành dict
print(data)
#Xử lý file lớn (hữu ích khi làm Big Data)
#Đọc file lớn theo dòng (tránh dùng .read() với file lớn)
with open("bigfile.txt", "r") as f:
    for line in f:
        print(line.strip())  # Xử lý từng dòng
        
