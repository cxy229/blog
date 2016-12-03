个人博客
- 网址 [www.cuizixin.top](http://www.cuizixin.top)

### post格式
```
---
layout     : post
title      : glossaries
categories : [English]
tags       : [notes]
---
```
- `timing: false` 默认文章在时间轴页面显示, false为不显示
- `life: true` 若life为true，文章改在生活页面显示
- `permalink: /life.html` 修改文章URL为自定义URL

### 添加图片
- 例如
<p>{{ site.blog.qiniu }}</p>
`<br><img src={{ site.blog.qiniu }}"b22dabc5b72748509379fd2c7837dfcd.png" height="400"><br>`
<br><img src={{ site.blog.qiniu }}"b22dabc5b72748509379fd2c7837dfcd.png" height="400"><br>

### 支持`LaTeX`

在需要用到公式的地方用$$ $$括起来

例如：
`$$E=mc^2$$`
