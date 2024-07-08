from flask import Flask, render_template,request

app = Flask(__name__)

listfromdb =  ["sunday",  "wednesday",  "friday"   ]

# Define a list of dictionaries representing Game of Thrones characters
characters = [
    {"number": 1, "name": "Arya Stark", "phone": "044545", "email": "Valan.Margulis@Winterfel.com", "photo": "arya-stark.jpg"},
    {"number": 2, "name": "Jon Snow", "phone": "045456465", "email": "Night.Watch@Wall.com", "photo": "jon-snow.jpg"},
    {"number": 3, "name": "Ned Stark", "phone": "04545", "email": "Ned@WF.com", "photo": "ned-stark.jpg"}
]

@app.route('/addDay', methods=['POST'])
def addDay():
    # Retrieve form data
    new_day = request.form['newDay']
    
    if new_day in listfromdb:
        
        return render_template("index.html", error = 'the day ' + new_day + ' already exists', listfromdb=listfromdb)
    else:
        listfromdb.append(new_day)
        return render_template('index.html', listfromdb=listfromdb)
    

@app.route('/login')
def loginPage():
    # Retrieve form data
    username = request.form['username']
    password = request.form['password']
    
    # Check if username and password are correct (this is a simple example)
    if username == 'user' and password == 'password':
        # In a real application, you would typically perform more robust authentication
        
        # Redirect to the login success page
        return render_template("index.html", user = username)
    else:
        # If login fails, render the login form again with an error message
        return render_template('login.html', error='Invalid username or password')

@app.route('/')
def index():
    print("request catched")
    
@app.route('/start')
def start():
    return "Hello world!"

@app.route('/html')
def html():
    return "<h1>Hello world!</h1>  <ul><li>sunday</li><li>wendesday</li> </ul>"
    

@app.route('/days')
def days():
    return render_template('index.html', listfromdb=listfromdb)

@app.route('/welcome')
def welcome():
    # Logic to retrieve and display all contact lists
    first_name = input("enter your name")
    return render_template("index.html", first_name=first_name)


@app.route('/generic_welcome')
def generic_welcome():
    first_name = "Arja"
    return render_template("index.html", first_name=first_name)


@app.route('/stam')
def stam():
    # Logic to retrieve and display all contact lists
    return "hello world"





if __name__ == "__main__":
    app.run(port=5000, debug=True )

    
    
    