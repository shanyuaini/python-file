#_*_coding:utf-8_*_
#version 2
#行政区域菜单
menu = {
    'sichuang' : {
        'my' : {
            'fc' : ['xs','nh','gs'],
            'yx' : ['富乐山','老龙山','师院'],
            'qt' : ['安县','梓潼','江油','三台']
        },
        'cd' : {
            'jn' : ['金牛1','金牛2','金牛3'],
            'ch' : ['成华区1','成华区2','成华区3','成华区4']
        },
        'qt' : {
            'cb' : ['广元','阿坝','甘孜'],
            'cn' : ['宜宾','西昌','攀枝花']
        }
    },
    'qita' : {
        'bf' : {
            'hb' : ['陕西','山西','乱说'],
            'db' : ['我也不知道'],
            'xb' : ['就不告诉你']
        },
        'nf' : ['华南,西南,东南']
    }
}
print menu
quit_flag = False  #退出标记
#取到第一级的index

#while True:
#while True:
for k,v in enumerate(menu.keys()):
    print '-->',k,v
choice_1 = str(input("请输入对应数字,"))
if choice_1.isdigit():
    choice_1 = int(choice_1)
    list_1 = list(menu.keys())
    key_1 = list_1[choice_1]
    for k ,v in enumerate(menu[key_1]):
        print  "-->-->",k,v
    choice_2 = str(input("请输入对应数字"))
    if choice_2.isdigit():
        choice_2 = int(choice_2)
        list_2 = list(menu[key_1].keys())
        key_2 = list_2[choice_2]
        for k,v in enumerate(menu[key_1][key_2]):
            print "-->-->-->",k,v
        choice_3 =str(input("请输入对应数字"))
        if choice_3.isdigit():
            choice_3 = int(choice_3)
            list_3 = list(menu[key_1][key_2].keys())
            key_3 = list_3[choice_3]
            print "-->-->-->-->",menu[key_1][key_2][key_3]
















'''
#version 1
input_area =raw_input("Please input area: ")
city_list = []

for key in menu:
    city_list.append(menu[key])
for i in city_list:
    if input_area in i:
        area_list = i[input_area]
        print area_list
'''