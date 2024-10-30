import PyPDF2
import itertools
import string
import concurrent.futures
from Crypto.Cipher import AES

def attempt_password(reader, prefix, middle, suffix):
    password = prefix + ''.join(middle) + suffix
    try:
        result = reader.decrypt(password)
        if result == 1:
            print(f"Tentativo con password: {password} (correct)")
            return password
        else:
            print(f"Tentativo con password: {password} (failed)")
    except PyPDF2.errors.DependencyError as e:
        print("Errore: PyCryptodome è richiesto per l'algoritmo AES. Assicurati di aver installato PyCryptodome.")
        return None
    except Exception as e:
        print(f"Tentativo con password: {password} (failed)")
    return None

def pdf_brute_force(file_path):
    # Definizione dei parametri di ricerca della password
    prefix = "xxx"
    suffix = "789"
    length = 10 - len(prefix) - len(suffix)  # Lunghezza della parte centrale della password

    # Caratteri che possono essere utilizzati nella password
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    # Carica il PDF
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        if not reader.is_encrypted:
            print("Il file PDF non è protetto da password.")
            return

        # Generazione di tutte le combinazioni possibili per la parte centrale della password
        combinations = itertools.product(chars, repeat=length)

        # Tentativi in parallelo
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_password = {executor.submit(attempt_password, reader, prefix, middle, suffix): middle for middle in combinations}
            for future in concurrent.futures.as_completed(future_to_password):
                result = future.result()
                if result:
                    print(f"Password trovata: {result}")
                    return

        print("Password non trovata.")

# Specificare il percorso del file PDF
directory = r"path of pdf"
pdf_brute_force(directory)