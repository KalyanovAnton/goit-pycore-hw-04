import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)
def structure_directory(directory: Path, indent: str = ""):
    try:
        if not directory.is_dir():
            print(Fore.RED + f"ПОМИЛКА: {directory} не є дерикторією")
            return
        for item_dir in directory.iterdir():
            if item_dir.is_dir():
                print(f"{indent}{Fore.BLUE}{item_dir.name}")
                structure_directory(item_dir, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item_dir.name}") 
    except FileNotFoundError:
        print(Fore.RED + f"Дерикторію {directory} не знайдено")
    except Exception as e:
        print(Fore.RED + f"Виникла несподівана помилка: {e}")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Використовуйте: python main.py <шлях\до\вашої\дерикторії>")
        sys.exit(1)
    directory_path = Path(sys.argv[1])
    if not directory_path.exists():
        print(Fore.RED + f"ПОМИЛКА: Шлях {directory_path} не існує.")
        sys.exit(1)  
structure_directory(directory_path)          
