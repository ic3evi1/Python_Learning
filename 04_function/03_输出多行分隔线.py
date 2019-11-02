def print_line(char, times):
    """
    打印出单行分隔线
    :param char: 分隔字符
    :param times: 每行分隔符个数
    """
    print(char * times)


def print_lines(char, times, row):
    """
    打印多行分隔线
    :param char: 分隔符
    :param times: 每行分隔符个数
    :param row: 行数
    """
    col = 0
    while col < row:
        print_line(char, times)
        col += 1

a = str(input("输入分隔符号："))
b = int(input("输入每行分隔符个数："))
c = int(input("输入输出分隔符行数："))
# 调用多行分隔线函数
print_lines(a, b, c)
