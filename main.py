import requests
from bs4 import BeautifulSoup

# all_jobs = []

# def scrape_page(url):
#     response = requests.get(url)

#     soup = BeautifulSoup(response.content, "html.parser",)

#     jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]
    
#     for job in jobs:
#         title = job.find("span", class_="title").text
#         company, position, region = job.find_all("span", class_="company")

#         if url:
#             url = job.find("div", class_="tooltip").next_sibling["href"]

#         job_data = {
#             "title" : title,
#             "company" : company.text,
#             "position" : position.text,
#             "region" : region.text,
#             "url" : f"https://weworemotely.com{url}",
#         }

#         all_jobs.append(job_data)


# def get_pages(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser",)

#     return len(soup.find("div", class_="pagination").find_all("span", class_="page"))
     

# total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")


# for x in range(total_pages):
#     url=f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
#     scrape_page(url)

# print(len(all_jobs))

url = "https://remoteok.com/remote-python-jobs"

keywords= ["flutter", "python", "golang"]

all_jobs = []

response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    })

def scrape_page(url):
    

    soup = BeautifulSoup(response.content, "html.parser",)

    #jobs = soup.find(id="jobsboard").find_all('tr')
    jobs= soup.find("table", id="jobsboard").find_all("tr", class_="job")
   
    for job in jobs:
        job_details = job.find("td", class_="company")
        title = job.find("td", class_="company").h2.text
        url = job.find("td", class_="company").a["href"]
        print(url)

        job_data = {
            "title" : title,
            # "company" : company.text,
            # "position" : position.text,
            # "region" : region.text,
             "url" : f"https://remoteok.com/remote-jobs/{url}",
        }

        all_jobs.append(job_data)
  
    #jobs2= jobs.find_all("tbody")
#


    #print(jobs)

if response.status_code == 200:
    scrape_page(url)
else :
     print(f"Failed to retrieve the page. Status code: {response.status_code}")
        