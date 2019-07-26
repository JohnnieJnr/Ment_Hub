from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, static_url_path='/static')
# will be set on heroku
# PASSWORD = os.environ.get('POSTGRES_PASS')

POSTGRES = {
   'user': 'postgres',
   'pw': 'qwerty',
   'db': 'mentor_database',
   'host': 'localhost',
   'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')

#@app.route('/all_mentors')
#def all_mentors():
#    mentors = Mentor.query.all()
#    print("mentors?")
#    print(mentors)
#    return render_template('mentors.html')
    

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


@app.route('/new_mentor', methods=['POST'])
def new_mentor():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('mainpage.html')

if __name__ == '__main__':
    app.run(port=5001, debug=True)
