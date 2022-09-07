import requests
from datetime import datetime

today = datetime.now()

NUTRITIONIX_API_ID = "<api-id>"
NUTRITIONIX_API_KEY = "<api-key>"

nutritionix_endpoint = "<nutritionix_endpoint>"
sheety_api_endpoint = "<sheety_endpoint>"

header = {
    'x-app-id': NUTRITIONIX_API_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
    'Content-Type': 'application/json'
}

attributes = {
    'query': input('What did you do today?: '),
    'gender': 'male',
    'weight_kg': 73,
    'height_cm': 175.01,
    'age': 18
}

summary  = requests.post(url=nutritionix_endpoint,headers=header, json=attributes)
content = summary.json()
exercise = [content['exercises'][i]['name'].title() for i in range(len(content['exercises']))]
duration = [content['exercises'][i]['duration_min'] for i in range(len(content['exercises']))]
calories = [content['exercises'][i]['nf_calories'] for i in range(len(content['exercises']))]


sheety_header = {
    'Authorization': '<id for basic authentication>'
}

workout = { 'workout': {
    'date': f"{today.strftime('%d/%m/%Y')}",
    'time': f"{today.strftime('%X')}",
    'exercise': f"{exercise}",
    'duration': f"{duration}",
    'calories': f"{calories}"
    }
}

sheety_auth = requests.get(url=f'{sheety_api_endpoint}', headers=sheety_header)
for i in range(len(exercise)):
    e = exercise[i]
    d = duration[i]
    c = calories[i]
    workout = {'workout': {
        'date': f"{today.strftime('%d/%m/%Y')}",
        'time': f"{today.strftime('%X')}",
        'exercise': f"{e}",
        'duration': f"{d}",
        'calories': f"{c}"
    }
    }
    sheet = requests.post(url=f'{sheety_api_endpoint}', headers=sheety_header, json=workout)
