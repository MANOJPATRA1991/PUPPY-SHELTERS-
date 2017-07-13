from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric

from sqlalchemy.ext.declarative import declarative_base

# to implement foreign key relationships
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

# Base maintains classes and tables relative to it
# Classes that we define inherit from the Base class
Base = declarative_base()


class Shelter(Base):
    # create a table named shelter
    __tablename__ = 'shelter'
    name = Column(String(80), nullable=False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(20))
    zipCode = Column(String(10))
    website = Column(String)
    id = Column(Integer, primary_key=True)


class Puppy(Base):
    # create a table named puppy
    __tablename__ = 'puppy'
    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    dateOfBirth = Column(Date)
    gender = Column(String(10), nullable=False)
    weight = Column(Numeric(10))
    picture = Column(String)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)


# INSERT AT END OF FILE
# creates an engine which provides connectivity to the puppyshelter database server
engine = create_engine('sqlite:///puppyshelter.db')

# goes into the database and adds the classes that we defined
# as new tables into the database
Base.metadata.create_all(engine)
