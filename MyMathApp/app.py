
from flask import Flask, render_template, request
from MyMath import MyMath

app = Flask(__name__)
my_math = MyMath()
number = ""

@app.route('/', methods=["GET", "POST"])
def index():
    error = ""
    if request.method == 'POST':
        if "Add" in request.form:
            if request.form["number"]:
                my_math.add_to_list(request.form["number"])
        elif "Calculate" in request.form:
            if len(my_math.num_list) > 1:
                my_math.calc()
            else:
                error = "List is less than 2 numbers."
        elif "Clear" in request.form:
            my_math.clear()

    return render_template('index.html', num_list=my_math.num_list, std_dev=my_math.std_dev, maximum=my_math.maximum, avg = my_math.avg, error = error)

@app.route('/buttons', methods=["GET","POST"])
def buttons():
    error = ""
    global number
    if request.method == 'POST':
        if "Add" in request.form:
            if request.form["number"]:
                my_math.add_to_list(request.form["number"])
                number = ""
        elif "Calculate" in request.form:
            if len(my_math.num_list) > 1:
                my_math.calc()
            else:
                error = "List is less than 2 numbers."
            number = ""
        elif "Clear" in request.form:
            my_math.clear()
            number = ""
        else:
            number += request.form["digit"]
    return render_template('buttons.html', num_list=my_math.num_list, std_dev=my_math.std_dev, maximum=my_math.maximum, avg = my_math.avg, error = error, number = number)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

