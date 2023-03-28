from flask import Flask

# Boot up the Flask app.
app = Flask(__name__)

# Blueprint imports for different routes.
from views import bp as view_bp
app.register_blueprint(view_bp)

# Run the application.
if __name__ == '__main__':
    app.run(debug = True)