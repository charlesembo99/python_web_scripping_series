from bs4 import BeautifulSoup
import requests
import time
print("Input some skills that you are not familiar with")
unfamiliar_skills = input('>..')
print(f'filtering out {unfamiliar_skills}')
def findJob():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_= 'clearfix job-bx wht-shd-bx')

    for index,job in enumerate(jobs):
        published_date = job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_= 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(f'./Scrapped_data/{index}','w') as f:
                    f.write(f'company name: {company_name.strip()} \n')
                    f.write(f'Required name: {skills.strip()} \n')
                    f.write(f'More info: {more_info}')
                print(f'file saved{index}')    

if __name__== '__main__':
    while True:
        findJob()
        time_wait = 10
        print(f'waiting for {time_wait} minutes')
        time.sleep(time_wait*60)
