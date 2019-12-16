import plotly
import plotly.graph_objs as go
import json

from flask import render_template, flash, request, redirect, session
from ORM import *
from WTForms import *

app.secret_key = 'development key'

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@app.route('/edit_company', methods = ['GET', 'POST'])
def edit_company():

    form = CompanyForm()
    select_result = Companies.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('companies.html', data=select_result, form=form)
        else:
            id = session['company_pk_data']
            company = Companies.query.filter_by(id=id).first()
            company.id = form.id.data, 
            company.registrationnumber = form.registrationnumber.data, 
            company.city = form.city.data, 
            company.country = form.country.data, 
            company.sizeofstaff = form.sizeofstaff.data

            db.session.commit()
            return render_template("companies.html", data=select_result, form=form)

    return render_template("companies.html", data=select_result, form=form)

@app.route('/edit_migration', methods = ['GET', 'POST'])
def edit_migration():

    form = MigrationForm()
    select_result = Migrations.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('migrations.html', data=select_result, form=form)
        else:
            id = session['migration_pk_data']
            migration = Migrations.query.filter_by(id=id).first()
            migration.databasefrom = form.databasefrom.data, 
            migration.databaseto = form.databaseto.data, 
            migration.hardwarenumber = form.hardwarenumber.data, 
            migration.id = form.id.data

            db.session.commit()
            return render_template("migrations.html", data=select_result, form=form)

    return render_template("migrations.html", data=select_result, form=form)

@app.route('/edit_company_migration', methods = ['GET', 'POST'])
def edit_company_migration():

    form = CompanyMigrationForm()
    select_result = CompanyMigration.query.filter_by().all()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required')
            return render_template('company-migration.html', data=select_result, form=form)
        else:
            [companyid, migrationid] = session['company_migration_data'].split('/')
            companyMigration = CompanyMigration.query.filter_by(companyid=companyid, migrationid=migrationid).first()
            companyMigration.companyid = form.companyid.data, 
            companyMigration.migrationid = form.migrationid.data, 
            db.session.commit()
            return render_template("company-migration.html", data=select_result, form=form)

    return render_template("company-migration.html", data=select_result, form=form)


@app.route('/companies', methods=['GET', 'POST'])
def companies():

    form = CompanyForm()
    select_result = Companies.query.filter_by().all()

    if request.method == 'POST':

        id_ = request.form.get('del')
        if (id_):
            selected_row = Companies.query.filter_by(id=id_).first()
            CompanyMigration.query.filter_by(companyid=id_).delete()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('companies.html', data=select_result, form=form)

        id_ = request.form.get('edit')
        if id_ is not None:
            selected_row = Companies.query.filter_by(id=id_).first()
            session['company_pk_data'] = id_
            return render_template("edit_company.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('companies.html', data=select_result, form=form)
        else:
            company = Companies(form.id.data, form.registrationnumber.data, form.city.data, form.country.data, form.sizeofstaff.data)
            db.session.add(company)
            db.session.commit()
            select_result.append(company)

    return render_template('companies.html', data=select_result, form=form)

@app.route('/companies-migrations', methods=['GET', 'POST'])
def companiesMigrations():

    form = CompanyMigrationForm()
    select_result = CompanyMigration.query.filter_by().all()

    if request.method == 'POST':

        id = request.form.get('del')
        if (id):
            [companyid, migrationid] = id.split('/')
            if (companyid and migrationid):
                selected_row = CompanyMigration.query.filter_by(companyid=companyid, migrationid=migrationid).first()
                db.session.delete(selected_row)
                db.session.commit()
                select_result.remove(selected_row)
                return render_template('company-migration.html', data=select_result, form=form)

        id = request.form.get('edit')
        if (id):
            [companyid, migrationid] = id.split('/')
            if (companyid and migrationid):
                selected_row = CompanyMigration.query.filter_by(companyid=companyid, migrationid=migrationid).first()
                session['company_migration_data'] = request.form.get('edit')
                return render_template("edit_company_migration.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('company-migration.html', data=select_result, form=form)
        else:
            company = CompanyMigration(form.companyid.data, form.migrationid.data)
            db.session.add(company)
            db.session.commit()
            select_result.append(company)

    return render_template('company-migration.html', data=select_result, form=form)


@app.route('/database-migrations', methods=['GET', 'POST'])
def migrations():

    form = MigrationForm()
    select_result = Migrations.query.filter_by().all()

    if request.method == 'POST':

        id_ = request.form.get('del')
        if (id_):
            selected_row = Migrations.query.filter_by(id=id_).first()
            CompanyMigration.query.filter_by(migrationid=id_).delete()
            db.session.delete(selected_row)
            db.session.commit()
            select_result.remove(selected_row)
            return render_template('migrations.html', data=select_result, form=form)

        id_ = request.form.get('edit')
        if id_ is not None:
            selected_row = Migrations.query.filter_by(id=id_).first()
            session['migration_pk_data'] = id_
            return render_template("edit_migration.html", row=selected_row, form=form)

        print(form.validate())
        if not form.validate():
            flash('All fields are required.')
            return render_template('migrations.html', data=select_result, form=form)
        else:
            migration = Migrations(form.databasefrom.data, form.databaseto.data, form.hardwarenumber.data, bool(form.sucess.data), form.id.data)
            db.session.add(migration)
            db.session.commit()
            select_result.append(migration)

    return render_template('migrations.html', data=select_result, form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    if request.method == 'POST':

        session['rel_db'] = request.form.get('rel_db')
        session['no_rel_db'] = request.form.get('no_rel_db')
        return redirect('/dashboard')

    staffSizes = ['A', 'B', 'C', 'D', 'E']
    select_result = db.session.query(Companies.sizeofstaff, db.func.count()).select_from(CompanyMigration).join(Companies, CompanyMigration.companyid == Companies.id).group_by(Companies.sizeofstaff)
    select_result2 = db.session.query(Companies.city, db.func.count()).select_from(CompanyMigration).join(Companies, CompanyMigration.companyid == Companies.id).group_by(Companies.city)

    migrationsAmount = [0, 0, 0, 0, 0]

    for s in select_result.all():
        staffSize = s[0]
        migrationsAmount[staffSizes.index(staffSize)] = s[1]
    
    cities = []
    migrations = []
    for s in select_result2.all():
        cities.append(s[0])
        migrations.append(s[1])
    
    graph = go.Figure([go.Bar(x=staffSizes, y=migrationsAmount)])
    graph2 = go.Figure([go.Bar(x=cities, y=migrations)])

    # bar, pie = go.Bar(x=codes, y=counting_stars, marker=dict(color='rgb(122, 122, 122)'))

    # data1, data2 = [bar], [pie]
    # ids = ["1", "2"]

    graphJSON1 = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON2 = json.dumps(graph2, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphJSON1=graphJSON1, graphJSON2 = graphJSON2)


if __name__ == '__main__':
    app.run(debug=True)