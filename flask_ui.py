'''
The module creates UI using flask.
'''

from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
from folium_map import create_map
from api import api_file_retriever

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    '''
    Returns main template of the site.
    '''
    return render_template('index.html')


@app.route('/submit', methods = ['POST'])
def submit():
    '''
    Returns a site for navigation
in the file.
    '''
    if not request.form.get('submission_user_name'):
        return render_template('error.html')

    geolocator = Nominatim(user_agent = 'JsonMaps')
    user_name = request.form.get('submission_user_name')
    try:
        friends_json = api_file_retriever(user_name)
    except:
        return render_template('error.html')

    locations = []
    names = []
    lenght = 0
    for friend in friends_json['users']:
        if lenght == 5:
            break
        coordinates = geolocator.geocode(friend['location'], exactly_one=True)
        if coordinates is None:
            continue
        locations.append(coordinates)
        names.append(friend['screen_name'])
        lenght += 1

    create_map(zip(locations, names))

    return render_template('map/JSON_map.html')


@app.route('/get_back', methods = ['POST'])
def get_back():
    '''
    Returns a main site template.
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
