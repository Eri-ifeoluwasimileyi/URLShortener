from flask import Flask
from flask_cors import CORS
from src.routes.route import urls

app = Flask(__name__)
CORS(app)
app.register_blueprint(urls)


if __name__ == '__main__':
    app.run(debug=True)
