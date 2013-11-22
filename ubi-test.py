from ubidots import ApiClient
import random

#Create an "API" object

api = ApiClient("12da9991c4229d9daf0c68b1432cf3485cf34165")

#Create a "Variable" object

test_variable = api.get_variable("528703c5f91b281828a54019")

#Here is where you usually put the code to capture the data, either through your GPIO pins or as a calculation. We'll simply put a random value here:

for x in xrange(1,200):
	test_value = random.randint(1,100)
	#Write the value to your variable in Ubidots
	test_variable.save_value({'value':test_value})
