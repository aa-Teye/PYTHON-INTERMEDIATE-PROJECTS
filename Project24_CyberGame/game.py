import time
import sys

class CyberEscape:
    def __init__(self, player_name):
        self.player_name = player_name
        self.inventory = []
        self.current_room = "Lobby"
        self.is_running = True

    def clear_screen(self):
        # Keeps the terminal clean
        print("\n" * 2)

    def start(self):
        print(f"--- WELCOME TO CYBER-ESCAPE v2.0 ---")
        print(f"Agent: {self.player_name}")
        print("Status: Trapped in the Digital Vault\n")
        time.sleep(1)
        
        while self.is_running:
            if self.current_room == "Lobby":
                self.lobby_room()
            elif self.current_room == "Mainframe":
                self.mainframe_room()

    def lobby_room(self):
        self.clear_screen()
        print(f"Current Location: [VIRTUAL LOBBY]")
        print("Inventory:", self.inventory if self.inventory else "Empty")
        print("-" * 30)
        print("1. Inspect 'terminal'")
        print("2. Try 'gate'")
        print("3. Type 'exit' to quit")
        
        choice = input("\nAction >> ").lower()

        if "terminal" in choice:
            password = input("ENTER SYSTEM PASSWORD: ")
            if password == "Ghan@2026":
                print("\n[✔] ACCESS GRANTED. 'Admin_Key' downloaded to your inventory.")
                if "Admin_Key" not in self.inventory:
                    self.inventory.append("Admin_Key")
            else:
                print("\n[✘] ACCESS DENIED. Intruder alert levels rising!")
            time.sleep(2)

        elif "gate" in choice:
            if "Admin_Key" in self.inventory:
                print("\n[✔] Authorization Verified. Opening Gate...")
                time.sleep(1)
                self.current_room = "Mainframe"
            else:
                print("\n[✘] ERROR: Security Clearance 'Level_1' Required.")
                time.sleep(2)

        elif "exit" in choice:
            self.is_running = False

    def mainframe_room(self):
        self.clear_screen()
        print("[THE MAINFRAME]")
        print("You are at the core. A giant 'Red_Button' is glowing.")
        
        choice = input("\nType 'press' to escape or 'back' to return: ").lower()

        if "press" in choice:
            print(f"\nExcellent work, {self.player_name}!")
            print("You've successfully breached the vault and escaped.")
            print("MISSION ACCOMPLISHED.")
            self.is_running = False
        elif "back" in choice:
            self.current_room = "Lobby"

if __name__ == "__main__":
    # Starting the game with your name
    game = CyberEscape("Alex Teye Ametepey")
    game.start()