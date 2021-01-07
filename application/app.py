from flask import Flask, render_template, url_for, request
from .model import __states, __room_types, __amenities, __property_types, parse_data, __pipe, case_template
import datetime
current_date = datetime.date.today().strftime('%Y-%m-%d')

app = Flask(__name__)

#Main route for Flask application (Landing page)
@app.route('/')
def main():
        return render_template('main.html')

#Routes for Navbar links (Menu)
@app.route('/<route>')
def navbar(route):
        if (route=="predictions"):
                return render_template('predictions.html', room_types=__room_types, property_types=__property_types, states=__states, current_date=current_date, amenities = __amenities)
        else:
                return render_template(f'{route}.html')

@app.route('/estimate', methods=['POST','GET'])
def estimate():
        if(request.method=='POST'):
                print(parse_data(request.form, case_template, request)['last_review_time'])
                prediction = int(__pipe.predict(parse_data(request.form, case_template, request))[0])
                # for key in request.form.keys():
                #         print(key)
                return render_template("predictions.html", script=1, prediction=prediction,  room_types=__room_types, property_types=__property_types, states=__states, current_date=current_date, amenities = __amenities)
        else:
                return navbar("predictions")

