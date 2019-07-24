from flask import Flask
from flask import render_template
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

POSTGRES = {
   'user': 'postgres',
   'pw': 'qwerty',
   'db': 'mentor_database',
   'host': 'localhost',
   'port': '5432',
}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

#class Mentor(db.Model):
#    __tablename__ = "mentor"
#    mentor_id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(100), nullable=False)
#    email = db.Column(db.String(100), nullable=False)
#    expertise = db.Column(db.String(200), nullable=False)
#    mentee_capacity = db.Column(db.Integer, nullable=False)
#    interest = db.Column(db.Text, nullable=False)
#    description = db.Column(db.Text, nullable=True)
#    password = db.Column(db.String(50), nullable=False)
#
#    def __init__(self, mentor_id, name, email, expertise, mentee_capacity, interest, description, password):
#        self.mentor_id = mentor_id
#        self.name = name
#        self.email = email
#        self.expertise = expertise
#        self.mentee_capacity = mentee_capacity
#        self.interest = interest
#        self.description = description
#        self.password = password
#
#    def __repr__(self):
#        return '<mentor %r>' % self.name
     
@app.route('/new_mentor', methods=['POST'])
def new_mentor():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(mentor).filter(mentor.email == email).count():
            me = mentor('name', 'email', 'expertise', 'interest', 'description' 'password')
            db.session.add(me)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('SignUp/Signup.html')
    
if __name__ == '__main__':
    app.run(port=5001, debug=True)