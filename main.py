dict1 = "Mark"
dict2 = "Alice"
dict3 = {}
for i in dict1:
    if i in dict3:
        dict3[i] += 1
    else:
        dict3[i] = 1
dict4 = dict3.copy()  
for key, value in dict3.items():
    if key in dict4:
        dict4[key]  += value
    else:
        dict4[key]    + value
print(dict1)
print(dict2) 
print(dict4)


dict1 = {"apple": 1, "banana" : 3,"tomato":2}
dict2 = {"banana": 4,"tomato":5,"aplle":6}
dict3 = dict1.copy()
for key,value in dict3:
    if isinstance(dict3[key],list):
        dict3[key].append(value)
    else:
        dict3[key] = [dict3[key],value]
else:
    dict3[key] = value
print(dict3)



dict = {"a":1,"b":2,"c":3}
dict2 = {}
for key in dict2(dict.keys()):
    dict2[key] = dict[key]
print(dict2)
dict3 = {}
for key in dict2(dict.keys(), ):
    dict3[key] = dict[key]
print(dict3)

dict1 = {"Alice":{"Phone":"098345781"},"Bob":{"Phone":"06760246534"},"Kris":{"Phone":"098561382"}}
dict2 = {"098345781":{"Name":"Alice"},"06760246534":{"Name":"Bob"},"098561382":{"Name":"Kris"}}
user = dict2[input("Enter your number : ")]
print(user)





