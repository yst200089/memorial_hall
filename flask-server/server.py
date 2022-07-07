from flask import Flask
app = Flask(__name__)

@app.route('/members')
def show_members():
    return {"members": ["Member1", "Member2", "Member3"]}

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)