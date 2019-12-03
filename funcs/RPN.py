def calc(expr, oper):
	b = int(expr.pop())
	a = int(expr.pop())
	if oper[-1] is '*':		expr.append(a*b)
	elif oper[-1] is '/':	expr.append(a//b)
	elif oper[-1] is '+':	expr.append(a+b)
	elif oper[-1] is '-':	expr.append(a-b)
	oper.pop()

def rpn_calc(msg, counter=False):
	o_high		= ['*', '/']
	o_low		= ['+', '-']
	other		= ['(', ')']
	odds		= ['+', '-', '*', '/', '(', ')']
	list_expr	= []
	list_oper	= []
	for i in msg:
		if i not in odds:
			if counter:
				x = list_expr.pop()
				list_expr.append(int(str(x)+str(i)))
			else:
				list_expr.append(int(i))
				counter = True
		else:
			counter = False

			if i in o_high:
				list_oper.append(i)
			elif i in o_low:
				if list_oper:
					if list_oper[-1] in other:
						list_oper.append(i)
					else:
						calc(list_expr, list_oper)
						list_oper.append(i)
				else:
					list_oper.append(i)
			elif i in other:
				if i is '(':
					list_oper.append(i)
				else:
					while list_oper[-1] is not '(':
						calc(list_expr, list_oper)
					list_oper.pop()
	while list_oper and len(list_expr) > 1:
		calc(list_expr, list_oper)

	answer = str(list_expr[0])
	list_expr	= []
	list_oper	= []

	return answer