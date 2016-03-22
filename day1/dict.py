"""
name_list = ["alex","eric","jack"]
print name_list
name_list.insert(2,"sylar")
print name_list
name_list.append("tom")
print name_list
name_list.append("rain")
print name_list
print name_list[1:4]
print name_list[-1]
print name_list[-3:]
print name_list[:4]
name_list[1] = "Eric"
name_list2 = ["alex","eric","jack"]
name_list.extend(name_list2)
print name_list
print name_list.count("alex")
name_list.sort()
print name_list
name_list.reverse()
print name_list

for i in range(name_list.count("alex")):name_list.remove("alex")
print name_list
"""
menu ={
    'Beijing':{
        "ChaoYang":['CICC','CCTV'],
        "HaiDian" :['BaiDu','YouKu']
    },
    'ShangHai':{
        "PuDong":['Ctrip','1 shop'],
        "PuXI" :['China Bank','America Bank']
    }
}
input_area =raw_input("Please input area: ")
city_list = []


for key in menu:
    city_list.append(menu[key])
for i in city_list:
    if input_area in i:
        area_list = i[input_area]
        print area_list

