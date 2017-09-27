from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'SUP BITCHES'

if __name__ == "__main__" :
	app.run()