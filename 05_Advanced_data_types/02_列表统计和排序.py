name_list = ["张三","李四","王麻子","张三"]
num_list = [9,1,4,7,6,2]

print(name_list)
print(num_list)

data = name_list.count("张三")
print(data)
print("-" * 40)
# 升序
name_list.sort()
num_list.sort()
print(name_list)
print(num_list)
print("-" * 40)
# 降序
name_list.sort(reverse = True)
num_list.sort(reverse = True)
print(name_list)
print(num_list)
print("-" * 40)

#翻转
name_list.reverse()
num_list.reverse()
print(name_list)
print(num_list)