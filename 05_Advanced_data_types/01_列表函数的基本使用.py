#定义一个列表
name_list = ["zhangsan","lisi","wangmazi"]

temp_list = ["张三","李四","王麻子"]

# 列表索引
data = name_list.index("zhangsan")
# 列表扩展
name_list.extend(temp_list)
# 列表删除
print(name_list)
name_list.remove("zhangsan")

print(name_list)
name_list.pop(0)

#添加元素
name_list.append("hello python")
name_list.insert(0,"hello word")


print(name_list)
print(data)