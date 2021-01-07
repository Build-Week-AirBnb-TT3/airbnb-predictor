import joblib
import os
import numpy as np
from pandas import Timedelta
import pandas as pd
import datetime
__pipe = joblib.load('application/xgb_w_scaler_pt.sav')

def parse_data(form, case_template, request):
    def convert(string):
        if (string.isnumeric()):
            return int(string)
        return True if string=='yes' else False

    case = case_template
    for key in form.keys():
        if (key=='last_review_time'):
            review_date = datetime.datetime.strptime(form[key], '%Y-%m-%d').date()
            current_date = datetime.datetime.today().date()
            time_delta = current_date - review_date
            case['last_review_time'] = int(time_delta.days)
            
        if (key=='amenities'):
            amenities = request.form.getlist('amenities')
            for am in amenities:
                case[am] = [True]
        else:
            print(key)
            case[key] = [convert(form[key])]
    return pd.DataFrame(case)












case_template = pd.DataFrame({'host_is_superhost': [True], 'host_has_profile_pic': [True], 'host_identity_verified': [True],
                    'property_type': ['Entire guesthouse'], 'room_type': ['Entire home/apt'],
                    'accommodates': [2], 'bathrooms': [1.0], 'bedrooms': [1.0], 'beds': [1.0], 'number_of_reviews': [275],
                    'instant_bookable': [True], 'location': ['Asheville'], 'state': ['NC'],
                    'last_review_time': [Timedelta('4 days 00:00:00').total_seconds()/100], 'number_of_amenities': [25],
                    'hot_water': [False], 'air_conditioning': [False], 'parking': [False], 'refrigerator': [False],
                    'patio_balcony': [False], 'wifi': [False], 'breakfast': [False], 'hair_dryer': [False],
                    'waterfront': [False], 'workspace': [False], 'kitchen': [False], 'fireplace': [False],
                    'tv': [False], 'clothes_dryer': [False]})

__states = ["CA", "NY", "HI", "MA", "NV", "DC", "IL", "LA", "TN", "TX",
                "WA", "MN", "OR", "CO", "RI", "NC", "NJ", "OH", "FL"]
__property_types = ['Entire guesthouse', 'Shared room in hostel', 'Entire guest suite',
       'Entire apartment', 'Entire cottage', 'Private room in house',
       'Entire house', 'Private room in bed and breakfast', 'Tiny house',
       'Private room in bungalow', 'Entire bungalow',
       'Private room in apartment', 'Entire loft', 'Entire cabin',
       'Room in boutique hotel', 'Private room in cottage',
       'Private room in guest suite', 'Entire condominium', 'Camper/RV',
       'Entire townhouse', 'Private room', 'Farm stay',
       'Private room in condominium', 'Private room in townhouse',
       'Room in bed and breakfast', 'Private room in guesthouse',
       'Entire place', 'Private room in hostel',
       'Room in serviced apartment', 'Entire villa',
       'Entire serviced apartment', 'Room in hostel',
       'Room in aparthotel', 'Room in hotel', 'Private room in villa',
       'Private room in loft', 'Shared room in apartment',
       'Shared room in house', 'Private room in resort']
__room_types = ["entire home/apt", "private room", "shared room", "hotel room"]
__amenities = ['hot_water','air_conditioning','parking','refrigerator','patio_balcony','wifi',
                'breakfast','hair_dryer','waterfront','workspace','kitchen','fireplace','tv','clothes_dryer']
