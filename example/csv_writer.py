import csv


source_data = [
    ["xiaoming", 12, '20230001'],
    ["xiaoli", 13, '20230002'],
    ["xiaowang", 12, '20230003'],
    ["xiaohong", 14, '20230004'],
]


with open('../data/students.csv', 'w') as f:
    # 创建csv编辑器
    writer = csv.writer(f)
    # 写标题
    writer.writerow(['name', 'age', 'no'])
    # 写内容
    writer.writerows(source_data)







