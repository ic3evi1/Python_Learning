student_info = ("张三",1.75,75,23)
print(student_info,type(student_info))

#元组的遍历
for person_info in student_info:
    print("张三的信息 %s" % person_info)

#元组的函数
print(student_info.index("张三"))
print(student_info.count("张三"))

#元组类型转换成列表
student_list = list(student_info)
print(type(student_info))