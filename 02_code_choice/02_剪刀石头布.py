"""
目标

1. 强化 多个条件 的 逻辑运算
2. 体会 import 导入模块（“工具包”）的使用

需求

1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
2. 电脑 随机 出拳
3. 比较胜负
"""

import random
# 定义一个猜拳输入转换函数
def play (date):
    if date == 1:
        return "石头[1]"
    elif date == 2:
        return "剪刀[2]"
    else:
        return "布[3])"
# 宣布游戏规则
print("石头剪刀布游戏决战规则：\n"
    "1.用户和系统的输出范围为:[1]=石头，[2]=剪刀,[3]=布。\n"
    "2.系统随机输出:[1]=石头，[2]=剪刀,[3]=布。\n"
    "3.用户输入的跟系统输出的作对比，判断输赢。\n"
    "4.用户输入非1、2、3的数字表示当轮弃权，系统获胜。\n"
    "5.决战结束后宣布决战结果\n")
# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
player = int(input("玩家出的拳 石头[1]／剪刀[2]／布[3]:"))
# 电脑 随机 出拳
computer = random.randint(1,3)
is_ture = True
# 检查输入的合法性
while is_ture:
    if player >3 or player <1:
        print("用户输入非1、2、3的数字表示当轮弃权，系统获胜。")
        player = int(input("玩家出的拳 石头[1]／剪刀[2]／布[3]:"))
    else:
        is_ture = False

# 输出玩家和电脑的出拳
print("玩家出拳 %s，电脑出拳 %s" % (play(player),play(computer)))

# 比较胜负
if(player == 1 and computer == 2)or(player == 2 and computer == 3)or(player == 3 and computer == 1):
    print("哎！电脑太菜了吧！")
elif player == computer:
    print("平局，再来一次吧！")
else:
    print("我擦，运气不好呀！")









