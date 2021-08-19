"""General page routes."""
from flask import Blueprint
from flask import current_app as app
from flask import render_template

from the_scripter.models import Record, NavLink

# Blueprint Configuration
home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route("/", methods=["GET"])
def home():
    """Homepage."""
    records = Record.query
    links = NavLink.query

    return render_template(
        "index.jinja2",
        title="The Scripter",
        subtitle="Use the forms below to generate SQL scripts to run in your \
            database",
        records=records,
        links=links,
        template="home-template",
    )


@home_bp.route("/about", methods=["GET"])
def about():
    """About page."""
    return render_template(
        "index.jinja2",
        title="About",
        subtitle="This is an example about page.",
        template="home-template page",
    )


@home_bp.route("/contact", methods=["GET"])
def contact():
    """Contact page."""
    return render_template(
        "index.jinja2",
        title="Contact",
        subtitle="This is an example contact page.",
        template="home-template page",
    )
