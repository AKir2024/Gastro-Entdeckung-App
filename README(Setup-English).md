# Gastro-Entdeckung-App
Find bars/restaurants that meet your specific needs

by Alexey Kirchner

Course: Development of web applications with Prof. Dr. Alexander Eck

Documentation: https://akir2024.github.io/Gastro-Entdeckung-App/

This is a Flask-based web application that allows regular restaurant visitors to share and search for restaurant tips. The application includes features such as user registration, login, adding tips, searching for tips with specific criteria, and setting user preferences.

## Features

- User registration and authentication
- Add restaurant tips with details (name, cuisine, price range, atmosphere)
- Search for tips using multiple criteria
- Set and update user preferences
- View detailed information about each restaurant tip

## Requirements

- Python 3.7+
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Bcrypt
- Flask-Login

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/AKir2024/Gastro-Entdeckung-App
   cd Gastro-Entdeckung-App
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install flask flask-sqlalchemy flask-wtf flask-bcrypt flask-login
   ```
4. Install the module requests:
   ```
   pip install requests
   ```
5. Install package:
   ```
   pip install email_validator
   ```

## Running the Application

1. Set the Flask application:
   ```
   export FLASK_APP=app.py  # On Windows, use `set FLASK_APP=app.py`
   ```

2. Run the application:
   ```
   flask run
   ```

3. Open a web browser and navigate to `http://127.0.0.1:5000/`

## Usage

1. Register a new account or log in if you already have one.
2. Add restaurant tips by clicking on "Add Tip" in the navigation menu.
3. Search for tips using the search form, which allows filtering by cuisine, price range, and atmosphere.
4. Set your preferences to customize your experience.
5. View detailed information about each restaurant by clicking on its name in the tip list.

## License

This project is licensed under the MIT License.
