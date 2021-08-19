from flask import Blueprint, render_template, request, flash
from the_scripter.models import NavLink, Record
from .form import RecordForm
from the_scripter import db
import os

# Blueprint Configuration
navigation_links_bp = Blueprint(
    "navigation_links_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@navigation_links_bp.route("/", methods=['GET', 'POST'])
def navigation_links_func():
    form = RecordForm()

    if request.method == 'POST':
        if form.validate_on_submit():

            new_record = NavLink()
            db.session.add(new_record)
            new_record.name = form.name.data
            new_record.link = form.link.data
            new_record.icon = form.icon.data
            db.session.commit()
            flash(f'Script {new_record.name} added to database!', 'success')
        else:
            flash('Check if all fields have the proper information.', 'danger')
            print("Form did not validate")

    records = Record.query
    links = NavLink.query

    return render_template(
        'navigation_links.html',
        form=form,
        records=records,
        links=links,
        title="SQL Script Generator"
    )
