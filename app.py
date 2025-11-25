# Import the flask class and create an instance of it
from flask import Flask
from blueprints.main import main as main_blueprint
from datetime import datetime

app = Flask(__name__)
app.register_blueprint(main_blueprint)

# Define a route and view function
@app.context_processor
def inject_globals():
    return {'current_year': datetime.now().year}


# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)