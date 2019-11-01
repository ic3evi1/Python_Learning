#定义苹果的单价
price=float(input("请输入苹果的单价（元/斤）："))

#定义购买重量
weight=float(input("请输入苹果的重量（斤）:"))

#计算付多少钱
money=price*weight

#print("苹果的单价",price,"元/斤，购买了",weight,"斤，需要付款：",money,"元")
#输出，学习格式化字符
print("苹果的单价 %.2f 元/斤，购买了 %.2f 斤，需要付款： %.2f 元" % (price,weight,money))