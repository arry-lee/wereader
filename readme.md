# 微信读书爬虫 wereader
作者 @arry-lee

## 主要功能

1. 获取书架上的书籍列表 get_bookshelf
2. 获取某本书的详情 get_bookinfo
3. 获取某本书的目录 get_chapters
4. 获取某本书你的全部笔记 get_bookmarklist
5. 获取你的所有有笔记的书单 get_notebooklist
6. 获取某一本书的热门划线 get_bestbookmarks

具体代码见 wereader.py

## 使用方法
1. 下载或克隆本项目
2. 命令行进入项目文件夹下 `python client.py` 运行客户端 client.py
3. 首次运行，根据提示粘贴cookie

## 获取cookie方法
以谷歌Chrome浏览器为例
- 浏览器打开 https://x.weread.qq.com
- 微信扫码登录确认，提示没有权限忽略即可
- 按F12进入开发者模式，依次点 Network -> Doc -> Headers-> cookie。复制 Cookie 字符串; 由于Cookie一段时间就会失效, 此后可重新登录获取

本项目如对您有所帮助，请给作者个小星星，谢谢~~~ 如有什么需求和问题也可以提 issue。