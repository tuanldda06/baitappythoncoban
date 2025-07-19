#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.
#Example : [5 6  6 3 3 7 7 ] --> second runner : 6
danhsach = list(map(int , input().split())
dsach = []
for i in danhsach : 
  if i not in dsach :
    dsach += i
dsach.sort(reverse = True)
print(danhsach[1])
#Cú pháp:danhsach.sort(reverse=False)
#reverse: Là tham số tùy chọn, mặc định là False.
#Nếu reverse=False (hoặc không chỉ định): Sắp xếp tăng dần (nhỏ → lớn).
#Nếu reverse=True: Sắp xếp giảm dần (lớn → nhỏ).
