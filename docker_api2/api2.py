# app2.py
from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# HTML template to display the results
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculation Result</title>
</head>
<body>
    <h1>Calculation Result</h1>
    <p>{{ result_message }}</p>
</body>
</html>
'''

# Function to call the first API and display results
@app.route('/calculate', methods=['GET'])
def calculate():
    a = request.args.get('a')
    b = request.args.get('b')
    
    # Ensure a and b are provided
    if not a or not b:
        return "Please provide both 'a' and 'b' parameters", 400
    
    # Call the sum and division APIs
    try:
        add_response = requests.get(f'http://first-api-service:5000/add?a={a}&b={b}')
        divide_response = requests.get(f'http://first-api-service:5000/divide?a={a}&b={b}')
        
        add_result = add_response.json().get('result', 'Error')
        divide_result = divide_response.json().get('result', 'Error')

        result_message = f"Sum of {a} and {b} is: {add_result}. Division of {a} by {b} is: {divide_result}."
    except Exception as e:
        return f"Error occurred: {str(e)}", 500
    
    # Render the result using a simple HTML template
    return render_template_string(HTML_TEMPLATE, result_message=result_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

