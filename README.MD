# 青年大学习截图生成器

## 修改

- 在原有基础上，将图片P成像从公众号截图完成的样子
- 生成的截图的顶部字体（`“青年大学习”第x季第x期`）随机，这里只放了三个，可以自己添加字体到`font`以生成更多不同样子的截图
- 添加docker部署选项

## 使用

### 本地使用

默认是为Docker部署准备的，使用前修改一下`MainServer.py`中：

```diff
- app.run(host='0.0.0.0',port=5000)
+ app.run(host='127.0.0.1',port=5000)
```

1. 运行脚本

   ```
   python MainSever.py
   ```

2. 打开浏览器访问`127.0.0.1:5000`，如果5000端口被占用，修改`MainSever.py`中的port：

   ```diff
   - app.run(host='127.0.0.1',port=5000)
   + app.run(host='127.0.0.1',port=new-port)
   ```

### Docker部署

查看[docker-qndxx](https://github.com/umm233/docker-qndxx)

---

**以上，以混**🙄

