#_*_coding:utf-8 _*_
__author__ = 'sylar'


data_list = range(0,100)
def binary_search(find_num,data):
    mid = len(data)/2       #先取得列表的长度中间值
    if mid > 0:
        if find_num > data[mid]:#如果传入的数 大于传入列表的中间数就取列表中间数的右边部分
            print 'data should in right',mid,data[mid:]
            binary_search(find_num,data[mid:])#用递归方法将结果传回函数继续判断
        elif find_num < data[mid]:#如果传入的数 小于传入列表的中间数就取列表中间数的左边部分
            print 'data should in left',mid,data[:mid]
            binary_search(find_num, data[:mid])#用递归方法将结果传回函数继续判断
        else:
            print 'find the num: %s'%data[mid]
    elif data[0] == find_n:
        print '\033[32;1mfind the num%s\033[0m'%data[mid]
    else:
        print 'cannot find the num',find_n

if __name__ == '__main__':
    find_n =raw_input('find:').strip()
    if find_n.isdigit():
        find_n = int(find_n)
        binary_search(find_n,data_list)#将输入的数字作为binary_search的find_num参数传进去
        if find_n in data_list:
            print '--->%s exist in list'%find_n