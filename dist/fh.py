# f=open('n2.txt','a')
# print(f.name)
# print(f.mode)
# print(f.writable())
# print(f.closed)
# print(f.readable())

f=open("n2.txt",'a')
data='this is python class'
f.write(data)
f.close()