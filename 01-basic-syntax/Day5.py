# Day5.字符串的使用

# 字符串运算符:简单操作字符串

# 字符串拼接(+)
print(1+1) # 算术运算符加号
print("a"+"b") # ab
st1="未来之星"
st2="你好" 
st3="!"
print(st1+st2+st3) # 字符串拼接运算符
# print("年龄"+18) TypeError: can only concatenate str (not "int") to str 类型不一致

# 字符串重复(*)
print("未来之星"*3) # 未来之星未来之星未来之星
print(1)
print("-"*10)
print(2)

# 成员运算符(in/not in):检查字符是否包含在另一个字符串里，Ture(真)或Flash(假)
name="未来之星"
print("未来"in name) # True
print("乔丹"in name) # Flash
print("乔丹"not in name) # True
print("未星"in name) # Flash 整体判断

# 索引与切片

# 索引(下标):按位置取单个字符
name="bing"
# 从左往右从0开始
print(name[0])
print(name[1])
print(name[2])
print(name[3])
# print(name[4]) IndexError: string index out of range 超出下标范围会报错
# 从右往左，从-1开始
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])

# 切片:截取字符串的一部分[起始索引:结束索引:步长]

mystring="hello world,hello bingbing"
print(mystring[:]) # hello world,hello bingbing

# 指定起始索引
print(mystring[2:]) # llo world,hello bingbing

# 指定结束索引(包前不包后)
print(mystring[:2]) # he

# 指定步长
# 正数: 从左往右切取
print(mystring[::5]) # h dlng
# 0(h)  0+5()  0+5+5(d)  0+5+5+5(l)  0+5+5+5+5(n)  0+5+5+5+5+5(g)
# 负数: 从右往左切取
print(mystring[::-5]) # gnld h
# 26(g)  26-5(n)  26-5-5(l)  26-5-5-5(d)  26-5-5-5-5()  26-5-5-5-5-5(h)

# 切片
print(mystring[2:14:2]) # lowrdh
# 2(l)  2+2(o)  2+2+2(w)  2+2+2+2(r)  2+2+2+2+2(d)  2+2+2+2+2+2(h)  


# 转义字符:处理特殊格式的文字，转义字符以\开头，用来表示不能直接输入的符号(比如换行、制表符)，相当于“文字的特殊命令”

# 制表符\t(空格\对其文本)
print("bingbing")
print("\tbingbing\tPython")

# 换行符\n(换行)
print("今天也要好好加油")
print("今天\n也要\n好好加油",end="\n")

# 单个反斜杠\=\\(最常用于文件路径)
# print("D:\tools\Python") # D:      ools\Python其中的\t转化为了转义字符空格了
print("D\\tools\\Python") # D\tools\Python这时路径可行

# 引号(字符串内只能输出单引号'或者双引号")
print("bingbing")
# print("bing"bing")  SyntaxError: unterminated string literal (detected at line 83)
print('bing"bing')
print("bing'bing")
# 如若既想用到单引号'又想用到双引号",此时需要用到\
# 输出单引号\'
print('单引号"双引号\'') # 单引号"双引号'
# 输出双引号\"
print("单引号'双引号\"") # 单引号'双引号"

# 原始字符串r(忽略所有转义)
print(r"D\tools\Python") # D\tools\Python可查


# 格式化字符串:优雅拼接变量和文字，把变量、数字或运算结果嵌入到字符串中，让输出更整齐(不用反复+拼接，避免报错)
name="bingbing"
age=18
# 输出: 我的姓名: bingbing，我的年龄: 18岁
print("我的姓名:",name,"，我的年龄:",age,"岁") # 可读性很差
# 格式化字符串f-string
print(f"我的姓名: {name}, 我的年龄: {age}") # 格式化

# 支持表达式
n1=3
n2=4
print(f"{n1}*{n2}={n1*n2}")
print(f"{n1} 对应的类型{type(n1)}")

# 数字格式化
# 整数: 可以设定最小宽度，并且补零
sid=1 # 学号
print(f"他的学号: 123")
print(f"他的学号: {sid:3}") # 设置最小宽度为3(默认前面补空格)
print(f"他的学号: {sid:03}") # 设置最小宽度为3(前面补0) # 001
# 小数: 设置精度
pi=3.1515926
print(f"保留十位小数: {pi:.10f}") # 超过则补零
print(f"保留两位小数: {pi:.2f}")
print(f"保留三位小数: {pi:.3f}") # 遵循四舍五入规则

# 对齐与填充
name="bingbing"
print(f"我的姓名: {name:20}") # 默认左对齐，宽度为20，不足后面补空格
print(f"我的姓名: {name:<20}") # 左对齐，宽度为20，不足后面补空格
print(f"我的姓名: {name:>20}") # 右对齐，宽度为20，不足前面补空格
print(f"我的姓名: {name:^20}") # 居中对其，宽度为20，不足两边补空格
print(f"我的姓名: {name:_<20}") # 左对齐，宽度为20，不足则使用下滑线填充(可自定义)
print(f"我的姓名: {name:_>20}") # 右对齐，宽度为20，不足则使用下滑线填充(可自定义)
print(f"我的姓名: {name:_^20}") # 居中对其，宽度为20，不足则使用下滑线填充(可自定义)
print(f"我的姓名: {name:1^20}") # 居中对其，宽度为20，不足则使用1填充


# 字符串常用内建函数: 高效处理文字

# 查找类(find/index/count)
name="bingbing"
print(name.find("g")) # 3
print(name.find("ng")) # 2
print(name.find("ss")) # -1表示没有

print(name.index("g")) # 3
print(name.index("ng")) # 2
# print(name.index("ss")) ValueError: substring not found会报错

print(name.count("b")) # 2
print(name.count("bin")) # 2
print(name.count("gb")) # 1

# 修改类函数(replace/ split/ strip/ lower/ upper)
name="bingbing"
print(name.replace("b", "B")) # Bingbing
print(name.split("g")) # ['bin', 'bin']
print(name.strip()) # bingbing
print(name.lower()) # bingbing
print(name.upper()) # BINGBING
