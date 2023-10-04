# Hinglish-translation-from-English-text
## Prerequisites

Before running the project, ensure that you have the following dependencies installed:

- Python 3.x
- Flask
- spaCy (with the English language model)
- googletrans==4.0.0-rc1

You can install the required libraries using pip:


```bash
    pip install Flask spacy googletrans==4.0.0-rc1
    python -m spacy download en_core_web_sm
```

## Project Structure
The project structure should look like this:
project_folder/

    ├── app.py
    |
    ├── templates/
    |   |
    │   └── index.html
    |
    ├── static/
    |
    └── translation_code.py

1. app.py: Contains the Flask application code.
2. templates/index.html: The HTML template for the translation interface.
3. static/: A directory for static files (e.g., CSS, JavaScript), if needed.
4. translation_code.py: Contains the translation logic

## Usage
1. Clone this repository to your local machine or download the source code.
2. Navigate to the project directory.
3. Run the Flask application:
```bash
python app.py
```
4. Open a web browser and go to http://127.0.0.1:5000.
5. Enter an English sentence in the input field and click "Translate."
6. The translated sentence will be displayed on the web page.


![Screenshot (187)](https://github.com/SAMBANGI-RAJU/Hinglish-translation-from-English-text/assets/115488085/db2df687-0e47-44d5-a229-85418aa1b2db)

## Demo

https://github.com/SAMBANGI-RAJU/Hinglish-translation-from-English-text/assets/115488085/674b8190-a34e-492f-9ce4-51daba77745a




