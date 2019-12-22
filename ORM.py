from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pbwhorszaqzeya:500d580dfd54f78747aab111e364762631e9b19264ca6790f6c81f1a3aaacb56@ec2-184-73-209-230.compute-1.amazonaws.com:5432/d1eh44bepdpl7'

db = SQLAlchemy(app)

companyMigrations = db.Table('companymigratesdatabase',
    db.Column('companyid', db.Integer, db.ForeignKey('company.id'), primary_key=True),
    db.Column('migrationid', db.Integer, db.ForeignKey('databasemigration.id'), primary_key=True)
)

class Companies(db.Model):

    __tablename__ = 'company'

    id = db.Column('id', db.String(36), primary_key=True)
    city = db.Column('city', db.String(100))
    registrationnumber = db.Column('registrationnumber', db.String(50))
    country = db.Column('country', db.String(50))
    sizeofstaff = db.Column('sizeofstaff', db.String(1))

    def __init__(self, id, registrationnumber, city, country, sizeofstaff):

        self.id = id
        self.registrationnumber = registrationnumber
        self.city = city
        self.country = country
        self.sizeofstaff = sizeofstaff

    def __repr__(self):

        return '<Company: id=%r, registrationnumber=%r, city=%r, country=%r, sizeofstaff=%r>'.format(self.id, self.registrationnumber, self.city, self.country, self.sizeofstaff)


class Migrations(db.Model):

    __tablename__ = 'databasemigration'

    databasefrom = db.Column('databasefrom', db.String( 50))
    databaseto = db.Column('databaseto', db.String(50))
    hardwarenumber = db.Column('hardwarenumber', db.String(36))
    sucess = db.Column('sucess', db.Boolean)
    id = db.Column('id', db.String(36), primary_key=True)

    def __init__(self, databasefrom, databaseto, hardwarenumber, sucess, id):

        self.databasefrom = databasefrom
        self.databaseto = databaseto
        self.hardwarenumber = hardwarenumber
        self.sucess = sucess
        self.id = id

    def __repr__(self):

        return '<Migration: databasefrom=%r, databaseto=%r, hardwarenumber=%r, sucess=%r, id=%r>'.format(self.databasefrom, self.databaseto, self.hardwarenumber, self.sucess, self.id)

class CompanyMigration(db.Model):

    __tablename__ = 'companymigratesdatabase'
    __table_args__ = {'extend_existing': True} 

    companyid = db.Column('companyid', db.String(36), db.ForeignKey('company.id'), primary_key=True)
    migrationid = db.Column('migrationid', db.String(36), db.ForeignKey('databasemigration.id'), primary_key=True)

    def __init__(self, companyid, migrationid):

        self.companyid = companyid
        self.migrationid = migrationid

    def __repr__(self):

        return '<CompanyMigration: companyid=%r, migrationid=%r>'.format(self.companyid, self.migrationid)

db.create_all()
