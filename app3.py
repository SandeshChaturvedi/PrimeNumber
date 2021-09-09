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
class Hello(Resource):

	# corresponds to the GET request.
	# this function is called whenever there
	# is a GET request for this resource
	def get(self):

		return jsonify({'message': 'hello world'})

	# Corresponds to POST request
	def post(self):
		
		data = request.get_json()	 # status code
		return jsonify({'data': data}), 201


# another resource to calculate the square of a number
class Square(Resource):

	def get(self, num):

		return jsonify({'square': num**2})
		
	
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


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')


# driver function
if __name__ == '__main__':

	app.run(debug = True)
