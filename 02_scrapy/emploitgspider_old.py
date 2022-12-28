'''
    Emploitg Spider
'''

import re
import scrapy


BASE_URL = 'https://www.emploi.tg'


class EmploitgSpider(scrapy.Spider):
    '''Emploitg Spider Class'''
    name = 'emploitg'
    start_urls = ['https://www.emploi.tg/recherche-jobs-togo?page=0']

    def parse(self, response):
        for job in response.css('div.job-title'):
            job_title = job.css('h5').css('a::text').get()
            
            try:
                recruiter = job.css('p.job-recruiter').css('a::text').get()
            except:
                recruiter = job.css('p.job-recruiter').css('a::text').get()
            
            overview = job.css('div.search-description::text').get()
            
            try:
                skills = job.css('div.job-tags').css('div.badge::text').getall()
            except:
                skills = job.css('div.job-tags').css('div.badge::text').getall()
            
            regions =  re.split('-|&', job.css('p::text')[-1].get().split(':')[1].replace(' ', ''))
            
            publish_date =  job.css('p.job-recruiter::text').get().split('|')[0].strip()
            
            try:
                link =  job.css('h5').css('a').attrib['href']
            except:
                link =  job.css('h5').css('a').attrib['href']
                
            yield {
                    'job_title': job_title,
                    'recruiter': recruiter,
                    'overview': overview,
                    'skills': skills,
                    'regions': regions,
                    'publish_date': publish_date,
                    'link': BASE_URL + link
                }
