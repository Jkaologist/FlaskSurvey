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

@app.route("/begin", methods=["GET", "POST"])
def question_render():
    return redirect('/questions/0')

@app.route("/questions/<int:num>")
def question_template(num):
    global responses
    flash(responses)
    if len(responses) == len(survey.questions):
        responses = [] #take this out later
        return render_template('completion.html')
    return render_template('question.html', question=survey.questions[len(responses)])

@app.route("/answer", methods=["GET", "POST"])
def question_responses():
    responses.append(request.form['answer'])
    return redirect(f'questions/{len(responses)}')
