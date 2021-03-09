id1=1
name1="苹果"
num1=500
price1=13.4
quanlity1 = "A+"
Origin1 = "山东"

id2=2
name2="香蕉"
num2=430
price2=11.3
quanlity2 = "S-"
Origin2 = "海南"

id3=3
name3="芒果"
num3=666
price3=16.3
quanlity3 = "SS"
Origin3 = "泰国"

print("---------------")
print("   水果商城    ")
print("--------------")
print("编号  名称    数量    价格    质量   产地")
print(id1,"  ",name1,"  ",num1,"  ",price1,"  ",quanlity1,"  ",Origin1)
print(id2,"  ",name2,"  ",num2,"  ",price2,"  ",quanlity2,"  ",Origin2)
print(id1,"  ",name3,"  ",num3,"  ",price3,"  ",quanlity3,"  ",Origin3)
print("总金额：",(num1*price1+num2*price2+num3*price3),"￥")