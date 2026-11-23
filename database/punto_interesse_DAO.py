from database.DB_connect import DBConnect
from model.punto_interesse import PuntoInteresse

class PuntoInteresseDAO:

    @staticmethod
    def get_punti_interesse() -> dict[str, PuntoInteresse] | None:
        """
        Restituisce tutti i punti di interesse
        :return: un dizionario di tutti i Punti di Interesse
        """
        cnx = DBConnect.get_connection()
        result = {}

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * 
                    FROM punto_interesse"""
        try:
            cursor.execute(query)
            for row in cursor:
                punto = PuntoInteresse(
                    id=row["id"],
                    nome=row["nome"],
                    voto_visitatori=row["voto_visitatori"]
                )
                result[punto.id] = punto
        except Exception as e:
            print(f"Errore durante la query get_punti_interesse: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result
