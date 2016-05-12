#-*-coding:utf-8-*-
#Python中任意的对象，只要它定义了可以返回一个迭代器的__iter__方法，或者#定义了可以支持下标索引的__getitem__方法(这些双下划线方法会在其他章节中#全面解释)，那么它就是一个可迭代对象。简单说，可迭代对象就是能提供迭代##器的任意对象。
#计算斐波那契数列的生成器
def fibon_gen(n):
	a=1
	b=1
	for i in range(n):
		yield a
		a,b=b,a+b
#普通版本
def fibon_loop(n):
	a=1
	b=1
	result=[]
	for i in range(n):
		result.append(a)
		a,b=b,a+b
	return result