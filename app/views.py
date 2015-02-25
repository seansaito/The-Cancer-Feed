from flask import render_template, redirect, url_for, request
from app import application, mail
from flask.ext.mail import Message
from config import ADMINS
from scraper import get_mnr_articles, get_gov_articles, get_research_articles
from random import randint

@application.route("/", methods = ["GET", "POST"])
@application.route("/index", methods=["GET", "POST"])
def index():
    mnr_articles = get_mnr_articles()
    gov_articles = get_gov_articles()
    research_articles = get_research_articles()
    funfacts = [
        "Immunotherapy is the treatment of cancer using the functions of the human immune system",
        "beta-Carotene, found in veggies and fruits such as carrots, can in fact increase the risk of lung cancer for smokers/alcoholics",
        "LASER in laser therapy, which is a form of cancer treatment, stands for light amplification by stimulated emission of radiation",
        "The top 5 most common cancers among men and women are: 1.Lung 2.Breast 3.Colorectal 4.Prostate and 5.Stomach",
        "The number of new cases of cancer is expected to increase by 70 percent over the next 20 years (WHO)",
        "Tobacco use is the most important risk factor for cancer causing around 20 percent of global cancer deaths and around 70 percent of global lung cancer deaths (WHO)",
        "Cancer can originate almost anywhere in the body",
        "Specific cancers can be more prevalent in different areas. For example, Japan has a high frequency of stomach cancer",
        "Studies have suggested that the risk of developing some kinds of cancers (i.e. colon, stomach) is not determined by heredity.",
        "Radiation can also cause cancer, especially skin cancer",
        "Viruses can also cause cancer. For example, the Hepatitis B viruses can increase the risk of developing liver cancer",
        "The HPV (human papillomavirus), which can be transmitted via sexual contact, is a major cause of cervical cancer, as well as a cause for penile cancer",
        "Metastatis is the process of the cancer cells to penetrate into lymphatic and blood vessels. This allows cancer cells to circulate through the bloodstream and grow in normal tissues elsewhere",
        "Angiogenesis is the process of forming new blood vessels. This is required for a malignant cancer tumor to grow and spread through the body",
        "While normal cells perform apoptosis (programmed death), cancer cells lack this function and instead grow more rapidly",
        "Some drugs can inhibit angiogenesis of cancer cells, preventing them from growing further",
        "There are more than 100 types of 'cancer'",
        "Leading a healthy lifestyle is often the best way to prevent cancer"
    ]
    funfact = funfacts[randint(0, len(funfacts)-1)]
    return render_template("index.html",
            mnr_articles=mnr_articles, gov_articles=gov_articles,
            research_articles=research_articles, funfact=funfact)

@application.route("/resources", methods = ["GET", "POST"])
def resources():
    return render_template("resources.html")

@application.route("/feedback", methods=["GET", "POST"])
def feedback():
    return render_template("feedback.html")

@application.route("/videos", methods=["GET", "POST"])
def videos():
    return render_template("videos.html")

@application.route("/feedback_answer", methods=["POST"])
def feedback_answer():
    q1 = request.form["q1"]
    q2 = request.form["q2"]
    q3 = request.form["q3"]
    q4 = request.form["q4"]
    q5 = request.form["q5"]
    q6 = request.form["q6"]
    msg = Message("feedback", sender=ADMINS[0], recipients=ADMINS)
    body = "<p>What did you learn from the website?: %s\n </p> <p>What did you like about the website itself?: %s\n </p> <p>What did you not like?: %s\n </p> <p>Are you more interested in cancer now?: %s\n </p> <p>Email: %s\n </p> <p>Any other suggestions/comments?: %s\n</p>" % (q1, q2, q3, q4, q5, q6)
    send_email(msg, body)
    if q6 == "42":
        return redirect(url_for("prize"))
    return redirect(url_for("index"))

@application.route("/prize")
def prize():
    return render_template("prize.html")

def send_email(msg, body):
    msg.html = body
    with application.app_context():
        mail.send(msg)
