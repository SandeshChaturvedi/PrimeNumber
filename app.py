# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
	
class isPrime(Resource):
	def get(self, num):  
		# Checking that given number is more than 1  
		
		if(num > 1):
			for i in range(2,num):
				if (num % i) == 0:
					print(num,"is not a prime number")
					return jsonify({'isPrime': 'false'})
					break
			else:
				print(num,"is a prime number")
				return jsonify({'isPrime': 'true'})
                
		else:
			print(num,"is not a prime number")
			return jsonify({'isPrime': 'false'})
			
			

# adding the defined resources along with their corresponding urls
api.add_resource(isPrime, '/isprime/<int:num>')


# driver function
if __name__ == '__main__':

	app.run(host ='0.0.0.0', port = 5001, debug = True)
