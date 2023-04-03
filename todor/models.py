from todor import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_by = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text)
    state = db.Column(db.Boolean, default=False)

    def __init__(self, create_by, title, desc, state=False):
        self.create_by = create_by
        self.title = title
        self.desc = desc
        self.state = state

    def __repr__(self):
        return f'<Todo {self.title}>'
