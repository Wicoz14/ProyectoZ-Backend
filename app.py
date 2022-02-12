from flask import Flask

import db

app = Flask(__name__)

print(db.listar())