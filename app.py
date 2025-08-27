from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

# Menu data
beef_burgers = {
    'Cheeseburger': 4.99,
    'Double Cheeseburger': 5.50,
    'BBQ Bacon Supreme': 7.50,
    'Chicken Burger': 4.35
}

fries = {
    'Small Fries': 3.50,
    'Medium Fries': 4.50,
    'Large Fries': 5.50
}

drinks = {
    'Coca-Cola': 3.95,
    'Mountain Dew': 3.95,
    '7UP': 3.95,
    'Solo': 3.95,
    'Fanta': 3.95,
    'Lipton Ice Tea': 4.95
}

shakes = {
    'The Clogger Shake': 6.99,
    'Vanilla Shake': 6.99,
    'Strawberry Shake': 6.99
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
        order = input('Select what you would like to order: ')
  
        if order == 1:

        elif

        else 

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

#add a thing so it looks at the user's local time and gives a time 10 mins after the point for the ready.
#add figma design to slideshow
