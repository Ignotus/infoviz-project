from flask import Flask, render_template, redirect, url_for
from flask_assets import Environment, Bundle

from random import uniform

from core.configuration import init
import core.parser as parser
import core.data_manip as data_manip

# Import blueprint modules
route_modules = ['data', 'citymap']
for module in route_modules:
    exec('from routes.%s import *' % (module))

app = Flask(__name__)

# Init the flask application by parameters
init(app)

# Route / will redirect users to the citymap_main function
# from the citymap blueprint
@app.route('/')
def main():
    return redirect(url_for("citymap.citymap_main"))

# Achtung! Run the app from the directory src to make it works
region_info = parser.parse_region_data('../data/polygon-info.csv')

park_data = parser.parse_park_data('../data/green-areas-and-parks.csv')
park_data = data_manip.add_postcode_for_places(region_info, park_data)

sport_data = parser.parse_sport_fields_data('../data/open-sport-fields.csv')
sport_data = data_manip.add_postcode_for_places(region_info, sport_data)

# not done yet
#function_data = parser.parse_building_function_data('../data/FUNCTIEKAART_region.dbf')
#function_data = 

places_data = park_data + sport_data

construct_data(region_info = region_info, places_data = places_data)
construct_citymap()

# Registers flask modules (called Blueprints)
app.register_blueprint(data)
app.register_blueprint(citymap)

assets = Environment(app)

js_main = Bundle("js/main.js", "js/main.js",
                 filters="jsmin", output="gen/min.js")


assets.register("js_main", js_main)

if __name__ == '__main__':
    # Run the app
    app.run(host='0.0.0.0')
