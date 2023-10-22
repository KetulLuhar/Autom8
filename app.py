from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/studentlogin')
def studentlogin():
    return render_template('user.html')

@app.route('/client')
def client():
    return render_template('client.html')

@app.route('/createAccount')
def createAccount():
    return render_template('createAccount.html')

@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html')

@app.route('/password')
def password():
    return render_template('password.html')

@app.route('/menu1')
def menu1():
    return render_template('menu1.html')

if __name__ == "__main__":  
    app.run(debug=True)