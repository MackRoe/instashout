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

# profiles = [
#     { 'profile_name': 'Test', 'profile_number': '0000000000', 'contact_number': '1111111111', 'contact_provider': "Verizon" }
# ]

@app.route('/admin')
def reference_list():
    """Show all profiles, admin """
    return render_template('ref_list.html', profiles=profiles.find())

@app.route('/profile/new')
def profiles_new():
    """Create a new profile"""
    return render_template('profile_new.html')


@app.route('/admin', methods=['POST'])
# error: view is not a valid object id
# it must be a 12-byte input or a 24-character hex string
def profile_submit():
    """Submit a new profile"""
    profile = {
        'profile_name': request.form.get('profile_name'),
        'profile_number': request.form.get('profile_number'),
        'contact_number': request.form.get('contact_number'),
        'contact_provider': request.form.get('contact_provider')
    }
    print(profile)
    profiles.insert_one(profile)
    # profile = profiles.find_one({'_id': ObjectId(profile_id)})
    # error: profile_id is not defined
    return redirect(url_for('reference_list', profile=profile))

# @app.route('/profile/<profile_id>')
# def profile_view(profile_id):
#     """Show profile"""
#     # performs GET from db
#     profile = profiles.find_one({'_id': ObjectId(profile_id)})
#     return render_template('profile_view.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)