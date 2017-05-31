## Background

This contains the scripts to scrape the courtcases and make the data available through API. Scrapping is a very heavy process, takings days to complete the process. Don't do the scrapping regularly and use the API to use the courtcases data. 

## Scrapping Courtcases

### Requirements for scrapping

* `pip install scrapy`
* `pip install peewee`
* `pip install MySQL-python`

### Running the scrapy

* Cleanup data for fresh scrapping `mysql -uroot -p -e "DROP DATABASE IF EXISTS moldova_courtcases;CREATE DATABASE moldova_courtcases CHARACTER SET utf8 COLLATE utf8_general_ci;"`
* copy `dbconfig.py.bak` to `dbconfig.py` and update database information
* `scrapy list` should show the spider name
* `scrapy crawl Cases` will start to crawl, create html file and save to database

### Scrapy with pause and resume

* follow https://doc.scrapy.org/en/latest/topics/jobs.html 
* `scrapy crawl Cases -s JOBDIR=crawls/cases-1` to pause and restart the job
* `ctrl+c` to stop and above command to restart again

### Testing Scrapy in Shell

* Run `scrapy shell https://cac.instante.justice.md/ro/hot`
* You may run scrapy code and see the results one by one
    * Run the followings one line at a time
    ```
    from scrapy.selector import Selector
    decisions = sel.xpath('//table/tbody/tr')
    courtName = sel.xpath('//h2[contains(@class,"site-name")]/a/text()').extract()
    courtName
    ```
    * You will see the court name in the shell
* Once it works, then copy the working code in the sourcefile

## API

### Requirements

* `pip install flask`
* `pip install gunicorn`

### Testing API

* `python api.py` will serve the API in port 8090.

#### Running API in CentOS-based server

* copy `moldovacourts_api.service.bak` to `moldovacourts_api.service` and update the project directory information
* create soft-link `ln -s /home/moldova-ocds/pydev/src/moldovacourts/moldovacourts_api.service /etc/systemd/system/moldovacourts_api.service`
* `systemctl start moldovacourts_api.service` to start the moldova_api gunicorn server

### Using API

* `domain:8090/courtcasescount?q=name` gives the count of cases for the given company name
* `domain:8090/courtcases?q=name` gives the cases lists in json for the given company name

```
[
  {
    "caseNumber": "26-2-587-02022017", 
    "caseType": "Civil", 
    "court": "Judec\u0103toria Drochia", 
    "deliveryDate": "", 
    "theme": "Ac\u021biuni privind \u00eencasarea datoriei", 
    "title": "AE\u00ce Sofmicrocredit vs R\u0103di\u021b\u0103 Igor Profire, \u021aurlea Violeta, Banu Sergiu - \u00eencasarea datoriei"
  }, 
  {
    "caseNumber": "20-2c-5683-27022017", 
    "caseType": "Civil", 
    "court": "Judec\u0103toria Chi\u0219in\u0103u", 
    "deliveryDate": "", 
    "theme": "Litigii privind executarea obligatiilor", 
    "title": "Casa Nationala de Asigurari So vs SRL Ladita Fermecata"
  }, 
  ...
]
```
