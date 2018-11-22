import numpy as np
import pandas as pd
import sys
import csv
import json

#默认是以逗号进行分割,sep=','这个参数可以不用写
#文件中的第一行作为列名/列索引
f = pd.read_csv('1.csv',sep=',')
#print(f)

#加上参数header=None时，列索引就会自动生成，而将文件中的
#所有数据作为真正的数据
#在这里明显不适用，当1.csv文件中没有abcd message时就适合用这种
#方法
f1 = pd.read_csv('1.csv',header=None)
#print(f1)

#将1.csv去掉第一行，保存到2.csv中,自动添加列索引
f2 = pd.read_csv('2.csv',header=None)
#print(f2)

#自定义列索引名
f3 = pd.read_csv('2.csv',names=['a','b','c','d','message'])
#print(f3)

#将message这一列中的数据作为index索引，index_col通常应用在把时间类型数据往前提
f4 = pd.read_csv('2.csv',
                 names=['a','b','c','d','message'],
                 index_col='message')

#print(f4)

#多层索引
f5 = pd.read_csv('3.csv',index_col=['key1','key2'])
#print(f5)

#文中有注释行的
f6 = pd.read_csv('4.csv',skiprows=[0,2,3])
#print(f6)

#文中有空类型的值，或者是缺数据,填补为空类型
f7 = pd.read_csv('5.csv',na_values=['NULL'])
#print(f7)

#如果要读取的文件非常大，可以分片/块读取,一次读取5行
f8 = pd.read_csv('6.csv',sep='\t',nrows=5)
#print(f8)

f9 = pd.read_csv('6.csv',sep='\t', chunksize=100)
#print(f9) #<pandas.io.parsers.TextFileReader object at ..>

#在循环外层声明一个空的DateFrame
total = pd.DataFrame([])
for i in f9:
#    print(i)
    #两个DateFrame上下连接
    total = pd.concat([total,i])

#print(total)


#将数据写入文本格式
data = pd.DataFrame({'someting':['one','two','three'],
                     'a':[1,5,9],
                     'b':[2,6,10],
                     'message':[None,'world','foo']})
#print(data)
#将二维DateFrame存入文件中
data.to_csv('out.csv')
#将行索引index取消，另一个参数header=False将列索引取消
data.to_csv('out.csv',index=False)
#在终端输入中查看文件内容
data.to_csv(sys.stdout)

n = np.arange(7)
#将一维数组作为参数，生成一个一维的Series
data2 = pd.Series(n)
#print(data2)
#print(data2.index) RangeIndex(start=0, stop=7, step=1)
#自定义index,生成一个Datetime的index object
ind = pd.date_range('1/1/2018',periods=7)
#print(ind)

#将这个index object作为上面data2 的index
data2 = pd.Series(n,index=ind)
#print(data2)
data2.to_excel('out.xlsx')

#不是只能用pandas来读取csv文件的,可以导入import csv
f = open('1.csv')
reader = csv.reader(f)
#print(reader)#csv.reader object
#for line in reader:
#    print(line)

lines = list(csv.reader(open('1.csv')))
#print(lines)
header = lines[0]
#print(header)
values = lines[1:-1]
#print(values)

#手动写入文件
with open('mydata.csv','w') as f:
    writer = csv.writer(f,delimiter=';')
    writer.writerow(header)
    for i in values:
         writer.writerow(i)
         

#json格式数据
jsonstr = """
{"姓名": "张三",
 "住处": ["天朝", "挖煤国", "万恶的资本主义日不落帝国"],
 "宠物": null,
 "兄弟": [{"姓名": "李四", "年龄": 25, "宠物": "汪星人"},
          {"姓名": "王五", "年龄": 23, "宠物": "喵星人"}]
}
"""
obj = json.loads(jsonstr)
f = pd.DataFrame(obj["兄弟"])
#print(f)


