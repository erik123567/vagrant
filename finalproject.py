from flask import Flask
from flask import Flask, render_template , request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


app = Flask(__name__)
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
     return render_template('restaurants.html', restaurants = restaurants)


@app.route('/restaurant/new')
def newRestaurant():
	return render_template('newRestaurant.html', methods=['GET', 'POST'], restaurants = restaurants)

@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
	restaurant_name = ""
	apps = []
	for r in restaurants:
		if r['id'] == str(restaurant_id):
			restaurant_name = r['name']

	return render_template('editRestaurant.html', restaurant_id = restaurant_id, restaurant_name = restaurant_name)

@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
	# get the key then use del on it
	restaurant_name = ""
	for r in restaurants:
		if r['id'] == str(restaurant_id):
			restaurant_name = r['name']
	return render_template('deleteRestaurant.html', restaurant_name = restaurant_name)


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
	restaurant_name = ""
	apps = []
	entree = []
	for r in restaurants:
		if r['id'] == str(restaurant_id):
			restaurant_name = r['name']
	for i in items:
		if i['course'] == 'Appetizer':
			apps.append(i)

	return render_template('menu.html', restaurant_name = restaurant_name, items=items, apps = apps)

	
	
@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
	restaurant_name = ""
	for r in restaurants:
		if r['id'] == str(restaurant_id):
			restaurant_name = r['name']
	return render_template('newMenuItem.html',restaurant_name = restaurant_name)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id,menu_id):
	restaurant_name = ""
	for r in restaurants:
		if r['id'] == str(restaurant_id):
			restaurant_name = r['name']
	return render_template('editmenuitem.html', restaurant_name = restaurant_name)
	
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem():

	return "This page is for deleting menu item %s" % menu_id


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
