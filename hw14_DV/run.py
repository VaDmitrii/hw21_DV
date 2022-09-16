from flask import Flask

from database_views import database_blueprint

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.json.ensure_ascii

app.register_blueprint(database_blueprint)

if __name__ == "__main__":
    app.run()

