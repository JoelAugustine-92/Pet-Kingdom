# app.py (FULL & FINAL - NO ERRORS)
import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User

# ----------------------------------------------------------------------
# 1. Setup
# ----------------------------------------------------------------------
basedir = os.path.abspath(os.path.dirname(__file__))
instance_dir = os.path.join(basedir, "instance")
os.makedirs(instance_dir, exist_ok=True)

app = Flask(__name__, instance_path=instance_dir)
app.config.update(
    SECRET_KEY="super-secret-key-2025",
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(instance_dir, 'petkingdom.db')}",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

# ----------------------------------------------------------------------
# 2. Extensions
# ----------------------------------------------------------------------
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))  # Fixed warning

# ----------------------------------------------------------------------
# 3. Create DB + Test User
# ----------------------------------------------------------------------
with app.app_context():
    db.create_all()
    if not db.session.get(User, 1):
        test = User(email="test@example.com")
        test.set_password("password123")
        db.session.add(test)
        db.session.commit()

# ----------------------------------------------------------------------
# 4. Products
# ----------------------------------------------------------------------
products = [
    {"id": 1, "name": "Frog Squeak Toy", "price": 9.99, "image": "https://m.media-amazon.com/images/I/61hM4m3f7sL._AC_UF1000,1000_QL80_.jpg"},
    {"id": 2, "name": "Holistic Cat Food", "price": 19.99, "image": "https://m.media-amazon.com/images/I/71YXutzyifL.jpg"},
    {"id": 3, "name": "Love Bird Cage", "price": 49.99, "image": "https://www.shutterstock.com/image-photo/colorful-love-bird-cage-600w-1083030581.jpg"},
    {"id": 4, "name": "Mini Aquarium", "price": 29.99, "image": "https://www.thesprucepets.com/thmb/cT5X6a0amN-S3yQK1ZoqwTWy0gA=/6016x0/filters:no_upscale():strip_icc()/little-fish-in-fish-tank-or-aquarium--gold-fish--guppy-and-red-fish--fancy-carp-with-green-plant--underwater-life--1092909414-5c59c92bc9e77c000102d1b5.jpg"},
    {"id": 5, "name": "Leather Leash", "price": 14.99, "image": "https://assets.roguefitness.com/f_auto,q_auto,c_limit,w_1600,b_rgb:ffffff/catalog/Gear%20and%20Accessories/Accessories/Everyday%20Gear/WL0016/WL0016-H_ko6zhi.png"},
    {"id": 6, "name": "Donut Cat Bed", "price": 24.99, "image": "https://m.media-amazon.com/images/I/71pECtR8MxL._AC_UF1000,1000_QL80_.jpg"},
]

# ----------------------------------------------------------------------
# 5. Routes
# ----------------------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html", current_user=current_user, products=products)

@app.route("/shop")
def shop():
    return render_template("index.html", current_user=current_user, products=products, scroll_to="shop")

# CART ROUTES (ADDED!)
@app.route("/add_to_cart/<int:product_id>", methods=["POST"])
@login_required
def add_to_cart(product_id):
    session.setdefault('cart', []).append(product_id)
    session.modified = True
    product = next(p for p in products if p['id'] == product_id)
    flash(f"{product['name']} added to cart!", "success")
    return redirect(url_for("shop"))

@app.route("/cart")
@login_required
def cart():
    cart_items = [next(p for p in products if p['id'] == pid) for pid in session.get('cart', [])]
    total = sum(item['price'] for item in cart_items)
    return render_template("cart.html", cart_items=cart_items, total=total)

@app.route("/remove_from_cart/<int:product_id>", methods=["POST"])
@login_required
def remove_from_cart(product_id):
    session['cart'] = [pid for pid in session.get('cart', []) if pid != product_id]
    session.modified = True
    return redirect(url_for("cart"))

@app.route("/checkout")
@login_required
def checkout():
    session.pop('cart', None)
    flash("Checkout successful!", "success")
    return redirect(url_for("home"))

# AUTH
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()
        if user and user.check_password(request.form["password"]):
            login_user(user, remember="remember" in request.form)
            return redirect(url_for("home"))
        flash("Invalid email or password", "error")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if User.query.filter_by(email=request.form["email"]).first():
            flash("Email already registered!", "error")
        else:
            user = User(email=request.form["email"])
            user.set_password(request.form["password"])
            db.session.add(user)
            db.session.commit()
            flash("Registered! Log in.", "success")
            return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/toggle_dark_mode', methods=['POST'])
def toggle_dark_mode():
    session['dark_mode'] = not session.get('dark_mode', False)
    return '', 204

# ----------------------------------------------------------------------
# 6. Run
# ----------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)