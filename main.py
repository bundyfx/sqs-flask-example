from flask import Flask
from main_page import main_page

app = Flask(__name__)
app.register_blueprint(main_page)

app.register_blueprint(main_page, url_prefix='/pages')

if __name__=='__main__':
  app.run()
