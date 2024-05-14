import os
import subprocess

import keyboard


def find_directory(name, path):
    for root, dirs, files in os.walk(path):
        if name in dirs:
            return os.path.join(root, name)


def kill_explorer():
    os.system('chcp 65001 && taskkill /f /im explorer.exe')


def run_explorer():
    os.system('chcp 65001 && explorer.exe')


def main():
    print(f'Game found at: {dir_path}')
    exe_path = dir_path + r'\Content\start_protected_game.exe'
    print(f'Game path: {exe_path}')
    print('\nPress "Caps Lock" to kill explorer.exe.')
    print('Press "Alt + Home" to run explorer.exe.')

    subprocess.run(exe_path)

    keyboard.add_hotkey('caps lock', kill_explorer)
    keyboard.add_hotkey('alt+home', run_explorer)
    keyboard.wait('ctrl+shift+q')


if __name__ == '__main__':
    dir_path = find_directory('The Texas Chain Saw Massacre - PC Edition', 'D:\\')
    if dir_path:
        main()
    else:
        print('Game not found.')
