







#::::::::::::blog.py class:::::::::::::::::::::::::::::::::::::::::::::


import uuid
import datetime
from models.post import Post
from database import Database
_author_ = 'Greg'


class Blog(object):
    def _init_(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date, or leave blank for today (in format DDMMYYYY): ")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=datetime.datetime.strptime(date, "%d%m%y"))
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }
    #:::::::::::::::Decided to use classmethod later
    # @staticmethod
    # def get_from_mongo(self):
    #     blog_data = Database.find_one(collection='blog',
    #                                   query={'id': id})
    #     return Blog(author=blog_data['author']

    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs',
                                      query={'id': id})
        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   id=blog_data['id'])
                   
                   
                   
                   
            #::::::::::::::::::::::::::::::Blog.py app:::::::::::::::::::::::::::::::::::::::::::::::::::::::::       
                   
                   
                   
from database import Database
from models.blog import Blog

Database.initialize()

blog = Blog(author="Jose",
            title="Sample title",
            description="Sample decscription")

blog.new_post()

blog.save_to_mango()

Blog.from_mango()

from_database =Blog.from_mongo(blog.id)
  #blog.get_posts()        #Post.from blog equivallent

print(blog.get_psosts())



#:::::::::::::::::::::::::::::::::::::Errormsg::::::::::::::::::::::::::::::::::::::::::

C:\Terminal_blog\Scripts\python.exe C:/Users/greg/PycharmProjects/Terminal_blog/app2.py
Traceback (most recent call last):
  File "C:/Users/greg/PycharmProjects/Terminal_blog/app2.py", line 53, in <module>
    blog = Blog(author="Jose",
TypeError: Blog() takes no arguments

Process finished with exit code 1
