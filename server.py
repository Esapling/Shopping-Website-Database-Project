#! venv/bin/python3
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5 
from models import LoginForm
import os
from database_manager import DatabaseManagement
from category_manager import Category
from product_manager import Product
SECRET_KEY = os.urandom(32)
app = Flask(__name__)
#app.config['SECRET_KEY'] = SECRET_KEY
app.secret_key = SECRET_KEY
bootstrap = Bootstrap5(app)


#seperate relative methods in diff modules with classes

@app.route("/products/<product_id>")
def add_box(product_id):
    pass

@app.route("/welcome")
def register_user():
    pass

@app.route("/users/<user_id>")
def update_registered_user():
    pass


@app.route("/products/<product_id>")
def product_page(product_id):
    pass

@app.route("/box/<user_id>")
def show_box(user_id):
    pass

@app.route("/")
@app.route("/<category_id>")
def home(category_id = 0):
    image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRITa7y1G8H3t5etxA6oyfOUO01v_YrImYpkQ&usqp=CAU"
    db_category = Category()
    categories = db_category.getRecords() # list of tuples each tuple element is a row or record
    db_products = Product()
    products = []
    
    if int(category_id) >= 1:
        products = db_products.getCategoryProducts(category_id= int(category_id)) # get products in a certain category
        print(products)
    else:
        products = db_products.getRecords() # get all products
        print(products)
    
    return render_template("index.html", image_url = image_url, 
                           categories = categories, 
                           products = products)



@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    is_valid_form = login_form.validate_on_submit() # check if the form filled up  correctly
    if request.method == 'GET':
        return render_template('login.html', form = login_form)
    elif request.method == 'POST' and is_valid_form:
        email = login_form.email.data
        password = login_form.password.data
        user = (email, password)
        #is_user_registered = check_user_registered(user) # check if there is a user with given data
        return render_template("user_page.html")
    else:
        return "HELLO WHY NOT POST WORKING"
if __name__ == "__main__":
    app.run(debug=True)


"""
@app.route("/")
def home():
    image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRITa7y1G8H3t5etxA6oyfOUO01v_YrImYpkQ&usqp=CAU"
    db_category = Category()
    categories = db_category.getRecords() # list of tuples each tuple element is a row or record
    movie.title
    movie.year
    movie.ranking
    movie.review
    movie.description
    categories = db_category.getRecords()
    print(categories)
    print(type(categories))
    return render_template("index.html", image_url = image_url, categories = categories)
"""