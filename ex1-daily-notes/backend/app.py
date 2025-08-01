from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from mongoengine import connect
from config import Config

from routes.auth import auth
from routes.notes import notes

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
JWTManager(app)

# เชื่อมต่อ MongoDB ด้วย mongoengine โดยตรง
# เชื่อม MongoDB ด้วย URI เดียว
connect(host=app.config["MONGODB_SETTINGS"]["host"])

# Register Blueprints
app.register_blueprint(auth, url_prefix="/api")
app.register_blueprint(notes, url_prefix="/api")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)