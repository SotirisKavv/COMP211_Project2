To test the program, run python3 computeSales.py < inputCommands | grep -v "^$" | rev | grep ^[0-9] | cut -f1,2 -d  | rev
