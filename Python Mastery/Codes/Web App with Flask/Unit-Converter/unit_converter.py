
from flask import Flask, request, render_template

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

@app.route('/')
def home():
    return render_template('converter.html')

@app.route('/convert', methods=['POST'])
def convert():
    unit_type = request.form['unit_type']
    value = float(request.form['value'])
    if unit_type == 'c_to_f':
        result = celsius_to_fahrenheit(value)
        message = f"{value} Celsius is {result} Fahrenheit"
    elif unit_type == 'f_to_c':
        result = fahrenheit_to_celsius(value)
        message = f"{value} Fahrenheit is {result} Celsius"
    # Handle other conversions...
    return render_template('converter.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, port=8080)

