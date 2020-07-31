import requests
import os


def recipe_search(ingredient, health, preference):
    # API information
    app_id = os.environ['APP_ID']
    app_key = os.environ['APP_KEY']
    
    # basic request
    request = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}'

    if health == 'all':
        pass  # do nothing
    else:  # either vegan or vegetarian, add to basic request
        request += f'&health={health}' 

    if preference == 'no-pref':
        pass
    elif preference == 'balanced':
        request += f'&diet=balanced' # get meals labeled balanced, add to basic request 
    elif preference == 'easy':
        request += f'&ingr=4' # get meals with no more than 4 ingredients, add to basic request

    result = requests.get(request)
    data = result.json() # json decode method, turn data into a native python datatype 
    hits = data['hits']

    return hits
