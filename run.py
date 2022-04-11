from flask import Flask, render_template
import plotly
import json
import scripts.fundamentals as funds

app = Flask(__name__)

@app.route("/")
def index():
    greetings = "Hello World, this is my first plotly plot"


    plot = funds.get_dividends("AAPL")

    plotly_plot = json.dumps(plot, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("home.html", greetings=greetings, plotly_plot= plotly_plot)


if __name__ == "__main__":
    app.directory='./'
    app.run(host='127.0.0.1', port=5000)