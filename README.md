# Hinglish-translation-from-English-text

This Python project demonstrates a simple translation pipeline using the spaCy and Googletrans libraries. It translates English sentences to Hindi while preserving nouns in English.

## Prerequisites

Before running the project, ensure you have the following prerequisites installed:

- Python 3.x
- `spacy` library
- `googletrans` library
## Project Structure
The project directory structure looks like this:
Assignment/ 

  ├── app.py
  
  ├── templates/
  │   └── index.html
  ├── static/
  ├── translation_code.py
  └── README.md


You can install the required libraries using `pip`:

```bash
pip install spacy googletrans==4.0.0-rc1
python -m spacy download en_core_web_sm

