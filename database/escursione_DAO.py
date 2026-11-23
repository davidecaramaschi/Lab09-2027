from database.DB_connect import DBConnect
from model.escursione import Escursione

class EscursioneDAO:

    @staticmethod
    def get_escursioni() -> dict[str, Escursione] | None:
        """
        Restituisce tutte le escursioni
        :return: un dizionario di tutte le Escursioni
        """
        cnx = DBConnect.get_connection()
        result = {}
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT *
                    FROM escursione"""
        try:
            cursor.execute(query)
            for row in cursor:
                escursione = Escursione(
                    id=row["id"],
                    nome=row["nome"],
                    durata_giorni=row["durata_giorni"],
                    costo=float(row["costo"]),
                    id_parco=row["id_parco"]
                )
                result[escursione.id] = escursione
        except Exception as e:
            print(f"Errore durante la query get_escursioni: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result

    @staticmethod
    def get_escursioni_punti_interesse() -> list | None:
        """
        Restituisce tutte le relazioni
        :return: una lista di dizionari [{"id_escursione": ..., "id_punto_interesse": ...}]
        """
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * 
                    FROM escursione_punto_interesse """
        try:
            cursor.execute(query)
            for row in cursor:
                result.append({
                    "id_escursione": row["id_escursione"],
                    "id_punto_interesse": row["id_punto_interesse"]
                })
        except Exception as e:
            print(f"Errore durante la query get_escursioni_punti_interesse: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result
