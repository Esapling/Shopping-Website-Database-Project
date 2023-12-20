#! venv/bin/python3
from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

from models import LoginForm, SignUpForm, UpdateProfileForm
import os
from database_manager import DatabaseManagement
from category_manager import Category
from product_manager import Product
from customer_manager import Customer, FavBox, ShopBox
from random import shuffle

from config import DEBUG, PORT, username, password, database

# from regUserManager import RegUser
from utilities import hashPassword

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
# app.config['SECRET_KEY'] = SECRET_KEY
app.secret_key = SECRET_KEY
bootstrap = Bootstrap5(app)

csrf = CSRFProtect()
csrf.init_app(app)

# separate relative methods in diff modules with classes

"""
    TODO:
        [ ] User Profile
            [~] Update
            [ ] Delete
        [ ] Favorites
            [ ] Insert
            [ ] Delete
        [ ] Items more(?)
            [ ] Sort alphabetical
            [ ] Sort cost
        [ ] Buying
            [ ] Add to cart
            [ ] Payment (?)
            [ ] Stock control
        [ ] Shoppingcart/box
            [ ] See past transactions
            [ ] Bill
        [ ] Admin
            [ ] Add new item
            [ ] Delete item
            [ ] Update item
            [ ] Add new category
            [ ] Delete category
            [ ] Update category
            [ ] Add new user
            [ ] Delete user
            [ ] Update user
            [ ] See all transactions
            [ ] See all users
            [ ] See all items
            [ ] See all categories
            [ ] See all favorites
            [ ] See all shopping carts
            [ ] See all users
        [ ] Searchbox
            
"""

@app.route("/favourites/<product_id>")
def add_shopbox(product_id):
    # check if user logged in first
    if 'logged_in' not in session or session['logged_in'] != True:
        return redirect(url_for('login', msg="Please first log in"))
    else:
        customer_obj = Customer()
        customer_id = customer_obj.getCustomerIdByEmail(session['user_email'])
        if customer_id is not None:
            fav_box_obj = ShopBox()
            fav_box_obj.addItemToShopBox(customer_id=customer_id, product_id=product_id)
            flash('The item successfully added to your shop box!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Error:', 'User is not found')
            return redirect(url_for('home'))


@app.route("/favourites/<product_id>")
def add_favs(product_id):
    # check if user logged in first
    print("SUCCES ON CALLING METHODs")
    if 'logged_in' not in session or session['logged_in'] != True:
        return redirect(url_for('login', msg="Please first log in"))
    else:
        customer_obj = Customer()
        customer_id = customer_obj.getCustomerIdByEmail(session['user_email'])
        if not (customer_id is None):
            fav_box_obj = FavBox()
            fav_box_obj.addItemToFavBox(customer_id=customer_id, product_id=product_id)
            flash('The item successgully added to your favs!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Error:', 'User is not found')
            return redirect(url_for('home'))


@app.route("/products/<product_id>")
def add_box(product_id):
    return "THERE YOU GO"


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
def home(category_id=0):
    image_url = "https://dlcdnrog.asus.com/rog/media/157809658839.webp"
    # "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRITa7y1G8H3t5etxA6oyfOUO01v_YrImYpkQ&usqp=CAU"

    db_category = Category()
    categories = db_category.getRecords()  # list of tuples each tuple element is a row or record
    db_products = Product()
    products = []
    print(category_id)
    if int(category_id) >= 1:
        products = db_products.getCategoryProducts(category_id=int(category_id))  # get products from a certain category
    #        print(products)
    else:
        products = db_products.getRecords()  # get all products
    #       print(products)

    shuffle(products)
    return render_template("index.html", image_url=image_url,
                           categories=categories,
                           products=products)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    msg = request.args.get('msg')  # Retrieve the 'msg' parameter from the URL query string
    if request.method == 'GET':
        return render_template('login.html', form=login_form, msg=msg)
    elif request.method == 'POST' and login_form.validate_on_submit():  # check if the form filled up correctly
        customer_obj = Customer()
        email = login_form.email.data
        password = login_form.password.data

        customer = customer_obj.validataCustomerRegistered(email_addr=email, password=password)
        if customer is None:
            msg = "No user is found with given email, please sign up or check your email"
            return render_template("login.html", form=login_form, msg=msg)
        elif customer is False:
            msg = "Invalid password, please enter your password again."
            return render_template("login.html", form=login_form, msg=msg)
        else:
            customer = customer_obj.getCustomerByEmail(email=email)
            session['logged_in'] = True
            session['user_email'] = email
            print("THIS IS YOUR EMAIL")
            print(session['user_email'])
            print(email)
            return render_template("user_page.html", customer=customer, email=email)
    else:
        return "INVALID REQUEST"


@app.route('/sign_up', methods=["GET", "POST"])
def sign_up(msg=None):
    signUpForm = SignUpForm()
    if request.method == 'GET':
        return render_template('sign_up.html', form=signUpForm)
    elif request.method == 'POST' and signUpForm.validate_on_submit():
        customer_dict = {
            "name": signUpForm.name.data,
            "phone": signUpForm.phone.data,
            "address": signUpForm.address.data,
            "email": signUpForm.email.data,
            "password": signUpForm.password.data
        }
        customer_obj = Customer()
        customer_id = customer_obj.checkCustomerExistByPhone(customer_phone=customer_dict['phone'])
        if customer_id is None:  # 1st case no user exist
            print("THIS METHOD WORKED90123")
            customer_obj.addCustomer(customer_dict)
            msg = "You successfully registered, you can log in now."
            return redirect(url_for('login', msg=msg))
        else:
            # 2nd case , customer_id is not none ->  user with given phone number already registered,
            is_customer_registered = customer_obj.checkCustomerRegisteredById(customer_id)
            if is_customer_registered:
                msg = f"Welcome {customer_dict['name']}, you have already registered, you can log in."
                print("THIS METHOD WORKED213")
            else:  # 3rd case customer exists but not registered yet
                msg = "You successfully registered , you can Log in now"
                customer_obj.registerCustomer(customer_id, customer_dict["email"], customer_dict["password"])
                print("THIS METHOD WORKED3123")
            return redirect(url_for('login', msg=msg))
    else:
        return "SOMETHING WENT WRONG"


# Update user profile code. For empty fields, it will keep the old values.
@app.route('/login/update_profile', methods=["GET", "POST"])
def update_profile():
    updateProfileForm = UpdateProfileForm()
    if request.method == 'GET':
        customer_obj = Customer()
        customer = customer_obj.getCustomerByEmail(email=session['user_email'])
        return render_template('update_profile.html', customer=customer, form=updateProfileForm)
    elif request.method == 'POST' and updateProfileForm.validate_on_submit():
        customer_dict = {
            "name": updateProfileForm.name.data,
            "phone": updateProfileForm.phone.data,
            "address": updateProfileForm.address.data,
            "email": updateProfileForm.email.data
        }
        customer_obj = Customer()
        customer_id = customer_obj.checkCustomerExistByPhone(customer_phone=customer_dict['phone'])
        if customer_id is None:
            msg = "You are not registered yet, please sign up first."
            return redirect(url_for('sign_up', msg=msg))
        else:
            customer_obj.updateCustomer(customer_id, customer_dict)
            msg = "You successfully updated your profile."
            return redirect(url_for('login', msg=msg))
    else:
        return "SOMETHING WENT WRONG"


if __name__ == "__main__":
    app.config.from_object("config")
    port = app.config.get("PORT", 5000)
    debug = app.config.get("DEBUG")
    app.run(port=PORT, debug=DEBUG)

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
