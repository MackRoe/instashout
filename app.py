from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from get_domain import DomainSMS
# import config
# from twilio.rest import Client
# -- saving for v2 --

app = Flask(__name__)
client = MongoClient()
db = client.InstaShout
profiles = db.profiles
profile_location = "at home"
# twilio_client = Client(config.account_sid, config.auth_token)
# -- saving for v2 --


@app.route('/')
def index():
    """Return homepage."""
    # provider_domain = DomainSMS.assign_domain(contact_provider)
    active_user = ObjectId("5da7949afd809f6f7ef35e84")
    return render_template('home.html', msg="🔊 InstaShout 🔊", profile_id=active_user)

""" USER STORIES
Users can create a profile (new/create) √
Users can view their profile (show)
Users can delete their profile (destroy) √
Users can edit their profile (edit/update) √
User can send an InstaShout √
User is informed their InstaShout has been sent
"""

@app.route('/admin')
def reference_list():
    """Show all profiles, admin """
    return render_template('ref_list.html', profiles=profiles.find())

@app.route('/profile/new')
def profiles_new():
    """Create a new profile"""
    return render_template('profile_new.html')


@app.route('/admin', methods=['POST'])
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
    return redirect(url_for('reference_list', profile=profile))

@app.route('/profile/<profile_id>')
def profile_view(profile_id):
    """Show individual profile"""
    profile = profiles.find_one({'_id': ObjectId(profile_id)})
    return render_template('profile_view.html', profile=profile)

@app.route('/profile/<profile_id>/edit')
def profile_edit(profile_id):
    """Show the edit form for a profile"""
    profile = profiles.find_one({'_id': ObjectId(profile_id)})
    return render_template('profile_edit.html', profile=profile)

@app.route('/profiles/<profile_id>', methods=['POST'])
def profiles_update(profile_id):
    """Submit an edited profile"""
    updated_profile = {
        'profile_name': request.form.get('profile_name'),
        'profile_number': request.form.get('profile_number'),
        'contact_number': request.form.get('contact_number'),
        'contact_provider': request.form.get('contact_provider')
    }
    profiles.update_one(
        {'_id': ObjectId(profile_id)},
        {'$set': updated_profile})

    active_user = ObjectId("5da7949afd809f6f7ef35e84")
    return redirect(url_for('profile_view'), profile_id = active_user)

@app.route('/profiles/<profile_id>/delete', methods=['POST'])
def profiles_delete(profile_id):
    """Delete profile"""
    profiles.delete_one({'_id': ObjectId(profile_id)})
    return redirect(url_for('/'))


if __name__ == '__main__':
    app.run(debug=True)