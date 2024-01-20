# Import necessary modules from Flask
from flask import Flask,render_template

# Import the 'users' blueprint from the 'users.routes' module
from users.routes import users

# Create a Flask web application instace
app = Flask(__name__)

# Configure the database connection
app.config[
    "SQLALCHEMY_DATABASE_URI"
]="mysql://root:"
db = SQLALchemy(app)
# db.init_app(app)

# Enable debugging mode for the application
app.debug= True

# Register the 'users' blueprint with the application
app.register_blueprint(users)

# Define a route for the 'index' page
@app.route("/")
def index():
    # Render the sample.html templates when the '/index' route is accessed
    return render_template('index.html')

@app.route("/help")
def help():
    return render_template('help.html')

# Start the Flask application when this script is run
if __name__=='__main__':
  app.run()

