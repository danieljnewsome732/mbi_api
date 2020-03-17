"""Entry point."""
import os

from flask_script import Manager
from waitress import serve

from app import create_app
from mbi_api import blueprint

app = create_app(os.environ.get("ENV", "dev"))
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    """Run command to start the app."""
    if os.environ['ENV'].startswith('local'):
        app.run(
            host=app.config['HOST'],
            port=app.config['PORT']
        )
    else:
        serve(
            app, host=app.config['HOST'],
            port=app.config['PORT'],
            threads=app.config['THREADS']
        )

if __name__ == '__main__':
    manager.run()
