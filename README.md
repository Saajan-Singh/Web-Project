# Flask Authentication App

This project is a simple Flask application that implements user registration, authentication, and basic flash messaging using a local SQLite database. It utilizes Flask, SQLAlchemy, Flask-Login, and Jinja2 for templating.

## Project Structure

```
flask-auth-app
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── app.py            # Main application file with routes for login, signup, logout, etc.
│   ├── templates
│   │   ├── base.html
│   │   ├── login.html
│   │   └── signUp.html
│   └── static
│       └── styles.css
├── instance
│   └── config.py         # Configuration file (e.g., database URI, secret key)
├── venv                  # Virtual environment (not included in source control)
├── requirements.txt
├── run.py                # Entry point to run the Flask application
└── README.md
```

## Features

- **User Registration (Sign-Up):**  
  Users can sign up with their name, email, and password. If an email is already registered, the app flashes an error message.

- **User Authentication (Sign-In):**  
  Registered users can log in. Once logged in, the navigation shows a user icon which, when clicked, logs out the user.

- **Session Management:**  
  Secure session management using a secret key and Flask-Login.  
  ```python
  app.config['SECRET_KEY'] = 'a_very_complex_random_secret_key_2025!'
  ```

- **Flash Messages:**  
  Flash messages notify users of errors or successful actions. For example, a flash message appears if someone tries to sign up with an already registered email.

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd flask-auth-app
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Configure the application:**
   - Update the `instance/config.py` file (or directly in `app/app.py`) with your database URI and secret key if necessary.
   - Example configuration in `app/app.py`:
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
     app.config['SECRET_KEY'] = 'a_very_complex_random_secret_key_2025!'
     ```

6. **Initialize the database:**
   The database is automatically created when the app starts. If you need to recreate it, delete the existing `users.db` file and let the app call `db.create_all()` in its context.

7. **Run the application:**
   ```sh
   python run.py
   ```
   Open your web browser and go to `http://localhost:5000` to access the login and signup pages.

## Usage

- **Signup:**  
  Visit the signup page to create a new account. If the email is already registered, a flash message will inform you to use a different email.

- **Login:**  
  Visit the login page to sign in with your credentials. Once logged in, the navigation bar displays a user icon. Clicking the icon logs you out.

- **Logout:**  
  Authenticated users can log out by clicking the user icon in the navigation bar.

## License

This project is licensed under the MIT License.