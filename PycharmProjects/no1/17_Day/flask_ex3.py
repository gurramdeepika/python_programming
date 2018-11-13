from flask import Flask

app = Flask(__name__)

@app.route('/hello/<int:no>')
def helloworld(no):return 'count is %d !'%no

if __name__ == '__main__':app.run(debug=True)

#app.route(rule,options) instead of @app.route('/') rule - path , options - arguments