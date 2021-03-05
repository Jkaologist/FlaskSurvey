from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def index():
    return render_template('survey_start.html', survey=survey)

@app.route("/begin", methods=["GET", "POST"])
def question_render():
    session["responses"] = []
    return redirect('/questions/0')

@app.route("/questions/<int:num>")
def question_template(num):
    flash(session['responses'])
    if len(session['responses']) == len(survey.questions):
        return render_template('completion.html')
    return render_template('question.html', question=survey.questions[len(session['responses'])])

@app.route("/answer", methods=["GET", "POST"])
def question_responses():
    responses = session['responses']
    responses.append(request.form['answer'])
    session['responses'] = responses
    return redirect(f'questions/{len(responses)}')

