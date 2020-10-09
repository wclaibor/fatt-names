from pathlib import Path
from textgenrnn import textgenrnn
from spellchecker import SpellChecker

nameCsv = Path('./FaTTNames.csv')

textgen = textgenrnn()

textgen.train_from_file(nameCsv, batch_size=256, train_size=0.8, is_csv=1, dropout=0.05)
textgen.generate_to_file('./names50.txt', n=100)

spellChecker = SpellChecker()
