from ai_assistant import ai_assistant
from recon_engine import recon_engine
from helpers import print_colored

def main():
    print_colored("Welcome to the Cybersecurity AI Tool!", "green")
    print_colored("Choose an option:", "cyan")
    print("1. AI Assistant")
    print("2. Recon Tool")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        ai_assistant()
    elif choice == "2":
        recon_engine()
    else:
        print_colored("Invalid choice. Exiting.", "red")

if __name__ == "__main__":
    main()
