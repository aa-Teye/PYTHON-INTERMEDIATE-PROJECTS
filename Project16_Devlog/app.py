from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# This creates a file called 'projects.db' in your folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)

# Define how our Database looks
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database within the application context
with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        project_title = request.form['title']
        project_desc = request.form['description']
        new_project = Project(title=project_title, description=project_desc)

        try:
            db.session.add(new_project)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your project"
    else:
        # Get all projects from the database, newest first
        projects = Project.query.order_by(Project.date_created.desc()).all()
        return render_template('index.html', projects=projects)

if __name__ == "__main__":
    app.run(debug=True)