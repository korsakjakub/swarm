from flask import Flask, render_template, request

from config import Config
from simulation import simulate

app = Flask(__name__,
            static_url_path='',
            static_folder=Config.gif_dir,
            template_folder=Config.templates)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_inputs = request.form
        for key in form_inputs:
            value = form_inputs[key]
            if key == "v0" and 0.1 < float(value) < 10:
                Config.v0 = int(value)
            if key == "a" and 0.0 <= float(value) <= 1.0:
                Config.a = float(value)
            if key == "r" and 0.1 < float(value):
                Config.r = float(value)
            if key == "rb" and 0.1 < float(value):
                Config.rb = float(value)
            if key == "birds_amount" and 1 < int(value) < 10000:
                Config.birds_amount = int(value)
            if key == "time_range" and 2 < int(value) < 500:
                Config.time_range = int(value)
            if key == "include_predator":
                Config.include_predator = bool(value)
        if request.form.get('simulate') == 'simulate':
            simulate()
    return render_template('index.html',
                           v0=Config.v0,
                           a=Config.a,
                           r=Config.r,
                           rb=Config.rb,
                           birds_amount=Config.birds_amount,
                           time_range=Config.time_range,
                           include_predator=Config.include_predator
                           )


if __name__ == '__main__':
    app.run(port=6666, host="0.0.0.0")
