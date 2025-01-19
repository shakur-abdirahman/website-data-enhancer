import requests
from bs4 import BeautifulSoup
import csv
from autogen import ConversableAgent

def fetch_and_crawl_website(url):
    """Fetch and crawl a website to extract its content, limiting to 1000 characters."""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return f"Failed to fetch website: Status code {response.status_code}"
        
        soup = BeautifulSoup(response.content, "html.parser")
        text = ' '.join(soup.stripped_strings)[:1000]  # Limit to 1000 characters
        return text if text else "No visible text found."
    except requests.exceptions.RequestException as e:
        return f"Error fetching website: {str(e)}"

def main():
    # Agent configuration with API key included
    api_key = ""  # Replace with your actual API key
    config_list = [{"model": "gpt-3.5-turbo", "api_key": api_key}]
    llm_config = {"config_list": config_list, "temperature": 0.7}

    agent = ConversableAgent(
        name="web_crawler",
        llm_config=llm_config,
        human_input_mode="NEVER",
    )

    # Read URLs from websites.csv
    input_file = "websites.csv"
    output_file = "page-extract.csv"

    with open(input_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer.writerow(["Website", "Summary"])  # Write header to output file

        for row in reader:
            if not row: continue  # Skip empty rows
            url = row[0].strip()
            print(f"Processing {url}...")

            # Fetch and summarise website content
            website_content = fetch_and_crawl_website(url)
            if "Failed to fetch" not in website_content and "Error fetching" not in website_content:
                reply = agent.generate_reply(
                    messages=[
                        {"content": f"Summarise the following content and identify what the website does:\n\n{website_content}", "role": "user"}
                    ]
                )
                summary = reply.strip()
            else:
                summary = website_content  # Use error message as summary

            # Write result to CSV
            writer.writerow([url, summary])

    print(f"Processing complete! Results saved to {output_file}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}")