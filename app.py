from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Job Listing Aggregator API!"})

@app.route('/jobs')
def jobs():
    sample_jobs = [
        {"title": "Data Scientist", "company": "Detroit Tech", "location": "Detroit, MI"},
        {"title": "Software Engineer", "company": "TechStart", "location": "Ann Arbor, MI"},
        {"title": "AI Policy Analyst", "company": "Policy Lab", "location": "Remote"}
    ]
    return jsonify(sample_jobs)

if __name__ == '__main__':
    app.run(debug=True)
