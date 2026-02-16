# Task Manager (Todo) - Python
# Auteur: Nawal Achiche
import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
    return []


def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")


def add_task(tasks):
    title = input("Titre de la tâche: ").strip()
    if not title:
        print("Titre vide -> annulé.")
        return
    task = {
        "id": int(datetime.now().timestamp()),
        "title": title,
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Tâche ajoutée.")


def list_tasks(tasks):
    if not tasks:
        print("Aucune tâche.")
        return
    print("\n--- Mes tâches ---")
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t["done"] else "⬜"
        print(f"{i}. {status} {t['title']}")
    print("-----------------\n")


def toggle_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Numéro de la tâche à cocher/décocher: "))
        if idx < 1 or idx > len(tasks):
            print("Numéro invalide.")
            return
        tasks[idx - 1]["done"] = not tasks[idx - 1]["done"]
        save_tasks(tasks)
        print("✅ Statut modifié.")
    except ValueError:
        print("Entrée invalide.")


def delete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("Numéro de la tâche à supprimer: "))
        if idx < 1 or idx > len(tasks):
            print("Numéro invalide.")
            return
        removed = tasks.pop(idx - 1)
        save_tasks(tasks)
        print(f"🗑️ Tâche supprimée: {removed['title']}")
    except ValueError:
        print("Entrée invalide.")


def main():
    tasks = load_tasks()
    while True:
        print("=== Task Manager ===")
        print("1) Ajouter une tâche")
        print("2) Voir les tâches")
        print("3) Cocher / Décocher une tâche")
        print("4) Supprimer une tâche")
        print("0) Quitter")
        choice = input("Choix: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            toggle_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "0":
            print("Bye 👋")
            break
        else:
            print("Choix invalide.\n")


if __name__ == "__main__":
    main()
