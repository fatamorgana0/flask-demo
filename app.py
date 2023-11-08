from flask import Flask, render_template, jsonify

app = Flask(__name__)

WARRIORS = [
  {
    'id' : 1,
    'name' : 'Samukai',
    'background' : 'Spinjitzu',
    'avg pay for the job' : 'million credits'
    
  },
  {
    'id' : 2,
    'name' : 'Belmont',
    'background' : 'Romania',
    'avg pay for the job' : '100 German franks'
  },
  {
    'id' : 3,
    'name' : 'Chupacabra',
    'avg pay for the job' : '10000 $$'

  }
]
@app.route("/warriors")
def list_warriors():
  return jsonify(WARRIORS)


@app.route("/")
def hello_world():
  return render_template('home.html', warriors = WARRIORS, protagonist = "Jack")

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)