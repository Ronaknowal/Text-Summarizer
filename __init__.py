from flask import Flask, redirect, url_for, request ,render_template
from main import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/output',methods=['POST'])
def output():
    if request.method == 'POST':
        textvalue = request.form.get("textarea", None)
        num_s=request.form.get("num_s", type=int)
        reverse=False
        if "reverse" in request.form:
            reverse = True
        return render_template('Output_Content.html', res=outputsumm(textvalue,num_s,reverse))

if __name__ == '__main__':
    app.run(debug=True)