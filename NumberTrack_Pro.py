#!/usr/bin/python3
import requests
import os
import time
import random
import sys
import datetime
import hashlib

# ==================== CONTACT INFO ====================
CONTACT_NUMBER = "+918409978725"
CONTACT_WHATSAPP = "8409978725"
CHANNEL_NAME = "@HACKERxTRADER"

# ==================== LICENSE CONFIGURATION ====================
LICENSE_DIR = os.path.expanduser("~/licenses")
ADMIN_USER = "HACKERxTRADER"
ADMIN_PASS = "84099"

# ==================== HACKING EFFECTS COLORS ====================
R = '\033[91m'
G = '\033[92m'
C = '\033[96m'
W = '\033[93m'
B = '\033[94m'
P = '\033[95m'
GR = '\033[90m'
BL = '\033[30m'
BG_R = '\033[41m'
BG_G = '\033[42m'
RESET = '\033[0m'
BOLD = '\033[1m'
BLINK = '\033[5m'
DIM = '\033[2m'

# ==================== LICENSE FUNCTIONS ====================

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def ensure_license_dir():
    if not os.path.exists(LICENSE_DIR):
        os.makedirs(LICENSE_DIR)

def generate_license_key(username, expiry_date):
    data = f"{username}_{expiry_date}_HACKERxTRADER_{CONTACT_NUMBER}"
    return hashlib.md5(data.encode()).hexdigest()[:16]

def get_days_left(expiry_str):
    try:
        expiry_date = datetime.datetime.strptime(expiry_str, "%d-%m-%Y").date()
        current_date = datetime.datetime.now().date()
        return (expiry_date - current_date).days
    except:
        return -999

def license_banner():
    print(f"""{R}
╔══════════════════════════════════════════════════════════════╗
║     {C}🔐 NUMBER TRACK v4.0 - LICENSED 🔐{R}                        ║
║     {W}Channel: {G}{CHANNEL_NAME}{R}{W}                               ║
║     {W}Contact: {G}{CONTACT_NUMBER}{R}{W}                            ║
╚══════════════════════════════════════════════════════════════╝{RESET}
    """)

def small_banner():
    print(f"""{R}
╔════════════════════════════════════════════╗
║     {C}🔐 LICENSE MANAGER 🔐{R}                      ║
║     {W}Contact: {G}{CONTACT_NUMBER}{R}{W}                 ║
╚════════════════════════════════════════════╝{RESET}
    """)

# ==================== NUMBER TRACK FUNCTIONS (TERE WALE) ====================

def matrix_rain():
    for _ in range(5):
        line = ''.join(random.choice(['0', '1']) for _ in range(50))
        print(f"{G}{line}{RESET}")
        time.sleep(0.03)

def glitch_effect():
    glitch_chars = ['░', '▒', '▓', '█', '▄', '▀']
    for _ in range(3):
        line = ''.join(random.choice(glitch_chars) for _ in range(60))
        print(f"{R}{line}{RESET}")
        time.sleep(0.05)
    for _ in range(2):
        line = ''.join(random.choice(glitch_chars) for _ in range(60))
        print(f"{G}{line}{RESET}")
        time.sleep(0.05)

def hack_progress_bar():
    print(f"{R}┌─────────────────────────────────────────────────┐{RESET}")
    for i in range(101):
        bar_length = int(i / 2)
        bar = '█' * bar_length + '░' * (50 - bar_length)
        print(f"\r{R}│{RESET}{G}{bar}{RESET}{R}│ {i}%{RESET}", end='')
        time.sleep(0.01)
    print(f"\n{R}└─────────────────────────────────────────────────┘{RESET}")

