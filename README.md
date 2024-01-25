Welcome to Castle Chess, your friendly tournament management companion! This Python application helps you manage club players, organize tournaments, and generate reports with ease.

Quick Start:

Install dependencies:

Run python -m venv env to create a virtual environment.
Activate the environment: source env/bin/activate.
Install dependencies: pip install -r requirements.txt.
Run the application:

Run python app.py from the project directory.
Follow the prompts:

Choose to create a new tournament or manage an existing one.
Register players, enter match results, advance rounds, and generate reports.
Features:

Manage clubs and players.
Create and manage tournaments with rounds and schedules.
Enter match results and track player standings.
Generate printable reports in plain text or HTML format.
Maintain data persistence via JSON files.
Instructions:

Setup:

Create directories for data/clubs and data/tournaments to store club and tournament data.
Edit app.py and tournaments.py to customize settings like number of rounds and default pairings logic.
Usage:

The Main Screen displays available tournaments and actions.
Choose actions like registering players, entering results, advancing rounds, or generating reports.
Follow the prompts and use clear menus to navigate the application.
Report Generation:

From the tournament screen, choose "Generate Report".
The output will be displayed in either plain text or HTML (depending on settings).
The HTML report will be saved in the flake8_report/index.html file.
Additional Notes:

For code quality checks, run flake8 and refer to the generated report for style and formatting suggestions.
Feel free to modify and extend the code to suit your specific needs.