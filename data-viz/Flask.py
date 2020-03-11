from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/map1')
def map1():
    return render_template('map1.html', title='Map1')

@app.route('/map1_1')
def map1_1():
    return render_template('map1_1.html', title='Map1_1')
@app.route('/map1_2')
def map1_2():
    return render_template('map1_2.html', title='Map1_2')

@app.route('/map1_3')
def map1_3():
    return render_template('map1_3.html', title='Map1_3')
@app.route('/map2')
def map2():
    return render_template('map2.html', title='Map2')

@app.route('/map3')
def map3():
    return render_template('map3.html', title='Map3')
@app.route('/projet')
def projet():
    return render_template('projet.html', title='Elections')
@app.route('/')
def index():
    return render_template('index.html', title='Pzim !')







if __name__ == "__main__":
    app.run()


