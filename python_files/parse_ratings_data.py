#python file to parse the ratings.dat file
data_array = []
counter = 0
dubbu = 0
with open("ratings.dat") as f:
	for line in f:
		if dubbu>2:
			break
		data_array.append([])
		colon_counter = 0
		number = 0
		num_list = ['1','2','3','4','5','6','7','8','9','0']
		for i in line:
			#print i
			if i == ":":
				colon_counter += 1
			if colon_counter%2 == 1:
				data_array[counter].append(number)
				print number
				number = 0
				continue
			if i in num_list:
				#print i
				number = number*10 + int(i)
				#print number
			if i =='\n':
				data_array[counter].append(number)
				print number
				number = 0
		counter +=1
		dubbu +=1
print data_array[:20]


