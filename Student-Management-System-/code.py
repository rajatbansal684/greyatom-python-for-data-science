# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class= class_1+class_2
print(new_class)
# Append the list
new_class.append('Peter Warden')
print(new_class)
# Print updated list
print(new_class)

# Remove the element from the list
new_class.remove('Carla Gentry')
# Print the list
print(new_class)

# Create the Dictionary
courses={'Math':65,'English':70,'History':80, 'French':	70,  'Science':	60 }


# Slice the dict and stores  the all subjects marks in variable
variable=[courses['Math'], courses['English'], courses['History'], courses['French'], courses['Science']]

# Store the all the subject in one variable `Total`
total = sum(variable)
# Print the total
print(total)
# Insert percentage formula
percentage= total * 100/500
# Print the percentage
print(percentage)


# Given string# Create the Dictionary
mathematics={'Geoffrey Hinton':78,'Andrew Ng':	95, 'Sebastian Raschka':65, 'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66, 'Peter Warden':75 }
max_marks_scored = max(mathematics,key = mathematics.get)
topper = max_marks_scored
print(topper)

Name=topper.split()

#Quote = " I love data "

# To split the words of a sentence
#print('-'*20)

# To access one word based on index
#print(Quote.split()[2])
#output: ['I', 'love', 'data'] and data


# Create variable first_name 
first_name=Name[0]

# Create variable Last_name and store last two element in the list
Last_name=Name[1]

# Concatenate the string
full_name= Last_name+' '+first_name

# print the full_name
print(full_name)
certificate_name = full_name.upper()
# print the name in upper case
print(certificate_name)

# Code ends here






