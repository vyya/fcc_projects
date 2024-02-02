def arranger(expression):
	lst = []
	for item in expression:
		memb = item.split(' ')
		lst.append(memb)
	print(lst)
    for i in range(0, 2):
        print('{:>5s'.format(lst[i][0]))
arranger(['32 + 698', '3801 - 2'])i
