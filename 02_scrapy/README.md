# Web Scraping with Scrapy
Hello, I'm [Joseph Konka](https://www.linkedin.com/in/joseph-koami-konka/), Python enthousiast. Python provide packages to interact with databases, this is what these notebooks will cover, interaction with databases using Python. I hope it will help you to understand the subject. Bye !

## Setup environment (Windows Git Bash)
```sh
python -m venv env
source env/Scripts/activate
pip install -r requirements.txt
```

## Get started with Scrapy Shell
```bash
$ scrapy shell

>>> fetch('https://www.emploi.tg/recherche-jobs-togo?page=0') 
2022-11-19 07:24:31 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.emploi.tg/recherche-jobs-togo?page=0> (referer: None)

>>> response.css('div.job-title').css('h5').css('a::text').getall()
['Chargé de Clientèle Bilingue', 'Directeur Général', 'Commercial H/F', 'Sales Development Representative', 'Marketing Studies Manager, International Scope', 'Medical Communication Manager', 'Contrôleur de Gestion Expérimenté', 'Secrétaire Comptable H/F', 'Assistant de Direction Opérationnel', 'Commercial H/F', 'Superviseur des Ventes - Togo', 'Chauffeur Professionnel', "Apporteur D'affaire", 
'Commercial H/F', 'Web Designer', 'Développeur D’applications Back End (H/F) -  PHP (SYMFONY, LARAVEL)', 'Développeur D’application Front End Web/Mobile (H/F) - Angular/Ionic', 'Senior Software Backend Engineer NodeJS- Frankfurt, Germany', 'Développeur Junior', 'Responsable Hygiène Sécurité Environnement (H/F) - Lomé', 'Software Developer PHP, Laravel, MySQL- Frankfurt, Germany', 'Senior Software Backend Engineer GoLang- Frankfurt, Germany', 'Enseignant du Primaire et Secondaire', 'Regional Director - West and Central Africa / Sector : N.G.O', 'Gérante Assistante (boutique )']

>>> response.css('div.job-title').css('p.job-recruiter').css('a::text').get()
'MAJOREL'

>>> response.css('div.job-title').css('p.job-recruiter::text').get().split('|')[0].strip() 
'19.11.2022'

```

## Start nwe project
```bash
$ scrapy startproject emploitg

$ scrapy crawl emploitg -O jos.json
```

## Setting
`ROBOTSTXT_OBEY = False`

## Troubleshooting
- [How to ignore robots.txt for Scrapy spiders)](https://www.simplified.guide/scrapy/ignore-robots)

## Let's get in touch
[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/joekakone)](https://github.com/joekakone) [![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/joseph-koami-konka/)](https://www.linkedin.com/in/joseph-koami-konka/) [![Twitter Badge](https://img.shields.io/badge/-Twitter-blue?style=flat-square&logo=Twitter&logoColor=white&link=https://www.twitter.com/joekakone)](https://www.twitter.com/joekakone) [![Gmail Badge](https://img.shields.io/badge/-Gmail-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:joseph.kakone@gmail.com)](mailto:joseph.kakone@gmail.com)