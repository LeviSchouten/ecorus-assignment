# import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine

Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'age': self.age,
            'id': self.id
        }

    def happy_birthday(self):
        self.age += 1

    def change_name(self, name):
        self.name = name


class Office(Base):
    __tablename__ = 'offices'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id
        }

    def start_working_for(self, person):
        self.people_working.append(person)

    def finished_working_for(self, person):
        if person in self.people_working:
            self.people_working.remove(person)


class PersonWorking(Base):
    __tablename__ = 'people_working'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    office_id = Column(Integer, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'person_id': self.person_id,
            'office_id': self.office_id
        }


engine = create_engine('sqlite:///offices-collection.db')
Base.metadata.create_all(engine)
