# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import *

API_KEY = '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'
import random
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = API_KEY

words = {
    "Ball":"ball.svg.jpg",
    "Dog":"dog.png",
    "Elephant":"elephant.jpg",
    "Frog":"frog.jpeg",
    "Giraffe":"giraffe.jpg",
    "House":"house.jpg",
    "Ice cream":"ice cream.jpg",
    "Jellyfish":"jellyfish.png",
    "Kangaroo":"kangaroo.png",
    "Lion":"lion.png",
    "Monkey":"monkey.png",
    "Nurse":"nurse.png.jpeg",
    "Penguin":"penguin.png",
    "Queen":"queen.png",
    "Rabbit":"rabbit.png",
    "Sun":"sun.jpeg",
    "Turtle":"turtle.jpeg",
    "Umbrella":"umbrella.jpeg",
    "Violin":"violin.jpeg",
    "Whale":"whale.jpeg",
    "Xylophone":"xylophone.jpeg",
    "Yellow":"yellow.png",
    "Zebra":"zebra.jpeg",
    "Rainbow":"rainbow.png",
    "Student":"student.png",
    "Teacher":"teacher.png",
    "Doctor":"doctor.jpeg",
    "Engineer":"engineer",
    "Books":"books.jpg",
    "King":"king.png",
}


@app.route("/", methods=("GET", "POST"))
def home():
    return render_template("Home.html")

@app.route("/book",methods=("GET","POST"))
def book():
    if request.method == "POST":
        learn = request.form.get("book", False)
        age = request.form.get("age", False)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_learn(learn, age),
            temperature=0.6,
            max_tokens=900
        )
        return redirect(url_for("book", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("Book.html", result=result)


def generate_learn(learn, age):
    return """Explain  {0} like you are explaining it to a {1} year old . I need just the explaination and not any other sentance.""".format(learn, age)

@app.route("/math",methods=("GET","POST"))
def math():

    if request.method == "POST":
        global math
        math = request.form.get("math", False)
        age = request.form.get("age",False)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_math(math,age),
            temperature=0.6,
            max_tokens = 900
        )
        return redirect(url_for("math", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("math.html",result=result,math=math)
def generate_math(math,age):
    return """explain and solve {0} for a {1} year old concisely.I just need the explaination and nothing else.""".format(math,age)

@app.route("/learn", methods=("GET", "POST"))
def index():

    if request.method == "POST":
        global word
        word = random.choice(list(words.keys()))

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(word),
            temperature=0,
            max_tokens=900
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result, word=word, image = words[word])


def generate_prompt(w):
    return """Explain what a {} is for a 10 year old in a sentence.:""".format(
        w.capitalize()
    )


if __name__ == "__main__":
    app.run(debug=True)
