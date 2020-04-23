'''
Title: python tips 
Author: Chow
date: 2020/4/23
'''

1、多行语句，除了在{}、()、[]外，多行语句在末尾使用反斜杠(\)，分开。

2、多行注释和多行字符串，用''' or """。使用r可以让反斜杠不发生转义。如 r"a line with \n" 则\n会显示，并不是换行

3、Python中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。

4、Python可以在同一行中使用多条语句，语句之间使用分号(;)分割。

5、end关键字，print(a, end=',')

6、迭代器(iter)和生成器(yield)。在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 
	并在下一次执行 next() 方法时从当前位置继续运行。
	一、迭代器：
	it = iter(list)
    print(next(it))

	二、生成器：
	import sys
	def fibonacci(n): # 生成器函数 - 斐波那契
	    a, b, counter = 0, 1, 0
	    while True:
	        if (counter > n): 
	            return
	        yield a
	        a, b = b, a + b
	        counter += 1
	f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
	while True:
	    try:
	        print (next(f), end=" ")
	    except StopIteration:
	        sys.exit()


7、函数的不定长参数 * and **
	一、 *vartuple： 
	def printinfo( arg1, *vartuple):
	   print (arg1)
	   for var in vartuple:
	      print (var)
	   return
	结果：printinfo( 70, 60, 50 ) -> 70 60 50


	二、 **vardict:
	def printinfo( arg1, **vardict ):
	   print (arg1)
	   print (vardict)
	结果：printinfo(1, a=2,b=3) -> 1  {'a': 2, 'b': 3}


8、匿名函数lambda
	sum = lambda arg1, arg2: arg1 + arg2
	结果：print(sum(1, 2)) -> 3


9、格式化函数
	eg: 
	"I love {0}, my name is {1}".format('Baobao', 'Chow')  #当{}为空时，默认按照指定顺序带入
	"I love {person1}, my name is {person2}".format(person1='Baobao', person='Chow')


10、数据结构：
	一、列表当作堆栈使用：
		stack = [1, 2, 3]
		stack.append(4)
		stack.pop()  # FILO

	二、列表当作队列使用：
		queue = [1, 2, 3]
		queue.append(4)
		queue.popleft()  # FIFO

	三、列表推倒式：
		vector1 = [1, 2, 3]		
		[x**2 for x in vector1] -> [1, 4, 9]  # 列表
		{x: x**2 for x in vector1} -> {1: 1, 2: 4, 3: 9}  # 字典

		vector2 = [' a  ', 'b', '   c']
		[x.strip() for x in vector2] -> ['a', 'b', 'c']

		加上if过滤器：
		[x+1 for x in vector1 if x > 1] -> [3, 4]

		加上循环：
		[x*y.strip() for x in vector1 for y in vector2] -> ['a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc']


	四、遍历技巧：
		字典：for k, v in knights.items():
		索引：for i, v in enumerate():
		多个：for q, a in zip(questions, answers):
		反向：for i in reversed(range(1, 10, 2)):
		排序：for f in sorted(set(basket)):  # sorted并不修改原值，list.sort()改变原值
		注意：result2 = sorted(my_dict, key=lambda x:my_dict[x])  # key后边加了一个函数，将函数值排序

11、小技巧：
	repr(int(math.pow(i, 3))).rjust(5)  # repr()返回string，math.pow()乘方，rjust(5, ' ')右对齐，默认为空格








