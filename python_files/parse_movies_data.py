#python file to parse the movies.dat file
import numpy as np 

def parse_movies_data():
	data_array = []
	counter = 0
	working_string = ''
	with open('movies.dat') as f:
		for line in f:
			if counter > 1:
				break
			for i in range(0,len(line)):
				if line[i]==':' and line[i-1]==':':
					working_string = working_string + '^'
				elif line[i]==':':
					a=1
				else:
					#print line[i]
					working_string = working_string + line[i]
	#print working_string[:200]
	counter = 0
	flag = 0
	number = ''

	for i in working_string:
		data_array.append([])
		if i == '^':
			data_array[counter].append(number)
			number = ''
			continue
		elif i =='\n':
			data_array[counter].append(number)
			#print number
			number = ''
			flag = 1
			counter +=1
		else:
			number = number + i
	temp = data_array[:3883]
	data_array = temp
	for i in range(0,len(data_array)):
		data_array[i][0] = int(data_array[i][0])

	#print data_array[10]
	tag_array = []
	
	for i in range(0,len(data_array)):
		counter = 0
		tag_array.append([])
		number = ''
		for j in data_array[i][2]:
			if j == "|":
				counter += 1
				tag_array[i].append(number)
				number = ''
			else:
				number = number + j
		tag_array[i].append(number)

	#print tag_array[-1]
	tag_list = []
	for i in tag_array:
		for j in i:
			if j not in tag_list:
				tag_list.append(j)
	#print tag_list
	#print len(tag_list)

	tags_vector = []
	for i in tag_array:
		temp = np.zeros(len(tag_list))
		#print temp
		
		for j in i:
			#print j, type(j)
			for k in range(0,len(tag_list)):
				#print k, type(k)
				if tag_list[k] == j:
					temp[k] = 1
		tags_vector.append(temp)
		#try - list comprehension way of doing this - temp = [1 for k in tag_list if tag_list[k] == j]

	#print tags_vector[0]

	return data_array, tag_list, tags_vector
#parse_movies_data()
	#print len(data_array), data_array[3800:3883]
	#data_array is smaller than 3952 because there are some serial numbers that are missing from the dataset
