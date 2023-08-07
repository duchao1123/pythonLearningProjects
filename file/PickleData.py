"""
=====================  序列化数据  ==========================
pickle
使用的数据类型，int、string、list、tuple、set、dict都可以序列化，
dump(*el, file)保存为二进制文件，load()已相同的顺序解读数据
"""

import pickle
import time


int_value = 100
str_value = 'python'
list_value = [1, 2, 3]
tuple_value = (1, 2, 3)
set_value = {1, 2, 3}
dict_value = {'key': 'value'}

with open("./testfilelocation/pickle_data.plk", 'wb') as f:  # 'wb' 以二进制写的方式打开文件， with是上下文，自动保存文件操作，不受一场阻断
    pickle.dump((int_value, str_value), f)
    pickle.dump(list_value, f)
    pickle.dump(tuple_value, f)
    pickle.dump(set_value, f)
    pickle.dump(dict_value, f)


print("开始休眠10s")
time.sleep(10)
print("休眠结束")

with open('./testfilelocation/pickle_data.plk', 'rb') as f:  # 'rb' 读取二进制文件
    i_v, s_v = pickle.load(f)
    l_v = pickle.load(f)
    t_v = pickle.load(f)
    set_v = pickle.load(f)
    d_v = pickle.load(f)
    print(i_v, s_v, l_v, t_v, set_v, d_v, sep='\n')
















