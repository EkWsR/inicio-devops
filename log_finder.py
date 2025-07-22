#!/usr/bin/env python3
import re
import sys  # Módulo para acceder a los argumentos


def filter_logs_by_year(file_path, year):
    """Filtra líneas de un archivo de logs que contengan un año específico."""
    matching_logs = []
    try:
        with open(file_path, "r") as f:
            for line in f:
                if re.search(str(year), line):
                    matching_logs.append(line.strip())
        return matching_logs
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no se encuentra.")
        return []


def main():
    # Verificar que se pasaron los argumentos correctos
    if len(sys.argv) != 3:
        print("Uso: python3 script.py <archivo> <año>")
        print("Ejemplo: python3 script.py logs.txt 2025")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        year = int(sys.argv[2])
    except ValueError:
        print("Error: El año debe ser un número entero")
        sys.exit(1)

    logs = filter_logs_by_year(file_path, year)
    if logs:
        print(f"Logs encontrados para el año {year}:")
        for log in logs:
            print(f"- {log}")
    else:
        print(f"No se encontraron logs para el año {year}.")


if __name__ == "__main__":
    main()