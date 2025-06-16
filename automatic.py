import pyautogui
import time
import json
import os

azioni = []  # lista di azioni: ("click", (x, y)) o ("scrivi", (x, y))
counter = 1
file_azioni = "azioni.json"

print("Comandi disponibili:")
print("   INVIO: registra un click alla posizione attuale")
print("   1 + INVIO: registra una scrittura 'pagina_X' alla posizione attuale")
print("   0 + INVIO: esegue le azioni in loop")
print("   s + INVIO: salva le azioni su file")
print("   e + INVIO: esegue le azioni da file")
print("   Ctrl+C: per interrompere un loop")

while True:
    comando = input("> ")

    if comando == "":
        pos = pyautogui.position()
        azioni.append(("click", pos))
        print(f"[Click] Registrato: {pos[0]}, {pos[1]}")

    elif comando == "1":
        pos = pyautogui.position()
        azioni.append(("scrivi", pos))
        print(f"[Scrivi] Registrato: {pos[0]}, {pos[1]}")

    elif comando == "s":
        with open(file_azioni, "w") as f:
            json.dump(azioni, f)
        print(f"✅ Azioni salvate su '{file_azioni}'")

    elif comando == "e":
        if os.path.exists(file_azioni):
            with open(file_azioni, "r") as f:
                azioni = json.load(f)
            print(f"✅ Azioni caricate da '{file_azioni}'")
        else:
            print(f"❌ File '{file_azioni}' non trovato.")

    elif comando == "0":
        if not azioni:
            print("⚠️ Nessuna azione da eseguire.")
            continue

        print("▶️ Inizio esecuzione in loop. Premi Ctrl+C per fermare.")
        try:
            while True:
                for azione, (x, y) in azioni:
                    pyautogui.moveTo(x, y)
                    if azione == "click":
                        pyautogui.click()
                    elif azione == "scrivi":
                        pyautogui.click()
                        pyautogui.write(f"pagina_{counter}", interval=0.05)
                        counter += 1
                    time.sleep(1)
        except KeyboardInterrupt:
            print("\n⏹️ Loop interrotto. Puoi registrare nuove posizioni o uscire.")
