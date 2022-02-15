from flask import Flask
from main.routes.authDp import authBp
from main.configurations.database.db import db_session

app = Flask(__name__)
app.config.from_object('main.configurations.config')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


app.register_blueprint(authBp, url_prefix='/auth')