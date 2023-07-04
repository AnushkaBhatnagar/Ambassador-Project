from flask import Flask
from db import access_db
app = Flask(__name__)

@app.route("/")
def hello():
  s = access_db("SELECT * FROM Persons;")
  print(s)
  return "Hello World!"

if __name__ == "__main__":
  app.run(debug=True, port=8000)
