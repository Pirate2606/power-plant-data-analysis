from flask import Flask
from datetime import datetime
import pandas as pd
from data_analysis import previous_day_yield, mean_difference, total_yield_given_day

# Inalizing app
app = Flask(__name__)


# Home page
@app.route('/')
def home():
    return ('''
    <h2>Routes:</h2>
    <ul>
        <li>/past_output_yield/plant_id<p>Example: /past_output_yield/4135001</p></li>
        <li>/total_yield/plant_id/date<p>Example: /total_yield/4135001/2020-05-15</p></li>
        <li>/mean_difference/plant_id<p>Example: /mean_difference/4135001</p></li>
    </ul>
    ''')


# Get past output yield using plant ID
@app.route('/past_output_yield/<plant_id>')
def past_output_yield(plant_id):
    if plant_id == "4135001":
        plant_data = pd.read_csv("Plant_1_Generation_Data.csv")
    elif plant_id == "4136001":
        plant_data = pd.read_csv("Plant_2_Generation_Data.csv")
    else:
        return "<h1>No such plant exists.</h1>"
    yield_ = previous_day_yield(plant_data)
    return "<h1>Yield = " + str(yield_) + "</h1>"


# Total yield for a specific date
@app.route('/total_yield/<plant_id>/<date>')
def total_yield(plant_id, date):
    if plant_id == "4135001":
        plant_data = pd.read_csv("Plant_1_Generation_Data.csv")
    elif plant_id == "4136001":
        plant_data = pd.read_csv("Plant_2_Generation_Data.csv")
    else:
        return "<h1>No such plant exists.</h1>"
    year = date.split("-")[0]
    month = date.split("-")[1]
    date_ = date.split("-")[2]
    yield_ = total_yield_given_day(plant_data, year, month, date_)
    return "<h1>Yield on " + date + " = " + str(yield_) + "</h1>"


# Mean Difference using plant ID
@app.route('/mean_difference/<plant_id>')
def get_mean_difference(plant_id):
    if plant_id == "4135001":
        plant_data = pd.read_csv("Plant_1_Generation_Data.csv")
    elif plant_id == "4136001":
        plant_data = pd.read_csv("Plant_2_Generation_Data.csv")
    else:
        return "<h1>No such plant exists.</h1>"
    mean = mean_difference(plant_data)
    return "<h1>Mean difference = " + str(mean) + "</h1>"


if __name__ == "__main__":
    app.run()