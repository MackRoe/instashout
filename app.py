from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

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

@app.route('/profile/new')
def profile_new():
    """Create a new profile"""
    return render_template('profile_new.html')

@app.route('/profile/view', methods=['POST'])
def profile_submit():
    """Submit a new playlist."""
    profile = {
        'profile_name': request.form.get('profile_name'),
        'profile_number': request.form.get('profile_number'),
        'contact_number': request.form.get('contact_number'),
        'contact_provider': request.form.get('contact_provider')
    }
    # add info to db with the following:
    profiles.insert_one(profile)
    return redirect(url_for('profile_view'))

@app.route('/profile/<profile_id>')
def profile_view(profile_id):
    """Show profile"""
    # performs GET from db
    profile = profiles.find_one({'_id': ObjectId(profile_id)})
    return render_template('profile_view.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)