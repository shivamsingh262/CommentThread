# CommentThread
Disqus clone in Japronto framework (for learning purposes)

To do list:
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

License
----

MIT


   [japronto]: <https://github.com/squeaky-pl/japronto>
   [mongoengine]: <https://github.com/MongoEngine/mongoengine>
