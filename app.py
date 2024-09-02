# importing the libraries
from flask import Flask,render_template,request
from Tweets import scrapedata
from predictions import pre
import pickle
import pandas as pd

#  environemnt req --> E:\E\Data Science\FakeNewsTwitterProject\FinalFrontentTwitterProject\myenv
#  myenv/Scripts/activate

#Global variables

app=Flask(__name__)

#user defined routes
@app.route("/", methods=["GET" ,"POST" ])
def home1():   
    return render_template('base.html')


@app.route("/index",methods=['GET','POST'])
def home():
    global num 
    if request.method == "POST":
        num =request.form['number']
        if num is None or num == "":
            num = 10
    global df
    print(num)
    df = scrapedata(int(num))
    context = df
    return render_template('index.html',tables=context)
    # return render_template('index.html', tables=[df.to_html(classes='table table-stripped')] , titles=df.columns.values)

@app.route("/prediction",methods=['GET','POST'])
def predict():
    output = pre(list(df['text']))
    df['ouput'] = output
    context = df
    return render_template('prediction.html',tables=context)



if __name__ =='__main__':
    app.run(debug=True)       


