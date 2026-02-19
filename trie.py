import os
import json

FICHIER = "animes.json"

def charger_donnees():
    """Charge les données depuis le fichier JSON."""
    if os.path.exists(FICHIER):
        with open(FICHIER, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def sauvegarder_donnees(animes):
    """Sauvegarde le dictionnaire animes dans le fichier JSON."""
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(animes, f, indent=4, ensure_ascii=False)

def trier_animes(animes):
    """Trie le dictionnaire animes par ordre alphabétique des titres."""
    return dict(sorted(animes.items(), key=lambda x: x[0].lower()))

def main():
    animes = charger_donnees()
    if not animes:
        print("⚠️  Aucun anime trouvé dans le fichier.")
        return

    animes = trier_animes(animes)
    sauvegarder_donnees(animes)
    print("✅ JSON trié par ordre alphabétique !\n📊 Classement :")
    for i, (titre, note) in enumerate(animes.items(), 1):
        print(f"{i}. {titre} — {note}/10")

if __name__ == "__main__":
    main()
