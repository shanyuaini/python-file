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
