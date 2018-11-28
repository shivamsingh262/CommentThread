# CommentThread
Disqus clone in Japronto framework (for learning purposes)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

### To do list:
  - Implement templating system in Jinja2 for thread div
  - CSS + ajax calls
  - Apis:
    - Login
    - Post comment
    - Get comments
    - Upvote/Downvote

### Tech

* [Japronto] - Screaming-fast Python 3.5+ HTTP toolkit
* [Mongoengine] - A Python Object-Document-Mapper for working with MongoDB

### Installation

Install the required libraries and start the server (needs Python 3.5+)

```sh
$ pip install -r requirements.txt
$ python runserver.py
```


   [japronto]: <https://github.com/squeaky-pl/japronto>
   [mongoengine]: <https://github.com/MongoEngine/mongoengine>
