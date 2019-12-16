from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, Label
from wtforms import validators

class CompanyForm(Form):

    registrationnumber = StringField("Registration Number: ", [validators.data_required("Please, enter a Company Registration Number")])
    city = StringField("City: ", [validators.data_required("Please, enter a Company City")])
    country = StringField("Country ", [validators.data_required("Please, enter a Company Country")])
    sizeofstaff = StringField("Size of Staff: ", [validators.data_required("Please, enter a Company Size of Staff")])
    id = StringField("Id: ", [validators.data_required("Please, enter an ID")])

    submit = SubmitField("Enter")


class MigrationForm(Form):

    databasefrom = StringField("Database From: ", [validators.data_required("Please, enter a Migration Database From")])
    databaseto = StringField("Database To: ", [validators.data_required("Please, enter a Migration Database To")])
    hardwarenumber = StringField("Hardware Number: ", [validators.data_required("Please, enter a Migration Hardware Number")])
    sucess = StringField("Success: ", [])
    id = StringField("Id: ", [validators.data_required("Please, enter an Id")])

    submit = SubmitField("Enter")


class CompanyMigrationForm(Form):

    companyid = StringField("Company Id: ", [validators.data_required("Please, enter a Company Id")])
    migrationid = StringField("Migration Id: ", [validators.data_required("Please, enter a Migration Id")])

    submit = SubmitField("Enter")