
from dash_packages.index import app
# from dash_packages.reservoir_visualization import app2

@app.server.route("/")
def hello():
    print("nawaf")
    return "jokes"


@app.server.route("/dashboard")
def dashboard():
    return app.index()

@app.server.route('/apps/reservoir_parameters_analys')
def dashboard2():
    return app.index()

@app.server.route('/apps/reservoir_data_analys')
def dashboard3():
    return app.index()