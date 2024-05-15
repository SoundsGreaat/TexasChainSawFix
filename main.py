import subprocess
import threading
import keyboard

from colorama import Fore, Style
from art import text2art
from time import sleep

game_launched = False


def find_and_launch_game(game_name):
    try:
        powershell_command = f'Get-AppxPackage *{game_name}* | Select-Object -ExpandProperty InstallLocation'
        result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)

        if result.stdout:
            install_location = result.stdout.strip() + r'\start_protected_game.exe'
            print(f'Game found at: {install_location}')
            subprocess.Popen(f'explorer "{install_location}"')
            print(f'{Fore.YELLOW}Game launches...{Style.RESET_ALL}')
        else:
            print(f'{Fore.RED}Game not found{Style.RESET_ALL}')
    except Exception as e:
        print(f'{Fore.RED}Error{Style.RESET_ALL}: {e}')


def check_process(process_name):
    command = f'if (Get-Process -Name {process_name} -ErrorAction SilentlyContinue) {{ exit 0 }} else {{ exit 1 }}'
    result = subprocess.run(["powershell", "-Command", command], capture_output=True)
    return result.returncode == 0


def check_process_loop(process_name):
    while True:
        if not check_process(process_name):
            run_explorer()
            print(f'{Fore.RED}Game closed{Style.RESET_ALL}')
            break
        sleep(1)


def kill_explorer():
    subprocess.run('chcp 65001 && taskkill /f /im explorer.exe', shell=True, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)
    print(f'{Fore.GREEN}Explorer.exe killed{Style.RESET_ALL}')


def run_explorer():
    subprocess.run('chcp 65001 && explorer.exe', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f'{Fore.GREEN}Explorer.exe started{Style.RESET_ALL}')


def main():
    global game_launched
    print(text2art('TexasChainSawFix'))
    print(text2art('by SoundsGreaat', font='small'))
    find_and_launch_game('GunMedia.TheTexasChainSawMassacre-PCEdition')

    while True:
        if check_process('BBQClient-WinGDK-Shipping'):
            game_launched = True
            print(f'{Fore.GREEN}Game launched successfully{Style.RESET_ALL}')
            break

    threading.Thread(target=check_process_loop, args=('BBQClient-WinGDK-Shipping',)).start()

    print(f'\nPress {Fore.BLUE}"Caps Lock"{Style.RESET_ALL} to kill explorer.exe')
    print(f'Press {Fore.BLUE}"Alt + Home"{Style.RESET_ALL} to run explorer.exe\n')

    keyboard.add_hotkey('caps lock', kill_explorer)
    keyboard.add_hotkey('alt+home', run_explorer)
    keyboard.wait('ctrl+shift+q')


if __name__ == '__main__':
    main()
