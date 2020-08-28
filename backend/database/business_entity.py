from sqlalchemy import Column, Integer, String, ForeignKey
from .db_config import db
from sqlalchemy.orm import relationship, backref
from .freeway_business import freeway_business


class BusinessEntity(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    state = Column(String)
    city = Column(String)
    zip = Column(String)
    highways = Column(String)
    type_of_business = Column(String)
    miles_away = Column(String)
    avg_amt = Column(String)
    lat = Column(String)
    lng = Column(String)
    freeways = relationship(
        "Freeway", secondary=freeway_business, back_populates="business_entitys"
    )

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "state": self.state,
            "city": self.city,
            "zip": self.zip,
            "highways": self.highways,
            "type_of_business": self.type_of_business,
            "miles_away": self.miles_away,
            "avg_amt": self.avg_amt,
            "lat": self.lat,
            "lng": self.lng,
            "freeways": [freeway.format() for freeway in self.freeways],
        }

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
