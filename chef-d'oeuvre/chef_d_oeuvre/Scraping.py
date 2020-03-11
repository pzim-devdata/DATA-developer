#!/usr/bin/env python
# coding: utf-8

# In[41]:


import getpass
w=getpass.getpass("Veuiller entrer le mot de passe SMTP :")
destinataire=['pzimsimplon@protonmail.com','pzim@pzim.fr','pizim@posteo.net']
password=w
adresse_envoi='gmurtinlove@gmail.com'
smtp='smtp.gmail.com'
port=587
login=adresse_envoi


#!/usr/bin/env python
# coding: utf-8

# In[143]:

try:

    #!/usr/bin/env python
    # coding: utf-8

    # In[241]:


    #!pip install bs4 requests
    #!pip install pytz
    #!pip install -U googlemaps
    import googlemaps
    import os
    import csv
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    from datetime import datetime
    import pytz
    import time
    from tqdm import tqdm
    import shutil

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import lxml
    import smtplib
    import getpass

    #import re

    clé_api_google='AIzaSyAC3sVokoA2BXoD4e7nsHMk6BpFRtV1wFA'

    # path et nom des dossiers:
    emplacement_ancien_csv_ville='CSV/anciens_csv/anciens_csv_villes'
    emplacement_ancien_csv_transport='CSV/anciens_csv/anciens_csv_transport'
    emplacement_ancien_csv_voiture='CSV/anciens_csv/anciens_csv_voiture'
    #emplacement_ancien_csv_voiture_heure_de_pointe="anciens_csv/anciens_csv_voiture/heure_de_pointe"
    emplacement_ancien_csv_velo='CSV/anciens_csv/anciens_csv_velo'
    emplacement_ancien_csv_distance='CSV/anciens_csv/anciens_csv_distance'
    emplacement_anciens_donnees_non_traitees='CSV/anciens_csv/anciens_csv_non_traitees'
    emplacement_anciens_csv_coordonnees_geo='CSV/anciens_csv/anciens_csv_coordonnees_geo'

    emplacement_csv_villes='CSV/csv_villes'
    emplacement_csv_temps_transport='CSV/temps/temps_transports'
    emplacement_csv_temps_velo='CSV/temps/temps_velo'
    emplacement_csv_temps_voiture='CSV/temps/temps_voiture'
    #emplacement_csv_temps_voiture_heure_de_pointe="temps/temps_voiture"
    emplacement_csv_distance='CSV/distance'
    emplacement_donnees_non_traitees='CSV/donnees_non_traitees'
    emplacement_coordonnees_geo='CSV/coordonnees_geo_ville'

    today = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%H:%M:%S , LE %d/%m/%Y"))
    print('PROGRAMME DEMARRE A : '+today)


    # In[243]:


    


    # In[ ]:


    destinataire=['pzimsimplon@protonmail.com','pzim@pzim.fr','pizim@posteo.net']
    password=w
    adresse_envoi='gmurtinlove@gmail.com'
    smtp='smtp.gmail.com'
    port=587
    login=adresse_envoi


    # In[166]:


    print("\nI. Scraping des villes d'Île de France sur Wikipédia\n")
    print("    Scraping des villes d'Essonne")

    requete = requests.get("https://fr.wikipedia.org/wiki/Liste_des_communes_de_l%27Essonne")
    page = requete.content
    soup = BeautifulSoup(page, features="lxml")

    essonne=[]
    for a in tqdm(soup.find_all('td',{'style':'text-align:left;'})):
        essonne.append(str(a.text))

    print("    Nettoyage de la liste 'essonne'")
    for i in tqdm(range(0,len(essonne))):
        essonne[i]=essonne[i].replace('\n','')


    print("    Scraping des codes postaux d'Essonne")
    essonne_code_postal2=[]
    for a in tqdm(soup.find_all('td')):
        essonne_code_postal2.append(str(a.text))

    print("    Nettoyage de la liste 'essonne_code_postal2'")
    essonne_code_postal=[]
    for i in range (3,len(essonne_code_postal2),10):
        essonne_code_postal.append(essonne_code_postal2[i])
    del essonne_code_postal[-1]
    del essonne_code_postal[-1]
    i=-1
    for code in essonne_code_postal:
        i=i+1
        if len(code) > 5:
            essonne_code_postal[i]=essonne_code_postal[i][0:5]
    essonne_code_postal[0]='91000'
    df_essonne = pd.DataFrame(essonne)
    df_essonne[1]=pd.DataFrame(essonne_code_postal)


    # In[167]:


    print("    Scraping des villes des Hauts-de-Seine")

    requete = requests.get("https://fr.wikipedia.org/wiki/Liste_des_communes_des_Hauts-de-Seine")
    page = requete.content
    soup = BeautifulSoup(page, features="lxml")

    hauts_de_seine=[]
    for a in tqdm(soup.find_all('td',{'style':'text-align:left;'})):
        hauts_de_seine.append(str(a.text))

    print("    Nettoyage de la liste 'hauts_de_seine'")
    for i in tqdm(range(0,len(hauts_de_seine))):
        hauts_de_seine[i]=hauts_de_seine[i].replace('\n','')

    print("    Scraping des codes postaux des Hauts-de-Seine")
    hauts_de_seine_code_postal2=[]
    for a in tqdm(soup.find_all('td')):
        hauts_de_seine_code_postal2.append(str(a.text))

    print("    Nettoyage de la liste 'hauts_de_seine_code_postal2'")
    hauts_de_seine_code_postal=[]
    for i in range (3,len(hauts_de_seine_code_postal2),10):
        hauts_de_seine_code_postal.append(hauts_de_seine_code_postal2[i])
    del hauts_de_seine_code_postal[-154:-1]
    del hauts_de_seine_code_postal[-1]
    i=-1
    for code in hauts_de_seine_code_postal:
        i=i+1
        if len(code) > 5:
            hauts_de_seine_code_postal[i]=hauts_de_seine_code_postal[i][0:5]
    df_hauts_de_seine = pd.DataFrame(hauts_de_seine)
    df_hauts_de_seine[1]=pd.DataFrame(hauts_de_seine_code_postal)


    # In[168]:


    print("    Scraping des villes de Seine-et-Marne")

    requete = requests.get("https://fr.wikipedia.org/wiki/Communes_de_Seine-et-Marne")
    page = requete.content
    soup = BeautifulSoup(page, features="lxml")

    seine_et_marne=[]
    for a in tqdm(soup.find_all('td',{'style':'text-align:left;'})):
        seine_et_marne.append(str(a.text))

    print("    Nettoyage de la liste 'seine_et_marne'")
    for i in tqdm(range(0,len(seine_et_marne))):
        seine_et_marne[i]=seine_et_marne[i].replace('\n','')


    print("    Scraping des codes postaux de Seine-et-Marne")
    seine_et_marne_code_postal2=[]
    for a in tqdm(soup.find_all('td')):
        seine_et_marne_code_postal2.append(str(a.text))

    print("    Nettoyage de la liste 'seine_et_marne_code_postal2'")
    seine_et_marne_code_postal=[]
    for i in range (3,len(seine_et_marne_code_postal2),10):
        seine_et_marne_code_postal.append(seine_et_marne_code_postal2[i])
    del seine_et_marne_code_postal[-1]
    del seine_et_marne_code_postal[-1]
    i=-1
    for code in seine_et_marne_code_postal:
        i=i+1
        if len(code) > 5:
            seine_et_marne_code_postal[i]=seine_et_marne_code_postal[i][0:5]
    df_seine_et_marne = pd.DataFrame(seine_et_marne)
    df_seine_et_marne[1]=pd.DataFrame(seine_et_marne_code_postal)


    # In[169]:


    print("    Scraping des villes de Seine-Saint-Denis")

    requete = requests.get("https://fr.wikipedia.org/wiki/Communes_de_la_Seine-Saint-Denis")
    page = requete.content
    soup = BeautifulSoup(page, features="lxml")

    seine_saint_denis=[]
    for a in tqdm(soup.find_all('td',{'style':'text-align:left;'})):
        seine_saint_denis.append(str(a.text))

    print("    Nettoyage de la liste 'seine_saint_denis'")
    for i in tqdm(range(0,len(seine_saint_denis))):
        seine_saint_denis[i]=seine_saint_denis[i].replace('\n','')


    print("    Scraping des codes postaux de Seine-Saint-Denis")
    seine_saint_denis_code_postal2=[]
    for a in tqdm(soup.find_all('td')):
        seine_saint_denis_code_postal2.append(str(a.text))

    print("    Nettoyage de la liste 'seine_saint_denis_code_postal2'")
    seine_saint_denis_code_postal=[]
    for i in range (3,len(seine_saint_denis_code_postal2),10):
        seine_saint_denis_code_postal.append(seine_saint_denis_code_postal2[i])
    del seine_saint_denis_code_postal[-1]
    del seine_saint_denis_code_postal[-1]
    i=-1
    for code in seine_saint_denis_code_postal:
        i=i+1
        if len(code) > 5:
            seine_saint_denis_code_postal[i]=seine_saint_denis_code_postal[i][0:5]
    df_seine_saint_denis = pd.DataFrame(seine_saint_denis)
    df_seine_saint_denis[1]=pd.DataFrame(seine_saint_denis_code_postal)


    # In[170]:


    print("    Scraping des villes du Val-de-Marne")

    requete = requests.get("https://fr.wikipedia.org/wiki/Communes_du_Val-de-Marne")
    page = requete.content
    soup = BeautifulSoup(page, features="lxml")

    val_de_marne=[]
    for a in tqdm(soup.find_all('td',{'style':'text-align:left;'})):
        val_de_marne.append(str(a.text))

    print("    Nettoyage de la liste 'val_de_marne'")
    for i in tqdm(range(0,len(val_de_marne))):
        val_de_marne[i]=val_de_marne[i].replace('\n','')


    print("    Scraping des codes postaux du Val-de-Marne")
    val_de_marne_code_postal2=[]
    for a in tqdm(soup.find_all('td')):
        val_de_marne_code_postal2.append(str(a.text))

    print("    Nettoyage de la liste 'val_de_marne_code_postal2'")
    val_de_marne_code_postal=[]
    for i in range (6,len(val_de_marne_code_postal2),10):
        val_de_marne_code_postal.append(val_de_marne_code_postal2[i])
    del val_de_marne_code_postal[-1]
    del val_de_marne_code_postal[-1]
    i=-1
    for code in val_de_marne_code_postal:
        i=i+1
        if len(code) > 5:
            val_de_marne_code_postal[i]=val_de_marne_code_postal[i][0:5]
    df_val_de_marne = pd.DataFrame(val_de_marne)
    df_val_de_marne[1]=pd.DataFrame(val_de_marne_code_postal)


    # In[171]:


    print("    Scraping des villes du Val-d'Oise")

    requete = requests.get("https://fr.wikipedia.org/wiki/Communes_du_Val-d%27Oise")
    page = requete.content
    soup = BeautifulSoup(page, features="lxml")

    val_d_oise=[]
    for a in tqdm(soup.find_all('td',{'style':'text-align:left;'})):
        val_d_oise.append(str(a.text))

    print("    Nettoyage de la liste 'val_d_oise'")
    for i in tqdm(range(0,len(val_d_oise))):
        val_d_oise[i]=val_d_oise[i].replace('\n','')


    print("    Scraping des codes postaux du Val-d'Oise")
    val_d_oise_code_postal2=[]
    for a in tqdm(soup.find_all('td')):
        val_d_oise_code_postal2.append(str(a.text))

    print("    Nettoyage de la liste 'val_de_marne_code_postal2'")
    val_d_oise_code_postal=[]
    for i in range (3,len(val_d_oise_code_postal2),10):
        val_d_oise_code_postal.append(val_d_oise_code_postal2[i])
    del val_d_oise_code_postal[-1]
    del val_d_oise_code_postal[-1]
    i=-1
    for code in val_d_oise_code_postal:
        i=i+1
        if len(code) > 5:
            val_d_oise_code_postal[i]=val_d_oise_code_postal[i][0:5]
    df_val_d_oise = pd.DataFrame(val_d_oise)
    df_val_d_oise[1]=pd.DataFrame(val_d_oise_code_postal)


    # In[172]:


    print("    Scraping des villes des Yvelines")

    requete = requests.get("https://fr.wikipedia.org/wiki/Communes_des_Yvelines")
    page = requete.content
    soup = BeautifulSoup(page, features="lxml")

    yvelines=[]
    for a in tqdm(soup.find_all('td',{'style':'text-align:left;'})):
        yvelines.append(str(a.text))

    print("    Nettoyage de la liste 'yvelines'")
    for i in tqdm(range(0,len(yvelines))):
        yvelines[i]=yvelines[i].replace('\n','')


    print("    Scraping des codes postaux des Yvelines")
    yvelines_code_postal2=[]
    for a in tqdm(soup.find_all('td')):
        yvelines_code_postal2.append(str(a.text))

    print("    Nettoyage de la liste 'yvelines_code_postal2'")
    yvelines_code_postal=[]
    for i in range (3,len(yvelines_code_postal2),10):
        yvelines_code_postal.append(yvelines_code_postal2[i])
    del yvelines_code_postal[-1]
    del yvelines_code_postal[-1]
    i=-1
    for code in yvelines_code_postal:
        i=i+1
        if len(code) > 5:
            yvelines_code_postal[i]=yvelines_code_postal[i][0:5]
    df_yvelines = pd.DataFrame(yvelines)
    df_yvelines[1]=pd.DataFrame(yvelines_code_postal)


    # In[173]:


    today1 = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%Y%m%d_%H%M%S"))


    # In[174]:


    today1 = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%Y%m%d_%H%M%S"))
    print('\nCréation des CSVs de la liste des villes et des codes postaux pour chaque département:\n')

    #df = pd.DataFrame(yvelines)
    df_yvelines.to_csv(emplacement_csv_villes+'/yvelines'+today1+'.csv', index=False)
    print('    CSV pour les Yvelines créé')

    #df = pd.DataFrame(val_d_oise)
    df_val_d_oise.to_csv(emplacement_csv_villes+'/val_d_oise'+today1+'.csv', index=False)
    print("    CSV pour le Val d'Oise créé")

    #df = pd.DataFrame(val_de_marne)
    df_val_de_marne.to_csv(emplacement_csv_villes+'/val_de_marne'+today1+'.csv', index=False)
    print("    CSV pour le Val de Marne créé")

    #df = pd.DataFrame(seine_saint_denis)
    df_seine_saint_denis.to_csv(emplacement_csv_villes+'/seine_saint_denis'+today1+'.csv', index=False)
    print("    CSV pour la Seine-Saint-Denis créé")

    #df = pd.DataFrame(seine_et_marne)
    df_seine_et_marne.to_csv(emplacement_csv_villes+'/seine_et_marne'+today1+'.csv', index=False)
    print("    CSV pour la Seine et Marne")

    #df = pd.DataFrame(hauts_de_seine)
    df_hauts_de_seine.to_csv(emplacement_csv_villes+'/hauts_de_seine'+today1+'.csv', index=False)
    print("    CSV pour les Hauts-de-Seine créé")

    #df = pd.DataFrame(essonne)
    df_essonne.to_csv(emplacement_csv_villes+'/essonne'+today1+'.csv', index=False)
    print("    CSV pour l'Essonne créé")


    # In[175]:


    print('\nSuppression des anciens CSV :\n')
    print('    Nettoyage du dossier : '+emplacement_csv_villes)
    import os
    dossier_affaires= os.listdir(emplacement_csv_villes)

    for csv in dossier_affaires:
      if csv[-19:-4]!= today1:
        shutil.move(emplacement_csv_villes+"/"+str(csv), emplacement_ancien_csv_ville+"/"+str(csv))
    print("    Anciens CSV déplacés vers le dossier : "+emplacement_ancien_csv_ville)


    # In[245]:


    print("\n\nII. Scraping des temps de trajet et des distances vers Place du Châtelet à Paris\npour chacune des villes d'Île de France, suivant différents modes de transport :\n\n- Voiture : Trafic normal et heure de pointe\n- Transports en commun\n- Vélo \n")


    # In[178]:


    print("\nScraping des temps de trajet en voiture (trafic normal) dans les Yvelines :")
    tps_yvelines_voiture=[]
    temp2_list=[]
    coordonnees_villes_yvelines=[]
    k=-1
    for i in tqdm(yvelines):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=yvelines_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="driving",
                                                traffic_model='optimistic',
                                                 departure_time=datetime(2020, 1, 19, 6, 32, 19, 831260))
            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_yvelines_voiture.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_yvelines_voiture.append(temp_list)

    print('Création du CSV temps en voiture pour les Yvelines :')

    with open(emplacement_donnees_non_traitees+'/tps_yvelines_voiture'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_coordonnees_geo+'/coordonnees_villes_yvelines'+today1+'.csv', "w") as f:
        for x in tps_yvelines_voiture:

            try:
                lat = x[1][0]['legs'][0]['start_location']['lat']
                lng = x[1][0]['legs'][0]['start_location']['lng']
            except:
                lat=float('NaN')
                lng=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(lat)+','+str(lng)+'\n')
            coordonnees_villes_yvelines.append(ville)
            coordonnees_villes_yvelines.append(lat)
            coordonnees_villes_yvelines.append(lng)
    print("    CSV des coordonnées géographiques pour les Yvelines créé")

    with open(emplacement_csv_temps_voiture+'/yvelines'+today1+'.csv', "w") as f:
        for x in tps_yvelines_voiture:

            try:
                duree = x[1][0]['legs'][0]['duration_in_traffic']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en voiture pour les Yvelines créé")


    # In[179]:


    print('Création du CSV des distances pour les Yvelines:')

    with open(emplacement_csv_distance+'/yvelines'+today1+'.csv', "w") as f:
        for x in tps_yvelines_voiture:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances pour les Yvelines créé")


    # In[180]:


    print("Scraping des temps de trajet en voiture (heure de pointe) dans les Yvelines :")
    tps_yvelines_voiture_heure_de_pointe=[]
    temp2_list=[]
    k=-1
    for i in tqdm(yvelines):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=yvelines_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="driving",
                                                 traffic_model='pessimistic',
                                                 departure_time=datetime(2020, 1, 13, 8, 0, 19, 831260))

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_yvelines_voiture_heure_de_pointe.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_yvelines_voiture_heure_de_pointe.append(temp_list)

    print('Création du CSV temps en voiture en heure de pointe pour les Yvelines :')
    with open(emplacement_csv_temps_voiture+'/yvelines_heure_de_pointe'+today1+'.csv', "w") as f:
        for x in tps_yvelines_voiture_heure_de_pointe:

            try:
                duree = x[1][0]['legs'][0]['duration_in_traffic']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en voiture en heure de pointe pour les Yvelines créé")

    print('Création du CSV des distances en heure de pointe pour les Yvelines:')

    with open(emplacement_donnees_non_traitees+'/tps_yvelines_voiture_heure_de_pointe'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_distance+'/yvelines_heure_de_pointe'+today1+'.csv', "w") as f:
        for x in tps_yvelines_voiture_heure_de_pointe:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances en heure de pointe pour les Yvelines créé")


    # In[184]:


    print("Scraping des temps de trajet en voiture (trafic normal) dans le Val d'Oise :")
    tps_val_d_oise_voiture=[]
    temp2_list=[]
    coordonnees_villes_val_d_oise=[]
    k=-1
    for i in tqdm(val_d_oise):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=val_d_oise_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="driving", traffic_model='optimistic', 
                                                 departure_time=datetime(2020, 1, 19, 6, 32, 19, 831260))

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_val_d_oise_voiture.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_val_d_oise_voiture.append(temp_list)


    print("Création du CSV temps en voiture pour le Val d'Oise :")

    with open(emplacement_donnees_non_traitees+'/tps_val_d_oise_voiture'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_coordonnees_geo+'/coordonnees_villes_val_d_oise'+today1+'.csv', "w") as f:
        for x in tps_val_d_oise_voiture:

            try:
                lat = x[1][0]['legs'][0]['start_location']['lat']
                lng = x[1][0]['legs'][0]['start_location']['lng']
            except:
                lat=float('NaN')
                lng=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(lat)+','+str(lng)+'\n')
            coordonnees_villes_val_d_oise.append(ville)
            coordonnees_villes_val_d_oise.append(lat)
            coordonnees_villes_val_d_oise.append(lng)
    print("    CSV des coordonnées géographiques pour le Val d'Oise créé")      

    with open(emplacement_csv_temps_voiture+'/val_d_oise'+today1+'.csv', "w") as f:
        for x in tps_val_d_oise_voiture:

            try:
                duree = x[1][0]['legs'][0]['duration_in_traffic']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en voiture pour le Val d'Oise créé")

    print("Création du CSV des distances pour le Val d'Oise:")

    with open(emplacement_csv_distance+'/val_d_oise'+today1+'.csv', "w") as f:
        for x in tps_val_d_oise_voiture:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances pour le Val d'Oise créé")


    # In[185]:


    print("Scraping des temps de trajet en voiture (heure de pointe) dans le Val d'Oise :")
    tps_val_d_oise_voiture_heure_de_pointe=[]
    temp2_list=[]
    k=-1
    for i in tqdm(val_d_oise):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=val_d_oise_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="driving",
                                                traffic_model='pessimistic',
                                                 departure_time=datetime(2020, 1, 13, 8, 0, 19, 831260))

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_val_d_oise_voiture_heure_de_pointe.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_val_d_oise_voiture_heure_de_pointe.append(temp_list)

    print("Création du CSV temps en voiture en heure de pointe pour le Val d'Oise :")

    with open(emplacement_donnees_non_traitees+'/tps_val_d_oise_voiture_heure_de_pointe'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_temps_voiture+'/val_d_oise_heure_de_pointe'+today1+'.csv', "w") as f:
        for x in tps_val_d_oise_voiture_heure_de_pointe:

            try:
                duree = x[1][0]['legs'][0]['duration_in_traffic']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en voiture en heure de pointe pour le Val d'Oise créé")

    print("Création du CSV des distances en heure de pointe pour le Val d'Oise:")

    with open(emplacement_csv_distance+'/val_d_oise_heure_de_pointe'+today1+'.csv', "w") as f:
        for x in tps_val_d_oise_voiture_heure_de_pointe:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances en heure de pointe pour le Val d'Oise créé")


    # In[186]:


    print("Scraping des temps de trajet en voiture (trafic normal) dans le Val de Marne :")
    tps_val_de_marne_voiture=[]
    temp2_list=[]
    coordonnees_villes_val_de_marne=[]
    k=-1
    for i in tqdm(val_de_marne):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=val_de_marne_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="driving",traffic_model='optimistic', 
                                                 departure_time=datetime(2020, 1, 19, 6, 32, 19, 831260))

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_val_de_marne_voiture.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_val_de_marne_voiture.append(temp_list)

    print("Création du CSV temps en voiture pour le Val de Marne :")

    with open(emplacement_donnees_non_traitees+'/tps_val_de_marne_voiture'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_coordonnees_geo+'/coordonnees_villes_val_de_marne'+today1+'.csv', "w") as f:
        for x in tps_val_de_marne_voiture:

            try:
                lat = x[1][0]['legs'][0]['start_location']['lat']
                lng = x[1][0]['legs'][0]['start_location']['lng']
            except:
                lat=float('NaN')
                lng=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(lat)+','+str(lng)+'\n')
            coordonnees_villes_val_de_marne.append(ville)
            coordonnees_villes_val_de_marne.append(lat)
            coordonnees_villes_val_de_marne.append(lng)
    print("    CSV des coordonnées géographiques pour le Val de Marne créé")               

    with open(emplacement_csv_temps_voiture+'/val_de_marne'+today1+'.csv', "w") as f:
        for x in tps_val_de_marne_voiture:

            try:
                duree = x[1][0]['legs'][0]['duration_in_traffic']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en voiture pour le Val de Marne créé")

    print("Création du CSV des distances pour le Val de Marne:")

    with open(emplacement_csv_distance+'/val_de_marne'+today1+'.csv', "w") as f:
        for x in tps_val_de_marne_voiture:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances pour le Val de Marne créé")


    # In[187]:


    print("Scraping des temps de trajet en voiture (heure de pointe) dans le Val de Marne :")
    tps_val_de_marne_voiture_heure_de_pointe=[]
    temp2_list=[]
    k=-1
    for i in tqdm(val_de_marne):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=val_de_marne_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="driving",
                                                traffic_model='pessimistic',
                                                 departure_time=datetime(2020, 1, 13, 8, 0, 19, 831260))

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_val_de_marne_voiture_heure_de_pointe.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_val_de_marne_voiture_heure_de_pointe.append(temp_list)

    print("Création du CSV temps en voiture en heure de pointe pour le Val de Marne :")

    with open(emplacement_donnees_non_traitees+'/tps_val_de_marne_voiture_heure_de_pointe'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_temps_voiture+'/val_de_marne_heure_de_pointe'+today1+'.csv', "w") as f:
        for x in tps_val_de_marne_voiture_heure_de_pointe:

            try:
                duree = x[1][0]['legs'][0]['duration_in_traffic']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en voiture en heure de pointe pour le Val de Marne créé")

    print("Création du CSV des distances en heure de pointe pour le Val de Marne :")

    with open(emplacement_csv_distance+'/val_de_marne_heure_de_pointe'+today1+'.csv', "w") as f:
        for x in tps_val_de_marne_voiture_heure_de_pointe:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances en heure de pointe pour le Val de Marne créé")


    # In[197]:


    print("Scraping des temps de trajet en voiture (trafic normal) dans la Seine-Saint-Denis :")
    tps_seine_saint_denis_voiture=[]
    temp2_list=[]
    coordonnees_villes_seine_saint_denis=[]
    k=-1
    for i in tqdm(seine_saint_denis):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=seine_saint_denis_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="driving", traffic_model='optimistic'
                                                 ,departure_time=datetime(2020, 1, 19, 6, 32, 19, 831260))

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_seine_saint_denis_voiture.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_seine_saint_denis_voiture.append(temp_list)

    print("Création du CSV temps en voiture pour la Seine-Saint-Denis :")

    with open(emplacement_donnees_non_traitees+'/tps_seine_saint_denis_voiture'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_coordonnees_geo+'/coordonnees_villes_seine_saint_denis'+today1+'.csv', "w") as f:
        for x in tps_seine_saint_denis_voiture:

            try:
                lat = x[1][0]['legs'][0]['start_location']['lat']
                lng = x[1][0]['legs'][0]['start_location']['lng']
            except:
                lat=float('NaN')
                lng=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(lat)+','+str(lng)+'\n')
            coordonnees_villes_seine_saint_denis.append(ville)
            coordonnees_villes_seine_saint_denis.append(lat)
            coordonnees_villes_seine_saint_denis.append(lng)
    print("    CSV des coordonnées géographiques pour la Seine-Saint-Denis créé")        

    with open(emplacement_csv_temps_voiture+'/seine_saint_denis'+today1+'.csv', "w") as f:
        for x in tps_seine_saint_denis_voiture:

            try:
                duree = x[1][0]['legs'][0]['duration_in_traffic']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en voiture pour la Seine-Saint-Denis créé")

    print("Création du CSV des distances pour la Seine-Saint-Denis :")

    with open(emplacement_csv_distance+'/seine_saint_denis'+today1+'.csv', "w") as f:
        for x in tps_seine_saint_denis_voiture:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances pour la Seine-Saint-Denis créé")


    # In[198]:


    print("Scraping des temps de trajet en voiture (heure de pointe) dans la Seine-saint-Denis :")
    tps_seine_saint_denis_voiture_heure_de_pointe=[]
    temp2_list=[]
    k=-1
    for i in tqdm(seine_saint_denis):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=seine_saint_denis_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="driving",
                                                traffic_model='pessimistic',
                                                 departure_time=datetime(2020, 1, 13, 8, 0, 19, 831260))

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_seine_saint_denis_voiture_heure_de_pointe.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_seine_saint_denis_voiture_heure_de_pointe.append(temp_list)

    print("Création du CSV temps en voiture en heure de pointe pour la Seine-saint-Denis :")

    with open(emplacement_donnees_non_traitees+'/tps_seine_saint_denis_voiture_heure_de_pointe'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_temps_voiture+'/seine_saint_denis_heure_de_pointe'+today1+'.csv', "w") as f:
        for x in tps_seine_saint_denis_voiture_heure_de_pointe:

            try:
                duree = x[1][0]['legs'][0]['duration_in_traffic']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en voiture en heure de pointe pour la Seine-saint-Denis créé")

    print("Création du CSV des distances en heure de pointe pour la Seine-saint-Denis :")

    with open(emplacement_csv_distance+'/seine_saint_denis_heure_de_pointe'+today1+'.csv', "w") as f:
        for x in tps_seine_saint_denis_voiture_heure_de_pointe:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances en heure de pointe pour la Seine-saint-Denis créé")


    # In[9]:


    now = datetime(2020, 1, 5, 6, 32, 19, 831260)
    now


    # In[188]:


    print("Scraping des temps de trajet en voiture (trafic normal) dans la Seine et Marne :")
    tps_seine_et_marne_voiture=[]
    temp2_list=[]
    coordonnees_villes_seine_et_marne=[]
    k=-1
    for i in tqdm(seine_et_marne):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=seine_et_marne_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="driving", traffic_model='optimistic'
                                                 ,departure_time=datetime(2020, 1, 19, 6, 32, 19, 831260))

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_seine_et_marne_voiture.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_seine_et_marne_voiture.append(temp_list)

    print("Création du CSV temps en voiture pour la Seine et Marne :")

    with open(emplacement_donnees_non_traitees+'/tps_seine_et_marne_voiture'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_coordonnees_geo+'/coordonnees_villes_seine_et_marne'+today1+'.csv', "w") as f:
        for x in tps_seine_et_marne_voiture:

            try:
                lat = x[1][0]['legs'][0]['start_location']['lat']
                lng = x[1][0]['legs'][0]['start_location']['lng']
            except:
                lat=float('NaN')
                lng=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(lat)+','+str(lng)+'\n')
            coordonnees_villes_seine_et_marne.append(ville)
            coordonnees_villes_seine_et_marne.append(lat)
            coordonnees_villes_seine_et_marne.append(lng)
    print("    CSV des coordonnées géographiques pour la Seine et Marne créé")     

    with open(emplacement_csv_temps_voiture+'/seine_et_marne'+today1+'.csv', "w") as f:
        for x in tps_seine_et_marne_voiture:

            try:
                duree = x[1][0]['legs'][0]['duration_in_traffic']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en voiture pour la Seine et Marne créé")

    print("Création du CSV des distances pour la Seine et Marne :")

    with open(emplacement_csv_distance+'/seine_et_marne'+today1+'.csv', "w") as f:
        for x in tps_seine_et_marne_voiture:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances pour la Seine et Marne créé")


    # In[189]:


    print("Scraping des temps de trajet en voiture (heure de pointe) dans la Seine et Marne :")
    tps_seine_et_marne_voiture_heure_de_pointe=[]
    temp2_list=[]
    k=-1
    for i in tqdm(seine_et_marne):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=seine_et_marne_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="driving",
                                                traffic_model='pessimistic',
                                                 departure_time=datetime(2020, 1, 13, 8, 0, 19, 831260))

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_seine_et_marne_voiture_heure_de_pointe.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_seine_et_marne_voiture_heure_de_pointe.append(temp_list)

    print("Création du CSV temps en voiture en heure de pointe pour la Seine et Marne :")

    with open(emplacement_donnees_non_traitees+'/tps_seine_et_marne_voiture_heure_de_pointe'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_temps_voiture+'/seine_et_marne_heure_de_pointe'+today1+'.csv', "w") as f:
        for x in tps_seine_et_marne_voiture_heure_de_pointe:

            try:
                duree = x[1][0]['legs'][0]['duration_in_traffic']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en voiture en heure de pointe pour la Seine et Marne créé")

    print("Création du CSV des distances en heure de pointe pour la Seine et Marne :")

    with open(emplacement_csv_distance+'/seine_et_marne_heure_de_pointe'+today1+'.csv', "w") as f:
        for x in tps_seine_et_marne_voiture_heure_de_pointe:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances en heure de pointe pour la Seine et Marne créé")


    # In[190]:


    print("Scraping des temps de trajet en voiture (trafic normal) dans les Hauts-de-Seine :")
    tps_hauts_de_seine_voiture=[]
    temp2_list=[]
    coordonnees_villes_hauts_de_seine=[]
    k=-1
    for i in tqdm(hauts_de_seine):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=hauts_de_seine_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="driving", traffic_model='optimistic'
                                                 ,departure_time=datetime(2020, 1, 19, 6, 32, 19, 831260))

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_hauts_de_seine_voiture.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_hauts_de_seine_voiture.append(temp_list)

    print("Création du CSV temps en voiture pour les Hauts-de-Seine :")

    with open(emplacement_donnees_non_traitees+'/tps_hauts_de_seine_voiture'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))


    with open(emplacement_coordonnees_geo+'/coordonnees_villes_hauts_de_seine'+today1+'.csv', "w") as f:
        for x in tps_hauts_de_seine_voiture:

            try:
                lat = x[1][0]['legs'][0]['start_location']['lat']
                lng = x[1][0]['legs'][0]['start_location']['lng']
            except:
                lat=float('NaN')
                lng=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(lat)+','+str(lng)+'\n')
            coordonnees_villes_hauts_de_seine.append(ville)
            coordonnees_villes_hauts_de_seine.append(lat)
            coordonnees_villes_hauts_de_seine.append(lng)
    print("    CSV des coordonnées géographiques pour les Hauts de Seine créé")  


    with open(emplacement_csv_temps_voiture+'/hauts_de_seine'+today1+'.csv', "w") as f:
        for x in tps_hauts_de_seine_voiture:

            try:
                duree = x[1][0]['legs'][0]['duration_in_traffic']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en voiture pour les Hauts-de-Seine créé")

    print("Création du CSV des distances pour les Hauts-de-Seine :")

    with open(emplacement_csv_distance+'/hauts_de_seine'+today1+'.csv', "w") as f:
        for x in tps_hauts_de_seine_voiture:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances pour les Hauts-de-Seine créé")


    # In[191]:


    print("Scraping des temps de trajet en voiture (heure de pointe) dans les Hauts-de-Seine :")
    tps_hauts_de_seine_voiture_heure_de_pointe=[]
    temp2_list=[]
    k=-1
    for i in tqdm(hauts_de_seine):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=hauts_de_seine_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="driving",
                                                traffic_model='pessimistic',
                                                 departure_time=datetime(2020, 1, 13, 8, 0, 19, 831260))

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_hauts_de_seine_voiture_heure_de_pointe.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_hauts_de_seine_voiture_heure_de_pointe.append(temp_list)

    print("Création du CSV temps en voiture en heure de pointe pour les Hauts-de-Seine :")

    with open(emplacement_donnees_non_traitees+'/tps_hauts_de_seine_voiture_heure_de_pointe'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_temps_voiture+'/hauts_de_seine_heure_de_pointe'+today1+'.csv', "w") as f:
        for x in tps_hauts_de_seine_voiture_heure_de_pointe:

            try:
                duree = x[1][0]['legs'][0]['duration_in_traffic']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en voiture en heure de pointe pour les Hauts-de-Seine créé")

    print("Création du CSV des distances en heure de pointe pour les Hauts-de-Seine :")

    with open(emplacement_csv_distance+'/hauts_de_seine_heure_de_pointe'+today1+'.csv', "w") as f:
        for x in tps_hauts_de_seine_voiture_heure_de_pointe:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances en heure de pointe pour les Hauts-de-Seine créé")


    # In[192]:


    print("Scraping des temps de trajet en voiture (trafic normal) dans l'Essonne :")
    tps_essonne_voiture=[]
    temp2_list=[]
    coordonnees_villes_essonne=[]
    k=-1
    for i in tqdm(essonne):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=essonne_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="driving", traffic_model='optimistic'
                                                 ,departure_time=datetime(2020, 1, 19, 6, 32, 19, 831260))

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_essonne_voiture.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_essonne_voiture.append(temp_list)


    print("Création du CSV temps en voiture pour l'Essonne :")

    with open(emplacement_donnees_non_traitees+'/tps_essonne_voiture'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_coordonnees_geo+'/coordonnees_villes_essonne'+today1+'.csv', "w") as f:
        for x in tps_essonne_voiture:

            try:
                lat = x[1][0]['legs'][0]['start_location']['lat']
                lng = x[1][0]['legs'][0]['start_location']['lng']
            except:
                lat=float('NaN')
                lng=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(lat)+','+str(lng)+'\n')
            coordonnees_villes_essonne.append(ville)
            coordonnees_villes_essonne.append(lat)
            coordonnees_villes_essonne.append(lng)
    print("    CSV des coordonnées géographiques pour l'Essonne créé")

    with open(emplacement_csv_temps_voiture+'/essonne'+today1+'.csv', "w") as f:
        for x in tps_essonne_voiture:

            try:
                duree = x[1][0]['legs'][0]['duration_in_traffic']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en voiture pour l'Essonne créé")

    print("Création du CSV des distances pour l'Essonne :")

    with open(emplacement_csv_distance+'/essonne'+today1+'.csv', "w") as f:
        for x in tps_essonne_voiture:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances pour l'Essonne créé")


    # In[193]:


    print("Scraping des temps de trajet en voiture (heure de pointe) dans l'Essonne :")
    tps_essonne_voiture_heure_de_pointe=[]
    temp2_list=[]
    k=-1
    for i in tqdm(essonne):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=essonne_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="driving",
                                                traffic_model='pessimistic',
                                                 departure_time=datetime(2020, 1, 13, 8, 0, 19, 831260))

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_essonne_voiture_heure_de_pointe.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_essonne_voiture_heure_de_pointe.append(temp_list)

    print("Création du CSV temps en voiture en heure de pointe pour l'Essonne :")

    with open(emplacement_donnees_non_traitees+'/tps_essonne_voiture_heure_de_pointe'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_temps_voiture+'/essonne_heure_de_pointe'+today1+'.csv', "w") as f:
        for x in tps_essonne_voiture_heure_de_pointe:

            try:
                duree = x[1][0]['legs'][0]['duration_in_traffic']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en voiture en heure de pointe pour l'Essonne créé")

    print("Création du CSV des distances en heure de pointe pour l'Essonne :")

    with open(emplacement_csv_distance+'/essonne_heure_de_pointe'+today1+'.csv', "w") as f:
        for x in tps_essonne_voiture_heure_de_pointe:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances en heure de pointe pour l'Essonne créé")


    # In[194]:


    print('Suppression des anciens CSV voiture:\n')
    print('    Nettoyage du dossier : '+emplacement_csv_temps_voiture)
    import os
    dossier_affaires= os.listdir(emplacement_csv_temps_voiture)

    for csv in dossier_affaires:
      if csv[-19:-4]!= today1:
        #os.rename(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
        shutil.move(emplacement_csv_temps_voiture+"/"+str(csv), emplacement_ancien_csv_voiture+"/"+str(csv))
        #os.replace(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
    print("    Anciens CSV déplacés vers le dossier : "+emplacement_ancien_csv_voiture)


    # In[195]:


    print("Suppression des anciens CSV des coordonnées géographiques des villes d'IdF:\n")
    print('    Nettoyage du dossier : '+emplacement_coordonnees_geo)
    import os
    import shutil
    dossier_affaires= os.listdir(emplacement_coordonnees_geo)
    for csv in dossier_affaires:
      if csv[-19:-4]!= today1:
        #os.rename(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
        shutil.move(emplacement_coordonnees_geo+"/"+str(csv), emplacement_anciens_csv_coordonnees_geo+"/"+str(csv))
        #os.replace(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
    print("    Anciens CSV déplacés vers le dossier : "+emplacement_anciens_csv_coordonnees_geo)


    # In[215]:


    print('Scraping des temps de trajet en transport en Essonne :')
    tps_essonne_transport=[]
    temp2_list=[]
    k=-1
    for i in tqdm(essonne):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=essonne_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="transit")
                                                 #departure_time=now)

            if len(directions_result) == 0:
                print (i+': Temps de trajet vide. Nouvel essai avec les coordonnées geographiques')
                gmaps = googlemaps.Client(key=clé_api_google)
                now = datetime.now()
                direction=str(coordonnees_villes_essonne[k*3+1])+','+str(coordonnees_villes_essonne[k*3+2])
                directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="transit")


            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_essonne_transport.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_essonne_transport.append(temp_list)

    with open(emplacement_donnees_non_traitees+'/tps_essonne_transport'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))


    with open(emplacement_csv_temps_transport+'/essonne'+today1+'.csv', "w") as f:
        for x in tps_essonne_transport:

            try:
                duree = x[1][0]['legs'][0]['duration']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en transports pour l'Essonne créé")


    # In[222]:


    print('Scraping des temps de trajet en transport dans les Hauts de Seine :')
    tps_hauts_de_seine_transport=[]
    temp2_list=[]
    k=-1
    for i in tqdm(hauts_de_seine):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            destination=hauts_de_seine_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(destination,
                                                 "Place du Châtelet,Paris",
                                                 mode="transit")
                                                 #departure_time=now)

            if len(directions_result) == 0:
                print (i+': Temps de trajet vide. Nouvel essai avec les coordonnées geographiques')
                gmaps = googlemaps.Client(key=clé_api_google)
                now = datetime.now()
                direction=str(coordonnees_villes_hauts_de_seine[k*3+1])+','+str(coordonnees_villes_hauts_de_seine[k*3+2])
                directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="transit")


            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_hauts_de_seine_transport.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_hauts_de_seine_transport.append(temp_list)



    with open(emplacement_donnees_non_traitees+'/tps_hauts_de_seine_transport'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_temps_transport+'/hauts_de_seine'+today1+'.csv', "w") as f:
        for x in tps_hauts_de_seine_transport:

            try:
                duree = x[1][0]['legs'][0]['duration']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en transports pour les Hauts de Seine créé")


    # In[223]:


    print('Scraping des temps de trajet en transport dans la Seine et Marne :')
    tps_seine_et_marne_transport=[]
    temp2_list=[]
    k=-1
    for i in tqdm(seine_et_marne):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=seine_et_marne_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="transit")
                                                 #departure_time=now)

            if len(directions_result) == 0:
                print (i+': Temps de trajet vide. Nouvel essai avec les coordonnées geographiques')
                gmaps = googlemaps.Client(key=clé_api_google)
                now = datetime.now()
                direction=str(coordonnees_villes_seine_et_marne[k*3+1])+','+str(coordonnees_villes_seine_et_marne[k*3+2])
                directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="transit")


            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_seine_et_marne_transport.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_seine_et_marne_transport.append(temp_list)



    with open(emplacement_donnees_non_traitees+'/tps_seine_et_marne_transport'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))


    with open(emplacement_csv_temps_transport+'/seine_et_marne'+today1+'.csv', "w") as f:
        for x in tps_seine_et_marne_transport:

            try:
                duree = x[1][0]['legs'][0]['duration']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en transports pour la Seine et Marne créé")


    # In[224]:


    print('Scraping des temps de trajet en transport dans la Seine-Saint-Denis :')
    tps_seine_saint_denis_transport=[]
    temp2_list=[]
    k=-1
    for i in tqdm(seine_saint_denis):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            destination=seine_saint_denis_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(destination,
                                                 "Place du Châtelet,Paris",
                                                 mode="transit")
                                                 #departure_time=now)

            if len(directions_result) == 0:
                print (i+': Temps de trajet vide. Nouvel essai avec les coordonnées geographiques')
                gmaps = googlemaps.Client(key=clé_api_google)
                now = datetime.now()
                direction=str(coordonnees_villes_seine_saint_denis[k*3+1])+','+str(coordonnees_villes_seine_saint_denis[k*3+2])
                directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="transit")


            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_seine_saint_denis_transport.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_seine_saint_denis_transport.append(temp_list)



    with open(emplacement_donnees_non_traitees+'/tps_seine_saint_denis_transport'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))


    with open(emplacement_csv_temps_transport+'/seine_saint_denis'+today1+'.csv', "w") as f:
        for x in tps_seine_saint_denis_transport:

            try:
                duree = x[1][0]['legs'][0]['duration']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en transports pour la Seine-Saint-Denis créé")


    # In[225]:


    print('Scraping des temps de trajet en transport dans le Val de Marne :')
    tps_val_de_marne_transport=[]
    temp2_list=[]
    k=-1
    for i in tqdm(val_de_marne):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            destination=val_de_marne_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(destination,
                                                 "Place du Châtelet,Paris",
                                                 mode="transit")
                                                 #departure_time=now)

            if len(directions_result) == 0:
                print (i+': Temps de trajet vide. Nouvel essai avec les coordonnées geographiques')
                gmaps = googlemaps.Client(key=clé_api_google)
                now = datetime.now()
                direction=str(coordonnees_villes_val_de_marne[k*3+1])+','+str(coordonnees_villes_val_de_marne[k*3+2])
                directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="transit")


            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_val_de_marne_transport.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_val_de_marne_transport.append(temp_list)



    with open(emplacement_donnees_non_traitees+'/tps_val_de_marne_transport'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))


    with open(emplacement_csv_temps_transport+'/val_de_marne'+today1+'.csv', "w") as f:
        for x in tps_val_de_marne_transport:

            try:
                duree = x[1][0]['legs'][0]['duration']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en transports pour le Val de Marne créé")


    # In[226]:


    print("Scraping des temps de trajet en transport dans le Val d'Oise :")
    tps_val_d_oise_transport=[]
    temp2_list=[]
    k=-1
    for i in tqdm(val_d_oise):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            destination=val_d_oise_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(destination,
                                                 "Place du Châtelet,Paris",
                                                 mode="transit")
                                                 #departure_time=now)

            if len(directions_result) == 0:
                print (i+': Temps de trajet vide. Nouvel essai avec les coordonnées geographiques')
                gmaps = googlemaps.Client(key=clé_api_google)
                now = datetime.now()
                direction=str(coordonnees_villes_val_d_oise[k*3+1])+','+str(coordonnees_villes_val_d_oise[k*3+2])
                directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="transit")


            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_val_d_oise_transport.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_val_d_oise_transport.append(temp_list)



    with open(emplacement_donnees_non_traitees+'/tps_val_d_oise_transport'+today1+'.json', "w") as f:
            for x in temp2_list:
                f.write(str(x))        

    with open(emplacement_csv_temps_transport+'/val_d_oise'+today1+'.csv', "w") as f:
        for x in tps_val_d_oise_transport:

            try:
                duree = x[1][0]['legs'][0]['duration']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en transports pour le Val d'Oise créé")


    # In[227]:


    print("Scraping des temps de trajet en transport dans les Yvelines :")
    tps_yvelines_transport=[]
    temp2_list=[]
    k=-1
    for i in tqdm(yvelines):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            destination=yvelines_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(destination,
                                                 "Place du Châtelet,Paris",
                                                 mode="transit")
                                                 #departure_time=now)

            if len(directions_result) == 0:
                print (i+': Temps de trajet vide. Nouvel essai avec les coordonnées geographiques')
                gmaps = googlemaps.Client(key=clé_api_google)
                now = datetime.now()
                direction=str(coordonnees_villes_yvelines[k*3+1])+','+str(coordonnees_villes_yvelines[k*3+2])
                directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="transit")


            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_yvelines_transport.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)
            temp2_list.append(float('NaN'))
            temp_list=[i,float('NaN')]
            tps_yvelines_transport.append(temp_list)



    with open(emplacement_donnees_non_traitees+'/tps_yvelines_transport'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_temps_transport+'/yvelines'+today1+'.csv', "w") as f:
        for x in tps_yvelines_transport:

            try:
                duree = x[1][0]['legs'][0]['duration']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en transports pour les Yvelines créé")


    # In[230]:


    print('Suppression des anciens CSV transport:\n')
    print('    Nettoyage du dossier : '+emplacement_csv_temps_transport)
    import os
    dossier_affaires= os.listdir(emplacement_csv_temps_transport)

    for csv in dossier_affaires:
      if csv[-19:-4]!= today1:
        #os.rename(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
        shutil.move(emplacement_csv_temps_transport+"/"+str(csv), emplacement_ancien_csv_transport+"/"+str(csv))
        #os.replace(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
    print("    Anciens CSV déplacés vers le dossier : "+emplacement_ancien_csv_transport)


    # In[ ]:





    # In[229]:


    print("Scraping des temps de trajet en vélo dans l'Essonne :")
    tps_essonne_velo=[]
    temp2_list=[]
    k=-1
    for i in tqdm(essonne):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=essonne_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="bicycling")
                                                 #departure_time=now)

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_essonne_velo.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)

    print("Création du CSV temps en vélo pour l'Essonne :")

    with open(emplacement_donnees_non_traitees+'/tps_essonne_velo'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_temps_velo+'/essonne'+today1+'.csv', "w") as f:
        for x in tps_essonne_velo:

            try:
                duree = x[1][0]['legs'][0]['duration']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en vélo pour l'Essonne créé")

    print("Création du CSV des distances en vélo pour l'Essonne :")

    with open(emplacement_csv_distance+'/essonne_velo'+today1+'.csv', "w") as f:
        for x in tps_essonne_velo:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances en vélo pour l'Essonne créé")


    # In[ ]:


    print("Scraping des temps de trajet en vélo dans les Hauts de Seine :")
    tps_hauts_de_seine_velo=[]
    temp2_list=[]
    k=-1
    for i in tqdm(hauts_de_seine):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=hauts_de_seine_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="bicycling")
                                                 #departure_time=now)

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_hauts_de_seine_velo.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)

    print("Création du CSV temps en vélo pour les Hauts de Seine :")

    with open(emplacement_donnees_non_traitees+'/tps_hauts_de_seine_velo'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_temps_velo+'/hauts_de_seine'+today1+'.csv', "w") as f:
        for x in tps_hauts_de_seine_velo:

            try:
                duree = x[1][0]['legs'][0]['duration']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en vélo pour les Hauts de Seine créé")

    print("Création du CSV des distances en vélo pour les Hauts de Seine :")

    with open(emplacement_csv_distance+'/hauts_de_seine_velo'+today1+'.csv', "w") as f:
        for x in tps_hauts_de_seine_velo:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances en vélo pour les Hauts de Seine créé")


    # In[ ]:


    print("Scraping des temps de trajet en vélo dans la Seine et Marne :")
    tps_seine_et_marne_velo=[]
    temp2_list=[]
    k=-1
    for i in tqdm(seine_et_marne):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=seine_et_marne_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="bicycling")
                                                 #departure_time=now)

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_seine_et_marne_velo.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)

    print("Création du CSV temps en vélo pour la Seine et Marne :")

    with open(emplacement_donnees_non_traitees+'/tps_seine_et_marne_velo'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))


    with open(emplacement_csv_temps_velo+'/seine_et_marne'+today1+'.csv', "w") as f:
        for x in tps_seine_et_marne_velo:

            try:
                duree = x[1][0]['legs'][0]['duration']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en vélo pour la Seine et Marne créé")

    print("Création du CSV des distances en vélo pour la Seine et Marne :")

    with open(emplacement_csv_distance+'/seine_et_marne_velo'+today1+'.csv', "w") as f:
        for x in tps_seine_et_marne_velo:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances en vélo pour la Seine et Marne créé")


    # In[ ]:


    print("Scraping des temps de trajet en vélo dans la Seine-saint-Denis :")
    tps_seine_saint_denis_velo=[]
    temp2_list=[]
    k=-1
    for i in tqdm(seine_saint_denis):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=seine_saint_denis_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="bicycling")
                                                 #departure_time=now)

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_seine_saint_denis_velo.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)

    print("Création du CSV temps en vélo pour la Seine-saint-Denis :")

    with open(emplacement_donnees_non_traitees+'/tps_seine_saint_denis_velo'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_temps_velo+'/seine_saint_denis'+today1+'.csv', "w") as f:
        for x in tps_seine_saint_denis_velo:

            try:
                duree = x[1][0]['legs'][0]['duration']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en vélo pour la Seine-saint-Denis créé")

    print("Création du CSV des distances en vélo pour la Seine-saint-Denis :")

    with open(emplacement_csv_distance+'/seine_saint_denis_velo'+today1+'.csv', "w") as f:
        for x in tps_seine_saint_denis_velo:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances en vélo pour la Seine-saint-Denis créé")


    # In[ ]:


    print("Scraping des temps de trajet en vélo dans le Val de Marne :")
    tps_val_de_marne_velo=[]
    temp2_list=[]
    k=-1
    for i in tqdm(val_de_marne):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=val_de_marne_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="bicycling")
                                                 #departure_time=now)

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_val_de_marne_velo.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)

    print("Création du CSV temps en vélo pour le Val de Marne :")

    with open(emplacement_donnees_non_traitees+'/tps_val_de_marne_velo'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_temps_velo+'/val_de_marne'+today1+'.csv', "w") as f:
        for x in tps_val_de_marne_velo:

            try:
                duree = x[1][0]['legs'][0]['duration']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en vélo pour le Val de Marne créé")

    print("Création du CSV des distances en vélo pour le Val de Marne :")

    with open(emplacement_csv_distance+'/val_de_marne_velo'+today1+'.csv', "w") as f:
        for x in tps_val_de_marne_velo:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances en vélo pour le Val de Marne créé")


    # In[ ]:


    print("Scraping des temps de trajet en vélo dans le Val d'Oise :")
    tps_val_d_oise_velo=[]
    temp2_list=[]
    k=-1
    for i in tqdm(val_d_oise):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=val_d_oise_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="bicycling")
                                                 #departure_time=now)

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_val_d_oise_velo.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)

    print("Création du CSV temps en vélo pour le Val d'Oise :")

    with open(emplacement_donnees_non_traitees+'/tps_val_d_oise_velo'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_temps_velo+'/val_d_oise'+today1+'.csv', "w") as f:
        for x in tps_val_d_oise_velo:

            try:
                duree = x[1][0]['legs'][0]['duration']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en vélo pour le Val d'Oise créé")

    print("Création du CSV des distances en vélo pour le Val d'Oise :")

    with open(emplacement_csv_distance+'/val_d_oise_velo'+today1+'.csv', "w") as f:
        for x in tps_val_d_oise_velo:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances en vélo pour le Val d'Oise créé")


    # In[ ]:


    print("Scraping des temps de trajet en vélo dans les Yvelines :")
    tps_yvelines_velo=[]
    temp2_list=[]
    k=-1
    for i in tqdm(yvelines):
        k=k+1
        try:
            gmaps = googlemaps.Client(key=clé_api_google)
            now = datetime.now()
            direction=yvelines_code_postal[k]+' '+str(i)+' france'
            directions_result = gmaps.directions(direction,
                                                 "Place du Châtelet,Paris",
                                                 mode="bicycling")
                                                 #departure_time=now)

            temp2_list.append(directions_result)

            temp_list=[i,directions_result]
            tps_yvelines_velo.append(temp_list)
        except googlemaps.exceptions.ApiError as err :
            print(str(err) +' pour la ville : ' +i)

    print("Création du CSV temps en vélo pour les Yvelines :")

    with open(emplacement_donnees_non_traitees+'/tps_yvelines_velo'+today1+'.json', "w") as f:
        for x in temp2_list:
            f.write(str(x))

    with open(emplacement_csv_temps_velo+'/yvelines'+today1+'.csv', "w") as f:
        for x in tps_yvelines_velo:

            try:
                duree = x[1][0]['legs'][0]['duration']['text']
            except:
                duree=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(duree)+'\n')
    print("    CSV temps en vélo pour les Yvelines créé")

    print("Création du CSV des distances en vélo pour les Yvelines :")

    with open(emplacement_csv_distance+'/yvelines_velo'+today1+'.csv', "w") as f:
        for x in tps_yvelines_velo:

            try:
                distance = x[1][0]['legs'][0]['distance']['text']
            except:
                distance=float('NaN')
            ville = x[0]
            f.write(ville + ','+str(distance)+'\n')
    print("    CSV des distances en vélo pour les Yvelines créé")


    # In[232]:


    print('Suppression des anciens CSV voiture:\n')
    print('    Nettoyage du dossier : '+emplacement_csv_temps_velo)
    import os
    dossier_affaires= os.listdir(emplacement_csv_temps_velo)

    for csv in dossier_affaires:
      if csv[-19:-4]!= today1:
        #os.rename(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
        shutil.move(emplacement_csv_temps_velo+"/"+str(csv), emplacement_ancien_csv_velo+"/"+str(csv))
        #os.replace(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
    print("    Anciens CSV déplacés vers le dossier : "+emplacement_ancien_csv_velo)


    # In[233]:


    print('Suppression des anciens CSV distance:\n')
    print('    Nettoyage du dossier : '+emplacement_csv_distance)
    import os
    dossier_affaires= os.listdir(emplacement_csv_distance)

    for csv in dossier_affaires:
      if csv[-19:-4]!= today1:
        #os.rename(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
        shutil.move(emplacement_csv_distance+"/"+str(csv), emplacement_ancien_csv_distance+"/"+str(csv))
        #os.replace(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
    print("    Anciens CSV déplacés vers le dossier : "+emplacement_ancien_csv_distance)


    # In[234]:


    print('Suppression des anciens CSV données non traitées:\n')
    print('    Nettoyage du dossier : '+emplacement_donnees_non_traitees)
    import os
    dossier_affaires= os.listdir(emplacement_donnees_non_traitees)

    for csv in dossier_affaires:
      if csv[-20:-5]!= today1:
        #os.rename(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
        shutil.move(emplacement_donnees_non_traitees+"/"+str(csv), emplacement_anciens_donnees_non_traitees+"/"+str(csv))
        #os.replace(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
    print("    Anciens CSV déplacés vers le dossier : "+emplacement_anciens_donnees_non_traitees)


    # In[235]:


    today3 = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%H:%M:%S , LE %d/%m/%Y"))
    print('PROGRAMME TERMINE A : '+today3)


    # In[236]:


    def days_between(d1, d2):
        d1 = datetime.strptime(d1, "%H:%M:%S , LE %d/%m/%Y")
        d2 = datetime.strptime(d2, "%H:%M:%S , LE %d/%m/%Y")
        return abs((d2 - d1))


    # In[237]:


    x=days_between(today3,today)


    # In[238]:


    minutes = x.seconds / 60
    print("\nTemps d'éxécution du programme : ", int(minutes),"minutes") 


    # In[249]:


    destinataire=['pzimsimplon@protonmail.com','pzim@pzim.fr','pizim@posteo.net']
    password=w
    adresse_envoi='gmurtinlove@gmail.com'
    smtp='smtp.gmail.com'
    port=587
    login=adresse_envoi

    def send_mail(message):
        pw=password
        pw
        adresse=adresse_envoi
        adresse
        login
        #destinataire=destinataire
        destinataire
        sujet="Les temps de parcours ont été correctement scrappé l'execution du programme est terminée !"
        sujet
        message=str(message)
        message
        msg = MIMEMultipart()
        msg['From'] = adresse
        msg['To'] = ",".join(destinataire)
        msg['Subject'] = sujet 
        message = message
        msg.attach(MIMEText(message))
        mailserver = smtplib.SMTP(smtp, port)
        mailserver.ehlo()
        mailserver.starttls() #activer si besoin
        #mailserver.ehlo() #activer si besoins

        mailserver.login(login, pw)
        mailserver.sendmail(adresse,destinataire, msg.as_string())
        print(" Message envoyé !")
        mailserver.quit()


    # In[250]:


    print("Envoi du mail de confirmation de la bonne exécution du programme :\n")


    # In[251]:


    send_mail("Le programme de scraping des temps de trajet en IdF a correctment été exécuté.\nTemps d'execution du programme : "+str(int(minutes))+" minutes.\nProgramme terminé à "+today3)


    # In[ ]:




    
    

    
