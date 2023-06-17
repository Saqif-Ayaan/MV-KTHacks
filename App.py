from flask import Flask

def initApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'password'

    from Connector import connector
    
    app.register_blueprint(connector, url_prefix = '/')

    return app