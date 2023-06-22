import sys
import pandas as pd
import json


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score


"""
Fonction qui va mettre à jour et préparer le fichier CSV
"""
def update_csv(data):

    enc = OrdinalEncoder()

    data_temp = data[["num_veh"]]
    data.num_veh = enc.fit_transform(data_temp)

    data_temp = data[["ville"]]
    data.ville = enc.fit_transform(data_temp)
    timestamps = pd.to_datetime(data['date']).astype(int) // 10**9
    data['date'] = timestamps

    return data

def main():
    # Test des arguments
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print('\nERRROR:')
        print('Le premier est le nom d\'un fichier csv local qui répertorie les informations de l\'accident')
        print('Le deuxième argument est le nom d\'un fichier csv local qui contient la liste de tous les accidents')
        exit()

    # Récupération des arguments passés en commande
    data_info = pd.read_csv(sys.argv[1], sep=",")
    data_liste = pd.read_csv(sys.argv[2], sep=",")

    # Boucle pour lire chaque donnée du csv avec le bon indice
    """
    print("data_info")
    for i in data_info:
        for j in data_info[i]:
            print(i, " = ",j)
    """


    """
    print("\ndata_liste")
    for i in data_liste:
        for j in data_liste[i]:
            print(i, " = ", j)
    """


    # FAIRE PREDICTION KNN
    #print(type(data_liste))
    data_info = data_info[['descr_cat_veh', 'descr_agglo', 'descr_etat_surf', 'description_intersection', 'descr_dispo_secu', 'descr_type_col']]
    X = data_liste[['descr_cat_veh', 'descr_agglo', 'descr_etat_surf', 'description_intersection', 'descr_dispo_secu', 'descr_type_col']]
    y = data_liste['descr_grav']  # Adaptation de l'étiquette (gravité des accidents)

    k = 15
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X, y)

    # Create a list to store the results for each row
    results = []

    # Get the feature names
    feature_names = X.columns

    # Create a new DataFrame with feature names for prediction
    prediction_data = pd.DataFrame(data_info.values, columns=feature_names)

    # Make predictions for the prediction data
    y_pred = knn.predict(prediction_data)

    # Iterate over each row in data_info
    for index, row in prediction_data.iterrows():
        # Store the prediction result
        result = {
            "informations": {
                feature_names[i]: int(row[i]) for i in range(len(feature_names))
            },
            "gravite": int(y_pred[index])  # Set the predicted accident gravity
        }
        results.append(result)

    # Writing the JSON to a file
    json_object = json.dumps(results, indent=4)
    print(results)
    return json_object


main()
