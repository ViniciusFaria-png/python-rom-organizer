import os
import shutil
import zipfile
import py7zr
import rarfile
from pathlib import Path
import re
import stat

def set_permissions(path):
    os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

def rom_organizer(path):
    
    if not os.path.exists(path):
        print(f"The directory {path} does not exist.")
        return

    
    archives = os.listdir(path)
    count = 0


    sufix_pattern = re.compile(r'[\[\(].*?[\]\)]')

    roms = [archive for archive in archives if archive.endswith((
    '.nes', '.fds',  # NES
    '.smc', '.sfc', '.fig', '.swc', '.srm', '.zmv', '.zm4',  # SNES
    '.n64', '.N64', '.z64', '.v64',  # N64
    '.gb', '.gbc',  # Game Boy/Game Boy Color
    '.gba',  # Game Boy Advance
    '.nds',  # Nintendo DS
    '.gen', '.md', '.bin', '.smd', '.32x',  # Sega Genesis/Mega Drive
    '.sms',  # Sega Master System
    '.gg',  # Sega Game Gear
    '.cue', '.iso',  # Sega Saturn, TurboGrafx-CD/PC Engine CD, Neo Geo CD
    '.bin',  # Sega Saturn, Atari 2600, Atari 5200, Atari 7800, PlayStation, Intellivision, Vectrex
    '.cdi', '.gdi', '.mfd',  # Dreamcast
    '.img', '.ccd', '.mdf', '.chd', # PlayStation, PlayStation 2
    '.iso', '.cso',  # PSP, PlayStation 2
    '.a26', '.a52', '.a78',  # Atari 2600, Atari 5200, Atari 7800
    '.lnx',  # Atari Lynx
    '.j64', '.rom',  # Atari Jaguar, ColecoVision, MSX
    '.pce', '.dsk',  # TurboGrafx-16/PC Engine, MSX
    '.ngp', '.ngc',  # Neo Geo Pocket/Neo Geo Pocket Color
    '.ws', '.wsc',  # WonderSwan/WonderSwan Color
    '.d64', '.t64', '.prg',  # Commodore 64
    '.mx1', '.mx2',  # MSX
    '.col',  # ColecoVision
    '.int',  # Intellivision
    '.vec'  # Vectrex
    '.wad', '.linx', '.vb', '.part', '.zip', '.7z', '.rar', '.zm4', '.zmv'
    ))]

    for rom in roms:
        rom_path = os.path.join(path, rom)
        game_name, ext = os.path.splitext(rom)
        clean_game_name = re.sub(sufix_pattern, '', game_name).strip()
        dir_path = os.path.join(path, clean_game_name)

        if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                set_permissions(dir_path)

        if ext in ['.zip', '.7z', '.rar']:
        # Extrair o arquivo ZIP/7Z/RAR para uma pasta de mesmo nome
            try:
                if ext == '.zip':
                    with zipfile.ZipFile(rom_path, 'r') as zip_ref:
                        zip_ref.extractall(dir_path)
                        print(f"ZIP file extracted: {rom} -> {dir_path}")
                elif ext == '.7z':
                    with py7zr.SevenZipFile(rom_path, 'r') as sevenzip_ref:
                        sevenzip_ref.extractall(dir_path)
                        print(f"7z file extracted: {rom} -> {dir_path}")

                elif ext == '.rar':
                    with rarfile.RarFile(rom_path, 'r') as rar_ref:
                        rar_ref.extractall(dir_path)
                        print(f"RAR file extracted: {rom} -> {dir_path}")

                os.remove(rom_path)
                print(f"{type[1:].upper()} file removed: {rom}")
            except PermissionError as e:
                print(f"Permission error when extracting {rom}: {e}")
        else:
            try:
                shutil.move(rom_path, os.path.join(dir_path, rom))
                print(f"Moved: {rom} -> {dir_path}")
            except PermissionError as e:
                print(f"Permission error when moving {rom}: {e}")
        count += 1
    print(f"{count} files processed!!")

def main():
    while True:
        dir_roms = Path(input("Enter the path of the ROMs: "))
        rom_organizer(dir_roms)

        continue_input  = input("Enter 0 to exit, or ENTER to continue: ")
        if continue_input  == "0":
            break

if __name__ == "__main__":
    main()
    
