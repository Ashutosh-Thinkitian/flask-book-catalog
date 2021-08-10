from app import db  # from root __init__.py , db instance of SQLAlchemy
from datetime import datetime

class Publication(db.Model):
    __tablename__ ='publication'    # this is table name must be same with class name..but not capitalize

    # create columns
    id = db.Column(db.Integer, primary_key=True)  # --> remove  in  __init__() (Later changes)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'The Publisher name is {}'.format(self.name)

# create class for another table
class Book(db.Model):
    __tablename__ ='book'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    #   one to many relationship because each publication have more than one book
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))  # create foreign key with id from publication table

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):

        # self.id =id --> did not need because SQLAlchemy automatically fill this
        self.title =title
        self.author =author
        self.avg_rating=avg_rating
        self.format = book_format
        self.image = image
        self.num_pages =num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {} '.format(self.title, self.author)