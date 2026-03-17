import os
from dotenv import load_dotenv

def main():
    # Umgebungsvariablen aus der .env-Datei laden
    load_dotenv()
    
    # API-Key abrufen (Beispiel für OpenAI)
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("FEHLER: Kein API-Key gefunden. Bitte prüfen Sie Ihre .env-Datei!")
        return

    # Hier folgt die Implementierung des Labs
    print("Los geht's. Viel Erfolg beim Engineering Lab!")

if __name__ == "__main__":
    main()
