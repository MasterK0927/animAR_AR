from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/apply_filter', methods=['POST'])
def apply_filter():
    # Assuming your apply_filter.py takes some input, you can get it from the request
    # For example, if it's a file upload, you can access it using request.files['file']
    # Modify this part based on your requirements
    input_data = request.form.get('input_data')

    # Run your apply_filter.py script using subprocess
    subprocess.run(['python3', 'apply_filter.py', input_data])

    # Return a response as needed
    return "Filter applied successfully!"

if __name__ == '__main__':
    app.run(debug=True)
