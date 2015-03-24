#python file to parse the movies.dat file
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
print data_array[10]

#print len(data_array), data_array[3800:3883]
#data_array is smaller than 3952 because there are some serial numbers that are missing from the dataset


"""for i in range(0,len(data_array))
	if data_array[i]=='':
		print i"""
"""
	#print i
	if i == ":":
		colon_counter += 1
	if colon_counter%2 == 1:
		data_array[counter].append(number)
		#print number
		number = 0
		continue
	if i in num_list:
		#print i
		number = number + int(i)
		#print number
	if i =='\n':
		data_array[counter].append(number)
		#print number
		number = 0
	counter +=1

	if i == '\n':
		data_array.append([])
"""



"""


	for line in f:
		if counter > 4:
			break
		data_array.append([])
		colon_counter = 0
		number = ''
		num_list = ['1','2','3','4','5','6','7','8','9','0']
		for i in range(0,len(line)):
			#print i
			if line[i] == ":":
				colon_counter += 1
			
			if colon_counter%2 == 1 and line[i-1]==":":
				data_array[counter].append(number)
				#print number
				number = ''
				continue
			if colon_counter%2 == 1 and line[i-1]!=':':
				colon_counter -= 1
				continue
			
			number = number + line[i]
			
			if line[i] =='\n':
				data_array[counter].append(number)
				print number
				number = 0
		counter +=1
"""

"""
def parse_ratings_data():
	data_array = []
	counter = 0
	with open("ratings.dat") as f:
		for line in f:
			if counter>1000000:
				break
			data_array.append([])
			colon_counter = 0
			number = 0
			num_list = ['1','2','3','4','5','6','7','8','9','0']
			for i in range(0,len(line)):
				#print i
				if line[i] == ":":
					colon_counter += 1
				if colon_counter%2 == 1 and line[i-1]==":":
					data_array[counter].append(number)
					#print number
					number = ''
					continue
				if colon_counter%2 == 1 and line[i-1]!=':':
					colon_counter -= 1

				number = number + line[i]
				
				if line[i] =='\n':
					data_array[counter].append(number)
					#print number
					number = 0
			counter +=1
	#print data_array[1900:2000]
	return data_array
"""