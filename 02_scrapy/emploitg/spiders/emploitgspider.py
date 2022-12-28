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
            recruiter = job.css('p.job-recruiter a::text').get()
            yield {
                    'job_title': job.css('h5 a::text').get(),
                    'recruiter': job.css('p.job-recruiter b::text').get() if recruiter is None else recruiter,
                    'overview': job.css('div.search-description::text').get(),
                    'skills': job.css('div.job-tags div.badge::text').getall(),
                    'regions': re.split('-|&', job.css('p::text')[-1].get().split(':')[1].replace(' ', '')),
                    'publish_date': job.css('p.job-recruiter::text').get().split('|')[0].strip(),
                    'link': job.css('h5 a').attrib['href']
                }

        # Go to next page
        next_page = response.css('li.pager-next.active.last a')
        if next_page is not None:
            yield response.follow(BASE_URL + next_page.attrib['href'], callback=self.parse)
