from flask import Blueprint, render_template, request, flash, send_file
from the_scripter.models import Record, NavLink
from .functions import generateReplacementDict, script_creation
from .form import RecordForm, Form
from the_scripter import db
import os

# Blueprint Configuration
script_generator_bp = Blueprint(
    "script_generator_bp",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@script_generator_bp.route("/", methods=['GET', 'POST'])
def script_generator_func():
    form = RecordForm()
    links = NavLink.query


    if request.method == 'POST':
        if form.validate_on_submit():

            new_record = Record()
            db.session.add(new_record)
            new_record.name = form.name.data
            new_record.description = form.description.data
            new_record.link = form.link.data
            new_record.prefix = form.prefix.data
            
            if form.attachments.data:
                new_record.folder_path = os.path.join(
                        os.environ.get("UPLOAD_FOLDER"),
                        new_record.name.replace(' ', '_'))
                try:
                    os.makedirs(new_record.folder_path, exist_ok=True)
                except OSError as e:
                    print(e)
                for file in form.attachments.data:
                    file.save(new_record.folder_path + '/' + file.filename)
            db.session.commit()
            flash(f'Script {new_record.name} added to database!', 'success')
        else:
            flash('Check if all fields have the proper information.', 'danger')
            print("Form did not validate")

    records = Record.query

    return render_template(
        'script_generator.html',
        form=form,
        records=records,
        links=links,
        title="SQL Script Generator"
    )


@script_generator_bp.route("/<script_id>", methods=['GET', 'POST'])
def build_form(script_id):
    links = NavLink.query
    record = db.session.query(Record).filter_by(id=script_id).one()
    replacements = generateReplacementDict(record.folder_path, var='key_')
    # print(print("\n".join("{}\t{}".format(k, v) for k, v in replacements.items())))
    # print(replacements)
    form = Form(dictionary=replacements)

    if request.method == 'POST':
        loaded_replacements = {}
        for key, value in replacements.items():
            loaded_replacements[value] = request.form[key]
            # print(loaded_replacements[key], request.form[key], key, value)
        # print(print("\n".join("{}\t{}".format(k, v) for k, v in loaded_replacements.items())))
        if form.errors:
            flash(form.errors, 'danger')

        if form.validate():
            flash('Form validated', 'success')
            zipfile = script_creation(
                loaded_replacements, record.folder_path,
                os.path.join(record.folder_path, 'output'),
                record.name.replace(' ', '_'))
            print('./' + os.path.join(record.folder_path, 'output') + '/' + zipfile)
            flash(f'Script {zipfile} created and zipped', 'success')
            # return redirect('/downloadfile?filename=add-side_output/' + zipfile)
            return send_file('../' + os.path.join(record.folder_path, 'output') + '/' + zipfile,
                mimetype='zip', attachment_filename=zipfile,
                as_attachment=True)
        else:
            flash('Check if all fields have the proper information.', 'danger')
            flash(loaded_replacements, 'warning')

    return render_template(
        'script.html',
        form=form,
        record=record,
        links=links,
        size=len(replacements),
        replacements=replacements,
        title="SQL Script Generator"
    )