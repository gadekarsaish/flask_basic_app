from flask import Flask
app = Flask(__name__)
  
@app.route('/')
def hello():
    return "Welcome_to_the_flask_App (GitHub Repo)                                                        Version 4.0"
  
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug = True)
