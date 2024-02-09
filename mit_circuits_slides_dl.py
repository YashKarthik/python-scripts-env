import re
import requests
from bs4 import BeautifulSoup

homepage_html = requests.get("https://circuits.mit.edu/S23").content
souped_up_homepage = BeautifulSoup(homepage_html, "html.parser")
all_links = souped_up_homepage.find_all("a")

lec_url_pattern = r"https://circuits.mit.edu/_static/S23/handouts/lec(\w+)/lecture(\w+).pdf"

for link in all_links:
    pdf_url = link.get("href")
    match =  re.match(lec_url_pattern, pdf_url)

    if not match:
        continue

    lec_name = match.group(2)
    print(lec_name, pdf_url)

    pdf_content = requests.get(pdf_url).content

    with open("./pdfs/"+lec_name+".pdf", "wb") as pdf_file:
        pdf_file.write(pdf_content)
