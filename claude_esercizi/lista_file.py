import os

# Stampa la directory di lavoro corrente
print(f"Directory di lavoro corrente: {os.getcwd()}")

# Elenca tutti i file nella directory corrente
print("\nFile nella directory corrente:")
for file in os.listdir('.'):
    print(f" - {file}")

# Verifica specifica per il file vendite.csv
file_da_cercare = 'vendite.csv'
if os.path.exists(file_da_cercare):
    print(f"\nIl file {file_da_cercare} ESISTE!")
else:
    print(f"\nIl file {file_da_cercare} NON esiste nella directory corrente.")