---
layout     : post
title      : (翻译)SQLAlchemy Object Relational Tutorial
categories : [python]
tags       : [notes]
---
- [原文](http://docs.sqlalchemy.org/en/rel_1_1/orm/tutorial.html)

# Object Relational Tutorial
SQLAlchemy ORM（Object Relational Mapper）做的一件事就是将python中定义的类和数据库中的表联系起来。<br>

## version check

```python
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
1.1.0
```

## connecting

### `create_engine()`

用`create_engine()`连接数据库。<br>

```python
>>> from sqlalchemy import create_engine
>>> engine = create_engine('sqlite:///:memory:', echo=True)
```

`echo=True`表示要打印日志。<br>
`create_engine()`返回类型是`Engine`的一个实例，是数据库的核心接口。<br>

## declare a mapping 

这一部分讲的是怎么构造数据库表对应的python类。<br>

### `declarative_base()`

先生成一个基类`Base`。<br>

```python
>>> from sqlalchemy.ext.declarative import declarative_base

>>> Base = declarative_base()
```

写一下数据库表对应的类`User`，继承`Base`。<br>

```python
>>> from sqlalchemy import Column, Integer, String
>>> class User(Base):
...     __tablename__ = 'users'
...
...     id = Column(Integer, primary_key=True)
...     name = Column(String)
...     fullname = Column(String)
...     password = Column(String)
...
...     def __repr__(self):
...        return "<User(name='%s', fullname='%s', password='%s')>" % (
...                             self.name, self.fullname, self.password)
```

其中`__tablename__`是数据库表的表名，`Column`用来生成一列，`__repr__`用来输出类的信息，为可选项。<br>

## create a schema

### `__table__`

通过`__table__`生成类对应的Schema。<br>

```python
>>> User.__table__ 
Table('users', MetaData(bind=None),
            Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
            Column('name', String(), table=<users>),
            Column('fullname', String(), table=<users>),
            Column('password', String(), table=<users>), schema=None)
```

### `create_all()`

通过`create_all()`在数据库中创建所有的表。<br>

```python
>>> Base.metadata.create_all(engine)
SELECT ...
PRAGMA table_info("users")
()
CREATE TABLE users (
    id INTEGER NOT NULL, name VARCHAR,
    fullname VARCHAR,
    password VARCHAR,
    PRIMARY KEY (id)
)
()
COMMIT
```

## create an instance of the mapped class

```python
>>> ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
>>> ed_user.name
'ed'
>>> ed_user.password
'edspassword'
>>> str(ed_user.id)
'None'
```

## creating a session

`session`是ORM对数据库的句柄(handle)，通过`session`对数据库进行各种操作，比如插入，查询，修改和删除。<br>

```python
>>> from sqlalchemy.orm import sessionmaker
>>> Session = sessionmaker(bind=engine)
```

## adding and updating objects

```python
>>> ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
>>> session.add(ed_user)

>>> session.add_all([
...     User(name='wendy', fullname='Wendy Williams', password='foobar'),
...     User(name='mary', fullname='Mary Contrary', password='xxg527'),
...     User(name='fred', fullname='Fred Flinstone', password='blah')])

>>> session.commit()
```

## rolling back 

## querying 

```python
>>> for instance in session.query(User).order_by(User.id):
...     print(instance.name, instance.fullname)
ed Ed Jones
wendy Wendy Williams
mary Mary Contrary
fred Fred Flinstone

>>> for name, fullname in session.query(User.name, User.fullname):
...     print(name, fullname)
ed Ed Jones
wendy Wendy Williams
mary Mary Contrary
fred Fred Flinstone

>>> for row in session.query(User, User.name).all():
...    print(row.User, row.name)
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')> ed
<User(name='wendy', fullname='Wendy Williams', password='foobar')> wendy
<User(name='mary', fullname='Mary Contrary', password='xxg527')> mary
<User(name='fred', fullname='Fred Flinstone', password='blah')> fred

>>> for row in session.query(User.name.label('name_label')).all():
...    print(row.name_label)
ed
wendy
mary
fred

>>> from sqlalchemy.orm import aliased
>>> user_alias = aliased(User, name='user_alias')
```

### 给类起别名

```python
SQL>>> for row in session.query(user_alias, user_alias.name).all():
...    print(row.user_alias)
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
<User(name='wendy', fullname='Wendy Williams', password='foobar')>
<User(name='mary', fullname='Mary Contrary', password='xxg527')>
<User(name='fred', fullname='Fred Flinstone', password='blah')>
```

### limit

```python
>>> for u in session.query(User).order_by(User.id)[1:3]:
...    print(u)
<User(name='wendy', fullname='Wendy Williams', password='foobar')>
<User(name='mary', fullname='Mary Contrary', password='xxg527')>
```

### filter_by() 和 filter()

```python
>>> for name, in session.query(User.name).\
...             filter_by(fullname='Ed Jones'):
...    print(name)
ed

>>> for name, in session.query(User.name).\
...             filter(User.fullname=='Ed Jones'):
...    print(name)
ed

>>> for user in session.query(User).\
...          filter(User.name=='ed').\
...          filter(User.fullname=='Ed Jones'):
...    print(user)
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
```

### common filter operators

#### `equals`

```python
query.filter(User.name == 'ed')
```

#### `not equals`

```python
query.filter(User.name != 'ed')
```

#### `like`

```python
query.filter(User.name.like('%ed%'))
```

#### `in`

```python
query.filter(User.name.in_(['ed', 'wendy', 'jack']))

# works with query objects too:
query.filter(User.name.in_(
        session.query(User.name).filter(User.name.like('%ed%'))
))
```

#### `not in`

```python
query.filter(~User.name.in_(['ed', 'wendy', 'jack']))
```

#### `is null`

```python
query.filter(User.name == None)

# alternatively, if pep8/linters are a concern
query.filter(User.name.is_(None))
```

#### `is not null`

```python
query.filter(User.name != None)

# alternatively, if pep8/linters are a concern
query.filter(User.name.isnot(None))
```

#### `and`

```python
# use and_()
from sqlalchemy import and_
query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))

# or send multiple expressions to .filter()
query.filter(User.name == 'ed', User.fullname == 'Ed Jones')

# or chain multiple filter()/filter_by() calls
query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')
```

#### `or`

```python
from sqlalchemy import or_
query.filter(or_(User.name == 'ed', User.name == 'wendy'))
```

#### `match`

```python
query.filter(User.name.match('wendy'))
```

### returning lists and scalars

#### `all()` 返回一个 list

```python
>>> query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)
SQL>>> query.all()
[<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>,
      <User(name='fred', fullname='Fred Flinstone', password='blah')>]
```

#### `first()` 返回第一个值

```python
>>> query.first()
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
```

### using textual SQL

#### `from_statemnet(text())`

```python
>>> session.query(User).from_statement(
...                     text("SELECT * FROM users where name=:name")).\
...                     params(name='ed').all()
[<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>]
```

#### `.columns()`

```python
>>> stmt = text("SELECT name, id, fullname, password "
...             "FROM users where name=:name")
>>> stmt = stmt.columns(User.name, User.id, User.fullname, User.password)
SQL>>> session.query(User).from_statement(stmt).params(name='ed').all()
[<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>]
```

### counting 

```python
>>> session.query(User).filter(User.name.like('%ed')).count()
2
```

```python
>>> from sqlalchemy import func
SQL>>> session.query(func.count(User.name), User.name).group_by(User.name).all()
[(1, u'ed'), (1, u'fred'), (1, u'mary'), (1, u'wendy')]
```

```python
>>> session.query(func.count('*')).select_from(User).scalar()
4
```

## building a realationship

## working with related objects

## querying with joins

### using aliases

### using subqueries

### selecting entities from subqueries

### using EXISTS

### common relationship operators

## eager loading

### subquery load

### joined load

### explicit join + eagerload

## deleting

### configuring delete/delete-orphan cascade

## building a many to many relationship

## further reference 
