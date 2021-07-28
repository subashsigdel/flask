from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score >= 50:
        res = 'Pass'
    else:
        res = 'Fail'
    return render_template('result.html', result=res)


@app.route('/fail/<int:score>')
def fail(score):
    return "the person is failed and the marks is" + str(score)


@app.route('/submit', methods=['Post', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        python = float(request.form['python'])
        datascience = float(request.form['datascience'])
        total_score = (science + maths + python + datascience) / 4
    return redirect(url_for('success', score=total_score))


if __name__ == "__main__":
    app.run(debug=True)
