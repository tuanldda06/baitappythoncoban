#Trả về chuỗi đan xen lần lượt ký tự đầu của chuỗi s1 và ký tự cuối của chuỗi s2
def xuly(s1,s2 ):
    chuoicuoi = ""
    max_dai = max(len(s1),len(s2))
    s2daonguoc = s2[::-1]
    for i in range(max_dai) :
        if i < len(s1):
            chuoicuoi+=s1[i]
        if i < len(s2): 
            chuoicuoi += s2daonguoc[i]
#Hai dòng if độc lập nhau, nên đúng như bạn nghĩ: "không liên quan đến nhau" theo nghĩa là không cần phụ thuộc hay gắn kết logic.   
    return chuoicuoi
s1 = input()
s2 = input()
print(xuly(s1,s2))