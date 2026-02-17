from flask import Flask, render_template

app = Flask(__name__)

# Portfolio Data
projects = [
    {"id": 16, "name": "Dev-Log Tracker", "desc": "CRUD system for tracking daily coding progress."},
    {"id": 17, "name": "TaskMaster Pro", "desc": "Full-stack task manager with SQLite persistence."},
    {"id": 18, "name": "Network Monitor", "desc": "Automated server health and ping utility."},
    {"id": 19, "name": "Disk Guardian v2", "desc": "Interactive CLI tool for storage audits."}
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

if __name__ == "__main__":
    app.run(debug=True)