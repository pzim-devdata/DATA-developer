#!/usr/bin/env python
# coding: utf-8

# In[1]:


destinataire=''
password=''
adresse_envoi=''
smtp='smtp.'
port=587
login=adresse_envoi


try:

    import lxml
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    from datetime import datetime
    import time
    from datetime import datetime
    import pytz
    from tqdm import tqdm
    import os
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    import re
    import shutil


    # In[361]:


    emplacement_ancien_csv='old_csv'
    emplacement_fichier_affaires='cases_list'
    emplacement_fichier_liste_pays='countries_list'



    # In[362]:


    today = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%H:%M:%S , LE %d/%m/%Y"))
    print("LANCEMENT DU PROGRAMME A : "+today)


    # In[363]:


    #COLLECTE DES ADRESSES INTERNET DES PAYS A SCRAPER
    print("\nI. SCRAPING DES ADRESSES INTERNET DES PAYS")


    # In[364]:


    requete = requests.get("https://investmentpolicy.unctad.org/country-navigator")
    page = requete.content
    soup = BeautifulSoup(page, features="lxml")


    # In[365]:


    print("Scraping des adresses des pays :")


    # In[366]:


    liste=[]
    for a in tqdm(soup.find_all("div",{"class":"search-container country-select"})):
      liste.append(str(a))


    # In[367]:


    liste=list(set(liste))


    # In[368]:


    liste=str(liste).split('<option data-url=')


    # In[369]:


    #len(liste)


    # In[370]:


    liste.pop(0)


    # In[371]:


    numero_pays=[]
    for valuee in liste:
        chaine = str(valuee)
        pos1 = chaine.find("value=")
        pos2 = chaine.find(">")
      #extraction sans le 'href'
        pos1=pos1+len("value=")+1
        pos2=pos2-1
        sousChaine = chaine[pos1:pos2]
      #print (sousChaine)
        numero_pays.append(sousChaine)    


    # In[372]:


    #numero_pays


    # In[373]:


    adresses_pays=[]
    for nombre in numero_pays:
        adresses_pays.append('https://investmentpolicy.unctad.org/country-navigator/'+nombre)


    # In[374]:


    #adresses_pays


    # In[375]:


    today = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%Y%m%d_%H%M%S"))


    # In[376]:


    df = pd.DataFrame(adresses_pays)
    df.to_csv(emplacement_fichier_liste_pays+'/liste_des_adresses_des_pays'+today+'.csv', index=False)


    # In[377]:


    print("Liste des adresses Internet des pays créée dans le dossier : "+emplacement_fichier_liste_pays)


    # In[378]:


    print(" Patienter 10 secondes")
    for i in tqdm(range(100)):
        time.sleep(0.10)


    # In[19]:


    #VERIFICATION S'IL Y A DES MODIFICATIONS DANS LA LISTE DES PAYS
    print("\nVERIFICATION S'IL Y A DES MODIFICATIONS DANS LA LISTE DES PAYS :")


    # In[390]:


    dossier= os.listdir(emplacement_fichier_liste_pays)
    listetecsv=[]
    for csv in dossier:
      listetecsv.append(csv)


    # In[391]:


    listetecsv.sort()


    # In[392]:


    #Attention : Il est nécessaire d'avoir au moins deux CSV. Relancer le programme si besoin.
    try:
        avant_dernier_CSV=pd.read_csv(emplacement_fichier_liste_pays+'/'+listetecsv[-2], error_bad_lines=False)
        dernier_CSV=pd.read_csv(emplacement_fichier_liste_pays+'/'+listetecsv[-1])
    except :
        print("Attention : Il est nécessaire d'avoir au moins deux CSV. Relancer le programme.")


    # In[393]:


    def Diff(li1, li2): 
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
        return li_dif 


    # In[394]:


    today = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%d/%m/%Y à %H:%M:%S"))
    message1=[]
    if avant_dernier_CSV.equals(dernier_CSV)==False:
      print ('Modifications apportées au sommaire')
      avant_dernier_CSVliste=avant_dernier_CSV.values.tolist()
      dernier_CSVliste=dernier_CSV.values.tolist()
      modificationsliste=Diff(dernier_CSVliste,avant_dernier_CSVliste)
      modificationsliste=['\n'.join(sub_list) for sub_list in modificationsliste]


      for i in range(0,int(len(modificationsliste))):
        message1.append("* Voici l'affaire modifiée, supprimée ou ajoutée, dans la liste des pays de la page https://investmentpolicy.unctad.org/country-navigator : \nAdresse de l'affaire : \n"+str(modificationsliste[i])+' \nNofication créée le '+today)
        message1=list(set(message1))
       #print(message1)
      #sauvegarde message
        i=i+1
      #message1.append(str(liste_mail)+' Nofication crée le '+today)
        print('\nModifications sauvegardées dans la liste message1')
    else :
      print('Pas de modification de la liste des pays, pas de notification créée')
      message1=[]


    # In[395]:


    message1


    # In[396]:


    #SCRAPING DES PAGES DES PAYS
    print("\nII. SCRAPING DES PAGES DES PAYS")


    # In[397]:


    today2 = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%Y%m%d_%H%M%S"))
    for cases in tqdm(adresses_pays):
      requete_affaires = requests.get(cases)
      page_affaires = requete_affaires.content
      soup_affaires = BeautifulSoup(page_affaires, features="lxml")
      globals()['liste_affaire'+cases[29:]+"_"+today2]=[]
      for a in soup_affaires.find_all('div',{"class":"main-content-inner"}):
      #for a in soup_affaires.find_all('li'):
        globals()['liste_affaire'+cases[29:]+"_"+today2].append(str(a))
        df = pd.DataFrame(globals()['liste_affaire'+cases[29:]+"_"+today2])
        df.to_csv(emplacement_fichier_affaires+'/Affaire_'+cases[54:]+"_"+today2+'.csv', index=False)


    # In[398]:


    print("Les pages scrapées ont été sauvegardées dans le dossier : "+emplacement_fichier_affaires)


    # In[33]:


    print("Patienter 30 secondes")
    for i in tqdm(range(100)):
        time.sleep(0.30)



    # In[ ]:


    #VERIFICATION S'IL Y A DES MODIFICATIONS DANS LES AFFAIRES
    print("\nVERIFICATION S'IL Y A DES MODIFICATIONS DANS LES AFFAIRES :")


    # In[465]:


    import os
    dossier_affaires= os.listdir(emplacement_fichier_affaires)
    listetecsvaffaires=[]
    for csv in dossier_affaires:
      listetecsvaffaires.append(csv)


    # In[466]:


    listetecsvaffaires.sort()


    # In[467]:


    def listecsv_affaires_debut(x):
      chaine = str(x)

      pos2 = chaine.find('_',8)
      sousChaine = chaine[:pos2]
      #print (sousChaine)
      return(sousChaine)


    # In[468]:


    print('Classement des affaires : \n')
    liste_affaire_double=[]
    for affaire1 in tqdm(listetecsvaffaires):
      i=0    
      for affaire2 in listetecsvaffaires:

        if listecsv_affaires_debut(listetecsvaffaires[listetecsvaffaires.index(affaire1)])==listecsv_affaires_debut(listetecsvaffaires[listetecsvaffaires.index(affaire2)]):
          i=i+1
          if i>1:
            liste_affaire_double.append(affaire1)
            liste_affaire_double.append(affaire2)


    # In[469]:


    liste_affaire_double=list(set(liste_affaire_double))


    # In[470]:


    liste_affaire_double.sort(reverse=True)


    # In[471]:


    i=0
    for affaire_en_double in liste_affaire_double:
      i=i+1

      globals()['liste_double'+str(i)]=[]
      for affaire_en_double2 in liste_affaire_double:
        if affaire_en_double[0:11]==affaire_en_double2[0:11]:
          globals()['liste_double'+str(i)].append(affaire_en_double2)


    # In[472]:


    def Diff(li1, li2): 
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
        return li_dif 


    # In[473]:


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
          pos1 = len('Affaire')+chaine.find('Affaire')+1
          pos2 = chaine.find('_',8)
          print ("\nModifications apportées à l'affaire : "+globals()['liste_double'+str(j)][0][pos1:pos2])

          modificationsliste=['\n'.join(sub_list) for sub_list in modificationsliste]
          ancien =modificationsliste[0:int((len(modificationsliste)/2))]
          nouveau=modificationsliste[int((len(modificationsliste)/2)):]
          liste_mail=[]
          for i in range(0,len(modificationsliste)):
            liste_mail.append(modificationsliste[i])
      #sauvegarde message2
            i=i+1
          time.sleep(2) 
          ancien2=''
          for l in range(0,len(ancien)):
              ancien2=ancien2+ancien[l]
          indexancien=([(n.start(0)) for n in re.finditer('span>', ancien2)])
          indexancien.insert(0,0)
          indexancien.append(len(ancien2))

          nouveau2=''
          for m in range(0,len(nouveau)):
              nouveau2=nouveau2+nouveau[m]
          indexnouveau=([(o.start(0)) for o in re.finditer('span>', nouveau2)])
          indexnouveau.insert(0,0)
          indexnouveau.append(len(nouveau2))

          listeancien=[]
          p=0
          for q in range(0,len(indexancien)-1):
              p=p+1
              listeancien.append(ancien2[indexancien[q]:indexancien[p]])

          listenouveau=[]
          r=0
          for s in range(0,len(indexnouveau)-1):
              r=r+1
              listenouveau.append(nouveau2[indexnouveau[s]:indexnouveau[r]])

          message_Diff=Diff(listeancien,listenouveau) 

          ancien_Diff=message_Diff[:int(len(message_Diff)/2)]
          nouveau_Diff= message_Diff[int(len(message_Diff)/2):] 

          message2.append("* Modifications apportées à l'affaire numéro : "+globals()['liste_double'+str(j)][0][pos1:pos2] +"\n- Lien : https://investmentpolicy.unctad.org/country-navigator/"+globals()['liste_double'+str(j)][0][pos1:pos2]+ " \n\nVoici ce qui a été modifié, ajouté ou supprimé : \n"+str(nouveau_Diff)+' \nNotification créée le '+today)
          print('\nModifications sauvegardées dans la liste message2')

    if k==0 :
      print(' Pas de modification dans les affaires, pas de notification créée')
      message2=[]


    # In[474]:


    message2=list(set(message2))
    #message2


    # In[475]:


    if len(message2)>0:
      for i in range(0,len(message2)):
        message2[i]=str(message2[i]).replace("<li style=""margin-left: 20px;"">",'Traité crée, ajouté ou modifié : \n')
        message2[i]=str(message2[i]).replace("""[\'span>\\n</a>\\n</li>\\n<li style="margin-left: 20px;">\\n<a """, '\n')
        message2[i]=str(message2[i]).replace("- </\', \'span>\\n<span class=", '\n')
        message2[i]=str(message2[i]).replace('">\\n<\', \'span>', ' \n')
        message2[i]=message2[i].replace('>Full text: <a href="', 'Adresse de téléchargement du document MODIFIEE AJOUTEE OU SUPPRIMEE: https://investmentpolicy.unctad.org')
        message2[i]=message2[i].replace('" target="_blank">', ' \n- Langue MODIFIEE AJOUTEE OU SUPPRIMEE: ')
        message2[i]=str(message2[i]).replace('href="', ' https://investmentpolicy.unctad.org')
        message2[i]=str(message2[i]).replace('"language"','')
        message2[i]=str(message2[i]).replace("</a></\', \'span>",'\n')
        message2[i]=str(message2[i]).replace("- </\', \'span>\\n</a>\\n<span class=",'\n')
        message2[i]=str(message2[i]).replace("</a><br/>", '\n\n')
        message2[i]=str(message2[i]).replace("</a></\']",'\n')
        message2[i]=str(message2[i]).replace("<a ",'' )

        message2[i]=str(message2[i]).replace("</\'", '')
        message2[i]=str(message2[i]).replace(" \n\\n</a>\\n</li>\\n<li style=",'\n')
        message2[i]=str(message2[i]).replace("\\n</a>\\n</li>\\n<li style=", '')
        message2[i]=str(message2[i]).replace("margin-left: 20px;", '')
        message2[i]=str(message2[i]).replace(',', '')
        message2[i]=str(message2[i]).replace(">", '')
        message2[i]=str(message2[i]).replace('"','')
        message2[i]=str(message2[i]).replace("\\n",'\n')
        message2[i]=str(message2[i]).replace("[",'')
        message2[i]=str(message2[i]).replace("]",'\n')
        message2[i]=str(message2[i]).replace("- \n\n",'\n')
        message2[i]=str(message2[i]).replace("\n\n", "\n")
        message2[i]=str(message2[i]).replace("Voici ce qui a été modifié ajouté","\nVoici ce qui a été modifié ajouté")
        message2[i]=str(message2[i]).replace("'<div class=main-content-inner\n<div class=page-title style=margin-bottom: 30px;\n<div class=item-country\n<div class=country-flag\n<img alt=", '\n')
        message2[i]=str(message2[i]).replace("src=/Content/images/flags/1x1/eu.svg style=width: 55px; height: 55px;/\n</div\n<div class=country-info\n<h2",'')
        message2[i]=str(message2[i]).replace("</h2\n</div\n</div\n</div\n<div class=content-item\n<div class=page-title id=policy-measures-header\n<button class=js-toggle data-target=#policy-measures data-toggle=collapse\n<img alt=expand class=js-expanded src=/Content/images/circle-expand.png style=display:none;/\n<img alt=collapse class=js-collapsed src=/Content/images/circle-collapse.png/\n</button\n<h3Policy measures </h3\n</div\n<ul class=collapse in general-list id=policy-measures\n<li style=",'')
        message2[i]=str(message2[i]).replace("\n<span",' \n')
        message2[i]=str(message2[i]).replace("class=",'')
        message2[i]=str(message2[i]).replace("-\n<'\n",' \n')
        message2[i]=str(message2[i]).replace("\n","\n- ")
        message2[i]=str(message2[i]).replace("- -",'-')
        message2[i]=str(message2[i]).replace("  ", " ")
        message2[i]=str(message2[i]).replace("\n- \n",'\n\n')
        message2[i]=str(message2[i]).replace("\n\n- \n", "\n\n")
        message2[i]=str(message2[i]).replace("\n\n- </a",'')
        message2[i]=str(message2[i]).replace("\n- </a ",'')
        message2[i]=str(message2[i]).replace("</h4\n- </li\n- <li style=",'')
        message2[i]=str(message2[i]).replace("\n\n- </li\n- <li style=",'')
        message2[i]=str(message2[i]).replace("</li\n- <li style=",'')
        message2[i]=str(message2[i]).replace("dateDate","Date")
        message2[i]=str(message2[i]).replace("Date of signature",'Date de signature MODIFIEE, AJOUTEE ou CREEE')
        message2[i]=str(message2[i]).replace("'span\n",'\n')
        message2[i]=str(message2[i]).replace("'span",'/n- Traité crée, ajouté ou modifié : \n')
        message2[i]=str(message2[i]).replace("date",'Date MODIFIEE, AJOUTEE ou CREEE : ')

    #message2


    # In[476]:


    #message2


    # In[477]:


    #NETTOYAGE DES DOSSIERS
    print("\nIII NETTOYAGE DES DOSSIERS")


    # In[478]:


    print('Nettoyage du dossier : '+emplacement_fichier_affaires)
    import os
    dossier_affaires= os.listdir(emplacement_fichier_affaires)

    for csv in dossier_affaires:
      if csv[-19:-4]!= today2:
        #os.rename(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
        shutil.move(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
        #os.replace(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
    print("Anciens CSV déplacés vers le dossier : "+emplacement_ancien_csv)


    # In[479]:


    #ENVOI DU MESSAGE S'IL EXISTE DES MODIFICATIONS DANS LA PAGE
    print("\nIV ENVOI DU MESSAGE S'IL EXISTE DES MODIFICATIONS DANS LA PAGE")


    # In[480]:


    message3=message1+message2


    # In[481]:


    def send_mail(message):
      pw=password
      pw
      adresse=adresse_envoi
      adresse
      login
      #destinataire=destinataire
      destinataire
      sujet="Modification(s) apportée(s) à la page unctad.org"
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
      mailserver.starttls() #a rajouter si necessaire
      #mailserver.ehlo() #a rajouter si necessaire
      mailserver.login(login, pw)
      mailserver.sendmail(adresse,destinataire, msg.as_string())
      print(" Message envoyé !")
      mailserver.quit()


    # In[482]:


    message1string=""
    for i in range(0,len(message1)):
      message1string=message1string+'\n\n'+str(message1[i])

    message2string=""
    for i in range(0,len(message2)):
      message2string=message2string+'\n\n'+str(message2[i])


    # In[483]:


    if len(message3)>0:

      send_mail(message1string+"\n\n********************"+message2string)
    else:
      print('Aucune modification de la page, aucun mail envoyé !')


    # In[484]:


    today = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%H:%M:%S , LE %d/%m/%Y"))
    print('PROGRAMME TERMINE A : '+today)

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
        sujet="La page unctad.org n'a pas pu être scrapée, il y a une erreur !"
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

    send_mail('Erreur lors du scraping de la page unctad.org. Veuillez verifier le programme\n'+e)




# In[ ]:




