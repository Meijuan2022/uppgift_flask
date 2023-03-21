# This is a sample Python Flask

from flask import Flask
from flask import render_template,request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("boder_collie_hemsidan.html")
@app.route("/Jorgen")
def hund_Jorgen():
    return render_template("hund_Jorgen.html")

@app.route("/result_uppgifter",methods=['POST','GET'])
def result_ug():
    if request.method == 'POST':
        return '''<h1 style="text-transform:uppercase;\
         border-top:1px solid #57b1dc;\
         border-bottom: 1px solid #57b1dc;">Tack!</h1>\
            <p>Vi har fått din hunds information,\
            och du finns nu på vår vänlista! Ser fram emot att träffa dig! </p>\
           <h3><a href="/"> Tillbaka hemsidan</a></h2>'''

@app.route("/test/register")
def register():
    return render_template("register.html")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port='5000')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
