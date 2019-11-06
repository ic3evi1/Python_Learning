students = [
    {"name": "阿土",
     "age": 20,
     "gender": True,
     "height": 1.7,
     "weight": 75.0},
    {"name": "小美",
     "age": 19,
     "gender": False,
     "height": 1.6,
     "weight": 45.0},
]
find_name = "小里"
for stu_info in students:
    print(stu_info)
    if stu_info["name"] == find_name:
        print("找到 %s 了\n" % find_name,stu_info)
        break
else:
    print("没有找到 %s" % find_name)
