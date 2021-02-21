## Data Engineer Test ##

### Test ###
Create a solution that crawls for articles from a news website, cleanses the response, stores in a
mongo database then makes it available to search via an API.
### Solution ###
* Scrapy framework based crawler which traverses page links recursively and uses xpath to fetch article details and text, then stores to external MongoDB server 
* Flask based REST API using MongoDB text search to get the list of documets containing a keyword
### Installation ###
* Download (or clone) the repo to your computer and unzip it.
* You should have [**Python 3**](https://www.python.org/downloads/) installed in your computer.
#### Use the package manager [pip](https://pip.pypa.io/en/stable/) to install these required packages :

 - [PyMongo](https://api.mongodb.com/python/current/)  
```bash
pip install pymongo
```
 - [DNS PYTHON](http://www.dnspython.org/)  
```bash
pip install dnspython
```
 - [Natural Language Toolkit](https://www.nltk.org/)  
```bash
pip install nltk
```
### Usage ###
Web crawler can accept either one url or a file containing line-separated urls as a command line parameter

For one url please use: `scrapy crawl news -a url={your_url}`

For a file please use: `scrapy crawl news -a filename={your_url_list_file}`

API is running on 0.0.0.0:5000

API search function is available at /getnews/:keyword, method=GET
