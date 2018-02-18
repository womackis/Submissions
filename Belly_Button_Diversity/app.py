# import necessary libraries
import pandas as pd
import json
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, render_template, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///db/belly_button_biodiversity.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the table
otu = Base.classes.otu
samples = Base.classes.samples
samples_metadata = Base.classes.samples_metadata

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# Query the database and send the jsonified results

@app.route('/names')
    # """List of sample names."""
def name_list():
    sample_list = samples.__table__.columns.keys()
    return jsonify(sample_list)


@app.route('/otu')
# """List of OTU descriptions."""
def otu_list():
    otu_results = session.query(otu.lowest_taxonomic_unit_found).all()
    otu_results = [x[0] for x in otu_results]
    return jsonify(otu_results)
    
    # first attempted code below but seemed unnecessary to create a dataframe for single list   
    # df = pd.DataFrame(otu_results, columns=['Description'])
    # return jsonify(df.to_dict(orient="records"))



@app.route('/metadata/<sample>')
    # """MetaData for a given sample.
def metadata(sample):
    sample_metadata = session.query(samples_metadata.AGE, samples_metadata.BBTYPE,
                                    samples_metadata.ETHNICITY, samples_metadata.GENDER,
                                    samples_metadata.LOCATION, samples_metadata.SAMPLEID).all()
    metadata_df = pd.DataFrame(sample_metadata)
    metadata_df['ID'] = 'BB_' + metadata_df['SAMPLEID'].astype(str)
    metadata_df = metadata_df.set_index('ID').to_dict('index')

    data = metadata_df[sample]
    metaData = []

    for x, y in data.items():
        xy = {'t0': x, 't1': y}
        metaData.append(xy)

    return jsonify(metaData)



@app.route('/wfreq/<sample>')
    # """Weekly Washing Frequency as a number.
def wfreq(sample):

    wfreq_data = session.query(samples_metadata.WFREQ, samples_metadata.SAMPLEID).all()
    wfreq_df = pd.DataFrame(wfreq_data)
    wfreq_df['ID'] = 'BB_' + wfreq_data['SAMPLEID'].astype(str)
    wfreq_df = wfreq_df.set_index('ID').to_dict('index')
    # Returns an integer value for the weekly washing frequency `WFREQ`
    data = int(wfreq_df[sample]['WFREQ'])

    return jsonify(data)



@app.route('/samples/<sample>')
# """OTU IDs and Sample Values for a given sample.

    # Sort your Pandas DataFrame (OTU ID and Sample Value)
    # in Descending Order by Sample Value
def sample_dict(sample):
    samples_df = pd.read_sql_table('samples', engine)
    samples_df = samples_df['otu_id', sample].sort_values(by=sample, ascending=0)
    samples_df.columns = ['otu_id', 'sample_value']

    samples_dict = samples_df.to_dict('list')

    return jsonify(samples_dict)




if __name__ == "__main__":
    app.run(debug=True)
