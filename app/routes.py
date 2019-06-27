from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        return "N/A"
    else:
        # userdata = formopener.dict_from(request.form)
        userdata = request.form
        print(userdata)
        state = userdata["state"]
        turtle = model.FindTurtle(state)
        return render_template("results.html", state = state, turtle = turtle)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')
    
@app.route('/Cite', methods=['GET', 'POST'])
def Cite():
    return render_template('Cite.html')