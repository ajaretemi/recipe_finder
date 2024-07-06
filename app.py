# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_recipes', methods=['POST'])
def find_recipes():
    ingredients = request.form.get('ingredients').split(',')
    diet = request.form.get('diet')

    api_key = '2416added1944d4884e4bc2773057dcd'
    base_url = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': api_key,
        'includeIngredients': ','.join(ingredients),
        'diet': diet,
        'number': 10,
        'addRecipeInformation': True  # Include additional information in the response
    }
    response = requests.get(base_url, params=params)

    # Print the entire JSON response for debugging
    print(response.json())

    if response.status_code == 200:
        data = response.json()
        recipes = data.get('results', [])
        return render_template('recipes.html', recipes=recipes, ingredients=ingredients)
    else:
        return 'Error fetching recipes'

if __name__ == '__main__':
    app.run(debug=True)
