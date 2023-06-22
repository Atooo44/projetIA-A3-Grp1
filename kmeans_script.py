import sys
import pandas as pd
from sklearn.cluster import KMeans
import json

# Test des arguments
if len(sys.argv) < 4 or len(sys.argv) > 4:
    print('\nERRROR:')
    print('Le premier argument est la latitude (float)')
    print('Le deuxième argument est la longitude(float)')
    print('Le troisième argument est le nom d\'un fichier csv local qui répertorie les centroides tel que :')
    print('\tlatitude;longitude\n\t45.97835662;0.716667\n\t48.3;-1.8\n\t...\n\n')
    exit()


def main(latitude, longitude, filename):
    # Récupération des varibles entrées en argument
    lat = latitude
    lon = longitude
    lat_lon = []
    final_array = []
    final_array.append(lat_lon)
    lat_lon.append(lat)
    lat_lon.append(lon)
    centroides = []

    # Lecture du fichier csv de centroides
    data = pd.read_csv(filename, sep=";")
    for i in range(0, len(data)):
        centre = []
        centre.append(data.latitude[i])
        centre.append(data.longitude[i])
        centroides.append(centre)

    # Prédiction du cluster avec KMeans
    kmeans = KMeans(n_clusters=len(data), n_init='auto').fit(centroides)
    pred = kmeans.predict(final_array)

    # Écriture du JSON
    dictionary = {
        "accident": [
            {
                "latitude": lat,
                "longitude": lon
            }
        ],
        "cluster": [
            {
                "latitude": kmeans.cluster_centers_[pred][0][0],
                "longitude": kmeans.cluster_centers_[pred][0][1]
            }
        ]
    }

    # Écriture du JSON dasn un fichier
    json_object = json.dumps(dictionary, indent=4)
    return json_object


main(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3])
