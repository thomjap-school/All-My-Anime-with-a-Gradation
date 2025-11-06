import os
import sys
import json

FICHIER = "animes.json"
animes = {}

def charger_donnees():
    global animes
    if os.path.exists(FICHIER):
        with open(FICHIER, "r", encoding="utf-8") as f:
            try:
                animes = json.load(f)
            except json.JSONDecodeError:
                animes = {}
    else:
        animes = {}

def sauvegarder_donnees():
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(animes, f, indent=4, ensure_ascii=False)

def anime():
    charger_donnees()

    while True:
        titre = input("Titre de l'anime (ou 'stop' pour terminer) : ").strip()
        if titre.lower() == "stop":
            break

        try:
            note = float(input(f"Note pour '{titre}' (sur 10) : "))
        except ValueError:
            print("⚠️  Merci d'entrer un nombre valide pour la note.")
            continue

        # Mise à jour ou ajout
        animes[titre] = note
        print(f"✅ '{titre}' enregistré avec une note de {note}/10.\n")

    sauvegarder_donnees()

    # Tri décroissant des notes
    classement = sorted(animes.items(), key=lambda x: x[1], reverse=True)

    print("\n📊 Classement du meilleur au moins bon :")
    for i, (titre, note) in enumerate(classement, 1):
        print(f"{i}. {titre} — {note}/10")

if __name__ == "__main__":
    try:
        anime()
    except KeyboardInterrupt:
        print("\n\n🛑 Interruption détectée. Fermeture du programme...")
        sauvegarder_donnees()
        sys.exit(0)
