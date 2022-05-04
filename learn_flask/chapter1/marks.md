```angular2html
@app.route('/')
def view_func():
    pass
```
这种语句注册路由，将URL和接下来的视窗函数绑定起来
使得在访问相应URL的时候使用对应的函数

```angular2html
url_for(view_func, name='xxx')
```
使用该函数能获取对应视窗函数的URL，有动态部分需要另加参数
