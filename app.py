import numpy as np
from flask import Flask, request, jsonify, render_template,redirect
import pickle as pkl
import pandas as pd

import spacy
nlp = spacy.blank("en")

app = Flask(__name__)



CV_NB = pkl.load(open("./Models/CV_NB.pkl","rb"))
TV_NB = pkl.load(open("./Models/TV_NB.pkl","rb"))

CVTransformer = pkl.load(open("./Models/CVTransformer.pkl","rb"))
TFTransformer = pkl.load(open("./Models/TFTransformer.pkl","rb"))


def predictions(text):
	doc = nlp(text)
	tokens = [token.text for token in doc]
	s = " ".join(tokens)
	CVProcess = CVTransformer.transform([s])
	TFProcess = TFTransformer.transform([s])
	p1 = CV_NB.predict(CVProcess)[0]
	p2 = TV_NB.predict(TFProcess)[0]

	return p1,p2

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=["POST","GET"])
def predict():
	if request.method == "POST":
		text = request.form["url"]
		p1,p2 = predictions(text)
		if(p1==1):
			msg1 = "The website is Phishy..!!!"
		else:
			msg1 = "The website is Safe."
		if(p2==1):
			msg2 = "The website is Phishy..!!!"
		else:
			msg2 = "The website is Safe."
		return render_template('index.html',res = (msg1,msg2))
	return redirect('/')


if __name__ == '__main__':
	app.run(debug=True)