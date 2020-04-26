# Function to delete pope's name from 'Consistory' variable

def del_pope(x):
	if x.find('Francis') != -1:
		return x.replace('Francis', '')
	elif x.find('Benedict\xa0XVI') != -1:
		return x.replace('Benedict\xa0XVI', '')
	elif x.find('John\xa0Paul\xa0II') != -1:
		return x.replace('John\xa0Paul\xa0II', '')
	else:
		return 999

# Function to delete reduntant indices from 'Consistory' variable    

def del_index(x):
        if x.find('[') != -1:
        	loc = x.find('[')
        	return x[:loc]
        else:
            	return x

# Function to delete reduntant indices from 'Consistory' variable    

def del_index(x):
        if x.find('[') != -1:
            	loc = x.find('[')
           	return x[:loc]
        else:
            	return x

# Function to delete 'latin' encoded spaces from given variable

def delete_latin_encoding(x):
	if x.find("\xa0") != -1:
		return x.replace("\xa0", " ")
	else:
		return x