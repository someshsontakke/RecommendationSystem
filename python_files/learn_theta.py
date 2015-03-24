#To complete objective 1. Learn theta for users
import parse_ratings_data, parse_movies_data, parse_users_data
ratings_array = parse_ratings_data.parse_ratings_data()
movies_array, tag_list, tags_vector = parse_movies_data.parse_movies_data()
users_array = parse_users_data.parse_users_data()

users_short = []
movies_short = []

for i in ratings_array:
	if i[0] not in users_short:
		users_short.append(i[0])
	if i[1] not in movies_short:
		movies_short.append(i[1])
#print len(users_short), len(movies_short)
temp = []
for i in movies_short:
	temp_0 = i
	for j in movies_array:
		if temp_0 == j[0]:
			temp1 = j
			break
	temp.append(temp1)
movies_short = temp

temp = []
for i in users_short:
	temp_0 = i
	for j in users_array:
		if temp_0 == j[0]:
			temp1 = j
			break
	temp.append(temp1)
users_short = temp
#print len(users_short), len(movies_short)

fv = len(tag_list)
