from flask import Flask, render_template, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def webapp():
    return render_template('web-caesar.html')

@app.route('/', methods=['GET','POST'])
def encrypt():
    if(request.method == 'POST'):
        rot = request.form['rot']
        text = request.form['text'] 
        encrypt_txt = rotate_string(str(text),int(rot))
	
        return render_template('encrypted.html', text=encrypt_txt)

if __name__ == "__main__":
    app.run()
