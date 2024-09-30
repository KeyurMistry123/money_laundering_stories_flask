from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the CSV file once at the start to avoid reloading each time
csv_file = "money_laundering_stories.csv"
df = pd.read_csv(csv_file)

# Function to get stories for a given individual
def get_stories(individual_name):
    # Filter the DataFrame for the given individual's name
    stories = df[df["Individual"].str.lower() == individual_name.lower()]
    return stories["Story"].tolist()

# Route for the homepage (search bar)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle search requests
@app.route('/search', methods=['POST'])
def search():
    individual_name = request.form['name']
    stories = get_stories(individual_name)
    return render_template('index.html', stories=stories, name=individual_name)

if __name__ == "__main__":
    app.run(debug=True)
