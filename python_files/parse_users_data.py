#python file to parse the users.dat file
def parse_users_data():
	data_array = []
	counter = 0
	working_string = ''
	with open('users.dat') as f:
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

	temp = data_array[:6040]
	data_array = temp

	for i in range(0,len(data_array)):
		data_array[i][0] = int(data_array[i][0])
		data_array[i][2] = int(data_array[i][2])
		data_array[i][3] = int(data_array[i][3])
		data_array[i][4] = int(data_array[i][4][:5])
		if data_array[i][1] == 'M':
			data_array[i][1] = 0
		else:
			data_array[i][1] = 1
	#print data_array[10], data_array[10][0]
	return data_array
