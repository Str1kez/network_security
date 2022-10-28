.EXPORT_ALL_VARIABLES:

PYTHONPATH=${PWD}
PYTHON = python3.11
CONDA = conda run python3

caesar_cipher:
	$$PYTHON caesar_cipher/main.py

caesar_hack:
	$$PYTHON caesar_hack/main.py

vigenere_cipher:
	$$PYTHON vigenere_cipher/main.py

xor_cipher:
	$$CONDA xor_cipher/main.py

format:
	$$PYTHON -m black -S -l 120 . && $$PYTHON -m isort .

.PHONY: caesar_cipher caesar_hack vigenere_cipher xor_cipher
