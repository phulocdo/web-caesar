from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def webapp():
    return render_template('web-caesar.html')


if __name__ == "__main__":
    app.run()