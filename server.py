#! venv/bin/python3
from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
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
        [⏳] User Profile
            [✔] Update
            [✔] Delete  
            [~] Warn user before delete
            [~] Logout (delete session)
            [⏳] Get access to user page from main page
            [ ] Stay logged in --> do not show login page everytime pls
        [✔] Favorites
            [✔] Insert (like)
            [✔] Delete (dislike)
            [✔] Stay on category page after like/dislike
            [⏳] Main page (like/dislike buttons)
            [?] See only favorites
        [⏳] Items 
            [⏳] Sort alphabetical
            [⏳] Sort by cost
            [ ] Add description column
            [ ] Scrape data for other categories
            [ ] More data (?)
        [⏳] Buying
            [✔] Add to cart - PUT /cart/
            [⏳] Check out / Payment - POST /cart/checkout/    + Stock control
        [ ] Shoppingcart/box
            [✔] See current cart - GET /cart/
            [~] Delete item from cart - DELETE /cart/<item_id>/
            [?] See past transactions - GET /cart/history/
            [X?] Bill (Created after transaction)
            [ ] What is lira button for?
        [ ] Stay logged in
            [ ] And don't show log tab when logged in
        [👀] Webpage design
            [ ] Add logo
            [✔] Add site name (remove database title)
            [ ] Replace login with user profile page
            [ ] Make products not demo-like (fix descriptions)
            [ ] At signup page leave page button needed 
            [ ] Update footer information
        [X] Stores
            [ ] Add products but from new store
            [ ] Implement stocking by store
            [ ] See all stores
        [X] Admin
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
        [X] Searchbar
            
"""


@app.route("/cart/", methods=['GET', 'POST'])
def cart():
    if 'logged_in' not in session or session['logged_in'] is not True:
        return redirect(url_for('login', msg="Please first log in"))
    else:
        customer_obj = Customer()
        customer_id = customer_obj.getCustomerIdByEmail(session['user_email'])
        if request.method == 'GET':
            if customer_id is not None:
                # get cart items
                products = customer_obj.getCartItems(customer_id)
                return render_template('cart.html', products=products)
            else:
                flash('Error:', 'User is not found')
                return redirect(url_for('home'))
        elif request.method == 'POST':
            # add to cart
            product_id = request.form.get("product_id", None)
            if customer_id is not None:
                customer_obj.addItemToCart(customer_id=customer_id, product_id=product_id)
                flash('Item successfully added to cart!', 'success')
                return redirect(request.referrer)
            else:
                flash('Error:', 'User is not found')
                return redirect(url_for('home'))


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


"""
@app.route("/favourites/<product_id>", methods=['GET'])
def add_favs(product_id):
    # check if user logged in first
    print("SUCCESS ON CALLING METHODs")
    if 'logged_in' not in session or session['logged_in'] is not True:
        return redirect(url_for('login', msg="Please first log in"))
    else:
        customer_obj = Customer()
        customer_id = customer_obj.getCustomerIdByEmail(session['user_email'])
        if not (customer_id is None):
            fav_box_obj = FavBox()
            fav_box_obj.addItemToFavBox(customer_id=customer_id, product_id=product_id)
            flash('The item successfully added to your favs!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Error:', 'User is not found')
            return redirect(url_for('home'))
"""


@app.route("/add_to_favs/<product_id>", methods=['POST'])
def add_to_favs(product_id):
    # check if user logged in first
    print("SUCCESS ON CALLING METHODs")
    if not session.get("user_email", None):
        return redirect(url_for('login', msg="Please first log in"))
    else:
        customer_obj = Customer()
        customer_id = customer_obj.getCustomerIdByEmail(session['user_email'])
        if not (customer_id is None):
            fav_box_obj = FavBox()
            fav_box_obj.addItemToFavBox(customer_id=customer_id, product_id=product_id)
            flash('Item added to favorites!', 'success')

            # return redirect(url_for('home'))
            return redirect(request.referrer)
        else:
            flash('Error:', 'User is not found')
            return redirect(url_for('home'))


@app.route("/remove_from_favs/<product_id>", methods=['POST'])
def remove_from_favs(product_id):
    # check if user logged in first
    print("SUCCESS ON CALLING METHODs")
    if not session.get("user_email", None):
        return redirect(url_for('login', msg="Please first log in"))
    else:
        customer_obj = Customer()
        customer_id = customer_obj.getCustomerIdByEmail(session['user_email'])
        if not (customer_id is None):
            fav_box_obj = FavBox()
            fav_box_obj.removeItemFromFavBox(customer_id=customer_id, product_id=product_id)
            flash('Item removed from favorites!', 'success')
            # refresh page code

            # return redirect(url_for('home'))
            return redirect(request.referrer)
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
        if session.get("customer_id", None):
            products = db_products.getCategoryProductsWithLikes(category_id=int(category_id),
                                                                customer_id=int(session["customer_id"]))
        else:
            products = db_products.getCategoryProducts(
                category_id=int(category_id))  # get products from a certain category
            products = list(
                map(lambda product: (product[0], product[1], product[2], product[3], product[4], product[5], False),
                    products))
            print(products)
    else:
        products = db_products.getRecords()  # get all products
        products = list(
            map(lambda product: (product[0], product[1], product[2], product[3], product[4], product[5], False),
                products))

    #       print(products)

    # sort the products
    # products = sorted(products, key=lambda x: x[6], reverse=True)

    # shuffle(products)
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
            session['customer_id'] = customer[4]
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
        if 'logged_in' not in session or session['logged_in'] is not True:
            return redirect(url_for('login', msg="Please first log in"))
        else:
            customer_obj = Customer()
            # FIXME: debug if user changes email will this work
            customer_id = customer_obj.getCustomerIdByEmail(session['user_email'])
            if customer_id is None:
                msg = "You are not registered yet, please sign up first."
                return redirect(url_for('sign_up', msg=msg))
            else:
                customer_obj.updateCustomer(customer_id, customer_dict)
                msg = "You successfully updated your profile."
                # TODO: is there need to update session values?
                # FIXME: Redirect to user profile page or main page?
                return redirect(url_for('login', msg=msg))
    else:
        return "SOMETHING WENT WRONG"


# Delete user account code. Log out the user after deleting the profile. # WIP
@app.route('/login/delete_user/<customer_id>', methods=["POST"])
def delete_user(customer_id):
    customer_obj = Customer()
    # customer_id = customer_obj.getCustomerIdByEmail(customer_email)
    if not session.get("user_email", None):
        return redirect(url_for('login', msg="Please first log in"))
    elif customer_id is None:
        msg = "You are not registered yet, please sign up first."
        return redirect(url_for('sign_up', msg=msg))
    else:
        customer_obj.deleteCustomer(customer_id)
        session['logged_in'] = False
        session['user_email'] = None
        session['customer_id'] = None
        msg = "You successfully deleted your profile."
        # flash(msg, 'success')
        return redirect(url_for('login', msg=msg))


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
