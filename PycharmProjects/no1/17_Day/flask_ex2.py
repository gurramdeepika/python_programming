from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>/<name1>')
def helloworld(name,name1):return 'Hello %s , Hi..!!! %s!'%(name,name1)

if __name__ == '__main__':app.run(debug=True)

#app.route(rule,options) instead of @app.route('/') rule - path , options - arguments