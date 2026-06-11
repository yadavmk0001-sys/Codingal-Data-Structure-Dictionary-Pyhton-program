test_dict = {'Codingal':3, 'is':2, 'best':2, 'for':2, 'coding':1}

k = 2
v = 3
s = 1
res = 0
ser = 0
esr = 0
for key in test_dict:
    if test_dict[key] == k:
        res += 1

for key in test_dict:
    if test_dict[key] == v:
        ser += 1

for key in test_dict:
    if test_dict[key] == s:
        esr += 1      

print("Frequency of k is : ", str(res))
print("Frequency of v is : ", str(ser))
print("Frequency of s is : ", str(esr))