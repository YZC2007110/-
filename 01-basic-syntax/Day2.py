# Day2.变量的定义与赋值

# 定义变量
# 变量名=值

# 直接赋值
phone=1301112222
print(phone)

# 把一个变量的值赋给另一个变量
phone2=phone
print(phone2)

#支持表达式赋值：先计算，再把计算结果赋值给变量
num=3*4
print(num)

print("bingbing") #带引号的是文字数据（文字值），数据/值是可以直接使用的
# print(bingbing) # NameError: name 'bingbing' is not defined 不带引号的是变量名，变量名必须先赋值再使用
bingbing=123
print(bingbing)

# 变量的两个重要特性

# 1.动态类型：主打灵活，后边的值会覆盖前面的值重新计算
variable=10
variable=100.5
variable="bingbing"
print(variable)

# 2.序列赋值：适合批量赋值，变量名和数值要一一对应(第n个值就赋值给第n个变量)
Python,mysql,html=99,87,98
# Python,mysql,html=99,87 #ValueError: not enough values to unpack (expected 3, got 2)
print(Python)
print(mysql)
print(html)

# 变量命名必须符合规定
# 1.只能用字母、数字、下滑线：比如user_name、num1、_class(合法);user!name、stu id(不合法，有特殊符号或者空格)
# 2.不能以数字开头:比如num1(合法);1num(不合法)
# 3.不能用python关键字：比如class、true、if(这些是phtyon自带的"特殊功能词"，不能当变量名)
# 4.严格区分大小写:name、Name、NAME是三个不同的变量，调用时要去区分大小写

# 命名建议规范
# 1.见名知义：比如student_name(学生年龄)、book_name(书名)
# 2.下划线分割法：全小写，单词之间用_连接，比如student_name
# 3.大驼峰命名法：每个单词首字母大写，比如StudentName

# 变量的数据类型：不同数据有不同"格式"

# 1.数值类型(用于存储数字，可计算)
# 整型(int)：整数(正负零)，比如100，-50,0
money=10000
print(money)
print(type(money))

# 浮点型(float)：小数，比如11.34，-0.5
print(type(float))

# 布尔型(bool):只有两个值，Ture(真)和false(假)，用于判断(比如"是否及格""是否登录")
print(type(True)) # 真
print(type(False)) # 假

# 2.字符串类型(str)：用于储存文字
# 单行串字符：使用单引号或双引号包裹，只能在一行内定义
print(type('bingbing'))
print(type("Hello world"))
# 注意：打印字符串时只会打印文字，不会显示引号
print("Hello world")

# 多行字符串：使用三引号(三对单引号/三对双引号)定义，可存多行内容
print(type("""你好
      我是新手
      小白"""))

# 空值None：表示什么都没有
print(type(None)) # <class 'NoneType'>
# 注意不要把None和0或者空字符搞混，不同数据不同类型


"""核心总结
1. 变量本质:内存中带标签的"储物盒",用于存储、复用、修改数据。
2. 赋值规则：变量名=值，先算右边再装盒，必须赋值再使用。
3. 命名要求：字母+数字+下划线、不能以数字开有、不能用关键字、区分大小写；推荐"见名知义"和"下划线分割法"。
4. 常用数据类型：
    数值型:int(整数)、float(小数)、bool(Ture/Flase);
    字符串:str(单/双/三引号包裹);
    空值:None(表示无内容)。
5 .关键技巧:用type(变量名)可查看变量的数据类型；序列赋值要保证变量和数据数量一致。"""