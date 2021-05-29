import json
import csv

# Ce script python a été réalisé par Axelle Lecroq et Léa Périssier 
# afin de créer un dataset pouvant servir à visualiser le nombre de naissance
# par quart de siècle.

# Ce script a été utilisé au sein d'un jupyter notebook.

def writeJSON(file, data):
        with open(file, mode='w') as f:
            json.dump(data, f)

def getJSON(path):
   with open(path, encoding="iso-8859-15" ) as data_file:
       data = json.load(data_file)
   return data;

def is_int(date : str):
    letter =  "abcdefghijklmnopqrstuvwxyz"
    
    for i in letter:
        if i in date:
            return False
    return True

leonore = getJSON("data/leonore.json")
dates = {}

for i in leonore :
    year = i["null"][4][:4]
    try :
        if is_int(year) == False :
            pass
        elif year not in dates.keys():
            dates[year] = 1
        else : 
            dates[year] +=1
    except: print(i)

writeJSON("dates_leonore.json", dates)

qrt_siecle = {"1700-1724" : 0, "1725-1749" : 0, "1750-1774": 0, "1775-1799": 0 ,
             "1800-1824" : 0, "1825-1849" : 0, "1850-1874": 0, "1875-1899": 0 ,
             "1900-1924" : 0, "1925-1949" : 0, "1950-1974": 0, "1975-1999": 0 ,
             "2000-2024" : 0}

leo = getJSON("dates_leonore.json")
for i in leo.keys():
    i= int(i)
    if 1700 < i and i< 1724 :
        qrt_siecle["1700-1724"] = qrt_siecle["1700-1724"] + leo[str(i)]
    elif 1725 < i and i < 1749 :
        qrt_siecle["1725-1749"] = qrt_siecle["1725-1749"] + leo[str(i)]
    elif 1750 < i and i < 1774 :
        qrt_siecle["1750-1774"] = qrt_siecle["1750-1774"] + leo[str(i)]
    elif 1775 < i and i < 1799 :
        qrt_siecle["1775-1799"] = qrt_siecle["1775-1799"] + leo[str(i)]
    elif 1800 < i and i < 1824 :
        qrt_siecle["1800-1824"] = qrt_siecle["1800-1824"] + leo[str(i)]
    elif 1825 < i and i < 1849 :
        qrt_siecle["1825-1849"] = qrt_siecle["1825-1849"] + leo[str(i)]
    elif 1850 < i and i < 1874 :
        qrt_siecle["1850-1874"] = qrt_siecle["1850-1874"] + leo[str(i)]
    elif 1875 < i and i < 1899 :
        qrt_siecle["1875-1899"] = qrt_siecle["1875-1899"] + leo[str(i)]
    elif 1900 < i and i < 1924 :
        qrt_siecle["1900-1924"] = qrt_siecle["1900-1924"] + leo[str(i)]
    elif 1925 < i and i < 1949 :
        qrt_siecle["1925-1949"] = qrt_siecle["1925-1949"] + leo[str(i)]
    elif 1950 < i and i < 1974 :
        qrt_siecle["1950-1974"] = qrt_siecle["1950-1974"] + leo[str(i)]
    elif 1975 < i and i < 1999 :
        qrt_siecle["1975-1999"] = qrt_siecle["1975-1999"] + leo[str(i)]
    elif 2000 < i and i < 2024 :
        qrt_siecle["2000-2024"] = qrt_siecle["2000-2024"] + leo[str(i)]

writeJSON("qrtsiecle_leonore.json", qrt_siecle)