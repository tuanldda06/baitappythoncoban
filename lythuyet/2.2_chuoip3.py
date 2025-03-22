#Các phương thưc biến đổi
a = 'tUaaaaNNNN BeeeeeEEooooooO neeeeeeEEEEeeee'
print(a.capitalize())
print(a.lower())
print(a.upper())
print(a.title())
print(a.swapcase())

#Các phương thức định dạng :
a = 'aaaaaaa'.center(10,'#')
print(a)
b = 'aaa'.rjust(12,'%')
print(b)
c = 'aaaa'.ljust(14,'&')
print(c)
#Các phương thức xử lý
a = 'abcd'.encode()
print(a)
b = b'abcd'.decode()
print(b)
c = ''.join(['1','2','3'])
print(c)
d = '%'.join(('1','2','3','5'))
print(d)
e = '$'.join({'1','3','5'})#join có thể là 1 tuple, list ,... hoặc 1 iterable
print(e)
k = 'ab aa aa abccc aa'.replace('aa','tuann')
print(k)