def loading_animation(text):
    print(f"{W}[*] {text}{RESET}", end='', flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print('.', end='', flush=True)
    print()

def skull_banner():
    print(f"""{R}
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║      {C}██████╗ {W}████████╗{G}██████╗  {B}█████╗ {P}██╗  ██╗{R}    ║
    ║      {C}██╔══██╗{W}╚══██╔══╝{G}██╔══██╗{B}██╔══██╗{P}██║ ██╔╝{R}    ║
    ║      {C}██████╔╝{W}   ██║   {G}██████╔╝{B}███████║{P}█████╔╝ {R}    ║
    ║      {C}██╔══██╗{W}   ██║   {G}██╔══██╗{B}██╔══██║{P}██╔═██╗ {R}    ║
    ║      {C}██████╔╝{W}   ██║   {G}██║  ██║{B}██║  ██║{P}██║  ██╗{R}    ║
    ║      {C}╚═════╝ {W}   ╚═╝   {G}╚═╝  ╚═╝{B}╚═╝  ╚═╝{P}╚═╝  ╚═╝{R}    ║
    ║                                                          ║
    ╠══════════════════════════════════════════════════════════╣
    ║     {BLINK}{R}⚠ DARK WEB OSINT TOOL ⚠{RESET}{R}                      ║
    ║     {C}Channel: {G}{CHANNEL_NAME}{R}{R}                           ║
    ║     {C}Tool: {G}NumberTrack v4.0{R}{R}                             ║
    ║     {C}Status: {BLINK}{G}[ LICENSED ]{RESET}{R}                      ║
    ╚══════════════════════════════════════════════════════════╝{RESET}
    """)

def lookup_number(mobile):
    url = f"https://exploitsindia.site/track/live.php?exploits={mobile}"
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            return response.text
        return None
    except:
        return None

def display_hacked_data(data, mobile):
    print(f"\n{R}{'═'*60}{RESET}")
    print(f"{BLINK}{G}✓✓✓ TARGET COMPROMISED ✓✓✓{RESET}")
    print(f"{R}{'═'*60}{RESET}")
    
    lines = data.split('\n')
    for line in lines:
        if 'Name:' in line:
            print(f"{G}┌──[{R}HACKERxTRADER{R}]──┐{RESET}")
            print(f"{G}│ 👤 {BOLD}{line.strip()}{RESET}")
        elif 'Father Name:' in line:
            print(f"{C}│ 👨 {line.strip()}{RESET}")
        elif 'Mobile:' in line and 'Alternate' not in line:
            print(f"{W}│ 📱 {line.strip()}{RESET}")
        elif 'Address:' in line:
            print(f"{P}│ 🏠 {line.strip()}{RESET}")
        elif 'Circle:' in line:
            print(f"{B}│ 📡 {line.strip()}{RESET}")
        elif 'Aadhaar:' in line:
            print(f"{R}│ 🆔 {line.strip()} {BLINK}[LEAKED]{RESET}")
        elif 'Alternate:' in line:
            print(f"{W}│ 📞 {line.strip()}{RESET}")
        elif '@Cyb3rS0ldier' in line or 'BUY API' in line:
            continue
    
    print(f"{G}└──[{R}DATA DUMP COMPLETE{R}]──┘{RESET}")
    print(f"{R}{'═'*60}{RESET}")

def save_hacked_data(data, mobile):
    filename = f"LEAKED_{mobile}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"=== LEAKED BY HACKERxTRADER ===\n")
        f.write(f"=== TOOL: NumberTrack v4.0 ===\n")
        f.write(f"=== TARGET: {mobile} ===\n")
        f.write(f"{'='*50}\n\n")
        f.write(data)
    return filename

def run_number_track():
    """Main NumberTrack functionality"""
    clear()
    matrix_rain()
    time.sleep(0.5)
    clear()
    skull_banner()
    time.sleep(1)
    
    while True:
        print(f"\n{R}┌─────────────────────────────────────────────────┐{RESET}")
        print(f"{R}│{RESET} {BOLD}{G}⚠ SYSTEM READY ⚠{RESET}                         {R}│{RESET}")
        print(f"{R}├─────────────────────────────────────────────────┤{RESET}")
        print(f"{R}│{RESET} {W}[?] ENTER TARGET NUMBER:{RESET}                       {R}│{RESET}")
        print(f"{R}└─────────────────────────────────────────────────┘{RESET}")
        
        mobile = input(f"\n{G}┌─[{R}NumberTrack@{CHANNEL_NAME}{R}]\n└──{W}# {RESET}").strip()
        
        if not mobile:
            print(f"{R}{BLINK}[!] INVALID INPUT DETECTED [!]{RESET}")
            continue
        
        mobile = mobile.replace('+', '').replace(' ', '').replace('-', '')
        
        print(f"\n{R}{'█'*60}{RESET}")
        print(f"{G}[TARGET LOCKED]{RESET} {W}{mobile}{RESET}")
        print(f"{R}{'█'*60}{RESET}")
        
        loading_animation("CONNECTING TO DARK API")
        loading_animation("BYPASSING SECURITY")
        loading_animation("DECRYPTING PAYLOAD")
        
        print(f"{R}\n[HACKING PROGRESS]{RESET}")
        hack_progress_bar()
        
        print(f"{G}\n[+] INJECTING EXPLOIT...{RESET}")
        time.sleep(0.5)
        
        glitch_effect()
        
        raw_data = lookup_number(mobile)
        
        if raw_data:
            print(f"{BLINK}{G}[✓] EXPLOIT SUCCESSFUL{RESET}")
            display_hacked_data(raw_data, mobile)
            filename = save_hacked_data(raw_data, mobile)
            
            print(f"\n{G}[✓] LEAK SAVED: {R}{filename}{RESET}")
            print(f"{G}[✓] CHANNEL: {W}{CHANNEL_NAME}{RESET}")
            print(f"{G}[✓] TOOL: {W}NumberTrack v4.0{RESET}")
            print(f"{G}[✓] CONTACT: {W}{CONTACT_NUMBER}{RESET}")
        else:
            print(f"{R}{BLINK}[X] EXPLOIT FAILED - NO DATA RETURNED{RESET}")
        
        print(f"\n{R}{'─'*60}{RESET}")
        print(f"{W}[?] SCAN ANOTHER TARGET? (y/n):{RESET}")
        again = input(f"{G}┌─[{R}NumberTrack{R}]\n└──{W}# {RESET}").lower()
        
        if again != 'y':
            print(f"\n{G}[+] CLOSING BACKDOOR...{RESET}")
            print(f"{R}[+] STAY UNDERGROUND{RESET}")
            print(f"{C}[+] {CHANNEL_NAME}{RESET}")
            print(f"{C}[+] Contact: {CONTACT_NUMBER}{RESET}")
            matrix_rain()
            break
        
        clear()
        skull_banner()

# ==================== LICENSE MANAGEMENT FUNCTIONS ====================

def user_login():
    """User login with username and license key"""
    clear()
    small_banner()
    
    print(f"{C}════════════════════════════════════════════{RESET}")
    print(f"{C}🔑 USER LOGIN 🔑{RESET}")
    print(f"{C}════════════════════════════════════════════{RESET}")
    
    username = input(f"{G}Enter username: {RESET}").strip()
    license_key = input(f"{G}Enter license key: {RESET}").strip()
    
    license_file = os.path.join(LICENSE_DIR, f"{username}.lic")
    
    if not os.path.exists(license_file):
        print(f"\n{R}✗ LICENSE NOT FOUND!{RESET}")
        print(f"{W}Contact {CONTACT_NUMBER} to purchase license{RESET}")
        time.sleep(3)
        return False
    
    with open(license_file, 'r') as f:
        content = f.read()
    
    license_data = {}
    for line in content.split('\n'):
        if '=' in line:
            key, value = line.split('=', 1)
            license_data[key] = value
    
    if license_data.get('LICENSE_KEY') != license_key:
        print(f"\n{R}✗ INVALID LICENSE KEY!{RESET}")
        print(f"{W}Contact {CONTACT_NUMBER} for support{RESET}")
        time.sleep(3)
        return False
    
    expiry_str = license_data.get('EXPIRY')
    days_left = get_days_left(expiry_str)
    
    if days_left < 0:
        print(f"\n{R}{'='*50}{RESET}")
        print(f"{R}⚠️ LICENSE EXPIRED ⚠️{RESET}")
        print(f"{R}{'='*50}{RESET}")
        print(f"{W}Expired on: {R}{expiry_str}{RESET}")
        print(f"{W}Days overdue: {R}{abs(days_left)}{RESET}")
        print(f"{R}{'='*50}{RESET}")
        print(f"{W}Contact {CONTACT_NUMBER} to renew{RESET}")
        time.sleep(4)
        return False
    
    print(f"\n{G}{'='*50}{RESET}")
    print(f"{G}✓ LICENSE VALID ✓{RESET}")
    print(f"{G}{'='*50}{RESET}")
    print(f"{W}User: {C}{username}{RESET}")
    print(f"{W}Expiry: {C}{expiry_str}{RESET}")
    print(f"{W}Days left: {G}{days_left}{RESET}")
    print(f"{G}{'='*50}{RESET}")
    time.sleep(2)
    
    return True

def admin_login():
    """Admin login to create licenses"""
    clear()
    small_banner()
    
    print(f"{C}════════════════════════════════════════════{RESET}")
    print(f"{C}👑 ADMIN LOGIN 👑{RESET}")
    print(f"{C}════════════════════════════════════════════{RESET}")
    
    username = input(f"{G}Username: {RESET}")
    password = input(f"{G}Password: {RESET}")
    
    if username == ADMIN_USER and password == ADMIN_PASS:
        print(f"\n{G}✓ ADMIN ACCESS GRANTED ✓{RESET}")
        time.sleep(1)
        return True
    else:
        print(f"\n{R}✗ INVALID CREDENTIALS ✗{RESET}")
        time.sleep(2)
        return False

def list_all_licenses():
    """Show all created licenses"""
    clear()
    small_banner()
    
    print(f"{C}════════════════════════════════════════════{RESET}")
    print(f"{C}📋 ALL LICENSES 📋{RESET}")
    print(f"{C}════════════════════════════════════════════{RESET}")
    
    if not os.path.exists(LICENSE_DIR):
        print(f"{W}No licenses found{RESET}")
        return
    
    license_files = os.listdir(LICENSE_DIR)
    
    if len(license_files) == 0:
        print(f"{W}No licenses found{RESET}")
        return
    
    for lic_file in license_files:
        if lic_file.endswith('.lic'):
            username = lic_file.replace('.lic', '')
            with open(os.path.join(LICENSE_DIR, lic_file), 'r') as f:
                content = f.read()
            
            for line in content.split('\n'):
                if line.startswith('EXPIRY='):
                    expiry = line.split('=')[1]
                    days = get_days_left(expiry)
                    
                    if days >= 0:
                        status = f"{G}ACTIVE{RESET}"
                        days_show = f"{G}{days}{RESET}"
                    else:
                        status = f"{R}EXPIRED{RESET}"
                        days_show = f"{R}{days}{RESET}"
                    
                    print(f"{W}User: {C}{username}{RESET} | Expiry: {expiry} | Days: {days_show} | {status}")
                    break
    
    print(f"\n{C}════════════════════════════════════════════{RESET}")
    input(f"{W}Press Enter to continue...{RESET}")

def create_license():
    """Admin creates a new license for a user"""
    clear()
    small_banner()
    
    print(f"{C}════════════════════════════════════════════{RESET}")
    print(f"{C}🆕 CREATE NEW LICENSE 🆕{RESET}")
    print(f"{C}════════════════════════════════════════════{RESET}")
    
    username = input(f"{G}Enter username: {RESET}").strip()
    
    if not username:
        print(f"{R}Invalid username!{RESET}")
        return
    
    license_file = os.path.join(LICENSE_DIR, f"{username}.lic")
    if os.path.exists(license_file):
        overwrite = input(f"{W}License already exists! Overwrite? (y/n): {RESET}")
        if overwrite.lower() != 'y':
            return
    
    print(f"\n{W}Select expiry duration:{RESET}")
    print(f"{C}1. 3 Days{RESET}")
    print(f"{C}2. 5 Days{RESET}")
    print(f"{C}3. 7 Days{RESET}")
    print(f"{C}4. 10 Days{RESET}")
    print(f"{C}5. 15 Days{RESET}")
    print(f"{C}6. 30 Days{RESET}")
    print(f"{C}7. Custom Date (DD-MM-YYYY){RESET}")
    print(f"{C}8. Unlimited (1 Year){RESET}")
    
    choice = input(f"\n{G}Choose [1-8]: {RESET}")
    
    current_date = datetime.datetime.now()
    
    expiry_options = {"1": 3, "2": 5, "3": 7, "4": 10, "5": 15, "6": 30}
    
    if choice in expiry_options:
        days = expiry_options[choice]
        expiry_date = current_date + datetime.timedelta(days=days)
        expiry_str = expiry_date.strftime("%d-%m-%Y")
        days_text = f"{days} days"
    elif choice == "7":
        while True:
            expiry_str = input(f"{G}Enter expiry date (DD-MM-YYYY): {RESET}")
            try:
                expiry_date = datetime.datetime.strptime(expiry_str, "%d-%m-%Y")
                days_diff = (expiry_date - current_date).days
                if days_diff <= 0:
                    print(f"{R}Date must be in future! Use tomorrow or later{RESET}")
                    continue
                days_text = f"{days_diff} days"
                break
            except:
                print(f"{R}Invalid format! Use DD-MM-YYYY (example: 10-06-2026){RESET}")
    elif choice == "8":
        expiry_date = current_date + datetime.timedelta(days=365)
        expiry_str = expiry_date.strftime("%d-%m-%Y")
        days_text = "1 year (Unlimited)"
    else:
        print(f"{R}Invalid choice!{RESET}")
        return
    
    license_key = generate_license_key(username, expiry_str)
    user_password = f"HACKER{expiry_str.replace('-', '')}{username[:3].upper()}"
    
    with open(license_file, 'w') as f:
        f.write(f"USERNAME={username}\n")
        f.write(f"EXPIRY={expiry_str}\n")
        f.write(f"LICENSE_KEY={license_key}\n")
        f.write(f"PASSWORD={user_password}\n")
        f.write(f"CREATED={current_date.strftime('%d-%m-%Y %H:%M:%S')}\n")
        f.write(f"CONTACT={CONTACT_NUMBER}\n")
    
    print(f"\n{G}{'='*60}{RESET}")
    print(f"{G}{BLINK}✓ LICENSE CREATED SUCCESSFULLY ✓{RESET}")
    print(f"{G}{'='*60}{RESET}")
    print(f"{W}┌────────────────────────────────────────┐{RESET}")
    print(f"{W}│ {C}USER DETAILS{RESET}                              {W}│{RESET}")
    print(f"{W}├────────────────────────────────────────┤{RESET}")
    print(f"{W}│ {G}Username: {C}{username}{RESET}                      {W}│{RESET}")
    print(f"{W}│ {G}License Key: {C}{license_key}{RESET}                 {W}│{RESET}")
    print(f"{W}│ {G}Password: {C}{user_password}{RESET}                  {W}│{RESET}")
    print(f"{W}│ {G}Expiry: {C}{expiry_str} ({days_text}){RESET}        {W}│{RESET}")
    print(f"{W}└────────────────────────────────────────┘{RESET}")
    print(f"{G}{'='*60}{RESET}")
    print(f"{W}📞 Share these details with the user:{RESET}")
    print(f"{C}   Username: {username}{RESET}")
    print(f"{C}   License Key: {license_key}{RESET}")
    print(f"{W}   Contact for support: {G}{CONTACT_NUMBER}{RESET}")
    print(f"{G}{'='*60}{RESET}")
    
    input(f"\n{W}Press Enter to continue...{RESET}")

def delete_license():
    """Admin deletes a user's license"""
    clear()
    small_banner()
    
    print(f"{C}════════════════════════════════════════════{RESET}")
    print(f"{C}🗑️ DELETE LICENSE 🗑️{RESET}")
    print(f"{C}════════════════════════════════════════════{RESET}")
    
    username = input(f"{G}Enter username to delete: {RESET}")
    
    license_file = os.path.join(LICENSE_DIR, f"{username}.lic")
    
    if os.path.exists(license_file):
        confirm = input(f"{R}Delete license for '{username}'? (y/n): {RESET}")
        if confirm.lower() == 'y':
            os.remove(license_file)
            print(f"{G}✓ License deleted!{RESET}")
        else:
            print(f"{W}Cancelled{RESET}")
    else:
        print(f"{R}License not found!{RESET}")
    
    time.sleep(2)

def admin_panel():
    """Admin main panel"""
    while True:
        clear()
        license_banner()
        
        print(f"{C}════════════════════════════════════════════{RESET}")
        print(f"{C}👑 ADMIN PANEL 👑{RESET}")
        print(f"{C}════════════════════════════════════════════{RESET}")
        print(f"{G}1. Create New License{RESET}")
        print(f"{C}2. List All Licenses{RESET}")
        print(f"{W}3. Delete License{RESET}")
        print(f"{C}4. Contact Support{RESET}")
        print(f"{R}5. Exit to Main Menu{RESET}")
        print(f"{C}════════════════════════════════════════════{RESET}")
        
        choice = input(f"\n{G}Select option: {RESET}")
        
        if choice == "1":
            create_license()
        elif choice == "2":
            list_all_licenses()
        elif choice == "3":
            delete_license()
        elif choice == "4":
            clear()
            small_banner()
            print(f"{G}{'='*50}{RESET}")
            print(f"{W}📞 CONTACT INFORMATION:{RESET}")
            print(f"{G}   Phone: {CONTACT_NUMBER}{RESET}")
            print(f"{G}   WhatsApp: {CONTACT_WHATSAPP}{RESET}")
            print(f"{G}   Channel: {CHANNEL_NAME}{RESET}")
            print(f"{G}{'='*50}{RESET}")
            input(f"{W}Press Enter to continue...{RESET}")
        elif choice == "5":
            break
        else:
            print(f"{R}Invalid option!{RESET}")
            time.sleep(1)

def contact_info():
    clear()
    small_banner()
    print(f"{G}{'='*50}{RESET}")
    print(f"{W}📞 CONTACT INFORMATION:{RESET}")
    print(f"{G}   Phone: {CONTACT_NUMBER}{RESET}")
    print(f"{G}   WhatsApp: {CONTACT_WHATSAPP}{RESET}")
    print(f"{G}   Channel: {CHANNEL_NAME}{RESET}")
    print(f"{G}{'='*50}{RESET}")
    input(f"{W}Press Enter to continue...{RESET}")

# ==================== MAIN MENU ====================

def main():
    ensure_license_dir()
    
    while True:
        clear()
        license_banner()
        
        print(f"{C}════════════════════════════════════════════{RESET}")
        print(f"{C}📋 MAIN MENU 📋{RESET}")
        print(f"{C}════════════════════════════════════════════{RESET}")
        print(f"{G}1. User Login (Run NumberTrack){RESET}")
        print(f"{C}2. Admin Login (Create Licenses){RESET}")
        print(f"{W}3. Contact Support{RESET}")
        print(f"{R}4. Exit{RESET}")
        print(f"{C}════════════════════════════════════════════{RESET}")
        print(f"{W}📞 Need License? Contact: {G}{CONTACT_NUMBER}{RESET}")
        
        choice = input(f"\n{G}Select option: {RESET}")
        
        if choice == "1":
            if user_login():
                run_number_track()
            else:
                print(f"{W}Press Enter to continue...{RESET}")
                input()
        elif choice == "2":
            if admin_login():
                admin_panel()
        elif choice == "3":
            contact_info()
        elif choice == "4":
            print(f"{G}Thank you! Contact {CONTACT_NUMBER} for support{RESET}")
            sys.exit(0)
        else:
            print(f"{R}Invalid option!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
