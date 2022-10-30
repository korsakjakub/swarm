from flask import Flask, render_template, request
from simulation import simulate

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('simulate') == 'simulate':
            simulate()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
