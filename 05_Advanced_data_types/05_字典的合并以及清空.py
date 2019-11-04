stu_dict = {"name":"lg","age":18}

#统计字典元素个数

print(len(stu_dict))

#合并

temp_dict = {"height":1.75,"name":"hw"}
stu_dict.update(temp_dict)
print(stu_dict)
#清空
# stu_dict.clear()
# print(stu_dict)

#字典遍历

for key in stu_dict:
    print(" %s = %s " % (key, stu_dict[key]))
    print(stu_dict[key])