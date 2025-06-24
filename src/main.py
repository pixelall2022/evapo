import os
import time
import getpass
import threading
import keyboard  # pip install keyboard
from utils.shutdown import shutdown_machine

kill_switch_active = False

def activate_kill_switch():
    global kill_switch_active
    kill_switch_active = True
    print("Kill switch activated via hotkey. Shutdown disabled.")

def monitor_kill_switch():
    # Listen for ctrl+1+space
    keyboard.add_hotkey('ctrl+1+space', activate_kill_switch)
    keyboard.wait()  # Keeps the thread alive

def monitor_logins():
    logged_in_users = set()
    
    while True:
        if kill_switch_active:
            print("Kill switch active. Shutdown disabled.")
            time.sleep(60)
            continue

        current_users = set([getpass.getuser()])
        
        new_users = current_users - logged_in_users
        if new_users:
            for user in new_users:
                print(f"User {user} has logged in. Initiating shutdown...")
                shutdown_machine()
        
        logged_in_users = current_users
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    print("Evapo is running. Press Ctrl+1+Space to activate the kill switch and stop shutdowns.")
    # Start kill switch monitor in a separate thread
    threading.Thread(target=monitor_kill_switch, daemon=True).start()
    monitor_logins()