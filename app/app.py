from flask import Flask, request, render_template, redirect, url_for, flash
from models import db, User
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'a_very_complex_random_secret_key_2025!'

db.init_app(app)
# existing_user query removed as it is not needed here
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

# @app.route('/')
# def index():
#     return render_template('option.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email').strip()
        password = request.form.get('password')
        
        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please log in or use a different email.', 'danger')
            return redirect(url_for('signup'))
        
        # Save directly without hashing for now, but consider hashing in production
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flash('An error occurred. Please try again.', 'danger')
            return redirect(url_for('signup'))
            
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            login_user(user)  # <--- mark the user as logged in
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check your email and password.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Ensure static folder is correctly referenced in templates
@app.context_processor
def inject_static_url():
    return dict(static_url='/static')

if __name__ == '__main__':
    app.run(debug=True)