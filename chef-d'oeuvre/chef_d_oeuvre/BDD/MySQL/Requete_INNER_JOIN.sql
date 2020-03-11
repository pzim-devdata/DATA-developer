use IDF;
SELECT Villes.Ville, Villes.Code_postal,Coordonnees_geo.Latitude,Coordonnees_geo.Longitude,  Temps_voiture_pointe.Temps AS Temps_voiture_heure_de_pointe,Temps_voiture.Temps AS Temps_voiture_normal, Temps_velo.Temps AS Temps_velo, Temps_transport.Temps AS Temps_transport, Distance_voiture_pointe.Distance AS Distance_voiture_pointe, Distance_voiture.Distance AS Distance_voiture_normal, Distance_velo.Distance AS Distance_velo from Villes
INNER JOIN Temps_voiture_pointe
ON Villes.Ville = Temps_voiture_pointe.Ville
INNER JOIN Temps_voiture
ON Villes.Ville = Temps_voiture.Ville
INNER JOIN Temps_velo
ON Villes.Ville = Temps_velo.Ville
INNER JOIN Temps_transport
ON Villes.Ville = Temps_transport.Ville
INNER JOIN Distance_voiture_pointe
ON Villes.Ville = Distance_voiture_pointe.Ville
INNER JOIN Distance_voiture
ON Villes.Ville = Distance_voiture.Ville
INNER JOIN Distance_velo
ON Villes.Ville = Distance_velo.Ville
INNER JOIN Coordonnees_geo
ON Villes.Ville = Coordonnees_geo.Ville
