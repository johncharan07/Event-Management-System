from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'


mysql = MySQL(app)


@app.route('/')
def Home():
    return render_template('Home.html')


@app.route('/SignUp')
def SignUp():
    return render_template('SignUp.html')


@app.route('/SignUp', methods=['POST'])
def form():
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        Location = request.form['Location']
        NewPassword = request.form['NewPassword']
        ConfirmPassword = request.form['ConfirmPassword']
        Email = request.form['Email']
        cursor = mysql.connection.cursor()
        cursor.execute(
            ''' INSERT INTO eventmanagement VALUES(%s,%s,%s,%s,%s,%s)''', (FirstName, LastName, Location, NewPassword, ConfirmPassword,Email))
        mysql.connection.commit()
        cursor.close()
        return render_template('LogIn.html')


@app.route('/LogIn')
def LogIn():
    return render_template('LogIn.html')


@app.route('/MainHome', methods=['POST'])
def Home2():
    if request.method == 'POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        Subject = request.form['Subject']
        Number = request.form['Number']
        Email = request.form['Email']
       

        cursor = mysql.connection.cursor()
        cursor.execute(
            ''' INSERT INTO customers VALUES(%s,%s,%s,%s,%s,%s)''', (FirstName, LastName, Subject, Number, Email))
        mysql.connection.commit()
        cursor.close()
        return render_template('Home2.html')


@app.route('/MainHome')
def contactForm():
    return render_template('Home2.html')


@app.route('/LogIn', methods=['POST'])
def form2():
    if request.method == 'POST':
        UserName = request.form['UserName']
        Password = request.form['Password']
        cursor = mysql.connection.cursor()
        query = "SELECT * FROM eventmanagement where FirstName = %s and Password = %s"
        cursor.execute(query, (UserName, Password))

        result = cursor.fetchone()
        mysql.connection.commit()
        cursor.close()
        if result:
            return render_template('Home2.html')
        else:

            return render_template('Alert.html')


if __name__ == '__main__':
    app.run()
