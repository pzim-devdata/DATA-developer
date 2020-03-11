from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/capture_ecran_terminal_scraping')
def map1():
    return render_template('capture_ecran_terminal_scraping.html', title="Capture d'écran du terminal lors du scraping.html")

@app.route('/folium_meilleurs_villes')
def map1_1():
    return render_template('folium_meilleurs_villes.html', title="Meilleurs villes d'île de France")
@app.route('/folium_ville_moins_bons_kpi')
def map1_2():
    return render_template('folium_ville_moins_bons_kpi.html', title='Ville avec les moins bons KPIs')

@app.route('/folium_ville_sans_transport')
def map1_3():
    return render_template('folium_ville_sans_transport.html', title='Villes sans transport')
@app.route('/map2')
def map2():
    return render_template('map2.html', title='Map2')

@app.route('/Boxplots')
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


