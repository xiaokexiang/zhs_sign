# 科学上网签到脚本

---
<p style="text-align: center">
    <img src="https://img.shields.io/badge/create-2021.01.11-brightgreen" alt="2021.01.11"/>
    <img src="https://img.shields.io/badge/python-3.9-blue" alt="python-3.9"/>
    <img src="https://img.shields.io/badge/github%20-workflow-orange" alt="github action"/>
    <img src="https://img.shields.io/badge/License-GPL-yellow" alt="GPL"/>
</p>

### 特别声明
<b>此脚本只用于学习、测试使用，请勿将此项目的任何内容用于商业或非法目的！本人概不负责！</b>

### Step1

Fork [此项目](https://github.com/xiaokexiang/zhs_sign) ，并添加如下`Secret`到<b>`Settings -> Secrets`</b>中：

| key                 | 作用                     |
| ------------------- | ------------------------ |
| <b>`ZHS_COOKIE`</b> | 用于科学上网签到的cookie |
| <b>`PUSH_KEY`</b>   | 用于推送到微信的密钥     |
| <b>`BARK_PUSH_KEY`</b>   | 基于bark的推送    |
| <b>`PROXY_LOCK`</b>   | True/False 开启、关闭代理     |

### Step2

Cookie的复制方法，浏览器访问[网站（国内ip无法访问）](https://zhs.today/user)并登录，`F12`或`Ctrl + Shift + i`打开浏览器控制台，选择`Console`，输入命令：`copy(document.cookie)`并回车就会自动复制。

### Step3

- 推送信息至微信基于[server酱](http://sc.ftqq.com/3.version)，右上角使用github账号登录，然后点击发送消息菜单，并复制<b>`SCKEY`</b>
- 也支持基于[bark](https://github.com/Finb/Bark)的推送，可以推送到手机端，需要下载app
### Step4

1. 基于`Github action`实现脚本自动执行，如果不清楚`Github action`，点击[此处](http://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html)查看入门教程。
2. 定时任务执行基于`Cron`，如果不清楚点击[此处](https://leejay.top/post/linux%E4%B8%8Bcron%E5%AE%9A%E6%97%B6%E5%99%A8/)了解。
3. 可以自行编辑`.github/workflows/zhs_sign.yml`中的`cron: '0 1 * * *'`配置来修改脚本的触发事件，
也可以通过修改`README.md`文件，触发push的操作来执行脚本。

### TODO

- ~~基于Github Action的定时执行~~
- ~~基于bark推送信息（server前途未卜）~~

