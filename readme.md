# 微信读书爬虫 wereader
作者 @arry-lee

## 主要功能

1. 获取书架上的书籍列表 get_bookshelf
2. 获取某本书的详情 get_bookinfo
3. 获取某本书的目录 get_chapters
4. 获取某本书你的全部笔记 get_bookmarklist
5. 获取你的所有有笔记本书单 get_notebooklist
6. 获取某一本书的热门划线 get_bestbookmarks


具体代码见 wereader.py

## 使用方法
- 浏览器打开 https://x.weread.qq.com
- 微信扫码登录 确认，提示没有权限忽略即可
- F12 获取 Cookie 字符串拷贝到 settings.py 中
- Cookie 一段时间就会失效 必须重新登录获取


如有帮助，请给个小星星！
有什么问题也可以提 issue。