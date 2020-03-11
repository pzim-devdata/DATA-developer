#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


#!pip install bs4 requests
#!pip install pytz


# # Analyse de la page : https://pca-cpa.org :
# ##- Nouvelle affaire
# ##- Metadata changée dans la page de la liste des affaires
# ##- Nouveau document ajouté
# 
# Veuillez renseigner les variables ci-dessous :
destinataire=''
password=''
adresse_envoi=''
smtp='smtp.'
port=587
login=adresse_envoi




try:
    

    import os
    import csv
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    from datetime import datetime
    import pytz
    import re
    import time
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import lxml
    import smtplib
    from tqdm import tqdm
    import shutil

    emplacement_ancien_csv_sommaire='old_csv/old_summary_csv'
    emplacement_ancien_csv_affaires='old_csv/old_cases_csv'
    emplacement_ancien_csv_documents='old_csv/old_doc_csv'

    emplacement_fichier='summary'
    emplacement_fichier_affaires='cases'
    emplacement_fichier_documents='documents'
    

    # In[ ]:



    # In[ ]:


    today = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%H:%M:%S , LE %d/%m/%Y"))
    print('PROGRAMME DEMARRE A : '+today)


    # #Modification du sommaire de la page : 
    # ##https://pca-cpa.org/en/cases/

    # In[ ]:


    print("\nScraping du sommaire de la page https://pca-cpa.org/en/cases/")


    # In[ ]:


    requete = requests.get("https://pca-cpa.org/en/cases/")
    page = requete.content
    soup = BeautifulSoup(page, features="lxml")


    # In[ ]:


    liste=[]
    for a in soup.find_all('a'):
      liste.append(str(a))


    # In[ ]:


    listenettoyee=[]
    def adresse_liste(x):
      chaine = str(x)
      if re.findall('<a href="[0-9]', chaine):
        listenettoyee.append(str(x))


    # In[ ]:


    for i in range(0,len(liste)):
      adresse_liste(liste[i])
      i=i+1


    # In[ ]:


    today1 = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%Y%m%d_%H%M%S"))


    # In[ ]:


    df = pd.DataFrame(listenettoyee)
    df.to_csv(emplacement_fichier+'/liste'+today1+'.csv', index=False)


    # In[ ]:


    print("\nPatienter 30 secondes")
    for i in tqdm(range(100)):
        time.sleep(0.30)


    # In[ ]:


    dossier= os.listdir(emplacement_fichier)
    listetecsv=[]
    for csv in dossier:
      listetecsv.append(csv)


    # In[ ]:


    listetecsv.sort()


    # Attention : Il est necessaire d'avoir au moins deux CSV dans le dossier. Relancer le programme si besoin.

    # In[ ]:


    print("\nVérification s'il y a des modifications dans le sommaire de la page https://pca-cpa.org/en/cases/")


    # In[ ]:


    try:
        avant_dernier_CSV=pd.read_csv(emplacement_fichier+'/'+listetecsv[-2], error_bad_lines=False)
        dernier_CSV=pd.read_csv(emplacement_fichier+'/'+listetecsv[-1])
    except :
        print("\n\n\nAttention : Il faut au moins deux CSV. Relancer le programme.\n\n\n")


    # In[ ]:


    def adresse_modification(x):
      chaine2 = str(x)
      pos3 = chaine2.find('] ')
      pos4 = chaine2.find('</a>"')
      #extraction sans le 'href'
      pos3=pos3+len('] ')
      pos4=pos4-len('</a')
      sousChaine2 = chaine2[pos3:pos4]
      #print (sousChaine)
      messageaffaire=str(sousChaine2)


      chaine = str(x)
      pos1 = chaine.find('<a href="')
      pos2 = chaine.find('/">')
      #extraction sans le 'href'
      pos1=pos1+len('<a href="')
      sousChaine = chaine[pos1:pos2]
      #print (sousChaine)
      message="* Voici l'affaire modifiée, supprimée ou ajoutée, dans le sommaire de la page https://pca-cpa.org/en/cases/ : \n\nNom de l'affaire : "+str(sousChaine2)+"\nAdresse de l'affaire : \nhttps://pca-cpa.org/en/cases/"+str(sousChaine)
      return(message)


    # In[ ]:


    def Diff(li1, li2): 
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
        return li_dif 


    # In[ ]:


    today = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%d/%m/%Y à %H:%M:%S"))
    message1=[]
    if avant_dernier_CSV.equals(dernier_CSV)==False:
      print ('Modifications apportées au sommaire')
      avant_dernier_CSVliste=avant_dernier_CSV.values.tolist()
      dernier_CSVliste=dernier_CSV.values.tolist()
      modificationsliste=Diff(dernier_CSVliste,avant_dernier_CSVliste)
      modificationsliste=['\n'.join(sub_list) for sub_list in modificationsliste]


      for i in range(0,int(len(modificationsliste))):
        message1.append(adresse_modification(modificationsliste[i])+' \nNofication créée le '+today)
        message1=list(set(message1))
       #print(message1)
      #sauvegarde message
        i=i+1
      #message1.append(str(liste_mail)+' Nofication crée le '+today)
        print('\nModifications sauvegardées dans la liste message1')
    else :
      print('Pas de modification du sommaire, pas de notifiaction créée')
      message1=[]


    # In[ ]:


    #modificationsliste


    # In[ ]:


    #message1


    # #Modification des métadonnées des affaires
    # 

    # In[ ]:


    print("\nScraping des métadonnées pour chaque affaire")


    # In[ ]:


    def adresse_affaires(x):
      chaine = str(x)
      pos1 = chaine.find('<a href="')
      pos2 = chaine.find('/">')
      #extraction sans le 'href'
      pos1=pos1+len('<a href="')
      sousChaine = chaine[pos1:pos2]
      #print (sousChaine)
      adresse_mail='https://pca-cpa.org/en/cases/'+str(sousChaine)
      return(adresse_mail)



    # In[ ]:


    liste_des_adresses_des_affaires=[]
    for cases in listenettoyee:
      liste_des_adresses_des_affaires.append(adresse_affaires(cases))



    # In[ ]:


    #liste_des_adresses_des_affaires[1]


    # In[ ]:


    today2 = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%Y%m%d_%H%M%S"))
    for cases in tqdm(liste_des_adresses_des_affaires):
      requete_affaires = requests.get(cases)
      page_affaires = requete_affaires.content
      soup_affaires = BeautifulSoup(page_affaires, features="lxml")
      globals()['liste_affaire'+cases[29:]+"_"+today2]=[]
      for a in soup_affaires.find_all('tr'):
        globals()['liste_affaire'+cases[29:]+"_"+today2].append(str(a))
        df = pd.DataFrame(globals()['liste_affaire'+cases[29:]+"_"+today2])
        df.to_csv(emplacement_fichier_affaires+'/Affaire'+cases[29:]+"_"+today2+'.csv', index=False)


    # In[ ]:


    print("Patienter 30 secondes")
    for i in tqdm(range(100)):
        time.sleep(0.30)



    # In[ ]:


    print("\nVérification s'il y a des modifications dans les métadonnées des affaires")


    # In[ ]:


    import os
    dossier_affaires= os.listdir(emplacement_fichier_affaires)
    listetecsvaffaires=[]
    for csv in dossier_affaires:
      listetecsvaffaires.append(csv)


    # In[ ]:


    listetecsvaffaires.sort()


    # In[ ]:


    #listetecsvaffaires


    # In[ ]:


    def listecsv_affaires_debut(x):
      chaine = str(x)
      pos1 = chaine.find('Affaire')
      pos2 = chaine.find('_')
      sousChaine = chaine[pos1:pos2]
      #print (sousChaine)
      return(sousChaine)


    # In[ ]:


    #listetecsvaffaires[listetecsvaffaires.index('Affaire100_20190918_134444.csv')]


    # In[ ]:


    #listecsv_affaires_debut(listetecsvaffaires[listetecsvaffaires.index('Affaire100_20190919_091949.csv')])


    # In[ ]:


    liste_affaire_double=[]
    for affaire1 in listetecsvaffaires:
      i=0    
      for affaire2 in listetecsvaffaires:

        if listecsv_affaires_debut(listetecsvaffaires[listetecsvaffaires.index(affaire1)])==listecsv_affaires_debut(listetecsvaffaires[listetecsvaffaires.index(affaire2)]):
          i=i+1
          if i>1:
            liste_affaire_double.append(affaire1)
            liste_affaire_double.append(affaire2)


    # In[ ]:


    liste_affaire_double=list(set(liste_affaire_double))


    # In[ ]:


    liste_affaire_double.sort(reverse=True)


    # In[ ]:


    i=0
    for affaire_en_double in liste_affaire_double:
      i=i+1

      globals()['liste_double'+str(i)]=[]
      for affaire_en_double2 in liste_affaire_double:
        if affaire_en_double[0:11]==affaire_en_double2[0:11]:
          globals()['liste_double'+str(i)].append(affaire_en_double2)


    # In[ ]:


    def Diff(li1, li2): 
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
        return li_dif 


    # In[ ]:


    today = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%d/%m/%Y à %H:%M:%S"))
    k=0
    message2=[]
    for j in tqdm(range(1,(len(liste_affaire_double)+1))):
      dernier_csv=pd.read_csv(emplacement_fichier_affaires+'/'+globals()['liste_double'+str(j)][0])
      avant_dernier_csv=pd.read_csv(emplacement_fichier_affaires+'/'+globals()['liste_double'+str(j)][1])
      avant_dernier_csvliste_affaire=avant_dernier_csv.values.tolist()
      dernier_csvliste_affaire=dernier_csv.values.tolist()
      modificationsliste=Diff(avant_dernier_csvliste_affaire,dernier_csvliste_affaire)

      if avant_dernier_csv.equals(dernier_csv)==False:
          k=k+1      
          chaine=str(globals()['liste_double'+str(j)][0])
          pos1 = len('Affaire')+chaine.find('Affaire')
          pos2 = chaine.find('_')
          print ("\nModifications apportées à l'affaire : "+globals()['liste_double'+str(j)][0][pos1:pos2])

          modificationsliste=['\n'.join(sub_list) for sub_list in modificationsliste]
          ancien =modificationsliste[0:int((len(modificationsliste)/2))]
          nouveau=modificationsliste[int((len(modificationsliste)/2)):]
          liste_mail=[]
          for i in range(0,len(modificationsliste)):
            liste_mail.append(adresse_modification(modificationsliste[i]))
      #sauvegarde message2
            i=i+1
          time.sleep(2) 

          message2.append("* Modifications apportées à l'affaire : "+globals()['liste_double'+str(j)][0][pos1:pos2] +"\n- Lien : https://pca-cpa.org/en/cases/"+globals()['liste_double'+str(j)][0][pos1:pos2]+ " \n\nVoici ce qui a été modifié, ajouté ou supprimé : "+str(nouveau)+' Notification créée le '+today)
          print('\nModifications sauvegardées dans la liste message2')

    if k==0 :
      print(' Pas de modification dans les affaires, pas de notification créée')
      message2=[]



    # In[ ]:


    #message2


    # In[ ]:


    message2=list(set(message2))
    #message2


    # In[ ]:


    if len(message2)>0:
      for i in range(0,len(message2)):
        message2[i]=str(message2[i]).replace("</td>\\n</tr>'] ", '\n')
        message2[i]=message2[i].replace("['<tr>\\n<td>","\n- ")
        message2[i]=message2[i].replace("</td>\\n<td>"," : ")
        message2[i]=message2[i].replace(", '<tr>\\n<td>", '\n- ')
        message2[i]=message2[i].replace("</td>\\n</tr>'", '')
        message2[i]=str(message2[i]).replace("</td>\\n<td>", ' ')
        message2[i]=str(message2[i]).replace("</span></p>\\n<p><span lang=",', ')
        message2[i]=str(message2[i]).replace("\\n<p><span lang=",'- ')
        message2[i]=str(message2[i]).replace(";",' and ')
        message2[i]=str(message2[i]).replace("</span></p>", '')
        message2[i]=str(message2[i]).replace("<p>",'')
        message2[i]=str(message2[i]).replace("</p>\\n",', ' )
        message2[i]=str(message2[i]).replace("</p>",'')
        message2[i]=str(message2[i]).replace("\\n", '')
        message2[i]=str(message2[i]).replace(">",' ')
        message2[i]=str(message2[i]).replace("['<tr>\\n<td>", '- ')
        message2[i]=str(message2[i]).replace("</td>\\n<td>",' : ')
        message2[i]=str(message2[i]).replace("<br/", ' ')
        message2[i]=str(message2[i]).replace("<td>", '- ')
        message2[i]=str(message2[i]).replace("</td>\\n</tr>'] ",' \n')
        #message2[i]=str(message2[i]).replace(
    #message2


    # #Modification des documents des affaires

    # In[ ]:


    print("\nScraping des documents dans les affaires")


    # In[ ]:


    def adresse_documents(x):
      chaine = str(x)
      pos1 = chaine.find('<a href="')
      pos2 = chaine.find('/">')
      #extraction sans le 'href'
      pos1=pos1+len('<a href="')
      sousChaine = chaine[pos1:pos2]
      #print (sousChaine)
      adresse_mail='https://pca-cpa.org/en/cases/'+str(sousChaine)
      return(adresse_mail)


    # In[ ]:


    liste_des_adresses_des_documents=[]
    for cases in listenettoyee:
      liste_des_adresses_des_documents.append(adresse_documents(cases))



    # In[ ]:


    #liste_des_adresses_des_documents[0:5]


    # In[ ]:


    today3 = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%Y%m%d_%H%M%S"))
    for document in tqdm(liste_des_adresses_des_documents):
      requete_documents = requests.get(document)
      page_documents = requete_documents.content
      soup_documents = BeautifulSoup(page_documents, features="lxml")
      globals()['liste_document'+document[29:]+"_"+today3]=[]
      for a in soup_documents.find_all("div", {"class":"download-links"}):
        globals()['liste_document'+document[29:]+"_"+today3].append(str(a))
        i=0
        for i in range(0,len(globals()['liste_document'+document[29:]+"_"+today3])):
          globals()['liste_document'+document[29:]+"_"+today3][i]=globals()['liste_document'+document[29:]+"_"+today3][i].replace(' ','')
        df = pd.DataFrame(globals()['liste_document'+document[29:]+"_"+today3])
        df.to_csv(emplacement_fichier_documents+'/Document'+document[29:]+"_"+today3+'.csv', index=False)


    # In[ ]:


    print("Patienter 30 secondes")
    for i in tqdm(range(100)):
        time.sleep(0.30)


    # In[ ]:


    print("\nVérification s'il y a des modifications dans les documents des affaires")


    # In[ ]:


    import os
    dossier_documents= os.listdir(emplacement_fichier_documents)
    listetecsvdocuments=[]
    for csv in dossier_documents:
      listetecsvdocuments.append(csv)


    # In[ ]:


    listetecsvdocuments.sort()


    # In[ ]:


    #listetecsvdocuments[0:5]


    # In[ ]:


    def listecsv_documents_debut(x):
      chaine = str(x)
      pos1 = chaine.find('Document')
      pos2 = chaine.find('_')
      sousChaine = chaine[pos1:pos2]
      #print (sousChaine)
      return(sousChaine)


    # In[ ]:


    liste_document_double=[]
    for document1 in listetecsvdocuments:
      i=0    
      for document2 in listetecsvdocuments:

        if listecsv_documents_debut(listetecsvdocuments[listetecsvdocuments.index(document1)])==listecsv_documents_debut(listetecsvdocuments[listetecsvdocuments.index(document2)]):
          i=i+1
          if i>1:
            liste_document_double.append(document1)
            liste_document_double.append(document2)


    # In[ ]:


    #liste_document_double[0:5]


    # In[ ]:


    liste_document_double=list(set(liste_document_double))


    # In[ ]:


    #liste_document_double[0:5]


    # In[ ]:


    liste_document_double.sort(reverse=True)


    # In[ ]:


    #liste_document_double[0:13]


    # In[ ]:


    i=0
    for document_en_double in liste_document_double:
      i=i+1

      globals()['liste_double_document'+str(i)]=[]
      for document_en_double2 in liste_document_double:
        if document_en_double[0:12]==document_en_double2[0:12]:
          globals()['liste_double_document'+str(i)].append(document_en_double2)


    # In[ ]:


    #liste_double_document2


    # In[ ]:


    def Diff(li1, li2): 
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
        return li_dif 


    # In[ ]:


    today = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%d/%m/%Y à %H:%M:%S"))
    k=0
    message3=[]
    modificationsliste=[]
    for j in tqdm(range(1,(len(liste_document_double) +1))):
      dernier_csv=pd.read_csv(emplacement_fichier_documents+'/'+globals()['liste_double_document'+str(j)][0])
      avant_dernier_csv=pd.read_csv(emplacement_fichier_documents+'/'+globals()['liste_double_document'+str(j)][1])
      avant_dernier_csvliste_document=avant_dernier_csv.values.tolist()
      dernier_csvliste_document=dernier_csv.values.tolist()
      modificationsliste=Diff(avant_dernier_csvliste_document,dernier_csvliste_document)
      #set(dernier_csvliste_document) & set(avant_dernier_csvliste_document)

      #modificationsliste=[l for l, m in zip(dernier_csvliste_document, avant_dernier_csvliste_document) if l == m]
      #modificationsliste=['\n'.join(sub_list) for sub_list in modificationsliste]

      if avant_dernier_csv.equals(dernier_csv)==False and len(modificationsliste)>0:
        #k=k+1
        #modificationsliste=['\n'.join(sub_list) for sub_list in modificationsliste]
        #ancien =modificationsliste[0:int((len(modificationsliste)/2))]
        #nouveau=modificationsliste[int((len(modificationsliste)/2)):]
        #modificationsliste2=Diff(nouveau,ancien)
        #if len(modificationsliste2)>0:
          k=k+1
          chaine=str(globals()['liste_double_document'+str(j)][0])
          pos1 = len('Document')+chaine.find('Document')
          pos2 = chaine.find('_')
          print (" Document modifié pour l'affaire "+globals()['liste_double_document'+str(j)][0][pos1:pos2])

          modificationsliste=['\n'.join(sub_list) for sub_list in modificationsliste]
          #ancien =modificationsliste[0:int((len(modificationsliste)/2))]
          #nouveau=modificationsliste[int((len(modificationsliste)/2)):]
          #liste_mail=[]
          #for i in range(0,len(modificationsliste)):
           # liste_mail.append(adresse_modification(modificationsliste[i]))
      #Création de la notification
            #i=i+1
          time.sleep(2)
          #print(modificationsliste)
          #if modifie!=ancien
          #set(modifie) & set(ancien)
          message3.append("* Document(s) modifié(s) pour l'affaire : "+globals()['liste_double_document'+str(j)][0][pos1:pos2] +" \n- Lien de l'affaire : https://pca-cpa.org/en/cases/"+globals()['liste_double_document'+str(j)][0][pos1:pos2]+" \n\nVoici ce qui a été modifié, ajouté ou supprimé : "+str(modificationsliste)+" Notification créée le "+today)
          print('\nModifications sauvegardées dans la liste message3')
    if k==0 :
      print(' Pas de modification dans les affaires, pas de notifiaction créée')
      message3=[]


    # In[ ]:


    message3=list(set(message3))


    # In[ ]:


    #message3


    # In[ ]:


    if len(message3)>0:
      for i in range(0, len(message3)):
        message3[i]=message3[i].replace('[\'<divclass="download-links">\\n<ahref="','\n- ')
        message3[i]=message3[i].replace('"target="_blank">download</a>|\\n',' ')
        message3[i]=message3[i].replace('|\\n',' ')
        message3[i]=message3[i].replace(', \'<divclass="download-links">\\n<ahref="', '\n- ')
        message3[i]=message3[i].replace('\'<divclass="download-links">\\n<ahref="', '')
        #message3[i]=message3[i].replace(',', '\n- ')
        message3[i]=message3[i].replace('] ','\n')
        message3[i]=message3[i].replace("\\n</div>'" , '')
    #message3


    # #Envoi du message

    # In[ ]:


    print("\nEnvoi du message s'il y a des modifications")


    # In[ ]:


    message4=message1+message2+message3


    # In[ ]:


    #message4


    # In[ ]:


    def send_mail(message):
      pw=password
      pw
      adresse=adresse_envoi
      adresse
      login
      #destinataire=destinataire
      destinataire
      sujet="Modification(s) apportée(s) à la page de la Cour Permanente d'Arbitrage : https://pca-cpa.org"
      sujet
      message=str(message)
      message
      msg = MIMEMultipart()
      msg['From'] = adresse
      msg['To'] = destinataire
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


    # In[ ]:


    message1string=""
    for i in range(0,len(message1)):
      message1string=message1string+'\n\n'+str(message1[i])

    message2string=""
    for i in range(0,len(message2)):
      message2string=message2string+'\n\n'+str(message2[i])

    message3string=""
    for i in range(0,len(message3)):
      message3string=message3string+'\n\n'+str(message3[i])


    # In[ ]:


    if len(message4)>0:

      send_mail(message1string+"\n\n********************"+message2string+"\n\n********************"+message3string)
    else:
      print('Aucune modification de la page, aucun mail envoyé !')


    # Nettoyage des dossiers

    # In[ ]:


    print("\nNettoyage des dossiers\n")


    # In[ ]:


    print('Nettoyage du dossier : '+emplacement_fichier)
    import os
    dossier_affaires= os.listdir(emplacement_fichier)

    for csv in dossier_affaires:
      if csv[-19:-4]!= today1:
        #os.rename(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
        shutil.move(emplacement_fichier+"/"+str(csv), emplacement_ancien_csv_sommaire+"/"+str(csv))
        #os.replace(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
    print("Anciens CSV déplacés vers le dossier : "+emplacement_ancien_csv_sommaire)


    # In[ ]:


    print('Nettoyage du dossier : '+emplacement_fichier_affaires)
    import os
    dossier_affaires= os.listdir(emplacement_fichier_affaires)

    for csv in dossier_affaires:
      if csv[-19:-4]!= today2:
        #os.rename(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
        shutil.move(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv_affaires+"/"+str(csv))
        #os.replace(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
    print("Anciens CSV déplacés vers le dossier : "+emplacement_ancien_csv_affaires)


    # In[ ]:


    print('Nettoyage du dossier : '+emplacement_fichier_documents)
    import os
    dossier_affaires= os.listdir(emplacement_fichier_documents)

    for csv in dossier_affaires:
      if csv[-19:-4]!= today3:
        #os.rename(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
        shutil.move(emplacement_fichier_documents+"/"+str(csv), emplacement_ancien_csv_documents+"/"+str(csv))
        #os.replace(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
    print("Anciens CSV déplacés vers le dossier : "+emplacement_ancien_csv_documents)


    # In[ ]:


    today = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%H:%M:%S , LE %d/%m/%Y"))
    print('PROGRAMME TERMINE A : '+today)


    # In[ ]:


    aa='liste20191004_112927.csv'


    # In[ ]:


    aa[-19:-4]


    # In[ ]:

except Exception as e:
    
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    
    

    def send_mail(message):
        pw=password
        pw
        adresse=adresse_envoi
        adresse
        login
        #destinataire=destinataire
        destinataire
        sujet="La page https://pca-cpa.org n'a pas pu être scrapée, il y a une erreur !"
        sujet
        message=str(message)
        message
        msg = MIMEMultipart()
        msg['From'] = adresse
        msg['To'] = destinataire
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

    send_mail('Erreur lors du scraping de la page PCA. Veuillez verifier le programme\n'+e)




# In[ ]:




