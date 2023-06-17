from flask import Flask

def initApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'password'

    from Connector import st
    from Connector import qz
    from Connector import rd

    app.register_blueprint(st, url_prefix = '/')
    app.register_blueprint(rd, url_prefix = '/')
    app.register_blueprint(qz, url_prefix = '/')
    
    return app

  