except Exception as e:
    
    print("Erreur lors de l'execution du programme !\n")
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    
    destinataire=['pzimsimplon@protonmail.com','pzim@pzim.fr','pizim@posteo.net']
    password=w
    adresse_envoi='gmurtinlove@gmail.com'
    smtp='smtp.gmail.com'
    port=587
    login=adresse_envoi
    

    def send_mail(message):
        pw=password
        pw
        adresse=adresse_envoi
        adresse
        login
        #destinataire=destinataire
        destinataire
        sujet="Il y a une erreur lors du scrapping des temps de parcours!"
        sujet
        message=str(message)
        message
        msg = MIMEMultipart()
        msg['From'] = adresse
        msg['To'] = ",".join(destinataire)
        msg['Subject'] = sujet 
        message = message
        msg.attach(MIMEText(message))
        mailserver = smtplib.SMTP(smtp, port)
        mailserver.ehlo()
        mailserver.starttls() #activer si besoin
        mailserver.ehlo() #activer si besoins
        
        mailserver.login(login, pw)
        mailserver.sendmail(adresse,destinataire, msg.as_string())
        print("Message d'erreur envoyé !")
        mailserver.quit()

    send_mail("Erreur lors du scraping des temps de parcours. Veuillez vérifier le programme\nVoici l'erreur :\n"+str(e))




# In[ ]:




