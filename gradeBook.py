grades = [[ 101,97,98,70],
		[93,12,43,64],
		[100, 37,12,100]]
		

def grade_calculator(grid):	
	list = []
	count = 0
	total = 0
	
	for row in grid:	

		for column in row: #this will keep taking the nth item in the column ie. it will take item 1 in column 1 then item 1 in column 2 so the equivalent of the row
			total += float(column)
			count += 1
			
		average = total/count
		list.append(round(average,2))				
	return list


def class_average(grid):
	list = []

	for row in grid:	
		count = 0
		total = 0
		for column in row: #this will keep taking the nth item in the column ie. it will take item 1 in column 1 then item 1 in column 2 so the equivalent of the row
			total += float(column)
			count += 1
			
	average = total/count
	list.append(round(average,2))				
	return list
	
	
rowAverages = grade_calculator(grades)
print("Row averages:    {}".format(rowAverages))

classAverages = class_average(grades)
print 'class average: {}'.format(classAverages)