import pandas as pd
import numpy as np
import sys

def matrix_to_dataframe(work_matrix, input_df):
    """
    Renvoie la matrice des heures de travail au format pandas Dataframe.
    """
    # Définition des heures de travail valides (7h-23h)
    hours_range = range(7, 24)
    # On prend toutes les colonnes sauf 'Nom' (chaque jour).
    days = input_df.columns[1:]
    employee_names = input_df['Nom'].to_numpy()

    # Convertissement de la matrice 3D en une matrice 2D.
    flat_matrix = work_matrix.reshape(-1, work_matrix.shape[2])  # Flatten the first two dimensions
    df = pd.DataFrame(flat_matrix, columns=days)

    # Création d'un tableau de toutes les combinaisons possibles entre les noms des employés et les heures dans hours_range
    employee_hours = np.array(np.meshgrid(employee_names, hours_range)).T.reshape(-1, 2)

    # Ajout de ces combinaisons au dataframe
    df['Nom'] = employee_hours[:, 0]
    df['Horaires'] = employee_hours[:, 1].astype(int)

    # Ajustement de l'ordre des colonnes pour qu'elles correspondent à l'output attendu.
    df = df[['Nom', 'Horaires'] + list(days)] 

    return df

def parse_work_hours(work_hours_str):
    """
    Parsing du texte indiquant les heures de travail.
    Renvoie la liste de tuples représentant les intervals de temps de travail lorsque l'employé travaille.
    Renvoie une liste vide quand l'employé est en repos ou que la valeur d'entrée est invalide.
    """
    # On passe la chaine de caractères en minuscule afin d'éviter les erreurs de syntaxe (exemple : H -> h).
    work_hours_str = work_hours_str.lower()
    if work_hours_str == 'repos':
        return []
    try:
        intervals = work_hours_str.replace(' ', '').split('h')[:-1]
        return [(int(intervals[i]), int(intervals[i+1])) for i in range(0, len(intervals)-1, 2)]
    except ValueError:
        return []

def create_preprocessed_schedule(input_df):
    """
    Preprocessing du planning avec un parsing du texte indiquant les heures de travail pour chaque employé à chaque jour.
    Faire ce processing en amont, permet de diviser le nombre de lancements de la fonction de parsing par 17 (nombre de créneaux horaires) 
    Renvoie un dictionnaire avec comme clés : employé - jour et comme valeurs : la liste des créneaux horaires.
    """
    preprocessed_schedule = {}
    for employee_idx, (employee, work_hours) in enumerate(input_df.iterrows()):
        # On parcours toutes les colonnes sauf 'Nom' (chaque jour) et on applique le parsing.
        for day in input_df.columns[1:]:
            preprocessed_schedule[(employee_idx, day)] = parse_work_hours(work_hours[day])
    return preprocessed_schedule

def create_work_schedule_matrix(input_file_name):
    try:
        # Chargement du dataframe des données d'entrée à partir du fichier Excel du sujet
        input_df = pd.read_excel(input_file_name, sheet_name='Input')
    except Exception as err:
        print('The input Excel file should contain a sheet named \'Input\'')
        raise
    # Preprocessing des heures de travail
    preprocessed_schedule = create_preprocessed_schedule(input_df)

    # Définition des heures de travail valides (7h-23h)
    hours_range = range(7, 24)

    # Initialisation de la matrice (3 dimensions : Employés x Heures x Jours) à 0.
    work_matrix = np.zeros((len(input_df), len(hours_range), len(input_df.columns) - 1), dtype=int)

    # Remplissage de la matrice avec les données preprocessées plus haut
    for (employee_idx, day), intervals in preprocessed_schedule.items():
        day_idx = input_df.columns.get_loc(day) - 1
        for start, end in intervals:
            work_matrix[employee_idx, start-7:end-7, day_idx] = 1

    output_df = matrix_to_dataframe(work_matrix, input_df)
    print('Your matrix has been saved in the \'output.xlsx\' file in this directory, feel free to browse it')
    output_df.to_excel('output.xlsx', index=False)
    return output_df

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]
        create_work_schedule_matrix(input_file_name)
    else:
        print("Please provide the path to the input Excel file.")
        print("Usage: python p2.py path_to_input_file.xlsx")