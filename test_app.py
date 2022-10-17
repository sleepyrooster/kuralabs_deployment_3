from application import app, greet

def test_quick():
  a = "jeff"
  greeting = greet(a)
  assert greeting == "Hi jeff"

def test_home_page():
    response = app.test_client().get('/')
    assert response.status_code == 200
    
def test_URL_Page():
    response = app.test_client().get('/your-url')
    assert response.status_code == 302

#  def test_error_page():
#   response = app.test_client().get('/index.html')
#   assert response.status_code == 404
