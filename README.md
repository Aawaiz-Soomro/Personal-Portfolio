# Personal Portfolio

This repository contains a minimalist Flask application that renders a dark-mode personal portfolio for "Avery Quinn." The page showcases projects, skills, experience, and contact information with a high-fidelity visual design.

## Getting started

1. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the development server**
   ```bash
   flask --app app.py --debug run
   ```
4. Open [http://127.0.0.1:5000/portfolio](http://127.0.0.1:5000/portfolio) in your browser to view the site.

## Project structure

```
.
├── app.py                 # Entrypoint
├── app
│   ├── __init__.py        # Application factory + routes registration
│   ├── routes.py          # Portfolio blueprint and data
│   ├── static
│   │   └── css
│   │       └── portfolio.css
│   └── templates
│       └── portfolio.html
└── requirements.txt       # Python dependencies
```
