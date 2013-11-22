from ubidots import ApiClient
import random

#Create an "API" object

api = ApiClient("YOUR API KEY")

#Create a "Variable" object

test_variable = api.get_variable("YOUR VARIABLE ID")

#Here is where you usually put the code to capture the data, either through your GPIO pins or as a calculation. We'll simply put a random value here:

for x in xrange(1,200):
	test_value = random.randint(1,100)
	#Write the value to your variable in Ubidots
	test_variable.save_value({'value':test_value})
