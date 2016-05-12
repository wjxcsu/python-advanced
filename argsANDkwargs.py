#-*-coding:utf-8-*-
#python进阶
# *args和**kwargs的用法
#*args 是用来发送一个非键值对的可变数量的参数列表给一个函数.
def test_var_args(f_arg,*args):
	print 'first normal arg:',f_arg
	for arg in args:
		print 'another arg through *args:',arg