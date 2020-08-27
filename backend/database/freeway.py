from .db_config import db
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, backref
from .freeway_business import freeway_business

class Freeway(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_state = Column(String)
    end_state = Column(String)
    length = Column(String)
    business_entitys = relationship('BusinessEntity', secondary=freeway_business, back_populates='freeways')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def format(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'start_state' : self.start_state,
            'end_state' : self.end_state,
            'length' : self.length
        }

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()