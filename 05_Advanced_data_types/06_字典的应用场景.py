card_list = [
    {"name": "张三", "qq":"111", "phone": "119"},
    {"name": "李四", "qq": "112", "phone": "120"}
]

for card_info in card_list:
    for stu_info in card_info:
        print("%s : %s " % (stu_info,card_info[stu_info]))
    print(card_info)
    print("*" * 50)