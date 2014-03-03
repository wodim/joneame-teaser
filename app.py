from flask import Flask, render_template, request

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('login.html', failed=(request.method == 'POST'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=33333, debug=True)