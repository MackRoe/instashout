from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
db = client.InstaShout
profiles = db.profiles

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg="🔊 InstaShout 🔊")

""" USER STORIES
Users can create a profile (new/create)
Users can view their profile (show)
Users can delete their profile (destroy)
Users can edit their profile (edit/update)
User can send an InstaShout
User is informed their InstaShout has been sent
"""

if __name__ == '__main__':
    app.run(debug=True)