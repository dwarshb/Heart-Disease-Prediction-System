from flask import Flask
from importlib import reload 
from flask import render_template, url_for, redirect
from flask import request
import test
import models as dbHandler

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def Loggedin():
    if request.method == 'POST':
        #patient_id = request.form['patient_id']

        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        bp = int(request.form['resting_bp'])
        cholesterol = int(request.form['serum_cholestrol'])
        blood_sugar = int(request.form['fasting_sugar'])
        heart_rate = int(request.form['max_heart_rate'])
        exercise = int(request.form['exercise'])
        global g_bp, g_cholesterol, g_bloodsugar, g_heartrate, g_exercise, g_out
        g_bp = bp
        g_cholesterol = cholesterol
        g_bloodsugar = blood_sugar
        g_heartrate = heart_rate
        g_exercise = exercise


        #blood_sugar=int(blood_sugar)
        #print "down "
        #dbHandler.insertPatientDetails(patient_id,age,sex,bp,cholesterol,blood_sugar,
         #                    heart_rate,exercise)
        #print "down 1"
        reload(test)
        output=test.prediction(age,sex,cp,bp,cholesterol,blood_sugar,heart_rate,exercise)
        g_out=output

        return render_template('products.html',**globals())
    else:
        return render_template('index.html')


@app.route('/graph')
def graph(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    dataset=[g_bp, g_cholesterol ,g_bloodsugar,g_heartrate]
    #series = [{"name": 'Ideal', "data": [[120,140], [170,200], [70,100], [60,100]]}, {"name": 'Current', "data":dataset }]
    series = [{"name": 'Ideal', "data": [[130], [185], [85], [80]]}, {"name": 'Current', "data":dataset }]
    title = {"text": 'Graphical Report'}
    xAxis = {"categories": ['Blood Pressure', 'Cholesterol', 'Blood Sugar','Heart Rate']}
    yAxis = {"title": {"text": 'Range of values'}}
    return render_template('store.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/prediction')

def prediction():
    return render_template('products.html',**globals())

@app.route('/store')
def store():
    return render_template('store.html')


@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)

