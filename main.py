import shutil
import os
import sys


def backup_files(source_dir, target_dir):
    try:
        if not os.path.exists(source_dir):
            print("Error: El directorio fuente no existe.")
            return False
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        for filename in os.listdir(source_dir):
            shutil.copy(os.path.join(source_dir, filename), target_dir)
        print('Backup completed.')
    except Exception as e:
        print(f" Error durante el backup {e}")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python main.py <source_dir> <target_dir>")
        sys.exit(1)
    backup_files(sys.argv[1], sys.argv[2])
