#-*-coding:utf-8-*-
#python进阶
# *args和**kwargs的用法
#*args 是用来发送一个非键值对的可变数量的参数列表给一个函数.
def test_var_args(f_arg,*args):
	print 'first normal arg:',f_arg
	for arg in args:
		print 'another arg through *args:',arg
#**kwargs 允许你将不定长度的键值对, 作为参数传递给一个函数。 #如果你想要在一个函数里处理带名字的参数, 你应该使用**kwargs。
def greet_me(**kwargs):
	for key,value in kwargs.items():
		print '%s==%s'%(key,value)

print "ssss"


print "I love you"
