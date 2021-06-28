from flask import Flask, render_template

# Initialize App
app = Flask(__name__)

@app.route('/')
def home():

    return render_template('home.html')

@app.route('/object_detection')
def ObjectDetection():

    return render_template('object_detection.html')

if __name__ == "__main__":
    app.run(debug=True)
