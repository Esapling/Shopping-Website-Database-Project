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
from customer_manager import Customer, FavBox, ShopBox, Order
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
    ✔ : DONE
    ⏳ : WIP
    ~ : WIP in future
    ' ' : TODO
    ? : Not sure
    👀 : Flavor
    X : SKIPPED
    TODO:
        [⏳] User Profile
            [✔] Update
            [✔] When updating, block when email or phone are already taken
            [✔] Delete  
            [✔] Warn user before deletion
            [~] Logout (delete session)
            [~] Get access to user page from main page
            [ ] Stay logged in --> do not show login tab when logged in, show user profile tab
                <<<User tab and login tab should be different>>>
            [?] See past transactions - GET /login/<customer_id>/transactions/
            [X] While signing up address shouldn't be character limited
        [✔] Favorites
            [✔] Insert (like)
            [✔] Delete (dislike)
            [✔] Stay on category page after like/dislike
            [👀] Main page (like/dislike button coloring)
            [?] See only favorites --> getCategoryProductsWithLikes??
        [⏳] Items 
            [⏳] FIXME: Why is getCategoryProductsWithLikes called and not getCategoryProducts?
                        Also getCategoryProductsWithLikes is not working properly.
            [⏳] Sort alphabetical
            [⏳] Sort by cost
            [ ] Add description column
            [ ] Scrape data for other categories
            [ ] More data (?)
        [⏳] Purchase      
            [⏳] Check out / Payment - POST /cart/checkout/    + Stock control
            [👀] Mock transaction
            [X?] Bill class --> Create bill after transaction and add to database
            [?] Add to purchase history
            [👀] Make buy button more visible
            [ ] FIXME: Purchase result information message to user 
            [?] Add to purchase history
        [⏳] Shoppingcart/box
            [✔] Add to cart - PUT /cart/
            [✔] See current cart - GET /cart/
            [~] Remove item from cart - DELETE /cart/<item_id>/ --> Click on cart symbol to do so
            [⏳] Purchase    - POST /cart/checkout/
            [ ] What is lira button for? --> going to purchase page?
        [👀] Webpage design
            [ ] FIXME: CSRF token checks!!
            [ ] Add logo
            [✔] Add site name (remove database title)
            [ ] Replace login with user profile page
            [ ] Make products not demo-like (fix descriptions)
            [ ] At signup page leave page button needed 
            [ ] Update footer information
            [?] Product individual pages
        [X] Stores
            [ ] Store name column required
            [ ] Add products but from new store
            [ ] Implement stocking by store
        [X] Admin/Employees
            [ ] Add new item
            [ ] Delete item
            [ ] Update item
            [ ] Add new category
            [ ] Delete category
            [ ] Update category
            [ ] Add new user
            [ ] Delete user
            [ ] Update user
            [ ] Add new store
            [ ] Delete store
            [ ] Update store
            [ ] See all transactions
            [ ] See all users
            [ ] See all items
            [ ] See all categories
            [ ] See all favorites
            [ ] See all shopping carts
            [ ] See all users
        [X] Searchbar
            
