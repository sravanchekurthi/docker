from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html', message="Hello, World!")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

