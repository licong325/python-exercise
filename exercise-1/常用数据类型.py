"""
python中常用的数据据类型
数字-Number
    整数-int 浮点数-float 复数-complex 布尔-bool
字符串-String
列表-List
元组-Tuple
集合-Set
字典-DictionAry

"""
"""变量定义 变量名=变量值"""
a = 123
print('类型',type(a),a)

a = a - 10

print(a)


"""运算符"""
# a = 21
# b = 10
# c = 0
#
# # 加法
# c = a + b
# print("1 - c 的值为：", c)
#
# # 减法
# c = a - b
# print("2 - c 的值为：", c)
#
# # 乘法
# c = a * b
# print("3 - c 的值为：", c)
#
# # 除法
# c = a / b
# print("4 - c 的值为：", c)
#
# # 取余
# c = a % b
# print("5 - c 的值为：", c)
#
# # 修改变量 a 、b 、c
# a = 2
# b = 3
# # 次方运算
# c = a ** b
# print("6 - c 的值为：", c)
#
# a = 11
# b = 5
# # 取整
# c = a // b
# print("7 - c 的值为：", c)

"""类型转换"""
testChangeType = "123"
print(type(int(testChangeType)),testChangeType)
print(type(float(testChangeType)),testChangeType)
print(type(str(123)))
