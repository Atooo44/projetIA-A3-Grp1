def main():

  import sys
  import pandas as pd
  from sklearn.cluster import KMeans
  import json

  from sklearn.svm import SVC
  from sklearn.ensemble import RandomForestClassifier
  from sklearn.neural_network import MLPClassifier

  from joblib import dump, load


  # Test des arguments
  if sys.argv[2] != "SVM" and sys.argv[2] != "RF" and sys.argv[2] != "MLP":
      print('\nERROR : Le deuxième argument est la méthode de classification à utiliser parmi SVM, RF ou MLP\n')
      exit()

  if len(sys.argv) < 3 or len(sys.argv) > 3:
      print('\nERRROR:')
      print('Le premier argument est le nom d\'un fichier csv local qui répertorie les informations de l\'accident')
      print('Le deuxième argument est la méthode de classification à utiliser parmi SVM, RF ou MLP')
      exit()

  methode = sys.argv[2]
  # Récupération des arguments passés en commande
  data = pd.read_csv(sys.argv[1], sep=";", index_col=False)
  # Boucle pour lire chaque donnée du csv avec le bon indice
  #for i in data:
  #    print(i)
  #    for j in data[i]:
  #        print(j)


  if methode == "SVM":
      print("SVM method")
      svm = load('svm.joblib')
      gravite = svm.predict(data)

  if methode == "RF":
      print("RF method")
      rf = load('rf.joblib')
      gravite = rf.predict(data)

  if methode == "MLP":
      print("MLP method")
      mlp = load('mlp.joblib')
      gravite = mlp.predict(data)

  # Écriture du JSON
  dictionary = {
      "methode": methode,
      "informations": [
          {
              "desc_grav": data.descr_grav[0],
              "descr_athmo": data.descr_athmo[0],
              "num_acc": data.Num_Acc[0],
              "num_veh": data.num_veh[0],
              "id_usa": data.id_usa[0],
              "date": data.date[0],
              "ville": data.ville[0],
              "id_code_insee": data.id_code_insee[0],
              "latitude": data.latitude[0],
              "longitude": data.longitude[0],
              "descr_cat_veh": data.descr_cat_veh[0],
              "descr_agglo": data.descr_agglo[0],
              "descr_lum": data.descr_lum[0],
              "descr_etat_surf": data.descr_etat_surf[0],
              "description_intersection": data.description_intersection[0],
              "annee": data.an_nais[0],
              "age": data.age[0],
              "place": data.place[0],
              "descr_dispo_secu": data.descr_dispo_secu[0],
              "descr_motif_traj": data.descr_motif_traj[0],
              "descr_type_col": data.descr_type_col[0],
              "departement": data.departement[0]
          }
      ],
      "gravite": gravite
  }


  json_object = json.dumps(dictionary, indent=4)
  return json_object

main()