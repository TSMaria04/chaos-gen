import random
import pyperclip
from colorama import Fore, Style, init

init(autoreset=True)

# Словарь замен (L33t Speak)
LEET_DICT = {
    'a': ['4', '@'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'],
    's': ['$', '5'], 't': ['7', '+'], 'b': ['8'], 'g': ['9']
}

SPECIAL_CHARS = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-']

BANNER = rf"""
{Fore.MAGENTA}  ___  _  _   _   ___   _____  _  _ 
 / C \| || | /_\ / _ \ / _ \ \/ / 
|  _  | __ |/ _ \ \_  / \_  />  <  
 \_| |_|_||_/_/ \_\__/  \__/_/\_\ {Fore.CYAN}v1.0
"""

def generate_leet_password(word):
    result = []
    for char in word:
        char_lower = char.lower()
        # С вероятностью 70% меняем букву на спецсимвол
        if char_lower in LEET_DICT and random.random() < 0.7:
            replacement = random.choice(LEET_DICT[char_lower])
            result.append(replacement)
        else:
            # Случайный регистр
            result.append(char.upper() if random.random() > 0.5 else char.lower())
    
    # Добавляем хаос в начало и конец
    prefix = "".join(random.choices(SPECIAL_CHARS, k=2))
    suffix = "".join(random.choices(SPECIAL_CHARS, k=2)) + str(random.randint(10, 99))
    
    return f"{prefix}{''.join(result)}{suffix}"

if __name__ == "__main__":
    print(BANNER)
    print(Fore.YELLOW + "=== KPEAТИВНЫЙ ГЕНЕРАТОР ПАРОЛЕЙ ===")
    
    user_input = input("\nВведите базовое слово (например, cybersec): ").strip()
    
    if user_input:
        strong_pass = generate_leet_password(user_input)
        
        print("\n" + Fore.GREEN + "[+] Твой кастомный пароль готов:")
        print(Fore.CYAN + Style.BRIGHT + f"    {strong_pass}\n")
        
        # Копирование в буфер
        try:
            pyperclip.copy(strong_pass)
            print(Fore.GREEN + "[✔] Пароль автоматически скопирован в буфер обмена!")
        except Exception:
            pass
    else:
        print(Fore.RED + "[!] Слово не введено.")