# Stage
[Télécharger tout le projet :inbox_tray:](https://github.com/pzim-devdata/DATA-developer/releases/download/V1.0.0/work-experiencer.zip)
## Voici les 3 programmes effectués durant le stage :

- [scrape-iscid-mastez :blue_book:](https://github.com/pzim-devdata/DATA-developer/tree/master/work%20experience/scrape-icsid-master)
- [scrape-pca-master :blue_book:](https://github.com/pzim-devdata/DATA-developer/tree/master/work%20experience/scrape-pca-master)
- [scrape-unctad-master :blue_book:](https://github.com/pzim-devdata/DATA-developer/tree/master/work%20experience/scrape-unctad-master)


Il s'agit de scraper un site Internet avec BeautifullSoup, de reperer s'il a été modifié à des endroits spécifiques, de recenser ces modifications grâce à des sauvegardes en CSV et de mettre en forme ces modifications afin de les notifier par mail.

Il s'agit aussi de scraper des pages en Javascript et pour cela j'ai utilisé Selenium. Il a aussi fallu controler le scraping car des problemes de connexions peuvent alterer les données. Il faut donc detecter les données corrompues et relancer le processus de collecte automatiquement. 

A la fin du programme, un processus de nettoyage des dossiers est lancé afin qu'il n'y ai pas de trie à effectuer avec des anciens CSV, ce qui évite de perdre un temps considerable si des fichiers s'accumulent lors de la comparaison des CSV. Le dossiers sont donc auto-nettoyés et le programme ne s'altere pas avec le temps.

Trois sites ont été scrapés : PCA, ISCID et UNCTAD. 

Ces programmes ont été effectués en trois semaines.

Vous pouvez télécharger les programmes :
- [scrape-icsid-master.zip :inbox_tray:](https://github.com/pzim-devdata/DATA-developer/releases/download/V1.0.0/scrape-icsid-master.zip)
- [scrape-pca-master.zip :inbox_tray:](https://github.com/pzim-devdata/DATA-developer/releases/download/V1.0.0/scrape-pca-master.zip)
- [scrape-unctad-master.zip :inbox_tray:](https://github.com/pzim-devdata/DATA-developer/releases/download/V1.0.0/scrape-unctad-master.zip)

La structure des dossiers est deja créée, il faut juste lancer le fichier Python. Lisez les Readme dans les fichiers zip pour plus de précisions.
