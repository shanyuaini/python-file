list = ['foo','bar']
list.append("item")
fl = open('test.txt','w')
for i in  list :
    fl.write(i)
    fl.write("\n")
fl.close()