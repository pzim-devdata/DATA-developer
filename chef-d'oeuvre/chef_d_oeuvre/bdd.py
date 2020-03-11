#!/usr/bin/env python
# coding: utf-8

# In[7]:


import getpass
w=getpass.getpass("Veuiller entrer le mot de passe SMTP :")
w
destinataire=['pzimsimplon@protonmail.com','pzim@pzim.fr','pizim@posteo.net']
password=w
adresse_envoi='gmurtinlove@gmail.com'
smtp='smtp.gmail.com'
port=587
login=adresse_envoi

try:
    #!pip install pymysql

    import pymysql
    import os
    from datetime import datetime
    import pytz

    #import sys
    import pymongo
    from pymongo import MongoClient
    import json as JSON
    import pandas as pd

    from tqdm import tqdm
    import warnings
    warnings.filterwarnings("ignore")
    
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import lxml
    import smtplib
    
    import time
    import pipes


    # In[2]:


    host='localhost'
    user='simplon'
    password2='@Simplon92'

    emplacement_csv_villes='CSV/csv_villes'
    emplacement_csv_temps_transport='CSV/temps/temps_transports'
    emplacement_csv_temps_velo='CSV/temps/temps_velo'
    emplacement_csv_temps_voiture='CSV/temps/temps_voiture'
    emplacement_csv_distance='CSV/distance'
    emplacement_donnees_non_traitees='CSV/donnees_non_traitees'
    emplacement_coordonnees_geo='CSV/coordonnees_geo_ville'
    emplacement_donnees_non_traitees='CSV/donnees_non_traitees'


    # LOAD DATA INFILE 'c:/tmp/discounts.csv' 
    # INTO TABLE discounts 
    # FIELDS TERMINATED BY ',' 
    # ENCLOSED BY '"'
    # LINES TERMINATED BY '\n'
    # IGNORE 1 ROWS;

    # In[3]:
    today = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%H:%M:%S , LE %d/%m/%Y"))
    print('PROGRAMME DEMARRE A : '+today)

    print("I. Exportation des CSVs vers une base de donnée mySQL :")


    # In[4]:


    con = pymysql.connect(host=host,
                                    user=user,
                                    password=password2,
                                    autocommit=True,
                                    charset='utf8',
                                    local_infile=1)
    print('Connected to DB: {}'.format(host))

    cursor = con.cursor()


    # In[5]:


    #load_sql = "SHOW VARIABLES LIKE 'local_infile';"
    #cursor.execute(load_sql)


    # In[6]:


    print('Attribution des droits pour MySQL pour charger les CSVs')
    
    
    load_sql = "SET GLOBAL local_infile = 1;"
    cursor.execute(load_sql)


    # In[7]:


    load_sql = "DROP DATABASE IF EXISTS IDF";
    cursor.execute(load_sql)


    # In[8]:


    print("Création de la base de données IDF")
    load_sql = "CREATE DATABASE IDF CHARACTER SET utf8;"
    cursor.execute(load_sql)


    # In[9]:


    load_sql = "USE IDF;"
    cursor.execute(load_sql)


    # In[10]:


    print("Création de la table 'Coordonnees_geo'")
    load_sql = """create table Coordonnees_geo (Ville varchar(45) primary key, Latitude varchar(30), Longitude varchar(30)) ENGINE=InnoDB """;
    cursor.execute(load_sql)


    # In[11]:


    print("Intégration des données dans la table")
    for csv in os.listdir(emplacement_coordonnees_geo):
        phrase=str(emplacement_coordonnees_geo)+"/"+str(csv)

        load_sql = "LOAD DATA LOCAL INFILE '"+str(phrase)+"' INTO TABLE Coordonnees_geo FIELDS TERMINATED BY ',' ";
        cursor.execute(load_sql)    


    # In[12]:


    print("Création de la table 'Villes'")


    # In[13]:


    load_sql = """create table Villes ( Ville varchar(45) primary key, Code_postal varchar(45),foreign key (Ville) references Coordonnees_geo(Ville) on delete cascade)ENGINE=InnoDB""";
    cursor.execute(load_sql)


    # In[14]:


    print("Intégration des données dans la table")

    for csv in os.listdir(emplacement_csv_villes):
        phrase=str(emplacement_csv_villes)+'/'+str(csv)
        load_sql = "LOAD DATA LOCAL INFILE '"+str(phrase)+"' INTO TABLE Villes FIELDS TERMINATED BY ',' IGNORE 1 ROWS";
        cursor.execute(load_sql)


    # In[15]:


    print("Création de la table 'Distance_voiture'")


    # In[16]:


    load_sql = """create table Distance_voiture ( Ville varchar(45) primary key, Distance varchar(45),foreign key (Ville) references Coordonnees_geo(Ville) on delete cascade)ENGINE=InnoDB""";
    cursor.execute(load_sql)


    # In[17]:


    print("Intégration des données dans la table")

    liste_distance=[]
    for csv in os.listdir(emplacement_csv_distance):
        liste_distance.append(str(csv))
    liste_distance.sort()


    # In[18]:


    for csv in range(0,len(liste_distance),3):  
        phrase=str(emplacement_csv_distance)+'/'+liste_distance[csv]
        load_sql = "LOAD DATA LOCAL INFILE '"+str(phrase)+"' INTO TABLE Distance_voiture FIELDS TERMINATED BY ',' IGNORE 1 ROWS(Ville,Distance)";
        cursor.execute(load_sql)


    # In[19]:


    print("Création de la table 'Distance_voiture_pointe'")


    # In[20]:


    load_sql = """create table Distance_voiture_pointe ( Ville varchar(45) primary key, Distance varchar(45),foreign key (Ville) references Coordonnees_geo(Ville) on delete cascade)ENGINE=InnoDB""";
    cursor.execute(load_sql)


    # In[21]:


    print("Intégration des données dans la table")

    for csv in range(1,len(liste_distance),3):  
        phrase=str(emplacement_csv_distance)+'/'+liste_distance[csv]
        load_sql = "LOAD DATA LOCAL INFILE '"+str(phrase)+"' INTO TABLE Distance_voiture_pointe FIELDS TERMINATED BY ',' IGNORE 1 ROWS(Ville,Distance)";
        cursor.execute(load_sql)


    # In[22]:


    print("Création de la table 'Distance_velo'")


    # In[23]:


    load_sql = """create table Distance_velo ( Ville varchar(45) primary key, Distance varchar(45),foreign key (Ville) references Coordonnees_geo(Ville) on delete cascade)ENGINE=InnoDB""";
    cursor.execute(load_sql)


    # In[24]:


    print("Intégration des données dans la table")

    for csv in range(2,len(liste_distance),3):  
        phrase=str(emplacement_csv_distance)+'/'+liste_distance[csv]
        load_sql = "LOAD DATA LOCAL INFILE '"+str(phrase)+"' INTO TABLE Distance_velo FIELDS TERMINATED BY ',' IGNORE 1 ROWS(Ville,Distance)";
        cursor.execute(load_sql)


    # In[25]:


    print("Création de la table 'Temps_transport'")


    # In[26]:


    load_sql = """create table Temps_transport ( Ville varchar(45) primary key, Temps varchar(45),foreign key (Ville) references Coordonnees_geo(Ville) on delete cascade)ENGINE=InnoDB""";
    cursor.execute(load_sql)


    # In[27]:


    print("Intégration des données dans la table")

    for csv in os.listdir(emplacement_csv_temps_transport):  
        phrase=str(emplacement_csv_temps_transport)+'/'+csv
        load_sql = "LOAD DATA LOCAL INFILE '"+str(phrase)+"' INTO TABLE Temps_transport FIELDS TERMINATED BY ',' IGNORE 1 ROWS";
        cursor.execute(load_sql)


    # In[28]:


    print("Création de la table 'Temps_velo'")


    # In[29]:


    load_sql = """create table Temps_velo ( Ville varchar(45) primary key, Temps varchar(45),foreign key (Ville) references Coordonnees_geo(Ville) on delete cascade)ENGINE=InnoDB""";
    cursor.execute(load_sql)


    # In[30]:


    print("Intégration des données dans la table")

    for csv in os.listdir(emplacement_csv_temps_velo):  
        phrase=str(emplacement_csv_temps_velo)+'/'+csv
        load_sql = "LOAD DATA LOCAL INFILE '"+str(phrase)+"' INTO TABLE Temps_velo FIELDS TERMINATED BY ',' IGNORE 1 ROWS";
        cursor.execute(load_sql)


    # In[31]:


    print("Création de la table 'Temps_voiture'")


    # In[32]:


    load_sql = """create table Temps_voiture ( Ville varchar(45) primary key, Temps varchar(45), foreign key (Ville) references Coordonnees_geo(Ville) on delete cascade)ENGINE=InnoDB""";
    cursor.execute(load_sql)


    # In[33]:


    print("Intégration des données dans la table")


    liste_voiture=[]
    for csv in os.listdir(emplacement_csv_temps_voiture):
        liste_voiture.append(csv)
    liste_voiture.sort()


    # In[34]:


    for csv in range(0,len(liste_voiture),2):
        phrase=str(emplacement_csv_temps_voiture)+'/'+str(liste_voiture[csv])
        load_sql = "LOAD DATA LOCAL INFILE '"+str(phrase)+"' INTO TABLE Temps_voiture FIELDS TERMINATED BY ',' IGNORE 1 ROWS";
        cursor.execute(load_sql)


    # In[35]:


    print("Création de la table 'Temps_voiture_pointe'")


    # In[36]:


    load_sql = """create table Temps_voiture_pointe ( Ville varchar(45) primary key, Temps varchar(45),foreign key (Ville) references Coordonnees_geo(Ville) on delete cascade)ENGINE=InnoDB""";
    cursor.execute(load_sql)


    # In[37]:


    print("Intégration des données dans la table")


    for csv in range(1,len(liste_voiture),2):  
        phrase=str(emplacement_csv_temps_voiture)+'/'+str(liste_voiture[csv])
        load_sql = "LOAD DATA LOCAL INFILE '"+str(phrase)+"' INTO TABLE Temps_voiture_pointe FIELDS TERMINATED BY ',' IGNORE 1 ROWS";
        cursor.execute(load_sql)


    # In[38]:


    print("Toutes les données ont été intégrées dans la base de donnée MySQL 'IDF' !")


    # In[56]:


    input("Appuyer sur Enter")


    # In[ ]:

    print("Creation d'une backup dans le fichier Dump :")
    
    DB_HOST = 'localhost' 
    DB_USER = 'simplon'
    DB_USER_PASSWORD = '@Simplon92'
    #DB_NAME = '/backup/dbnameslist.txt'
    DB_NAME = 'IDF'
    BACKUP_PATH = 'BDD/MySQL/Dump'
    
    DATETIME = time.strftime('%Y%m%d-%H%M%S')
    TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME

    try:
        os.stat(TODAYBACKUPPATH)
    except:
        os.mkdir(TODAYBACKUPPATH)
        
    db = DB_NAME
    dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
    os.system(dumpcmd)
    gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
    os.system(gzipcmd)

    print ("")
    print ("Base de données sauvegardée !")
    print ("La sauvegarde a été créée dans le dossier : '" + TODAYBACKUPPATH)
    
    input("Appuyer sur Enter")

    # In[39]:


    print('\nII. Importation des données non traitées dans MongoDb :\n\n')


    # In[40]:


    client = MongoClient('localhost', 27017)
    print("Connecté à MongoDb !\n")


    # In[57]:


    db = client.IdF
    print("La BDD '"+str(db.name)+"' a été créée !\n")


    # In[58]:


    collection = db.Données_non_traitees
    print("La collection '"+str(collection.name)+"' a été créée !\n")


    # In[43]:

    print("Suppression des anciennes bases de données\n")
    collection.remove()


    # In[44]:


    collection.estimated_document_count()


    # In[45]:


    for json in tqdm(os.listdir(emplacement_donnees_non_traitees)):
        if os.path.getsize(emplacement_donnees_non_traitees+'/'+str(json)) <= 999999:
            #print(json)
            data = pd.read_csv(emplacement_donnees_non_traitees+'/'+str(json))

            payload = JSON.loads(data.to_json(orient='split'))
            collection.insert_one(payload)
            print("Le document Json : "+str(json)+" a été intégré \ndans la base de données MongoDb '"+str(db.name)+"' dans la collection '"+str(collection.name)+"'\n")


    # In[46]:


    print("\n\nDescription de la DB : taille de la DB, combien de collections, de documents :")


    # In[59]:


    print("\n- "+str(collection.estimated_document_count())+" documents ont été intégrés dans la base de données MongoDb '"+str(db.name)+"'\ndans la collection '"+str(collection.name)+"'")


    # In[61]:


    #print("\n- Affichage des stats de la BDD '"+str(db.name)+"' :\n")
    #print(db.command("dbstats"))


    # In[49]:


    #print("\n- Affichage des infos complètes de la collection "+str(collection.name)+" :")
    #input("Appuyer sur Enter")
    #print(db.command("collstats", collection.name))


    # In[55]:


    #print("\n- Affichage d'un document type :\n", collection.find_one())
    #input("Appuyer sur Enter")


    # In[63]:
    today3 = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%H:%M:%S , LE %d/%m/%Y"))
    print('PROGRAMME TERMINE A : '+today3)


    # In[302]:


    def days_between(d1, d2):
        d1 = datetime.strptime(d1, "%H:%M:%S , LE %d/%m/%Y")
        d2 = datetime.strptime(d2, "%H:%M:%S , LE %d/%m/%Y")
        return abs((d2 - d1))


    # In[304]:


    x=days_between(today3,today)


    # In[313]:

    secondes=x.seconds
    minutes = x.seconds / 60
    print("\nTemps d'éxécution du programme : ", int(secondes),"secondes")
    

    print("\nLes données non traitées ont été intégrées à MongoDb !\nFin du programme !")
    
    print("\nEnvoi du mail de confirmation de la bonne exéctution du programme :\n")
    
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
        sujet="Les BDD ont été correctement créées, l'exécution du programme est terminée !"
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
        print(" Message envoyé !")
        mailserver.quit()
    
    print("\nEnvoi du mail de confirmation de fin d'exécution du programme :")
    send_mail("Les BDD ont été correctement créées, l'exécution du programme est terminée.\nTemps d'execution du programme : "+str(int(secondes))+" secondes.\nProgramme terminé à "+today3)
    


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
        sujet="Il y a une erreur lors de l'insertion des données dans les BDD !"
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

    send_mail("Erreur lors de l'insertion des données dans les BDD. Veuillez vérifier le programme !\nVoici l'erreur :\n"+str(e))





# In[ ]:




