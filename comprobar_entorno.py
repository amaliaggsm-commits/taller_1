from pathlib import Path
import sys
import ipykernel
print(f"Python: {sys.version.split()[0]}")
print(f"Intérprete: {sys.executable}")
print(f"Proyecto: {Path.cwd()}")
print(f"ipykernel: {ipykernel.__version__}")