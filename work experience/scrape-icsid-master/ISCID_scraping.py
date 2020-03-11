#!/usr/bin/env python
# coding: utf-8

# In[8]:


#!/usr/bin/env python
# coding: utf-8

# J'utilise un driver Chrome 77 (ChromeDriver 77.0.3865.40) (https://chromedriver.chromium.org/downloads ). Il faut le mettre dans le même dossier que le fichier Python (emplacement_driver_chrome) et je suis sous Linux 64 bit Ubuntu.
# 
# Le navigateur (Version 77.0.3865.90 (Build officiel) (64 bits)) a les options par défaut.
# 
# Par ailleurs, vérifier que le swapfile est bien à 0B used à la fin de l'execution du code:
# sudo swapon --show pour verifier la taille du swap

# In[1]:
#from getpass import getpass

#pip install progressbar2
#pip install selenium
#pip install progressbar
destinataire=''
password=''
adresse_envoi=''
smtp='smtp.'
port=587
login=adresse_envoi

# In[ ]:


#import requests
#from bs4 import BeautifulSoup
#from selenium.webdriver.common.keys import Keys
#import csv
#import progressbar
try:
    
    import pandas as pd
    from datetime import datetime
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from datetime import datetime
    import pytz
    from tqdm import tqdm
    import os
    from tqdm import tqdm
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import smtplib
    import re
    import shutil


    # In[3]:


    emplacement_ancien_csv='old_csv'
    emplacement_driver_chrome='chromedriver'
    emplacement_fichier='cases_list'
    emplacement_fichier_affaires='cases'



    # I. Liste des affaires

    # In[ ]:


    today= str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%H:%M:%S LE %d/%m/%Y"))
    print('\nDEBUT DU PROGRAMME A '+today)


    # In[ ]:


    print('\nI. ANALYSE DE LA LISTE DES AFFAIRES (SOMMAIRE) : \n')


    # a) Scrapping

    # In[ ]:


    print('  1- Lancement du scraping :\n')


    # In[4]:


    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    #browser.save_screenshot('screenshot.png')


    # In[5]:


    prefs = {
        'profile.managed_default_content_settings.images': 2,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    }
    options.add_experimental_option('prefs', prefs)


    # In[6]:


    browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
    browser.implicitly_wait(30)
    browser.get("https://icsid.worldbank.org/en/Pages/cases/AdvancedSearch.aspx")
    time.sleep (15)


    # In[7]:


    #requete = driver.get("https://icsid.worldbank.org/en/Pages/cases/AdvancedSearch.aspx")
    #time.sleep (5)
    #page = driver.content
    #browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]/div[4]/div[1]/select").click()
    #time.sleep (7)
    #browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]/div[4]/div[1]/select").click()
    #aa=browser.find_element_by_xpath("//select[@class='CVpagecount ng-pristine ng-valid ng-touched']/option[text()='All']").click()
    browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]/div[4]/div[1]/select/option[3]").click()
    time.sleep (1)
    browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]/div[4]/div[1]/select/option[3]").click()
    time.sleep (1)


    # In[8]:


    liste=[]
    for a in tqdm(browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]/div[4]/table/tbody/tr/td[1]/a")):
        liste.append(str(a.get_attribute('href')))
    #browser.close()
    #liste                   


    # In[9]:


    browser.quit()
    try: 
        browser.close()
    except : #"InvalidSessionIdException"
        pass


    # In[10]:


    #soup = BeautifulSoup(browser.page_source)


    # In[11]:


    #liste=[]
    #for a in soup.find_all('td',{"class":"casecol1"}):
    #  liste.append(str(a))
    #browser.close()


    # In[12]:


    #liste


    # b) Nettoyage

    # In[ ]:


    print("\n  2- Nettoyage de la liste des affaires :")


    # In[13]:


    #listenettoyee=[]
    #for string in liste:
    #    pos1=string.find('href="..')
    #    pos1=pos1+len('href="..')
    #    pos2=string.find('" target="_blank">')
    #    string=string[pos1:pos2]
    #    listenettoyee.append('https:/'+string)
    listenettoyee=liste


    # In[14]:


    #listenettoyee


    # In[15]:


    today = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%Y%m%d_%H%M%S"))


    # In[16]:


    df = pd.DataFrame(listenettoyee)
    df.to_csv(emplacement_fichier+'/liste_des_affaires_'+today+'.csv', index=False)


    # In[ ]:


    print("\n Patienter 30 secondes\n")


    # In[17]:


    for i in tqdm(range(100)):
        time.sleep(0.30)


    # Verifications s'il y a des modifications dans la liste des affaires

    # In[ ]:


    print("\n  3- Comparaison de la liste des affaires :\n")


    # c) Comparaison des listes d'affaires

    # In[ ]:


    #print('COMPARAISON DES AFFAIRES\n')


    # In[18]:


    dossier= os.listdir(emplacement_fichier)
    listetecsv=[]
    for csv in dossier:
      listetecsv.append(csv)


    # In[19]:


    listetecsv.sort()


    # Attention : Il faut au moins deux CSV. Redemarrer le code si nécessaire.

    # In[20]:


    try:
        avant_dernier_CSV=pd.read_csv(emplacement_fichier+'/'+listetecsv[-2], error_bad_lines=False)
        dernier_CSV=pd.read_csv(emplacement_fichier+'/'+listetecsv[-1])
    except :
        print("\n\n\nAttention ! : Il faut au moins deux CSV. Relancer le programme!\n\n\n")


    # In[21]:


    def Diff(li1, li2): 
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
        return li_dif 


    # In[22]:


    #adresse_modification=???????????????


    # In[ ]:


    #print("\n4- Vérification si des modifications ont été apportées à la liste des affaires : \n")


    # In[ ]:


    print("\n  4- Création du message si des modifications ont été apportées \à la liste des affaires dans le sommaire:\n")


    # In[23]:


    today = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%d/%m/%Y à %H:%M:%S"))
    message1=[]
    if avant_dernier_CSV.equals(dernier_CSV)==False:
      print ('\nModifications apportées au sommaire')
      avant_dernier_CSVliste=avant_dernier_CSV.values.tolist()
      dernier_CSVliste=dernier_CSV.values.tolist()
      modificationsliste=Diff(dernier_CSVliste,avant_dernier_CSVliste)
      modificationsliste=['\n'.join(sub_list) for sub_list in modificationsliste]


      for i in tqdm(range(0,int(len(modificationsliste)))):

        chaine = str(modificationsliste[i])
        pos1= modificationsliste[i].find('CaseNo=')
        pos1= pos1+len('CaseNo=')
        sousChaine=chaine[pos1:]
        sousChaine=sousChaine.replace('%20',' ')

        modificationsliste[i]=modificationsliste[i].replace(' ','%20')
        message1.append("* Voici l'affaire modifiée, supprimée ou ajoutée, dans le sommaire de la page https://icsid.worldbank.org/en/Pages/cases/AdvancedSearch.aspx :\nNom de l'affaire : "+str(sousChaine)+" \nAdresse de l'affaire : "+modificationsliste[i]+" \nNofication créée le "+today)
        message1=list(set(message1))
       #print(message1)
      #sauvegarde message
        i=i+1
      #message1.append(str(liste_mail)+' Nofication crée le '+today)
        print('\nModifications sauvegardées dans la liste message1')
    else :
      print('\nPas de modification du sommaire, pas de notification créée\n')
      message1=[]


    # In[24]:


    #print(message1)


    # II. Affaires

    # In[ ]:


    print("\n\nII. ANALYSE DE CHAQUE AFFAIRE :\n")


    # a) Scraping

    # In[ ]:


    print('  1- Lancement du scraping :')


    # In[25]:


    listenettoyee.sort()
    len(listenettoyee)


    # In[26]:


    listenettoyee2=[]
    #for i in listenettoyee:
    for j in range(0,len(listenettoyee)):
        listenettoyee2.append(listenettoyee[j].replace('/', '_'))


    # In[27]:


    listenettoyee2.sort()
    #len(listenettoyee2)


    # In[28]:


    listenettoyee11=listenettoyee[:int(len(listenettoyee)/3)]
    #len(listenettoyee11)


    # In[29]:


    listenettoyee12=listenettoyee[int(len(listenettoyee)/3):int(len(listenettoyee)*2/3)]
    #len(listenettoyee12)


    # In[30]:


    listenettoyee13=listenettoyee[int(len(listenettoyee)*2/3):]
    #len(listenettoyee13)


    # In[31]:


    #len(listenettoyee11)+len(listenettoyee12)+len(listenettoyee13)


    # In[ ]:


    print('\n    1.1- Scraping 1/3 : \nSCRAPING DES AFFAIRES DE 1 A '+str(len(listenettoyee11))+' SUR '+str(len(listenettoyee2))+' :\n')


    # In[32]:


    today2 = str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%Y%m%d_%H%M%S"))
    options = Options()
    options.add_argument("--no-sandbox")
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    options.add_argument("--disable-dev-shm-usage")
    prefs = {
        'profile.managed_default_content_settings.images': 2,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    }
    options.add_experimental_option('prefs', prefs)
    #browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
    i=-1
    for cases in tqdm(listenettoyee11) :
        i=i+1
        try:

        #requete_affaires = requests.get(cases)
        #page_affaires = requete_affaires.content
        #soup_affaires = BeautifulSoup(page_affaires)

            browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
            globals()['liste_affaire'+cases[66:]+"_"+today2]=[]
            browser.implicitly_wait(30)
        #browser.execute_script("window.open('');")
        #Window_List = browser.window_handles
        #browser.switch_to_window(browser.window_handles[0])
            browser.get(str(cases))
            time.sleep(0.1)
            browser.get(str(cases))
            time.sleep(0.1)

        except Exception as e: 
            print(e)
            print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
            browser.quit()
            try: 
                browser.close()
            except :
                pass

            time.sleep(300)
            browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
            browser.implicitly_wait(30)
            browser.get(str(cases))
            time.sleep(10)
            browser.get(str(cases))
            time.sleep(10)
        #browser.find_element(by.linkText(str(cases))).sendKeys(Keys.chord(Keys.CONTROL,"t"))
        #time.sleep (2.5)
        #if i==200 or i==400 or i== 600 or i== 800:
         #   print("sleep")
          #  time.sleep (60)
        #Scrapping du titre :
        for titre in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/span"):
            try:
                globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(titre.text))
                df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                if len(globals()['liste_affaire'+cases[66:]+"_"+today2])==0 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][0])<25 or globals()['liste_affaire'+cases[66:]+"_"+today2][0]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][0]=='':
                    print("\nATTTENTION Le titre n'a pas été scrapé !!!, le processus recommence dans 30 secondes\n")
                    #print(globals()['liste_affaire'+cases[66:]+"_"+today2])
                    browser.quit()
                    try: 
                        browser.close()
                    except :
                        pass
                    time.sleep(30)
                    browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                    browser.implicitly_wait(30)
                    browser.get(str(cases))
                    time.sleep(0.1)
                    browser.get(str(cases))
                    time.sleep(10)
                    globals()['liste_affaire'+cases[66:]+"_"+today2]=[]
                    for titre in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/span"):
                        globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(titre.text))
                        df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                        df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

            except Exception as e: 
                print(e)
                print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
                browser.quit()
                try: 
                    browser.close()
                except :
                    pass

                time.sleep(300)
                browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                browser.implicitly_wait(30)
                browser.get(str(cases))
                time.sleep(10)
                browser.get(str(cases))
                time.sleep(10)
                globals()['liste_affaire'+cases[66:]+"_"+today2]=[]
                for titre in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/span"):
                    globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(titre.text))
                    df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                    df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                    if len(globals()['liste_affaire'+cases[66:]+"_"+today2])==0 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][0])<25 or globals()['liste_affaire'+cases[66:]+"_"+today2][0]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][0]=='':
                        print("\nATTTENTION Le titre n'a pas été scrapé !!!, le processus recommence dans 30 secondes\n")
                        #print(globals()['liste_affaire'+cases[66:]+"_"+today2][0])
                        browser.quit()
                        try: 
                            browser.close()
                        except :
                            pass
                        time.sleep(30)
                        browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                        browser.implicitly_wait(30)
                        browser.get(str(cases))
                        time.sleep(0.1)
                        browser.get(str(cases))
                        time.sleep(10)
                        globals()['liste_affaire'+cases[66:]+"_"+today2]=[]
                        for titre in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/span"):
                            globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(titre.text))
                            df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                            df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

        #Scraping de l'onglet principal : 

        for a in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #liste.append(str(a.get_attribute('href')))

       # soup_affaires = BeautifulSoup(browser.page_source)
        #for a in soup_affaires.find_all('div',{'class':'article article-body'}):
            try:
                globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(a.text))
                df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

                if len(globals()['liste_affaire'+cases[66:]+"_"+today2])<=1 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][1])<50 or globals()['liste_affaire'+cases[66:]+"_"+today2][1]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][1]=='':
                    print("\nATTTENTION L'onglet principal n'a pas été scrapé !!!, le processus recommence dans 30 secondes\n")
                    #print(globals()['liste_affaire'+cases[66:]+"_"+today2][1])
                    globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0]
                    browser.quit()
                    try: 
                        browser.close()
                    except :
                        pass
                    time.sleep(30)
                    browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                    browser.implicitly_wait(30)
                    browser.get(str(cases))
                    time.sleep(0.1)
                    browser.get(str(cases))
                    time.sleep(2)
                    for a in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
                        globals()['liste_affaire'+cases[66:]+"_"+today2].insert(1, str(a.text))
                        df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                        df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
            except Exception as e: 
                print(e)
                print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
                browser.quit()
                try: 
                    browser.close()
                except :
                    pass

                time.sleep(300)
                browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                browser.implicitly_wait(30)
                browser.get(str(cases))
                time.sleep(10)
                browser.get(str(cases))
                time.sleep(10)
                globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0]
                for a in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #liste.append(str(a.get_attribute('href')))

       # soup_affaires = BeautifulSoup(browser.page_source)
        #for a in soup_affaires.find_all('div',{'class':'article article-body'}):
                    globals()['liste_affaire'+cases[66:]+"_"+today2].insert(1, str(a.text))
                    df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                    df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

                if len(globals()['liste_affaire'+cases[66:]+"_"+today2])<=1 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][1])<50 or globals()['liste_affaire'+cases[66:]+"_"+today2][1]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][1]=='':
                    print("\nATTTENTION L'onglet principal n'a pas été scrapé !!!, le processus recommence dans 30 secondes\n")
                    #print(globals()['liste_affaire'+cases[66:]+"_"+today2][1])
                    browser.quit()
                    try: 
                        browser.close()
                    except :
                        pass
                    globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0]
                    browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                    browser.implicitly_wait(30)
                    time.sleep(30)
                    browser.get(str(cases))
                    time.sleep(0.1)
                    browser.get(str(cases))
                    time.sleep(2)
                    for a in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
                        globals()['liste_affaire'+cases[66:]+"_"+today2].insert(1, str(a.text))
                        df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                        df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

       # Scraping de l'onglet Materials :
       # browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()
       # browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()


       # time.sleep(1)
       # soup_affaires2 = BeautifulSoup(browser.page_source)
       # for b in soup_affaires2.find_all('div',{'class':'tab-content cdtl'}):
       #   globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(b))
       #   df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
       #   df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)


        #Scraping de l'onglet Procedural Details :
        try:
            browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
            time.sleep(0.1)
            browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
            time.sleep(1)
        except Exception as e: 
            print(e)
            print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
            browser.quit()
            try: 
                browser.close()
            except :
                pass
            time.sleep(300)
            browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
            browser.implicitly_wait(30)
            browser.get(str(cases))
            time.sleep(10)
            browser.get(str(cases))
            time.sleep(10)
            browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
            time.sleep(0.1)
            browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
            time.sleep(1)

        #soup_affaires3 = BeautifulSoup(browser.page_source)
        for c in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #for c in soup_affaires3.find_all('div',{'class':'tab-content cdtl'}):
            try:
                globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(c.text))
                df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                time.sleep(0.1)
                if len(globals()['liste_affaire'+cases[66:]+"_"+today2])< 3 or (str(globals()['liste_affaire'+cases[66:]+"_"+today2][2]) != 'No References Available' and (len(globals()['liste_affaire'+cases[66:]+"_"+today2])< 2 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][2])<50 or globals()['liste_affaire'+cases[66:]+"_"+today2][2]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][2]=='')):
                    #print(globals()['liste_affaire'+cases[66:]+"_"+today2][2])
                    print("\nL'onglet 'Procedural Details' est anormalement vide, le processus recommence le scrap dans 30 secondes\n")
                    browser.quit()
                    try: 
                        browser.close()
                    except :
                        pass
                    time.sleep(30)
                    browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                    browser.implicitly_wait(30)
                    browser.get(str(cases))
                    time.sleep(0.1)
                    browser.get(str(cases))
                    time.sleep(2)
                    browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                    time.sleep(0.1)
                    browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                    time.sleep(2)
                    globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0:2]
                    for c in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #for c in soup_affaires3.find_all('div',{'class':'tab-content cdtl'}):
                        globals()['liste_affaire'+cases[66:]+"_"+today2].insert(2, str(c.text))
                        df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                        df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                        time.sleep(0.1)

            except Exception as e: 
                print(e)
                print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
                browser.quit()
                try: 
                    browser.close()
                except :
                    pass
                time.sleep(300)
                browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                browser.implicitly_wait(30)
                browser.get(str(cases))
                time.sleep(10)
                browser.get(str(cases))
                time.sleep(10)
                browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                time.sleep(0.1)
                browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                time.sleep(1)
                globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0:2]
                for c in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
                    globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(c.text))
                    df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                    df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                    time.sleep(0.1)
                    if len(globals()['liste_affaire'+cases[66:]+"_"+today2])<= 2 or (str(globals()['liste_affaire'+cases[66:]+"_"+today2][2]) != 'No References Available' and (len(globals()['liste_affaire'+cases[66:]+"_"+today2])< 2 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][2])<50 or globals()['liste_affaire'+cases[66:]+"_"+today2][2]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][2]=='')):
                        #print(globals()['liste_affaire'+cases[66:]+"_"+today2][2])
                        print("\nL'onglet 'Procedural Details' est anormalement vide, le processus recommence le scrap dans 30 secondes\n")
                        browser.quit()
                        try: 
                            browser.close()
                        except :
                            pass
                        browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                        browser.implicitly_wait(30)
                        time.sleep(30)
                        browser.get(str(cases))
                        time.sleep(0.1)
                        browser.get(str(cases))
                        time.sleep(2)
                        browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                        time.sleep(0.1)
                        browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                        time.sleep(2)
                        globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0:2]
                        for c in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #for c in soup_affaires3.find_all('div',{'class':'tab-content cdtl'}):
                            globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(c.text))
                            df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                            df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                            time.sleep(0.1)



        browser.close()


    # In[ ]:


    print("\nSCRAPING 1/3 REUSSI !")


    # In[ ]:


    browser.quit()
    try: 
        browser.close()
    except :
        pass


    # In[ ]:


    print("\n Patienter 2 minutes\n")


    # In[ ]:


    for i in tqdm(range(100)):
        time.sleep(1.20)


    # In[ ]:


    print('\n\n    1.2- Scraping 2/3 : \nSCRAPING DES AFFAIRES DE '+str(len(listenettoyee11))+' A '+str((len(listenettoyee11)+len(listenettoyee12)))+' SUR '+str(len(listenettoyee2))+' :\n')


    # In[ ]:


    options = Options()
    options.add_argument("--no-sandbox")
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    options.add_argument("--disable-dev-shm-usage")
    prefs = {
        'profile.managed_default_content_settings.images': 2,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    }
    options.add_experimental_option('prefs', prefs)
    i=len(listenettoyee11)-1
    for cases in tqdm(listenettoyee12):
        i=i+1
        try:

        #requete_affaires = requests.get(cases)
        #page_affaires = requete_affaires.content
        #soup_affaires = BeautifulSoup(page_affaires)

            browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
            globals()['liste_affaire'+cases[66:]+"_"+today2]=[]
            browser.implicitly_wait(30)
        #browser.execute_script("window.open('');")
        #Window_List = browser.window_handles
        #browser.switch_to_window(browser.window_handles[0])
            browser.get(str(cases))
            time.sleep(0.1)
            browser.get(str(cases))
            time.sleep(0.1)

        except Exception as e: 
            print(e)
            print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
            browser.quit()
            try: 
                browser.close()
            except :
                pass

            time.sleep(300)
            browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
            browser.implicitly_wait(30)
            browser.get(str(cases))
            time.sleep(10)
            browser.get(str(cases))
            time.sleep(10)


        #browser.find_element(by.linkText(str(cases))).sendKeys(Keys.chord(Keys.CONTROL,"t"))
        #time.sleep (2.5)
        #if i==200 or i==400 or i== 600 or i== 800:
         #   print("sleep")
          #  time.sleep (60)
        #Scrapping du titre :
        for titre in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/span"):
            try:
                globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(titre.text))
                df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                if len(globals()['liste_affaire'+cases[66:]+"_"+today2])==0 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][0])<25 or globals()['liste_affaire'+cases[66:]+"_"+today2][0]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][0]=='':
                    print("\nATTTENTION Le titre n'a pas été scrapé !!!, le processus recommence dans 30 secondes\n")
                    #print(globals()['liste_affaire'+cases[66:]+"_"+today2])
                    browser.quit()
                    try: 
                        browser.close()
                    except :
                        pass
                    time.sleep(30)
                    browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                    browser.implicitly_wait(30)
                    browser.get(str(cases))
                    time.sleep(0.1)
                    browser.get(str(cases))
                    time.sleep(10)
                    globals()['liste_affaire'+cases[66:]+"_"+today2]=[]
                    for titre in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/span"):
                        globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(titre.text))
                        df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                        df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

            except Exception as e: 
                print(e)
                print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
                browser.quit()
                try: 
                    browser.close()
                except :
                    pass

                time.sleep(300)
                browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                browser.implicitly_wait(30)
                browser.get(str(cases))
                time.sleep(10)
                browser.get(str(cases))
                time.sleep(10)
                globals()['liste_affaire'+cases[66:]+"_"+today2]=[]
                for titre in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/span"):
                    globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(titre.text))
                    df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                    df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                    if len(globals()['liste_affaire'+cases[66:]+"_"+today2])==0 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][0])<25 or globals()['liste_affaire'+cases[66:]+"_"+today2][0]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][0]=='':
                        print("\nATTTENTION Le titre n'a pas été scrapé !!!, le processus recommence dans 30 secondes\n")
                        #print(globals()['liste_affaire'+cases[66:]+"_"+today2][0])
                        browser.quit()
                        try: 
                            browser.close()
                        except :
                            pass
                        time.sleep(30)
                        browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                        browser.implicitly_wait(30)
                        browser.get(str(cases))
                        time.sleep(0.1)
                        browser.get(str(cases))
                        time.sleep(10)
                        globals()['liste_affaire'+cases[66:]+"_"+today2]=[]
                        for titre in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/span"):
                            globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(titre.text))
                            df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                            df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

        #Scraping de l'onglet principal : 

        for a in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #liste.append(str(a.get_attribute('href')))

       # soup_affaires = BeautifulSoup(browser.page_source)
        #for a in soup_affaires.find_all('div',{'class':'article article-body'}):
            try:
                globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(a.text))
                df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

                if len(globals()['liste_affaire'+cases[66:]+"_"+today2])<=1 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][1])<50 or globals()['liste_affaire'+cases[66:]+"_"+today2][1]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][1]=='':
                    print("\nATTTENTION L'onglet principal n'a pas été scrapé !!!, le processus recommence dans 30 secondes\n")
                    #print(globals()['liste_affaire'+cases[66:]+"_"+today2][1])
                    globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0]
                    browser.quit()
                    try: 
                        browser.close()
                    except :
                        pass
                    time.sleep(30)
                    browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                    browser.implicitly_wait(30)
                    browser.get(str(cases))
                    time.sleep(0.1)
                    browser.get(str(cases))
                    time.sleep(2)
                    for a in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
                        globals()['liste_affaire'+cases[66:]+"_"+today2].insert(1, str(a.text))
                        df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                        df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
            except Exception as e: 
                print(e)
                print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
                browser.quit()
                try: 
                    browser.close()
                except :
                    pass

                time.sleep(300)
                browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                browser.implicitly_wait(30)
                browser.get(str(cases))
                time.sleep(10)
                browser.get(str(cases))
                time.sleep(10)
                globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0]
                for a in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #liste.append(str(a.get_attribute('href')))

       # soup_affaires = BeautifulSoup(browser.page_source)
        #for a in soup_affaires.find_all('div',{'class':'article article-body'}):
                    globals()['liste_affaire'+cases[66:]+"_"+today2].insert(1, str(a.text))
                    df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                    df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

                if len(globals()['liste_affaire'+cases[66:]+"_"+today2])<=1 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][1])<50 or globals()['liste_affaire'+cases[66:]+"_"+today2][1]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][1]=='':
                    print("\nATTTENTION L'onglet principal n'a pas été scrapé !!!, le processus recommence dans 30 secondes\n")
                    #print(globals()['liste_affaire'+cases[66:]+"_"+today2][1])
                    browser.quit()
                    try: 
                        browser.close()
                    except :
                        pass
                    globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0]
                    browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                    browser.implicitly_wait(30)
                    time.sleep(30)
                    browser.get(str(cases))
                    time.sleep(0.1)
                    browser.get(str(cases))
                    time.sleep(2)
                    for a in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
                        globals()['liste_affaire'+cases[66:]+"_"+today2].insert(1, str(a.text))
                        df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                        df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

       # Scraping de l'onglet Materials :
       # browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()
       # browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()


       # time.sleep(1)
       # soup_affaires2 = BeautifulSoup(browser.page_source)
       # for b in soup_affaires2.find_all('div',{'class':'tab-content cdtl'}):
       #   globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(b))
       #   df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
       #   df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)


        #Scraping de l'onglet Procedural Details :
        try:
            browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
            time.sleep(0.1)
            browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
            time.sleep(1)
        except Exception as e: 
            print(e)
            print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
            browser.quit()
            try: 
                browser.close()
            except :
                pass
            time.sleep(300)
            browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
            browser.implicitly_wait(30)
            browser.get(str(cases))
            time.sleep(10)
            browser.get(str(cases))
            time.sleep(10)
            browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
            time.sleep(0.1)
            browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
            time.sleep(1)

        #soup_affaires3 = BeautifulSoup(browser.page_source)
        for c in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #for c in soup_affaires3.find_all('div',{'class':'tab-content cdtl'}):
            try:
                globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(c.text))
                df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                time.sleep(0.1)
                if len(globals()['liste_affaire'+cases[66:]+"_"+today2])< 3 or (str(globals()['liste_affaire'+cases[66:]+"_"+today2][2]) != 'No References Available' and (len(globals()['liste_affaire'+cases[66:]+"_"+today2])< 2 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][2])<50 or globals()['liste_affaire'+cases[66:]+"_"+today2][2]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][2]=='')):
                    #print(globals()['liste_affaire'+cases[66:]+"_"+today2][2])
                    print("\nL'onglet 'Procedural Details' est anormalement vide, le processus recommence le scrap dans 30 secondes\n")
                    browser.quit()
                    try: 
                        browser.close()
                    except :
                        pass
                    time.sleep(30)
                    browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                    browser.implicitly_wait(30)
                    browser.get(str(cases))
                    time.sleep(0.1)
                    browser.get(str(cases))
                    time.sleep(2)
                    browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                    time.sleep(0.1)
                    browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                    time.sleep(2)
                    globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0:2]
                    for c in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #for c in soup_affaires3.find_all('div',{'class':'tab-content cdtl'}):
                        globals()['liste_affaire'+cases[66:]+"_"+today2].insert(2, str(c.text))
                        df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                        df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                        time.sleep(0.1)

            except Exception as e: 
                print(e)
                print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
                browser.quit()
                try: 
                    browser.close()
                except :
                    pass
                time.sleep(300)
                browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                browser.implicitly_wait(30)
                browser.get(str(cases))
                time.sleep(10)
                browser.get(str(cases))
                time.sleep(10)
                browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                time.sleep(0.1)
                browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                time.sleep(1)
                globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0:2]
                for c in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
                    globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(c.text))
                    df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                    df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                    time.sleep(0.1)
                    if len(globals()['liste_affaire'+cases[66:]+"_"+today2])<= 2 or (str(globals()['liste_affaire'+cases[66:]+"_"+today2][2]) != 'No References Available' and (len(globals()['liste_affaire'+cases[66:]+"_"+today2])< 2 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][2])<50 or globals()['liste_affaire'+cases[66:]+"_"+today2][2]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][2]=='')):
                        #print(globals()['liste_affaire'+cases[66:]+"_"+today2][2])
                        print("\nL'onglet 'Procedural Details' est anormalement vide, le processus recommence le scrap dans 30 secondes\n")
                        browser.quit()
                        try: 
                            browser.close()
                        except :
                            pass
                        browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                        browser.implicitly_wait(30)
                        time.sleep(30)
                        browser.get(str(cases))
                        time.sleep(0.1)
                        browser.get(str(cases))
                        time.sleep(2)
                        browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                        time.sleep(0.1)
                        browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                        time.sleep(2)
                        globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0:2]
                        for c in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #for c in soup_affaires3.find_all('div',{'class':'tab-content cdtl'}):
                            globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(c.text))
                            df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                            df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                            time.sleep(0.1)



        browser.close()


    # In[ ]:


    print("\nSCRAPING 2/3 REUSSI !")


    # In[ ]:


    browser.quit()
    try: 
        browser.close()
    except :
        pass


    # In[ ]:


    print("\n Patienter 2 minutes\n")


    # In[ ]:


    for i in tqdm(range(100)):
        time.sleep(1.20)


    # In[ ]:


    print('\n    1.3- Scraping 3/3 : \nSCRAPING DES AFFAIRES DE '+str((len(listenettoyee11)+len(listenettoyee12)))+' A '+str(len(listenettoyee2))+' : \n')


    # In[ ]:


    options = Options()
    options.add_argument("--no-sandbox")
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    options.add_argument("--disable-dev-shm-usage")
    prefs = {
        'profile.managed_default_content_settings.images': 2,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    }
    options.add_experimental_option('prefs', prefs)

    i=len(listenettoyee12)+len(listenettoyee11)-1
    for cases in tqdm(listenettoyee13):
        i=i+1
        try:

        #requete_affaires = requests.get(cases)
        #page_affaires = requete_affaires.content
        #soup_affaires = BeautifulSoup(page_affaires)

            browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
            globals()['liste_affaire'+cases[66:]+"_"+today2]=[]
            browser.implicitly_wait(30)
        #browser.execute_script("window.open('');")
        #Window_List = browser.window_handles
        #browser.switch_to_window(browser.window_handles[0])
            browser.get(str(cases))
            time.sleep(0.1)
            browser.get(str(cases))
            time.sleep(0.1)

        except Exception as e: 
            print(e)
            print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
            browser.quit()
            try: 
                browser.close()
            except :
                pass

            time.sleep(300)
            browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
            browser.implicitly_wait(30)
            browser.get(str(cases))
            time.sleep(10)
            browser.get(str(cases))
            time.sleep(10)


        #browser.find_element(by.linkText(str(cases))).sendKeys(Keys.chord(Keys.CONTROL,"t"))
        #time.sleep (2.5)
        #if i==200 or i==400 or i== 600 or i== 800:
         #   print("sleep")
          #  time.sleep (60)
        #Scrapping du titre :
        for titre in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/span"):
            try:
                globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(titre.text))
                df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                if len(globals()['liste_affaire'+cases[66:]+"_"+today2])==0 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][0])<25 or globals()['liste_affaire'+cases[66:]+"_"+today2][0]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][0]=='':
                    print("ATTTENTION Le titre n'a pas été scrapé !!!, le processus recommence dans 30 secondes")
                    #print(globals()['liste_affaire'+cases[66:]+"_"+today2])
                    browser.quit()
                    try: 
                        browser.close()
                    except :
                        pass
                    time.sleep(30)
                    browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                    browser.implicitly_wait(30)
                    browser.get(str(cases))
                    time.sleep(0.1)
                    browser.get(str(cases))
                    time.sleep(10)
                    globals()['liste_affaire'+cases[66:]+"_"+today2]=[]
                    for titre in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/span"):
                        globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(titre.text))
                        df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                        df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

            except Exception as e: 
                print(e)
                print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
                browser.quit()
                try: 
                    browser.close()
                except :
                    pass

                time.sleep(300)
                browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                browser.implicitly_wait(30)
                browser.get(str(cases))
                time.sleep(10)
                browser.get(str(cases))
                time.sleep(10)
                globals()['liste_affaire'+cases[66:]+"_"+today2]=[]
                for titre in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/span"):
                    globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(titre.text))
                    df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                    df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                    if len(globals()['liste_affaire'+cases[66:]+"_"+today2])==0 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][0])<25 or globals()['liste_affaire'+cases[66:]+"_"+today2][0]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][0]=='':
                        print("ATTTENTION Le titre n'a pas été scrapé !!!, le processus recommence dans 30 secondes")
                        #print(globals()['liste_affaire'+cases[66:]+"_"+today2][0])
                        browser.quit()
                        try: 
                            browser.close()
                        except :
                            pass
                        time.sleep(30)
                        browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                        browser.implicitly_wait(30)
                        browser.get(str(cases))
                        time.sleep(0.1)
                        browser.get(str(cases))
                        time.sleep(10)
                        globals()['liste_affaire'+cases[66:]+"_"+today2]=[]
                        for titre in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/span"):
                            globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(titre.text))
                            df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                            df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

        #Scraping de l'onglet principal : 

        for a in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #liste.append(str(a.get_attribute('href')))

       # soup_affaires = BeautifulSoup(browser.page_source)
        #for a in soup_affaires.find_all('div',{'class':'article article-body'}):
            try:
                globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(a.text))
                df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

                if len(globals()['liste_affaire'+cases[66:]+"_"+today2])<=1 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][1])<50 or globals()['liste_affaire'+cases[66:]+"_"+today2][1]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][1]=='':
                    print("\nATTTENTION L'onglet principal n'a pas été scrapé !!!, le processus recommence dans 30 secondes\n")
                    #print(globals()['liste_affaire'+cases[66:]+"_"+today2][1])
                    globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0]
                    browser.quit()
                    try: 
                        browser.close()
                    except :
                        pass
                    time.sleep(30)
                    browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                    browser.implicitly_wait(30)
                    browser.get(str(cases))
                    time.sleep(0.1)
                    browser.get(str(cases))
                    time.sleep(2)
                    for a in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
                        globals()['liste_affaire'+cases[66:]+"_"+today2].insert(1, str(a.text))
                        df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                        df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
            except Exception as e: 
                print(e)
                print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
                browser.quit()
                try: 
                    browser.close()
                except :
                    pass

                time.sleep(300)
                browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                browser.implicitly_wait(30)
                browser.get(str(cases))
                time.sleep(10)
                browser.get(str(cases))
                time.sleep(10)
                globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0]
                for a in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #liste.append(str(a.get_attribute('href')))

       # soup_affaires = BeautifulSoup(browser.page_source)
        #for a in soup_affaires.find_all('div',{'class':'article article-body'}):
                    globals()['liste_affaire'+cases[66:]+"_"+today2].insert(1, str(a.text))
                    df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                    df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

                if len(globals()['liste_affaire'+cases[66:]+"_"+today2])<=1 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][1])<50 or globals()['liste_affaire'+cases[66:]+"_"+today2][1]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][1]=='':
                    print("\nATTTENTION L'onglet principal n'a pas été scrapé !!!, le processus recommence dans 30 secondes\n")
                    #print(globals()['liste_affaire'+cases[66:]+"_"+today2][1])
                    browser.quit()
                    try: 
                        browser.close()
                    except :
                        pass
                    globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0]
                    browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                    browser.implicitly_wait(30)
                    time.sleep(30)
                    browser.get(str(cases))
                    time.sleep(0.1)
                    browser.get(str(cases))
                    time.sleep(2)
                    for a in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
                        globals()['liste_affaire'+cases[66:]+"_"+today2].insert(1, str(a.text))
                        df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                        df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)

       # Scraping de l'onglet Materials :
       # browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()
       # browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()


       # time.sleep(1)
       # soup_affaires2 = BeautifulSoup(browser.page_source)
       # for b in soup_affaires2.find_all('div',{'class':'tab-content cdtl'}):
       #   globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(b))
       #   df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
       #   df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)


        #Scraping de l'onglet Procedural Details :
        try:
            browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
            time.sleep(0.1)
            browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
            time.sleep(1)
        except Exception as e: 
            print(e)
            print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
            browser.quit()
            try: 
                browser.close()
            except :
                pass
            time.sleep(300)
            browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
            browser.implicitly_wait(30)
            browser.get(str(cases))
            time.sleep(10)
            browser.get(str(cases))
            time.sleep(10)
            browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
            time.sleep(0.1)
            browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
            time.sleep(1)

        #soup_affaires3 = BeautifulSoup(browser.page_source)
        for c in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #for c in soup_affaires3.find_all('div',{'class':'tab-content cdtl'}):
            try:
                globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(c.text))
                df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                time.sleep(0.1)
                if len(globals()['liste_affaire'+cases[66:]+"_"+today2])< 3 or (str(globals()['liste_affaire'+cases[66:]+"_"+today2][2]) != 'No References Available' and (len(globals()['liste_affaire'+cases[66:]+"_"+today2])< 2 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][2])<50 or globals()['liste_affaire'+cases[66:]+"_"+today2][2]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][2]=='')):
                    #print(globals()['liste_affaire'+cases[66:]+"_"+today2][2])
                    print("\nL'onglet 'Procedural Details' est anormalement vide, le processus recommence le scrap dans 30 secondes\n")
                    browser.quit()
                    try: 
                        browser.close()
                    except :
                        pass
                    time.sleep(30)
                    browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                    browser.implicitly_wait(30)
                    browser.get(str(cases))
                    time.sleep(0.1)
                    browser.get(str(cases))
                    time.sleep(2)
                    browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                    time.sleep(0.1)
                    browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                    time.sleep(2)
                    globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0:2]
                    for c in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #for c in soup_affaires3.find_all('div',{'class':'tab-content cdtl'}):
                        globals()['liste_affaire'+cases[66:]+"_"+today2].insert(2, str(c.text))
                        df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                        df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                        time.sleep(0.1)

            except Exception as e: 
                print(e)
                print('\n!!!!!!!!! ATTENTION probleme détecté, le processus recommence!!!!!!!!! Attendre 5 minutes\n')
                browser.quit()
                try: 
                    browser.close()
                except :
                    pass
                time.sleep(300)
                browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                browser.implicitly_wait(30)
                browser.get(str(cases))
                time.sleep(10)
                browser.get(str(cases))
                time.sleep(10)
                browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                time.sleep(0.1)
                browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                time.sleep(1)
                globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0:2]
                for c in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
                    globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(c.text))
                    df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                    df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                    time.sleep(0.1)
                    if len(globals()['liste_affaire'+cases[66:]+"_"+today2])<= 2 or (str(globals()['liste_affaire'+cases[66:]+"_"+today2][2]) != 'No References Available' and (len(globals()['liste_affaire'+cases[66:]+"_"+today2])< 2 or len(globals()['liste_affaire'+cases[66:]+"_"+today2][2])<50 or globals()['liste_affaire'+cases[66:]+"_"+today2][2]=='nan' or globals()['liste_affaire'+cases[66:]+"_"+today2][2]=='')):
                        #print(globals()['liste_affaire'+cases[66:]+"_"+today2][2])
                        print("\nL'onglet 'Procedural Details' est anormalement vide, le processus recommence le scrap dans 30 secondes\n")
                        browser.quit()
                        try: 
                            browser.close()
                        except :
                            pass
                        browser = webdriver.Chrome(options=options,executable_path=emplacement_driver_chrome)
                        browser.implicitly_wait(30)
                        time.sleep(30)
                        browser.get(str(cases))
                        time.sleep(0.1)
                        browser.get(str(cases))
                        time.sleep(2)
                        browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                        time.sleep(0.1)
                        browser.find_element_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/a").click()
                        time.sleep(2)
                        globals()['liste_affaire'+cases[66:]+"_"+today2]=globals()['liste_affaire'+cases[66:]+"_"+today2][0:2]
                        for c in browser.find_elements_by_xpath("/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/div[2]"):
        #for c in soup_affaires3.find_all('div',{'class':'tab-content cdtl'}):
                            globals()['liste_affaire'+cases[66:]+"_"+today2].append(str(c.text))
                            df = pd.DataFrame(globals()['liste_affaire'+cases[66:]+"_"+today2])
                            df.to_csv(emplacement_fichier_affaires+'/Affaire'+listenettoyee2[i][66:]+"_"+today2+'.csv', index=False)
                            time.sleep(0.1)



        browser.close()


    # In[ ]:


    print("\nSCRAPING 3/3 REUSSI !")


    # In[ ]:


    browser.quit()
    try: 
        browser.close()
    except :
        pass


    # In[ ]:


    print("\nPatienter 10 secondes\n")


    # In[ ]:


    for i in tqdm(range(100)):
        time.sleep(0.10)


    # b) Comparaison des affaires

    # In[ ]:


    print("\n  2- Comparaison des affaires :\n")


    # In[105]:


    import os
    dossier_affaires= os.listdir(emplacement_fichier_affaires)
    listetecsvaffaires=[]
    for csv in dossier_affaires:
      listetecsvaffaires.append(csv)


    # In[106]:


    #len(listetecsvaffaires)


    # In[107]:


    #len(listenettoyee2)


    # In[108]:


    listetecsvaffaires.sort()


    # In[109]:


    def listecsv_affaires_debut(x):
      chaine = str(x)
      pos1 = chaine.find('Affaire')
      pos2 = -19
      sousChaine = chaine[pos1:pos2]
      #print (sousChaine)
      return(sousChaine)


    # In[ ]:


    print('    2.1- Classement des affaires :\n')


    # In[110]:


    liste_affaire_double=[]
    for affaire1 in tqdm(listetecsvaffaires):
      i=0    
      for affaire2 in listetecsvaffaires:

        if listecsv_affaires_debut(listetecsvaffaires[listetecsvaffaires.index(affaire1)])==listecsv_affaires_debut(listetecsvaffaires[listetecsvaffaires.index(affaire2)]):
          i=i+1
          if i>1:
            liste_affaire_double.append(affaire1)
            liste_affaire_double.append(affaire2)


    # In[119]:


    liste_affaire_double=list(set(liste_affaire_double))


    # In[120]:


    liste_affaire_double.sort(reverse=True)


    # In[121]:


    #listecsv_affaires_debut(liste_affaire_double[6])


    # In[122]:


    i=0
    for affaire_en_double in liste_affaire_double:
      i=i+1

      globals()['liste_double'+str(i)]=[]
      for affaire_en_double2 in liste_affaire_double:
        if affaire_en_double[0:-19]==affaire_en_double2[0:-19]:
          globals()['liste_double'+str(i)].append(affaire_en_double2)


    # In[123]:


    #liste_double1


    # In[124]:


    def Diff(li1, li2): 
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
        return li_dif 


    # In[125]:


    #liste_affaire_double


    # In[ ]:


    print("\n  3- Création du message de notification s'il y a des modifications dans les affaires :\n")


    # In[126]:


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
          nom_affaire=str(dernier_csvliste_affaire[0])
          chaine=str(globals()['liste_double'+str(j)][0])
          pos1 = len('Affaire')+chaine.find('Affaire')
          pos2 = chaine.find('_')
          print ("\nModifications apportées à l'affaire : "+globals()['liste_double'+str(j)][0][pos1:-20])
          #for y in modificationsliste :
            #modificationsliste = [x for x in y if str(x) != 'nan']
          modificationsliste=['\n'.join(sub_list) for sub_list in modificationsliste]
          #print(modificationsliste)
          ancien =modificationsliste[0:int((len(modificationsliste)/2))]
          nouveau=modificationsliste[int((len(modificationsliste)/2)):]
          #liste_mail=[]
          #for i in range(0,len(modificationsliste)):
           # liste_mail.append(adresse_modification(modificationsliste[i]))
          #sauvegarde message2
          #  i=i+1
          time.sleep(2)

        #recuperer les phrases qui different entre ancien et nouveau
          ancien2=''
          for l in range(0,len(ancien)):
              ancien2=ancien2+ancien[l]
          indexancien=([(n.start(0)) for n in re.finditer('\n', ancien2)])
          indexancien.insert(0,0)
          indexancien.append(len(ancien2))

          nouveau2=''
          for m in range(0,len(nouveau)):
              nouveau2=nouveau2+nouveau[m]
          indexnouveau=([(o.start(0)) for o in re.finditer('\n', nouveau2)])
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

          #ancienneversion=message_Diff[0:int((len(message_Diff)/2))]
          #nouvelleversion=message_Diff[int((len(message_Diff)/2)):]

        #Création du message
          globals()['liste_double'+str(j)][0]=globals()['liste_double'+str(j)][0].replace('_','/')

          message2.append("* Modifications apportées à l'affaire : "+globals()['liste_double'+str(j)][0][pos1:-20] +"\n- Lien : https://icsid.worldbank.org/en/Pages/cases/casedetail.aspx?CaseNo="+globals()['liste_double'+str(j)][0][pos1:-20]+ " \n- Nom de l'affaire : "+str(nom_affaire)+" \n\nVoici ce qui a été modifié, ajouté ou supprimé : "+str(message_Diff)+' \nNotification créée le '+today)

          print('Modifications sauvegardées dans la liste message2\n')

    if k==0 :
      print(' \nPas de modification dans les affaires, pas de notification créée\n')
      message2=[]



    # In[127]:


    message2=list(set(message2))


    # c) Nettoyage

    # In[ ]:


    print("\n  4- Nettoyage du message de notification :\n")


    # In[128]:


    for i in range(0, len(message2)):
        message2[i]=message2[i].replace('[','\n')
        message2[i]=message2[i].replace(']','')
        message2[i]=message2[i].replace("'Subject of Dispute:", "\nONGLET PRINCIPAL :\nSubject of Dispute:")
        message2[i]=message2[i].replace("', '(a) Original Proceeding\\nDate\\nDevelopment", "\n\nONGLET PROCEDURAL DETAILS :")
        message2[i]=message2[i].replace('\\n','\n')
        message2[i]=message2[i].replace("', '",'\n')


    # In[129]:


    #message2


    # In[130]:


    browser.quit()
    try: 
        browser.close()
    except :
        pass


    # In[ ]:


    print(" Patienter 10 secondes\n")


    # In[131]:


    for i in tqdm(range(100)):
        time.sleep(0.10)


    # III. Nettoyage des dossiers

    # In[ ]:


    print('\nIII. NETTOYAGE DU DOSSIER : '+emplacement_fichier_affaires)


    # In[99]:


    import os
    dossier_affaires= os.listdir(emplacement_fichier_affaires)

    for csv in dossier_affaires:
      if csv[-19:-4]!= today2:
        #os.rename(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
        shutil.move(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
        #os.replace(emplacement_fichier_affaires+"/"+str(csv), emplacement_ancien_csv+"/"+str(csv))
    print("\nAnciens CSV déplacés vers le dossier : "+emplacement_ancien_csv)


    # IV. Envoi du message

    # In[ ]:


    print('\nIV. ENVOI DU MESSAGE SI DES MODIFICATIONS ONT ETE APPORTEES :\n')


    # In[132]:


    message3=message1+message2


    # In[133]:


    def send_mail(message):
      pw=password
      pw
      adresse=adresse_envoi
      adresse
      login
      #destinataire=destinataire
      destinataire
      sujet="Modification(s) apportée(s) à la page ICSID.wordbank.org"
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
      #mailserver.ehlo() #activer si besoin
      mailserver.login(login, pw)
      #mailserver.set_debuglevel(1) #activer si besoin
      mailserver.sendmail(adresse,destinataire, msg.as_string())
      print("\n Message envoyé !")
      mailserver.quit()


    # In[134]:


    message1string=""
    for i in range(0,len(message1)):
      message1string=message1string+'\n\n'+str(message1[i])

    message2string=""
    for i in range(0,len(message2)):
      message2string=message2string+'\n\n'+str(message2[i])


    # In[135]:


    if len(message3)>0:

      send_mail(message1string+"\n\n********************"+message2string)
    else:
      print('\nAucune modification de la page, aucun mail envoyé !\n')


    # In[ ]:


    #message2string


    # In[ ]:


    today= str(datetime.now(pytz.timezone("Europe/Paris")).strftime("%H:%M:%S LE %d/%m/%Y"))
    print('\nFIN DU PROGRAMME A '+today)


    # In[ ]:


    #Erreurs rencontrées lors de la conception du code :


        #NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"/html/body/form/div[12]/div/div/div[4]/div[2]/div[2]/div[1]/div/div[4]/div[2]/div/div[1]/div/div/div/div[1]/div/ul/li[2]/a"}
     #(Session info: chrome=77.0.3865.90)

        #OSError: [Errno 12] Cannot allocate memory

        #ElementClickInterceptedException: Message: element click intercepted: Element <a class="tabsctionCclss" data-toggle="tab" href="#sectionc" ng-click="getproceduredetails()" aria-expanded="true">...</a> is not clickable at point (840, 272). Other element would receive the click: <div class="casedetltile">...</div>
     #(Session info: headless chrome=77.0.3865.90)

        #TimeoutException: Message: timeout
     #(Session info: headless chrome=77.0.3865.90)

        #MaxRetryError: HTTPConnectionPool(host='127.0.0.1', port=49215): Max retries exceeded with url: /session/dd250767f8bc7c7d215a3897e62249b7/window (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7facdb1a9908>: Failed to establish a new connection: [Errno 111] Connection refused'))
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
        sujet="La page https://icsid.worldbank.org n'a pas pu être scrapée, il y a une erreur !"
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

    send_mail('Erreur lors du scraping de la page ISCID. Veuillez verifier le programme \n'+e)




# In[ ]:




