### PDF Password Unlocker

This script attempts to brute-force a password for an encrypted PDF file using a specific password structure. The password is assumed to start with the prefix "xxx" and end with the suffix "789", making the total password length 10 characters.

### Requirements

- Python 3.x
- PyPDF2 library
- pycryptodome library (for handling AES encryption)

To install the required libraries, run the following commands:

```sh
pip install PyPDF2 pycryptodome
```

### Usage

1. Set the path to your PDF file by modifying the `directory` variable in the script.
2. Run the script to start the brute-force process.

```sh
python pdf_brute_force.py
```

The script will attempt to find the password by trying all possible combinations for the middle part of the password, consisting of letters (both lowercase and uppercase) and digits.

### Disclaimer

This script is intended for educational purposes only. Do not use it to access files without the owner's permission. Unauthorized access to files may be illegal.

