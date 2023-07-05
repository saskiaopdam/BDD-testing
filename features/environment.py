import os
import tempfile
from behave import fixture, use_fixture
# flaskr is the sample application we want to test
# from flaskr import app, init_db
from main import app, init_db

@fixture
def flaskr_client(context, *args, **kwargs):
    context.db, app.config['DATABASE'] = tempfile.mkstemp()
    app.testing = True
    context.client = app.test_client()
    with app.app_context():
        init_db()
    yield context.client
    # -- CLEANUP:
    os.close(context.db)
    os.unlink(app.config['DATABASE'])

def before_feature(context, feature):
    # -- HINT: Recreate a new flaskr client before each feature is executed.
    use_fixture(flaskr_client, context)