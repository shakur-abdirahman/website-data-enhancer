This project fetches website content using requests and BeautifulSoup, summarises the content using an AI agent (ConversableAgent from the autogen library), and outputs the website URL along with the summary into a CSV file.

Features
	•	Fetches website content up to 1000 characters.
	•	Summarises the content using a GPT-4-powered agent.
	•	Outputs the website URL and summary in a page-extract.csv file.
	•	Reads URLs from an input file (websites.csv).
	•	Handles errors gracefully and includes them in the output.

Requirements
	•	Python 3.x
	•	requests library
	•	BeautifulSoup from bs4 for web scraping
	•	autogen library for AI interactions
	•	csv module (builtin)
