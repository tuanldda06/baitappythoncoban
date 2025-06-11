#Trả về chuỗi kết quả sau khi xóa các ký tự chẵn nếu chuỗi s có độ dài chẵn. (Tương tự xóa các ký tự lẻ với chuỗi lẻ).
def xuly(s):
    chuoi = ""
    dodaichuoi = len(s)
    for i in range(dodaichuoi):
        if i % 2 != dodaichuoi % 2 :
            chuoi += s[i]           
    return chuoi
s = input()
print(xuly(s))
#Vòng lặp kiểm tra i % 2 != dodaichuoi % 2:
#Khi chuỗi chẵn (dodaichuoi % 2 == 0) → giữ i % 2 != 0 → giữ các vị trí lẻ
#Khi chuỗi lẻ (dodaichuoi % 2 == 1) → giữ i % 2 != 1 → giữ các vị trí chẵn
#Tức là: giữ lại các ký tự không cùng "tính chẵn lẻ" với độ dài chuỗi.

