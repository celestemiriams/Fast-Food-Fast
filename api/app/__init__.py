"""
app root of the api endpoints
"""

from flask import Flask
from api.instances.config import DevelopmentConfig, ProductionConfig
from api.app.views import Urls


class Server:
    """Create flask object to start the server"""

    @staticmethod
    def create_app(config=None):
        """ This function returns the app"""

        app = Flask(__name__)
        app.config.update(config.__dict__ or {})
        Urls.generate(app)
        return app


App = Server().create_app(config=DevelopmentConfig)
