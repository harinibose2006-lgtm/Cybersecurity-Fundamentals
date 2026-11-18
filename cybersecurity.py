def cybersecurity_intro():
    print("\n--- Cybersecurity Fundamentals ---")
    print("Cybersecurity protects computers, networks and data from cyber attacks.")
    print("It helps maintain privacy, security and data protection.")


def hacker_types():
    print("\n--- Types of Hackers ---")
    print("1. White Hat Hacker - Ethical Hacker")
    print("2. Black Hat Hacker - Malicious Hacker")
    print("3. Grey Hat Hacker - Works between ethical and unethical boundaries")


def cia_triad():
    print("\n--- CIA Triad ---")
    print("1. Confidentiality - Protecting information")
    print("2. Integrity - Maintaining data accuracy")
    print("3. Availability - Ensuring data is accessible")


def cyber_threats():
    print("\n--- Common Cyber Threats ---")
    print("1. Malware - Malicious software")
    print("2. Phishing - Fraudulent messages")
    print("3. Ransomware - Malware that locks or encrypts data")


def security_tips():
    print("\n--- Cybersecurity Safety Tips ---")
    print("1. Use strong passwords.")
    print("2. Enable two-factor authentication.")
    print("3. Avoid suspicious links.")
    print("4. Update software regularly.")
    print("5. Use trusted antivirus software.")


while True:
    print("\n========== CYBERSECURITY TOOLKIT ==========")
    print("1. Cybersecurity Introduction")
    print("2. Types of Hackers")
    print("3. CIA Triad")
    print("4. Common Cyber Threats")
    print("5. Security Tips")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        cybersecurity_intro()
    elif choice == "2":
        hacker_types()
    elif choice == "3":
        cia_triad()
    elif choice == "4":
        cyber_threats()
    elif choice == "5":
        security_tips()
    elif choice == "6":
        print("Thank you for using Cybersecurity Toolkit!")
        break
    else:
        print("Invalid choice! Please try again.")