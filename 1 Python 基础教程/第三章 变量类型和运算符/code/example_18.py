# 初始化字符串
a = "don't put tabs or spaces in front of your paragraphs."

# 产生新的字符串，首字母大写。
a1 = a.capitalize()
print('产生新的字符串，首字母大写：' + a1)
#产生新的字符串，每个单词首字母大写
a2 = a.title()
print('产生新的字符串，每个单词首字母大写：'+a2)

#产生新的字符串，所有字符串转成大写
a3 = a.upper()
print('产生新的字符串，所有字符串转成大写：'+a3)

#产生新的字符串，所有字符串转成小写
a4 = a.lower()
print('产生新的字符串，所有字符串转成小写：'+a4)

#产生新的字符串，所有字符串大小写转换
a5 = a.swapcase()
print('产生新的字符串，所有字符串大小写转换:'+a5)
