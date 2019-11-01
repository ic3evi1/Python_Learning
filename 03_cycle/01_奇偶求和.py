# 计算 0 ~ 100 之间所有数字的累计求和结果
# 1. 在 while 上方定义一个变量，用于 存放最终计算结果
sum = 0
even_sum = 0
odd_sum = 0
i = 0
j = 0
k = 0
# 2. 在循环体内部，每次循环都用 最新的计算结果，更新 之前定义的变量
while i <= 100:
    print(i,end=" ")
    sum += i
    i += 1
print()
print("0 ~ 100 之间所有数字的累计求和结果 %d" % sum)

while j <= 100:
    if (j % 2 == 0):
        print(j,end=" ")
        even_sum += j
    j += 1
print()
print("0~100之间偶数求和结果 = %d" % even_sum)


while k <= 100:
    if (k % 2 == 1):
        print(k,end=" ")
        odd_sum += k
    k += 1
print()
print("0~100之间偶数求和结果 = %d" % odd_sum)