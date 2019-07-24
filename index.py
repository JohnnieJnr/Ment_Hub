from flask import Flask
from flask import render_template
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/mentor_database'
db = SQLAlchemy(app)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Create our database model
#class Mentor(db.Model):
#    __tablename__ = "mentor"
#    mentor_id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(100), nullable=False)
#    email = db.Column(db.String(100), nullable=False)
#    expertise = db.Column(db.String(200), nullable=False)
#    mentee_capacity = db.Column(db.Integer, nullable=False)
#    interest = db.Column(db.Text, nullable=False)
#    description = db.Column(db.Text, nullable=True)
#
#    def __init__(self, mentor_id, name, email, expertise, mentee_capacity, interest, description):
#        self.mentor_id = mentor_id
#        self.name = name
#        self.email = email
#        self.expertise = expertise
#        self.mentee_capacity = mentee_capacity
#        self.interest = interest
#        self.description = description
#        
#
#    def __repr__(self):
#        return '<mentor %r>' % self.name


#@app.route('/new_mentor', methods=['POST'] ['GET'])
#def new_mentor():
#    email = None
#    if request.method == 'POST':
#        email = request.form['email']
#        # Check that email does not already exist (not a great query, but works)
#        if not db.session.query(User).filter(User.email == email).count():
#            reg = User(email)
#            db.session.add(reg)
#            db.session.commit()
#            return render_template('success.html')
#    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5001, debug=True)