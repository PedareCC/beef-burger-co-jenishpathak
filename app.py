from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

# Menu data
beef_burgers = {
    'Cheeseburger': {
        'price': 4.99,
        'image': 'images/cheeseburger.avif',
        'calories': '300 kcal | 1255 kJ',
        'description': 'A juicy beef patty with melted cheese, fresh lettuce, and our special sauce.',
        'customizations': ['extra cheese', 'extra patty', 'bacon', 'lettuce', 'tomato', 'onions', 'pickles']
    },
    'Double Cheeseburger': {
        'price': 5.50,
        'image': 'images/double-cheeseburger.avif',
        'calories': '440 kcal | 1841 kJ',
        'description': 'Two beef patties with double cheese, topped with fresh vegetables and our signature sauce.',
        'customizations': ['extra cheese', 'extra patty', 'bacon', 'lettuce', 'tomato', 'onions', 'pickles']
    },
    'BBQ Bacon Supreme': {
        'price': 7.50,
        'image': 'images/bbq-bacon-supreme.avif',
        'calories': '520 kcal | 2176 kJ',
        'description': 'Premium beef patty with crispy bacon, BBQ sauce, cheese, and fresh vegetables.',
        'customizations': ['extra cheese', 'extra patty', 'extra bacon', 'lettuce', 'tomato', 'onions', 'pickles']
    },
    'Chicken Burger': {
        'price': 4.35,
        'image': 'images/chicken-burger.avif',
        'calories': '420 kcal | 1757 kJ',
        'description': 'Crispy chicken patty with fresh lettuce, mayo, and pickles.',
        'customizations': ['extra cheese', 'bacon', 'lettuce', 'tomato', 'onions', 'pickles']
    }
}

fries = {
    'Small Fries': {'price': 3.50, 'image': 'images/small-fries.avif'},
    'Medium Fries': {'price': 4.50, 'image': 'images/medium-fries.avif'},
    'Large Fries': {'price': 5.50, 'image': 'images/large-fries.avif'}
}   

drinks = {
    'Pepsi': {'price': 3.95, 'image': 'images/pepsi.png'},
    'Pepsi Max': {'price': 3.95, 'image': 'images/pepsi-max.png'},
    'Mountain Dew': {'price': 3.95, 'image': 'images/mountain-dew.png'},
    '7UP': {'price': 3.95, 'image': 'images/7up.png'},
    'Solo': {'price': 3.95, 'image': 'images/solo.png'},
    'Sunkist': {'price': 3.95, 'image': 'images/sunkist.png'},
    'Lipton Ice Tea': {'price': 4.95, 'image': 'images/lipton-ice-tea.png'}
}

shakes = {
    'The Clogger Shake': {'price': 6.99, 'image': 'images/clogger-shake.png'},
    'The Classic Shake': {'price': 6.99, 'image': 'images/vanilla-shake.png'},
    'The Strawberry Shake': {'price': 6.99, 'image': 'images/strawberry-shake.png'}
}

extra_ingredients = {
    'extra cheese': 1.00,
    'extra patty': 2.50,
    'bacon': 1.50,
    'extra sauce': 0.50
}

vegetables = {
    'lettuce': 0,
    'tomato': 0,
    'onions': 0,
    'pickles': 0,
    'mushrooms': 0.50
}

fry_addons = {
    'extra salt': 0.20,
    'chicken salt': 0.20
}
#add descriptions in HTML

total_order = []          
total_order_prices = []   


def menu():
    print('--- Beef Burger Menu ---')
    print(f"1. Cheeseburger for ${beef_burgers['Cheeseburger']}")
    print('2. Go to checkout.')


def customer_order():
    print("Hello World")

def check_out():
    print('\n--- Your Order Summary ---')

@app.route('/')
def home():
    return render_template('index.html',
                           beef_burgers=beef_burgers,
                           fries=fries,
                           drinks=drinks,
                           shakes=shakes,
                           now=datetime.now())

@app.route('/item/<category>/<item_name>')
def item_details(category, item_name):
    categories = {
        'burgers': beef_burgers,
        'fries': fries,
        'drinks': drinks,
        'shakes': shakes
    }
    
    if category in categories and item_name in categories[category]:
        item = categories[category][item_name]
        return render_template('item_details.html',
                             category=category,
                             item_name=item_name,
                             item=item,
                             extras=extra_ingredients,
                             vegetables=vegetables)
    return redirect(url_for('home'))

#add a thing so it looks at the user's local time and gives a time 10 mins after the point for the ready.
#add figma design to slideshow
