from flask import Blueprint, render_template

# views = Blueprintclea('views', __name__)

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")