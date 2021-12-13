#for bmi please visit http://127.0.0.1:5000/bmi
#for age detector please visit http://127.0.0.1:5000/age
#for simple flask webpage please visit http://127.0.0.1:5000

from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

#Age detector
@app.route('/age', methods = ["POST", "GET"])

def age():
    if request.method == "POST":
        user = request.form["nm"]
        
        return redirect(url_for("user", age = user))
    else:
        return render_template('input.html')

@app.route("/<int:age>")
def user(age):
    if age < 18:
        return f'Sorry your age {age} is under 18'
    else:
        return f'Come in please'
   
   
   
# BMI calculator   
@app.route('/bmi', methods = ["POST", "GET"])

def bmi():
    if request.method == "POST":
        weight = request.form["weight"]
        height = request.form["height"]
        
        return redirect(url_for("calc", weight = weight, height = height ))
    else:
        return render_template('mass.html')  
   
@app.route('/<int:weight>/<int:height>')

def calc(weight, height):
    heightTOmeter = height / 100
    bMi = weight / (heightTOmeter * heightTOmeter)
    return f"Your BMI is {bMi}"



#navbar
posts = [
    {
        'author' : 'Soso Kumladze',
        'title' : 'blog post 2',
        'content' : 'some content',
        'data' : 'may 15, 2020',
    },
    {
        'author' : 'givi Kumladze',
        'title' : 'blog post 23',
        'content' : 'some content2',
        'data' : 'march 25, 2020',
    }
]   
   

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts = posts, title = 'home')


@app.route('/about')
def about():
    return render_template("about.html", title = 'About')


@app.route('/contact')
def contact():
    return render_template("contact.html", title = 'Contact')



if __name__ == '__main__':
    app.run(debug=True)