# SQLAlchemy_Challenge : 

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from sqlalchemy import and_
from sqlalchemy import or_
import datetime as dt

# Import Flask
from flask import Flask
# Import JSON
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Sqlalchemy_challenge_hw/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


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

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of dates and precipitation"""
    
    # Measurement
    results_dates=session.query(Measurement.date).all()
    results_precip=session.query(Measurement.prcp).all()

    session.close()

    # Convert list of tuples into normal list
    results_dates2 = list(np.ravel(results_dates))
    results_precip2 = list(np.ravel(results_precip))

    # create dictionary from the two lists
    # reference : https://thispointer.com/python-how-to-convert-a-list-to-dictionary/
    zipbObj = zip(results_dates2, results_precip2)

    dict_precip=dict(zipbObj)

    return jsonify(dict_precip)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations"""
    # List of all stations
    results_station = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    session.close()

    return jsonify(results_station)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query the dates and temperature observations of the most active station for the last year of data.
    """Return a list of temperature of the most active station"""
    # Query all passengers
    tobs2 = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281').all()

    session.close()

     # Create a dictionary from tobs2 and append to a list of temperatures for one year
     # between '2016-01-11' and '2017-01-10'
     # reference: https://stackoverflow.com/questions/6899101/select-a-range-of-dates-in-python-dictionary
    all_tobs = []
    for date, tobs in tobs2:
        tobs_dict = {}
        if '2016-01-11' <= date <= '2017-01-10':
            tobs_dict["date"] = date
            tobs_dict["tobs"] = tobs
            all_tobs.append(tobs_dict)

    return jsonify(all_tobs)




if __name__ == "__main__":
    app.run(debug=True)
