from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def convert():
    result = None
    if request.method == 'POST':
        try:
            temp = float(request.form['temperature'])
            from_unit = request.form['from_unit']
            if from_unit == 'Celsius':
                result = f"{(temp * 9/5) + 32:.2f} Fahrenheit"
            else:
                result = f"{(temp - 32) * 5/9:.2f} Celsius"
        except ValueError:
            result = "Invalid input. Please enter a number."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
