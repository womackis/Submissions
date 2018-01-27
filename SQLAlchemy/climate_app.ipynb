{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "import datetime as dt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "\n",
    "from flask import Flask, jsonify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Database setup\n",
    "\n",
    "engine = create_engine(\"sqlite:///hawaii.sqlite\")\n",
    "\n",
    "# reflect an existing database\n",
    "Base = automap_base()\n",
    "\n",
    "# reflect  tables\n",
    "Base.prepare(engine, reflect=True)\n",
    "\n",
    "# Save classes\n",
    "Measurements = Base.classes.hawaii_measurements\n",
    "Stations = Base.classes.hawaii_stations\n",
    "\n",
    "# Create session link\n",
    "session = Session(engine)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Routes\n",
    "# /api/v1.0/precipitation\n",
    "# api details given say \"/precipitation\" but instructions say to query date and tobs\n",
    "\n",
    "@app.route(\"/api/v1.0/temperature\")\n",
    "def temperature(start_date, end_date):\n",
    "   #return temperature observations for given dates\n",
    "    temperature =session.query(Measurements.date,Measurements.tobs) \\\n",
    "             .filter(Measurements.date >= start_date).filter(Measurements.date <= end_date) \\\n",
    "             .all()\n",
    "    #Convert the query results to a Dictionary using date as the key and tobs as the value.\n",
    "    temp_results = []\n",
    "    for temp in temperature:\n",
    "        temperature_dict = {}\n",
    "        temperature_dict[\"date\"] = temp.date\n",
    "        temperature_dict[\"tobs\"] = temp.tobs\n",
    "       \n",
    "        temp_results.append(temperature_dict)\n",
    "\n",
    "    return jsonify(temp_results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# /api/v1.0/stations\n",
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "    # Return list of stations\n",
    "    stations =session.query(Stations.station,Stations.name).all()\n",
    "\n",
    "    return jsonify(stations)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# /api/v1.0/tobs\n",
    "#Return a json list of Temperature Observations (tobs) for the previous year\n",
    "@app.route(\"/api/v1.0/tobs\")\n",
    "def tobs():\n",
    "    tobs = session.query(Measurements.tobs) \\\n",
    "             .filter(Measurements.date >= '2016-08-03').filter(Measurements.date <= '2017-08-03').all()\n",
    "    \n",
    "    return jsonify(tobs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# /api/v1.0/<start> and /api/v1.0/<start>/<end>\n",
    "@app.route(\"/api/v1.0/<start>\") \n",
    "def start_range(start):\n",
    "    start_date = session.query(Measurements.date,func.avg(Measurements.tobs),func.min(Measurements.tobs),func.max(Measurements.tobs)) \\\n",
    "             .filter(Measurements.date >= start)\n",
    "        \n",
    "    return jsonify(single_date)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/<start>/<end>\")\n",
    "def start_end(start,end):\n",
    "    range = session.query(Measurements.date,func.avg(Measurements.tobs),func.min(Measurements.tobs),func.max(Measurements.tobs)) \\\n",
    "             .filter(Measurements.date >= start).filter(Measurements.date <= end)\n",
    "    return jsonify(range)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
