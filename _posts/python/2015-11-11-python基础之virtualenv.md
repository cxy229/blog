---
layout     : post
title      : python基础之virtualenv
categories : [python]
tags       : [notes]
---
* [文档https://virtualenv.pypa.io/en/latest/](https://virtualenv.pypa.io/en/latest/)
* [http://flask.pocoo.org/docs/0.10/installation/#virtualenv](http://flask.pocoo.org/docs/0.10/installation/#virtualenv)

```
mkdir myproject
cd myproject
#初始化 使用python3.5
virtualenv --python=/usr/bin/python3.5 venv
#安装
pip3 install aiohttp
```
```
$ mkdir myproject
$ cd myproject
$ virtualenv venv
New python executable in venv/bin/python
Installing distribute............done.
Now, whenever you want to work on a project, you only have to activate the corresponding environment. On OS X and Linux, do the following:

$ . venv/bin/activate
If you are a Windows user, the following command is for you:

$ venv\scripts\activate
Either way, you should now be using your virtualenv (notice how the prompt of your shell has changed to show the active environment).

Now you can just enter the following command to get Flask activated in your virtualenv:

$ pip install Flask
A few seconds later and you are good to go.
```