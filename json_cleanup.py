import csv

file_path='game/json_data.csv'

datas=[]

with open(file_path,mode='r',newline='') as file:
    reader=csv.reader(file)
    for lines in reader:
        datas.append(lines)

print('[')
datas=datas[2:-3]
for i in datas:
    i=str(i[0])
    i=i.replace(":",", \"y\" :")
    i=f"\"x\":{i}"
    i=i.split(' ')
    i[-1]=i[-1].replace('"','')
    i=str(''.join(i))
    print('    {\n    '+i+'\n },')
print("]")