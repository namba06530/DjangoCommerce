# --------------------------------------------------------------------------- #
#
# script python pour la génération des tables de la base de données
# et insertion des jeux de données
#
# simplifie les modifications fréquentes nécessaire lors de la phase de
# conception, permet de rejouer fréquemment une reconstruction complète
# des éléments, en mettant à jour seulement les instruction SQL qui
# ont changées.
#
# --------------------------------------------------------------------------- #
import os

if __name__ == '__main__':

    # adapter les valeurs en rapport avec la configuration de votre environnement
    # de développement
    SERVER = "127.0.0.1"
    PORT = 5452
    USER = "dev"
    PASSWORD = "dev"
    SCRIPTS_DIRECTORY = "/home/olivier/dev/DjangoEcommerce/_etude/database/scripts/"
    DATABASE = "django_platecom_db"

    SCRIPT_00 = "00_create_tables.sql"
    SCRIPT_01 = "01_role_sql_insert.sql"
    SCRIPT_02 = "02_utilisateur_sql_insert.sql"
    SCRIPT_03 = "03_produit_sql_insert.sql"

    scripts = []
    scripts.append(SCRIPT_00)
    scripts.append(SCRIPT_01)
    scripts.append(SCRIPT_02)
    scripts.append(SCRIPT_03)


    i = 0
    for script in scripts:
        print("Exécution de : '{0}'".format(script) + " ...")
        command = "PGPASSWORD={5} psql {0} -h {1} -p {2} -d {3} -a -f {4} > {6}".format(USER, SERVER, PORT, DATABASE, SCRIPTS_DIRECTORY + script, PASSWORD, SCRIPTS_DIRECTORY + "command_{0}.log".format(i))
        os.system(command)
        i = i + 1

    print("Fin des traitements.")
