Scrape project for data Unctad https://investmentpolicy.unctad.org/country-navigator

Analyse :

- Sommaire (liste des pays)
- Ajouts de documents dans la liste des pays

BeautifullSoup a été utilisé.
Pour fonctionner il faut simplement télécharger le projet en format zip, le décomprésser et le lancer dans le terminal avec la commande "```python Unctad_scraping.py```".

Il faut aussi modifier le fichier python afin d'y entrer les paramétres SMTP. Les dossiers sont deja créés.

Par ailleurs, vérifier que le swapfile est bien à 0B used à la fin de l'execution du code:
Pour verifier la taille du swap entrez cette commande dans le terminal : sudo swapon --show