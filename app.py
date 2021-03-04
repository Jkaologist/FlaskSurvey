from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

curr_question = 0

@app.route("/")
def index():

    return render_template('survey_start.html', survey = survey)

@app.route("/begin")
def question_render():

    return render_template('question.html', question = survey.questions[curr_question])