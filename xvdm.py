#X Video Download Manager main by xingyujie(xingyujie50@gmail.com)
#copyleft 2022 xingyujie
import os, re
import pywebio
import pywebio.input
import webbrowser
from pywebio.input import *
from pywebio.output import *
from pywebio import *
from pywebio.session import *
import time
print("""
Welcome to X Video Download Manager!
The service starts on port 22948 (http), the program will automatically open the browser, if not, please manually open http://localhost:22948 in the browser
""")
#webbrowser.open("http://localhost:22948")
def head():
    set_env(title="X Video Download Manager", auto_scroll_bottom=True)

def downloadernavbarhead():
    set_env(title="X Video Download Manager", auto_scroll_bottom=True)
    put_html("""
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="http://localhost:22948"></a>
    X Video Download Manager
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link" aria-current="page" href="http://localhost:22948/">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link active" href="http://localhost:22948/?app=downloader">Downloader</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Video website
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="http://youtube.com">Youtube</a>
          <a class="dropdown-item" href="http://bilibili.com">bilibili</a>
          <a class="dropdown-item" href="http://youku.com">youku</a>
          <a class="dropdown-item" href="http://tiktok.com">Tiktok</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="https://www.yumyumvideos.com/6-amazing-video-websites-that-arent-youtube-wp/">More</a>
        </div>
    </ul>
  </div>
</nav>

""")
def smallwelcomehead():
    put_html("<h1>X Video Download Manager</h1>")
    put_text('Welcome to X Video Download Manager')
    put_markdown('__The best Video Download Software in the world!__')
def bigwelcomehead():
    put_html("""
<div class="jumbotron">
  <h1 class="display-3">Welcome to X Video Download Manager!</h1>
  <p class="lead">This is the best video download tool. It can download online videos to local, files like MP4!</p>
  <hr class="my-4">
  <p>Free and fast, and open source!</p>
  <p class="lead">
    <a class="btn btn-primary btn-lg" href="http://localhost:22948/?app=downloader" role="button">Download video now</a>
  </p>
</div>
    """)
def line():
    put_text('_______________________',
    sep=' '
    )
def messagebox(message):
    os.system(f'mshta vbscript:msgbox("{message}",4,"X Video Download Manager")(window.close)')
def index():
    head()
    bigwelcomehead()
    #go_app("downloader")
    put_markdown("## Features")
    put_link("X Video Download Manager Downloader", url='http://localhost:22948/?app=downloader')
    line()
    put_link("About", url='http://localhost:22948/?app=about')
    line()
    put_link("Github", url='https://github.com/thomaswcy/X Video Download Manager')
def downloader_cmd(linkurl):
    messagebox("Start downloading...")
    if os.path.exists("%HOMEPATH%/Downloads/Video"):
        pass
    else:
        os.system("mkdir %HOMEPATH%/Downloads/Video")

    if re.search("(bilibili|163.com|56.com|acfun|baidu.com|baomihua|douban|douyu|ifeng|fun.tv|iqiyi|joy.cn|ku6.com|kugou|kuwo|le.com|lizhi.fm|lrts|miaopai|miomio|missevan|pixnet|pptv|iqilu|qq.com|weibo|sina|sohu|tudou|isuntv|zhanqi|cntv|mgtv|huomao|356yg|ixigua|xinpianchang|douyin|kuaishou|zhibo.tv|zhihu)", linkurl):
        os.system(f"start you-get.exe -o \"%USERPROFILE%\Downloads\Video\" {linkurl}")
    else:
        os.system(f"start yt-dlp.exe --no-mtime --output \"%USERPROFILE%/Downloads/Video/%(title)s.%(ext)s\"  --merge-output-format mp4 {linkurl}")
def putlink_again():
    put_link("Download other videos", url='http://localhost:22948/?app=downloader')
def downloader():
    downloadernavbarhead()
    smallwelcomehead()
    #put_text("We support video downloads of these websites: bilibili|163.com|56.com|acfun|baidu.com|baomihua|douban|douyu|ifeng|fun.tv|iqiyi|joy.cn|ku6.com|kugou|kuwo|le.com|lizhi.fm|lrts|miaopai|miomio|missevan|pixnet|pptv|iqilu|qq.com|weibo|sina|sohu|tudou|isuntv|zhanqi|cntv|mgtv|huomao|356yg|ixigua|xinpianchang|douyin|kuaishou|zhibo.tv|zhihu")
    downloader_cmd(pywebio.input.input("Please input link:"))
    with put_loading():
      time.sleep(5)
    start = "Start Downloading, Please wait... After the download is complete, the file will be saved to the Downloads/Video folder of your computer"
    toast(start)
    put_success(start)
    putlink_again()
def about():
    head()
    smallwelcomehead()
    put_markdown("## About X Video Download Manager")
    put_markdown("""
X Video Download Manager is made by:

Creator, thought of this project:
[thomaswcy (Topsy Chen)](https://github.com/thomaswcy)

This Project developer:
[xingyujie(Edward Hsing)](https://github.com/xingyujie)

[thomaswcy (Topsy Chen)](https://github.com/thomaswcy)

AGPL-V2.0 Release

""")
    put_html("""
<p align="center">
<img src="https://forthebadge.com/images/badges/built-with-love.svg">
<p>
<p align="center">
<img alt="GitHub All Releases" src="https://img.shields.io/github/downloads/thomaswcy/X Video Download Manager/total?style=for-the-badge">
<img alt="GitHub" src="https://img.shields.io/github/license/thomaswcy/X Video Download Manager?style=for-the-badge">
<p>
    """)
if __name__ == '__main__':
    start_server([index, downloader, about], debug=True, port=22948)
    pywebio.session.hold()
