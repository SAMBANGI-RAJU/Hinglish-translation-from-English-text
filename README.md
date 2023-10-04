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

`app.py: Contains the Flask application code.
``templates/index.html: The HTML template for the translation interface.
``static/: A directory for static files (e.g., CSS, JavaScript), if needed.
`translation_code.py: Contains the translation logic

## Usage
1. Clone this repository to your local machine or download the source code.
2. Navigate to the project directory.
3. Run the Flask application:

