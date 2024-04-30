from flask import Flask, request, render_template, send_file
import csv
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('c2.html')
@app.route('/coverpage.html')
def Index():
    return render_template('coverpage.html')

@app.route('/sectiondetails.html')
def Index1():
    return render_template('456.html')
@app.route('/studentsdetail.html')
def Index2():
    df =pd.read_csv('student_data.csv')
    df.columns=["studentNumber", "studentName", "jeePercentage", "atitScore", "emcetScore", "tenthScore", "twelfthScore"]
    # abc1= df.to_dict('records')
    return render_template('html.html',tables=df.to_html(), titles=[''])

@app.route('/htmL.html', methods=['POST'])
def submit():
    if request.method == 'POST':
        studentNumber = request.form['studentNumber']
        studentName = request.form['studentName']
        jeePercentage = request.form['jeePercentage']
        atitScore = request.form['atitScore']
        emcetScore = request.form['emcetScore']
        tenthScore = request.form['tenthScore']
        twelfthScore = request.form['twelfthScore']

        # Create a list with the form data
        data = [studentNumber, studentName, jeePercentage, atitScore, emcetScore, tenthScore, twelfthScore]

        # Write the data to a CSV file
        with open('student_data.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)

    df =pd.read_csv('student_data.csv')
    df.columns=["studentNumber", "studentName", "jeePercentage", "atitScore", "emcetScore", "tenthScore", "twelfthScore"]
    # abc1= df.to_dict('records')
    return render_template('html.html',tables=df.to_html(), titles=[''])

@app.route('/sectiondetails.html',methods=['POST'])
def submit1():
    if request.method == 'POST':
       name=request.form['section']
  
    df =pd.read_csv(name+'.csv')
    # abc1= df.to_dict('records')
    return render_template('Page.html',tables=df.to_html())


@app.route('/SEC-A.html')
def IndexA():
    return render_template('SEC-A.html')
@app.route('/SEC-B.html')
def IndexB():
    return render_template('SEC-B.html')
@app.route('/SEC-C.html')
def IndexC():
    return render_template('SEC-C.html')
@app.route('/SEC-D.html')
def IndexD():
    return render_template('SEC-D.html')
@app.route('/download')
def download():
    return send_file('student_data.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
    