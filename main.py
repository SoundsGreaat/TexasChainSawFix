import os
import subprocess
import keyboard
from colorama import Fore, Style


def find_and_launch_game(game_name):
    try:
        powershell_command = f'Get-AppxPackage *{game_name}* | Select-Object -ExpandProperty InstallLocation'
        result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)

        if result.stdout:
            install_location = result.stdout.strip() + r'\start_protected_game.exe'
            print(f'Game found at: {install_location}')
            subprocess.Popen(f'explorer "{install_location}"')
            print(f'{Fore.GREEN}Game launched{Style.RESET_ALL}')
        else:
            print(f'{Fore.RED}Game not found{Style.RESET_ALL}')
    except Exception as e:
        print(f'{Fore.RED}Error{Style.RESET_ALL}: {e}')


def kill_explorer():
    os.system('chcp 65001 && taskkill /f /im explorer.exe')


def run_explorer():
    os.system('chcp 65001 && explorer.exe')


def main():
    find_and_launch_game('GunMedia.TheTexasChainSawMassacre-PCEdition')
    print(f'\nPress {Fore.BLUE}"Caps Lock"{Style.RESET_ALL} to kill explorer.exe')
    print(f'Press {Fore.BLUE}"Alt + Home"{Style.RESET_ALL} to run explorer.exe')

    keyboard.add_hotkey('caps lock', kill_explorer)
    keyboard.add_hotkey('alt+home', run_explorer)
    keyboard.wait('ctrl+shift+q')


if __name__ == '__main__':
    main()
