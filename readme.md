## Issues

* If you get this error - You are linking against OpenSSL 0.9.8, which is no longer 
  * Run the following command `export CRYPTOGRAPHY_ALLOW_OPENSSL_098=1`

## Requirements

* pip install scrapy
* pip install peewee
* pip install MySQL-python


## Testing Scrapy in Shell

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
    * With hit and trial, i managed to read the value of pdf-base64 using `decision.xpath('.//td[contains(@class, "views-field views-field-base-url")]/form/input/@value').extract()[0]` in the shell
* Once it works, then copy the working code in the sourcefile

## Storing scrapped items to database

* follow instructions from http://stackoverflow.com/questions/10845839/writing-items-to-a-mysql-database-in-scrapy
* follow the tutorials https://github.com/scrapy/quotesbot, need to follow the scrapy process to make this work
* `scrapy startproject courtcases` and do the necessary coding

## Running the scrapy

* copy `dbconfig.py.back` to `dbconfig.py` and update database information
* `scrapy list` should show the spider name
* `scrapy crawl Cases` will start to crawl, create html file and save to database

### Scrapy with pause and resume

* follow https://doc.scrapy.org/en/latest/topics/jobs.html 
* `scrapy crawl Cases -s JOBDIR=crawls/cases-1` to pause and restart the job
* `ctrl+c` to stop and above command to restart again

## If testing scrapy with python file without any pipelines

* `scrapy runspider run.py -t csv -o all.csv` will write to csv file

## clean up database for fresh scrapping

mysql -uroot -p -e "DROP DATABASE IF EXISTS moldova_courtcases;CREATE DATABASE moldova_courtcases CHARACTER SET utf8 COLLATE utf8_general_ci;"








