from flask import Flask, render_template  # Import Flask to allow us to create our app
from math import floor

app = Flask(__name__)    # Create a new instance of the Flask class called "app"



#  Create a root route ("/") that responds with "Hello World!"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html') # Return the string 'Hello World!' as a response

# Create a route that responds with "Dojo!"
@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def dojo():
    return 'Dojo!'  # Return the string 'Hello World!' as a response

# Create a route that responds with "Hi" and whatever name is in the URL after /say/
# NINJA BONUS: Ensure the names provided in the 3rd task are strings
@app.route('/say/<string:name>')
def say(name):
    return f"Hi {name}!"
    # racecar
    # tacocat
    # race

@app.route('/multiply/<int:x>/<int:y>')
def multiply(x,y):
    result = x*y
    return render_template('multiply.html', x=x,y=y,result=result)

# Create a route that responds with the given word repeated as many times as specified in the URL
# NINJA BONUS: For the 4th task, ensure the 2nd element in the URL is an integer, and the 3rd element is a string
@app.route('/repeat/<int:a_number>/<string:a_string>')
def repeat(a_number, a_string):
    return f"{a_number * a_string}"

@app.route('/multiplication_table/<int:x>/<int:y>')
def multiplication_table(x,y):
    results = []
    for j in range(1,y+1):
        results_row = []
        for i in range(1, x+1):
            results_row.append(i*j)
        results.append(results_row)

    print(results)
    return render_template('table.html', table = results)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode. so that we can debug with Werkzeug

# this runs on a port 5000 which should allow to run without interfering with any other servers
# IP address slang is called dotted quad

# request response cycle. my machine "the client" makes a request to the server.
# 