"""

################################################################################################
#                                             Purhcase/Shop History                            #
################################################################################################
#TODO
@app.route("/purchase/<product_id>", methods=['GET', 'POST'])
def purchase(product_id):
    pass


@app.route("/history/<customer_id>", methods=['GET', 'POST'])
def see_shop_history(customer_id):
    if 'logged_in' not in session or session['logged_in'] is not True:
        return redirect(url_for('login', msg="Please first log in"))
    else:
        order_obj = Order()
        products_purchased = order_obj.getItems(customer_id= customer_id)
        return render_template('cart.html', products=products_purchased)
        #TODO

        
        

################################################################################################
#                                             Cart                                             #
################################################################################################
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


# Checkout function. Create a bill and then delete the cart items of user.
@app.route("/cart/checkout/", methods=['POST'])
def checkout():
    if 'logged_in' not in session or session['logged_in'] is not True:
        return redirect(url_for('login', msg="Please first log in"))
    else:
        customer_obj = Customer()
        customer_id = customer_obj.getCustomerIdByEmail(session['user_email'])
        if request.method == 'POST':
            if customer_id is not None:
                order_obj = Order()

                # Get cart items
                # Create bill
                # TODO: Create bill class and add bill to database
                #   Compute total cost and check stock, if stock is not enough, do not proceed
                #   Do mock transaction and create bill. Add bill to database
                # Create order for selected products
                # Message user if stock is not enough for some products
                # Use in_stock_arr as a mask to select only in stock products
                # Delete cart items, if order is successful
                # DO everything in one big query
                out_of_stock_products, order_res = order_obj.createOrder(customer_id)
                if order_res:
                    msg = 'Purchase successfully made!'
                    # FIXME: Message comes late
                    flash('Purchase successfully made!', 'success')
                else:
                    out_of_stock_products = [product[0] for product in out_of_stock_products]
                    if len(out_of_stock_products) == 1:
                        msg = 'Item {} is out of stock'.format(out_of_stock_products[0])
                    else:
                        msg = 'Items {} are out of stock'.format(", ".join(out_of_stock_products))
                    flash(msg, 'info')

                # TODO: Where should we redirect after checkout?
                return redirect(url_for('cart', msg=msg))
            else:
                flash('Error:', 'User is not found')
                return redirect(url_for('home'))
        else:
            return "INVALID REQUEST"


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


################################################################################################
#                                          Favorites                                           #
################################################################################################

# @app.route("/add_to_favs/<product_id>", methods=['POST'])
# def favs_manage(product_id):
#     # check if user logged in first
#     if not session.get("user_email", None):
#         return redirect(url_for('login', msg="Please first log in"))
#     else:
#         customer_obj = Customer()
#         customer_id = customer_obj.getCustomerIdByEmail(session['user_email'])
#         if not (customer_id is None):
#             fav_box_obj = FavBox()
#             item_exist = fav_box_obj.searchItem(customer_id=customer_id, product_id=product_id)
#             if item_exist != None:
#                 return redirect(url_for('remove_from_favs', product_id=product_id))
#             else:
#                 return redirect(url_for('add_to_favs', product_id=product_id))
#         else:
#             flash('User is not found')
#             return redirect(url_for('home'))
      


@app.route("/add_to_favs/<product_id>", methods=['POST', 'GET'])
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
            flash('User is not found')
            return redirect(url_for('home'))




@app.route("/remove_from_favs/<product_id>", methods=['POST', 'GET'])
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


@app.route("/box/<user_id>")
def show_box(user_id):
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


################################################################################################
#                                     Home (Products) Page                                     #
################################################################################################
@app.route("/")
@app.route("/filtered")
@app.route('/search', methods=['GET'])
@app.route("/<category_id>")
def home(category_id=0):
    #TODO :user should be able to sort products in a category as well 
          # now this config only lets user one option amongst search, sort, retrieve from a certain category
    image_url = "https://dlcdnrog.asus.com/rog/media/157809658839.webp"
    # "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRITa7y1G8H3t5etxA6oyfOUO01v_YrImYpkQ&usqp=CAU"
    product_obj = Product()
    products = []
    category_obj = Category()
    categories = category_obj.getRecords()  # list of tuples each tuple element is a row or record
    if "filtered" in request.args:
        filter_opt = request.args.get('filtered')
        products = product_obj.sortProductPrices(filter_opt)        
    elif 'search' in request.args:
        searched_product = request.get('search')
        products = product_obj.getProductsWithName(string=searched_product)
    elif int(category_id) >= 1:
        if session.get("customer_id", None):
            # FIXME: This case is incorrectly placed and does not work, needs fixing
            products = product_obj.getCategoryProductsWithLikes(category_id=int(category_id),
                                                                customer_id=int(session["customer_id"]))
        else:
            products = product_obj.getCategoryProducts(
                category_id=int(category_id))  # get products from a certain category
            products = list(
                map(lambda product: (product[0], product[1], product[2], product[3], product[4], product[5], False),
                    products))
            print(products)
    else:
        products = product_obj.getRecords()  # get all products
        products = list(
            map(lambda product: (product[0], product[1], product[2], product[3], product[4], product[5], False),
                products))

    return render_template("index.html", image_url=image_url,
                           categories=categories,
                           products=products)


################################################################################################
#                                         Login/Signup                                         #
################################################################################################
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

        customer = customer_obj.validateCustomerRegistered(email_addr=email, password=password)
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
            print(customer)
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


################################################################################################
#                                       Account Editing                                        #
################################################################################################

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
            customer_id = customer_obj.getCustomerIdByEmail(session['user_email'])
            if customer_id is None:
                msg = "You are not registered yet, please sign up first."
                return redirect(url_for('sign_up', msg=msg))
            else:
                if customer_obj.updateCustomer(customer_id, customer_dict):
                    msg = "You successfully updated your profile."
                else:
                    msg = "User with given email or phone already exists, please try again."
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
    #app.config.from_object("config")
    #port = app.config.get("PORT", 5000)
    debug = app.config.get("DEBUG")
    app.run(port=PORT, debug=DEBUG)


"""
@app.route("/")
def home():
    image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRITa7y1G8H3t5etxA6oyfOUO01v_YrImYpkQ&usqp=CAU"
    category_obj = Category()
    categories = category_obj.getRecords() # list of tuples each tuple element is a row or record
    movie.title
    movie.year
    movie.ranking
    movie.review
    movie.description
    categories = category_obj.getRecords()
    print(categories)
    print(type(categories))
    return render_template("index.html", image_url = image_url, categories = categories)

    
    """
