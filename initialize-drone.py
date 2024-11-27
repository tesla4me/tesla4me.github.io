# --- Hier werden die Module (Bibliotheken) aktiviert ---
# Aus dem Modul "time" brauchen wir nur den Befehl sleep für Pausen.
from time import sleep
# Aus dem Modul djitellopy brauchen wir die Kommandos fuer Tello.
from djitellopy import Tello
# Modul um die Tastatur fuer Eingaben verwenden zu koennen.
import keyboard
# Variable, damit die Kommandos aus dem Modul mit "drone" beginnen.
drone = Tello()
# Initialisierung der Drohne -> Wlan Verbindung muss bereits aufgebaut sein(!)
drone.connect()
# Um Batterie zu sparen wird das Videostreaming ausgeschaltet.
drone.streamoff()
# Ladestand der Batterie wird abgefragt und ausgegben.
SoC = drone.get_battery()
print("Ladestand",SoC,"Prozent")

# --- Ab hier kommen die Flugkommandos -> siehe Hilfsblatt ----
# Starten der Drohne - Standardmaessig schwebt sie auf ca. 50cm.
drone.takeoff()
# Pause von 1 sek -> Anstelle Pause weitere Befehle vom Hilfsblatt einfuegen.
sleep(0.2)
#Landen der Drohne
drone.land()
exit
