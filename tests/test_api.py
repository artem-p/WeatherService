# todo http://flask.pocoo.org/docs/0.11/testing/

import src.rest as rest

rest.app.config['TESTING'] = True
test_app = rest.app.test_client()


def test_redirect():
    resp = test_app.get('/')
    assert resp.status_code == 302
    assert resp.location == 'http://localhost/api/1.0/current'
    pass
