# SQLAlchemy_Challenge : 

# Import Flask
from flask import Flask
# Import JSON
from flask import Flask, jsonify

# Create an app
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Define what to do when a user hits the index route
@app.route("/")
def welcome():
    return (
        f"Welcome to My HI Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2017-01-01<br/>"
        f"/api/v1.0/2017-01-10"
    )



if __name__ == "__main__":
    app.run(debug=True)
