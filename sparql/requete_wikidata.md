# Requêtes SPARQL utilisées sur le SPARQL Endpoint de Wikidata
### Requête de base qui permet de récupérer toutes les informations nécessaires d'un coup
```SQL
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX ps: <http://www.wikidata.org/prop/statement/>
PREFIX pq: <http://www.wikidata.org/prop/qualifier/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bd: <http://www.bigdata.com/rdf#>

SELECT ?nom ?leonoreid ?bnfid ?datenaissance ?ville ?coordinatelieuN ?datedeces ?villedc ?coordinatelieudc ?diplome (group_concat(DISTINCT ?metier;separator=" | ") as ?professions)
WHERE {
  ?person wdt:P640 ?leonoreid;
          wdt:P1559 ?nom.
          
  OPTIONAL{?person wdt:P106 ?occupation.
           ?occupation rdfs:label ?metier.
    filter (lang(?metier)="fr")}
  
  OPTIONAL{?person wdt:P268 ?bnfid.}
  
  OPTIONAL{?person wdt:P569 ?datenaissance.
           ?person wdt:P19 ?lieuNaissance.
           ?lieuNaissance wdt:P625 ?coordinatelieuN.
           ?lieuNaissance rdfs:label ?ville.
   filter (lang(?ville)="fr")}
  
  OPTIONAL{?person wdt:P570 ?datedeces.
           ?person wdt:P20 ?lieudeces.
           ?lieudeces wdt:P625 ?coordinatelieudc.
           ?lieudeces rdfs:label ?villedc.
    filter (lang(?villedc)="fr")}
  
  OPTIONAL{?person wdt:P512 ?niveauacademique.
           ?niveauacademique rdfs:label ?diplome.
          filter (lang(?diplome)="fr")}
}
GROUP BY ?nom ?leonoreid ?bnfid ?datenaissance ?ville ?coordinatelieuN ?datedeces ?villedc ?coordinatelieudc ?diplome
```
Malheureusement le temps d'exécution de cette requête est bien trop long. Nous avons donc décidé de diviser cette large requête en requête plus par thématique afin pour résoudre pb du temps d'exécution trop long. Des jointures de tous les sets de données récupérés ont ensuite été effectuées.

### Requête pour faire les URI data bnf 
Une concaténation a été utilisée en raison de l’existence de plusieurs identifiants BnF pour un seul récipiendaire : `(group_concat(DISTINCT ?bnfid;separator=" |")`.

```SQL
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX ps: <http://www.wikidata.org/prop/statement/>
PREFIX pq: <http://www.wikidata.org/prop/qualifier/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bd: <http://www.bigdata.com/rdf#>

SELECT ?leonoreid  (group_concat(DISTINCT ?bnfid;separator=" |") as ?bnfids)
WHERE {
  ?person wdt:P640 ?leonoreid;
          wdt:P268 ?bnfid.}

GROUP BY ?leonoreid
```

### Requête pour récupérer les diplômes et les professions
Une concaténation a été utilisée du fait de la présence de plusieurs professions et diplômes pour certains récipiendaires.

```SQL
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX ps: <http://www.wikidata.org/prop/statement/>
PREFIX pq: <http://www.wikidata.org/prop/qualifier/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bd: <http://www.bigdata.com/rdf#>

SELECT ?nom ?leonoreid(group_concat(DISTINCT ?diplome;separator=" | ") as ?diplomes) (group_concat(DISTINCT ?metier;separator=" | ") as ?professions)
WHERE {
  ?person wdt:P640 ?leonoreid;
          wdt:P1559 ?nom.
          
 OPTIONAL{?person wdt:P106 ?occupation.
           ?occupation rdfs:label ?metier.
    filter (lang(?metier)="fr")}
  
  OPTIONAL{?person wdt:P512 ?niveauacademique.
           ?niveauacademique rdfs:label ?diplome.
          filter (lang(?diplome)="fr")}
}

GROUP BY ?nom ?leonoreid
```

### Requête pour récupérer les dates, lieux de naissance et de décès et leur géolocalisation
```SQL
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX ps: <http://www.wikidata.org/prop/statement/>
PREFIX pq: <http://www.wikidata.org/prop/qualifier/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX bd: <http://www.bigdata.com/rdf#>

SELECT ?nom ?leonoreid ?datenaissance ?ville ?coordinatelieuN ?datedeces ?villedc ?coordinatelieudc
WHERE {
  ?person wdt:P640 ?leonoreid;
          wdt:P1559 ?nom.
  
  OPTIONAL{?person wdt:P569 ?datenaissance.
           ?person wdt:P19 ?lieuNaissance.
           ?lieuNaissance wdt:P625 ?coordinatelieuN.
           ?lieuNaissance rdfs:label ?ville.
   filter (lang(?ville)="fr")}
  
  OPTIONAL{?person wdt:P570 ?datedeces.
           ?person wdt:P20 ?lieudeces.
           ?lieudeces wdt:P625 ?coordinatelieudc.
           ?lieudeces rdfs:label ?villedc.
    filter (lang(?villedc)="fr")}
}
```

### Requêtes pour les villes et leur géolocalisation
#### Les communes tunisiennes 
Nous avons pris l'exemple de la Tunisie pour présenter la requête effectuée afin de récupérer les villes et les coordonnées géographiques de ces dernières pour un pays mais cette même requête a également été faite pour les États-Unis, le Vietnam, le Maroc, l'Algérie.

```SQL
SELECT DISTINCT ?pays ?ville (group_concat(DISTINCT ?coordonnees;separator=" | ") as ?coordonnesgroup)
WHERE {
       ?city wdt:P17 wd:Q948;
             wdt:P31/wdt:P279* wd:Q41067667;
             wdt:P625 ?coordonnees;
             rdfs:label ?ville.
            filter (lang(?ville)="fr")
  wd:Q948 rdfs:label ?pays.
  filter (lang(?pays)="fr")
}
GROUP BY ?ville ?pays
```
#### Pour les capitales mondiales
```SQL
SELECT DISTINCT ?pays ?capitale ?coordonnees
WHERE { 
       ?city wdt:P31 wd:Q5119;
             wdt:P17 ?payscode;
             rdfs:label ?capitale.
             filter (lang(?capitale)="fr")
         ?city wdt:P625 ?coordonnees.
        ?payscode rdfs:label ?pays.
           filter (lang(?pays)="fr")
}
```