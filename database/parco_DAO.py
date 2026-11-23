from database.DB_connect import DBConnect
from model.parco import Parco

class ParcoDAO:

    @staticmethod
    def get_parchi() -> list[Parco] | None:
        """
        Restituisce tutti i parchi
        :return: lista di tutti i Parchi
        """
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * 
                    FROM parco"""
        try:
            cursor.execute(query)
            for row in cursor:
                parco = Parco(
                    id=row["id"],
                    nome=row["nome"]
                )
                result.append(parco)
        except Exception as e:
            print(f"Errore durante la query get_parchi: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result
