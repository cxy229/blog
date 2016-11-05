---
layout     : post
title      : sqlalchemy
categories : [English]
tags       : [notes]
---

#### sqlalchemy 遍历
```
with engine_part.connect() as con:

    meta = MetaData(engine_part)
    colla = Table('Colla', meta, autoload=True)

    stm = select([colla])
    rs = con.execute(stm)
    for tmp in rs:
        c = Colla(tmp[1], tmp[2], tmp[3], tmp[4], tmp[5], tmp[6], tmp[7], tmp[8], tmp[9], tmp[10], tmp[11]
        , tmp[12], tmp[13], tmp[14], tmp[15], tmp[16], tmp[17], tmp[18], tmp[19], tmp[20], tmp[21], tmp[22])
        session_all.add(c)
        print(c)
    session_all.commit()
```
