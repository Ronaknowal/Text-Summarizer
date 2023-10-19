# Text-Summarizer

## Working of this Application :
The Application is Command line based executable under Python Environment and
uses popular Python micro web framework that is FLASK.This Application consist of 2 main pages runs in LocalHost wherein intially a form is given to the user based on the content entered(text+required no of lines+rearrange checkbox) and on submit by the user,Accordingly the Summarizied Content is analyzed with support and importing of some python packages.This data is exported to the next connecting page.


## Software Requirements:
* Python 3+ any version or editors like Pycharm(Used in creating this application in Windows) 
* Install required Python Libraries as follows
## Live Testing The App
Install all the required libraries
```sh
$ pip install -r requirements.txt
```

* For exporting and processing the data,run the following script in new .py (exists as a setup.py file in this repo) file before ruuning the application as follows:
```sh
import nltk
nltk.download('stopwords')
nltk.download('word_tokenize')
nltk.download('sent_tokenize')
```
*  After installing above libraries,we need to import those and use the functionality in this application.

#### In order to run and intialize the application there are 2 alternative methods :

* Method - 1 : Run from Editor in venv and view localhost application in any Browser with link (http://127.0.0.1:5000/)
* Method - 2 : Run from command prompt with specified path location of project by using following command
```sh
python __init__.py
```
