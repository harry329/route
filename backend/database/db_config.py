from sqlalchemy import Column, String, Integer, Table,ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate , MigrateCommand
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()
migrate = Migrate()

def set_up_db(app):
    print("I am in setup db")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}/{}'.format('localhost:5432', 'route')
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()
    db.create_all()