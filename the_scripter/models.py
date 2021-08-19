
"""Data models."""
from . import db
from dataclasses import dataclass
from flask_sqlalchemy import event


# Script Generator models
@dataclass
class Record(db.Model):
    """
    Table to store the records
    """
    __tablename__ = "sql_scripts_tbl"

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(64), index=False, unique=True, nullable=False)
    description = db.Column(db.Text, index=False, unique=False, nullable=True)
    link        = db.Column(db.String(128), index=True, unique=True, nullable=False)
    prefix      = db.Column(db.String(10), index=False, unique=False, nullable=True)
    folder_path = db.Column(db.String(256), index=False, unique=True, nullable=False)

    def __str__(self) -> str:
        return f'{self.id}, {self.name}, {self.description}, \
            {self.link}, {self.prefix}, {self.folder_path}'


# class Attachment(db.Model):
#     """
#     Table to store the SQL Scripts as SQL or zip
#     """
#     __tablename__ = 'attachments'

#     id = db.Column(db.Integer, primary_key=True)
#     record_id = db.Column(db.Integer, db.ForeignKey('sql_scripts.id'))
#     attachment = db.Column(db.BLOB)

#     # Relationship
#     sql_script = db.relationship(
#         'Record',
#         backref=db.backref('attachments', lazy='dynamic',
#                            collection_class=list)
#     )


# class scripter_form_fields(db.Model):
#     """
#     Table to store the SQL Scripts as SQL or zip
#     """
#     __tablename__ = 'scripter_form_fields'

#     id = db.Column(db.BigInteger, autoincrement=True, primary_key=True)
#     record_id = db.Column(db.Integer, db.ForeignKey('sql_scripts.id'))
#     attachment = db.Column(db.BLOB)


# Navigation Link model
@dataclass
class NavLink(db.Model):
    """
    Table to store the records
    """
    __tablename__ = "nav_link_tbl"

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(64), index=True, unique=True, nullable=False)
    link        = db.Column(db.String(128), index=False, unique=True, nullable=False)
    icon      = db.Column(db.String(32), index=False, unique=False, nullable=True)

    def __str__(self) -> str:
        return f'{self.id}, {self.name}, {self.link}, {self.icon}'


# pre-set Navigational links
@event.listens_for(NavLink.__table__, 'after_create')
def insert_initial_values(*args, **kwargs):
    db.session.add(NavLink(name='Home', link='/', icon='bi-house-fill'))
    db.session.add(NavLink(name=' Script Generator', link='/script_generator/', icon='bi bi-file-code-fill'))
    db.session.add(NavLink(name=' NavLink Form', link='/navigation_links/', icon='bi bi-link-45deg'))
    db.session.commit()
