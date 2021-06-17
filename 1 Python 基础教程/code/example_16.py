import time
# --------------测试一------------------------------
# 开始时间
startTime1 = time.time()
a = ""
for i in range(1000000):
    a += "sxt"

endTime1 = time.time()

print("测试一运算时间：" + str(endTime1 - startTime1))
# --------------测试二------------------------------
# 开始时间
startTime2 = time.time()
li = []

for i in range(1000000):
    li.append("sxt")
a = "".join(li)
endTime2 = time.time()
print("测试二运算时间：" + str(endTime2 - startTime2))
