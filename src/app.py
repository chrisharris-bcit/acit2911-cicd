from flask import Flask
from .routes.dogs import dogs_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(dogs_bp)
    return app

    # localhost:5000
    # localhost:5000/dogs       get all dogs
    # localhost:5000/dogs/1     get dog with id 1

if __name__ == '__main__':
    app = create_app()
    app.run()