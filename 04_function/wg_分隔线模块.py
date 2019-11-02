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
name = "我是一个模块"