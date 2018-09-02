from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

from account.controllers.accountCtrl import account_controller
from post.controllers.postCtrl import posts_controller


app.register_blueprint(posts_controller)
app.register_blueprint(account_controller)

app.secret_key = 'aSlrCPmKhb6kN2i4t3k_UOFx'
app.run(debug=True)