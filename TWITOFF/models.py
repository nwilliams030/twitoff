from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users that we analyze"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)
    # this makes it look nicer when returning
    def __repr__(self):
        return '<User {}>'.format(self.name)

class Tweet(DB.Model):
    """Tweets we pull"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300
    # these link the user to the tweets, one user to many tweet relationship
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
    # formatting
    def __repr__(self):
        return '<Tweet {}>'.format(self.text)
