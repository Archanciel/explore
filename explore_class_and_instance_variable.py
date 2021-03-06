class Shark:

	# Class variables
	animal_type = "fish"
	location = "ocean"

	# Constructor method with instance variables name and age
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# Method with instance variable followers
	def set_followers(self, followers):
		print("This user has " + str(followers) + " followers (type " + self.animal_type + ')')
		print('class animal type ', Shark.animal_type)

def main():
	# First object, set up instance variables of constructor method
	sammy = Shark("Sammy", 5)

	# Print out instance variable name
	print(sammy.name)

	# Print out class variable location
	print(sammy.location)

	# Second object
	stevie = Shark("Stevie", 8)

	# Print out instance variable name
	print(stevie.name)

	# Use set_followers method and pass followers instance variable
	stevie.set_followers(77)

	# Print out class variable animal_type
	print('stevie type ', stevie.animal_type)
	print('sammy type ', sammy.animal_type)

	sammy.animal_type = 'squale'

	# Print out class variable animal_type
	print('stevie type ', stevie.animal_type)
	print('sammy type ', sammy.animal_type)
	sammy.set_followers(12)

if __name__ == "__main__":
	main()