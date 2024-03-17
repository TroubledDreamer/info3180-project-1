from . import db


class Properties(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    numBedrooms = db.Column(db.String(80))
    numBathrooms = db.Column(db.String(80))
    location = db.Column(db.String(300))
    price = db.Column(db.String(80))
    types = db.Column(db.String(80))
    description = db.Column(db.String(80))
    photo = db.Column(db.String(80))

    def __repr__(self):
        # return str(self.title,self.title,self.numBedrooms, self.numBathrooms,self.location,self.price,self.types,self.description,self.photo
        return str(self.title)




    def __init__(self, title, numBedrooms, numBathrooms, location, price, types, description, photo):
        
        self.title = title
        self.numBedrooms = numBedrooms
        self.numBathrooms = numBathrooms
        self.location = location
        self.price = price
        self.types = types
        self.description = description
        self.photo = photo
