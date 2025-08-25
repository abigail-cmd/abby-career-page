from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/apply')
def apply():
    return render_template('apply.html')
    

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug =True)