"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app, forms
from flask import render_template, request, redirect, url_for, send_from_directory, flash
from .forms import PropertyForm
import psycopg2
from app.models import Properties
from . import db
from werkzeug.utils import secure_filename
import os





###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/properties/create', methods=['GET', 'POST'])
def newProperty():
    form = PropertyForm()

    if request.method == 'POST' and form.validate_on_submit():

        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
        new_property = Properties(
            title=form.propertyTitle.data,
            description=form.description.data,
            numBedrooms=form.numBedrooms.data, 
            numBathrooms=form.numBathrooms.data,
            location=form.location.data,
            price=form.price.data,
            types=form.types.data, 
            photo=form.photo.data.filename 

        )
        
        db.session.add(new_property)
        db.session.commit()
        

        flash('Successful submission', 'success')
        return redirect(url_for('properties')) 
    else:

        print(form.errors)
    return render_template('newProperty.html' , form = form)



@app.route('/properties')
def properties():
    all_properties = Properties.query.all()

    return render_template('properties.html', properties=all_properties)

@app.route('/properties/<property_id>')
def property(property_id):
    properties_in_location = Properties.query.filter_by(id= property_id ).all()

    print(properties_in_location)

    return render_template('property.html', property=properties_in_location)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

@app.route('/uploads/<filename>')
def get_image(filename):
    upload_folder = app.config['UPLOAD_FOLDER']
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)


