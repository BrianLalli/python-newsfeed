from app.routes import home

def create_app(test_config=None):
  @app.route('/hello')
  def hello():
    return 'hello world'

  # register routes
  app.register_blueprint(home)

  return app