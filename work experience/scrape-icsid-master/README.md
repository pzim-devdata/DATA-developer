# scrape-icsid

Scrape project for data ICSID http://icsid.worldbank.org/.

Analyse :
- Sommaire (liste des affaires)
- Modifications dans les affaires

Selenium a été utilisé.

Pour fonctionner il faut simplement télécharger le projet en format zip, le décomprésser et le lancer dans le terminal avec la commande "```python ISCID_scraping.py```". 
Il faut aussi modifier le fichier python afin d'y entrer les paramétres SMTP. Les dossiers sont deja créés.

Le driver Chrome 77 (ChromeDriver 77.0.3865.40) (https://chromedriver.chromium.org/downloads ) a été utilisé. 
Il faut le mettre dans le même dossier que le fichier Python (emplacement_driver_chrome) et le systéme d'exploitation utilisé est Linux 64 bit Ubuntu.

Le navigateur Chrome (Version 77.0.3865.90 (Build officiel) (64 bits)) a les options par défaut.
Pour l'installer saisir cette commande dans le terminal : 
```wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb```

ATTENTION :
- Chromedriver doit etre dans le même dossier que le fichier python (decompressez-le)
- Chromedriver et le navigateur Chrome doivent avoir la même version (ici 77.0.3865)

Par ailleurs, vérifier que le swapfile est bien à 0B used à la fin de l'execution du code:
Pour verifier la taille du swap entrez cette commande dans le terminal : sudo swapon --show 

