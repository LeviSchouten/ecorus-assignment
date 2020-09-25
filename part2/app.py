from database_setup import Base, Person, Office, PersonWorking
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import Flask, request, jsonify

app = Flask(__name__)


engine = create_engine(
    'sqlite:///offices-collection.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/person', methods=['GET', 'POST'])
def person():
    if request.method == 'POST':
        new_person = Person(name=request.json['name'],
                            age=request.json['age'])
        session.add(new_person)
        session.commit()
        return f'person {new_person.name} created!', 201
    else:
        people = session.query(Person).all()
        return jsonify(people=[person.serialize for person in people]), 200


@app.route('/person/<int:person_id>/birthday', methods=['POST'])
def person_birthday(person_id):
    person = session.query(Person).filter_by(id=person_id).one()
    person.happy_birthday()
    session.commit()
    return jsonify(person.serialize), 200


@app.route('/person/<int:person_id>/name', methods=['POST', 'PUT'])
def person_name(person_id):
    person = session.query(Person).filter_by(id=person_id).one()
    person.change_name(name=request.json['name'])
    session.commit()
    return jsonify(person.serialize), 200


@app.route('/office', methods=['GET', 'POST'])
def office():
    if request.method == 'POST':
        new_office = Office(name=request.json['name'])
        session.add(new_office)
        session.commit()
        return jsonify(new_office.serialize), 201
    else:
        offices = session.query(Office).all()
        return jsonify(offices=[office.serialize for office in offices]), 200


@app.route('/office/<int:office_id>/add', methods=['POST'])
def office_add(office_id):
    # simulate start_working_for method
    new_person_working = PersonWorking(
        office_id=office_id, person_id=request.json['person_id'])
    session.add(new_person_working)
    session.commit()
    return jsonify(new_person_working.serialize)


@app.route('/office/<int:office_id>/remove', methods=['POST'])
def office_remove(office_id):
    # simulate finished_working_for method
    person_working = session.query(PersonWorking).filter_by(
        office_id=office_id, person_id=request.json['person_id']).first()
    session.delete(person_working)
    session.commit()
    return 'removed'


@app.route('/peopleworking', methods=['GET'])
def people_working():
    # show list of all working people and where they work
    people_working = session.query(PersonWorking).all()
    return jsonify(people_working=[person.serialize for person in people_working])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4996)
