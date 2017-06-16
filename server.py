from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# YOUR ROUTES GO HERE
JOB_SELECTION = ['Software Engineer', 'QA Engineer', 'Product Manager']

@app.route("/")
def index():
    """Return the simple homepage promising to make dreams come true by joining our company."""

    return render_template("index.html")



@app.route("/application-success", methods=["GET"])
def serve_app_form():
    """Return a page showing the basic application form to join us today."""

    return render_template("application-form.html")



@app.route('/response', methods=["POST"])
def show_madlib():
    """Show applicant application submission success message."""

    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    salary = request.args.get("salary")
    job = request.args.get("job_title")

    return render_template("application-success.html",
                           first_name=first_name,
                           last_name=last_name,
                           job=job,
                           salary=salary,
                           )


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
