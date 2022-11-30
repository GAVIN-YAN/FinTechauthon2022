# a= [1,2,3,4]
# b= [3,5,4]
# print(a+b)
# print(list(set(a)-set(b)))


# for i in range(len(b)):
#     if b[i] in a:
#         a.remove(b[i])
# # c = a.remove(b)
# print(a)

# myDict = {'a':1,'b':[],'c':3,'d':[]}
# print(myDict)
# a= myDict
# # myDict = {}
# myDict['a'] = 3
# print(myDict, a)

# if [] in myDict.values():
#     del myDict['a']
# print(myDict)

# print(235%2)
# print(random.sample([2,4,5,7,8,9,0], 3))
# b =[2,4,5,7,8,9,0]
# print(b+1)
import numpy as np
import pandas as pd
from mpmath import re

q = [2, 4, 6]
b = [4]
for i in range(len(q)):
    # exec(f'n{q[i]-1}=q[i]-1')
    exec(f'n{i}=q[i]-1')
    # exec(f'n{q[i] - 1}=q+b')
# for j in range(3):
#     b.append(creat)

# for i in range(3):
#     locals() ['x' + str(i)] = np.zeros((2,2))


# print(x0)
x = range(2, 236)
print(x[12])

xx = [4, 3, 8]
for i in xx:
    print(i)

qqq = {"ww": 33, "ee": 44}
for k, v in qqq:
    print(k, v)

n11 = 3
b = 11
exec(f'f=n{b}')
print(f)

# c= b + int(exec(f'n{b}'))
# print(c)
# a = [4,5]
# for i in range(2):
#     exec(f'n{b}.append(a[i]*2)')
# print(n11)

# c ={}
# c["ee"] = 0
# for i in range(2,6):
#     c["ee"] = c["ee"] +i
# print(c)

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[1, 2], [3, 4]])
#
# a = np.c_[a, b, b]
# print(a)
#
# k = "asd"
# v = "ad"
# # print(k-v)
#
#
# m = "G22"
# print(type(int(m.replace("G", ''))))
#
# for i in range(0):
#     print("aaa")
#
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# k = [43, 2, 8]
# # print(k.remove(43))
# # print("k:", k)
# # print("c:", c)
# if k != None:
#     print("kongde")

# import os
# lists = os.listdir('C:/Users/icome/Desktop/FL_data/ieee118zh@20partitions')
# # lists.sort(key=lambda x: int(x.split('@')[0]))
# print(lists)
# print(type(lists[0]))
#
# x=[1,2,3,4,5,6]
# print(x[2:-1])
#
#
#
file ='yanfeng.csv'
print(file.replace(".csv", ''))
print(file)

str = 'G103@18-order.csv'
a = str.split('@')
b = str.split('@')[0].split('G')[1]
# c = int(str.split("@"[0].split('G')[1])
# b = re.findall('^.*@', str)
print(a,b)
# re.match(pattern, string, flags=0)


# h = []
# h[2] = 3
# print(h)



a = [6,7,8,9]
print(a.index(8))

c=[range(1, 36)]
print(c)


# a = [
#     [1,2,4],
#     [3,4]]
# for i in a:
#     for j in range(len(i)):
#         i[j] = i[j] * 1000
# print(a)

generator_neighbourGenerators ={4:"44", 5:"55", 3:"33", 1:"11"}
b = sorted(generator_neighbourGenerators.items())
print(b)
cc=[]
for i in range(len(generator_neighbourGenerators)):
    cc.append(b[i][1])
print(cc)



# xx ={3:"33", 4:"44"}
# xx = generator_neighbourGenerators
# print(xx)

# res = dict()
# temp = []
# for key, val in generator_neighbourGenerators.items():
#     if val not in temp:
#         temp.append(val)
#         res[key] = val

for i in range(2):
    res = dict()
    res = {i: i}
    print(res)

a = '222'
if 'xx' in locals().keys():
    print("true")

for j in reversed(range(1, 5)):
    print(j)