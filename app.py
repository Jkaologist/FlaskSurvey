from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.route("/")
def index():
    return render_template('survey_start.html', survey=survey)

@app.route("/begin")
def question_render():
    return render_template('question.html', question=survey.questions[0])

@app.route("/answer", methods=["GET", "POST"])
def responses():
    responses.append(request.args)
# This is where we are at
    return render_template("question.html")

@app.route("/questions/answer")
def next_question():
    return render_template('question.html', question=survey.questions[len(responses)])
