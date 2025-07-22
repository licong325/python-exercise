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
# a = 123
# print('类型',type(a),a)
#
# a = a - 10
#
# print(a)


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
# testChangeType = "123"
# print(type(int(testChangeType)),testChangeType)
# print(type(float(testChangeType)),testChangeType)
# print(type(str(123)))


"""数组 List"""
# testList = [1,2,3]
# print(testList)


"""元组 Tuple"""
# # 定义之后不支持改变，使用索引获取对应项的值，
# testTuple = (1, 2, 3)
# print(testTuple[0])
# # 如果元组只有一项，用逗号来消除数学公式中的歧义
# testTuple2 = (1,)
# print(testTuple2[0])


"""字典DictionAry，其实就是对象"""
# testDict = {
#     "userName":"张三",
#     "age":22,
# }
# # 通过key获取，如果没有会报错
# print(testDict["userName"])
# # 通过内置方法获取，如果不存在，返回None或者指定值
# print(testDict.get("userName"))
# print(testDict.get("userName2"))
# print(testDict.get("userName2","指定值"))


"""集合 Set，存储一组不重复的key的集合，无序"""
# 自身会有一些方法
testSet = {"a", "b", 2}
print(testSet)
testSet2 = {"a", "b", 2, "c", 2}
print(testSet2)
# 两个set可以做数学意义上的交集、并集等操作
print(testSet & testSet2)
print(testSet | testSet2)
print(testSet ^ testSet2)
