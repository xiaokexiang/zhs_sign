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

Fork [此项目](https://github.com/xiaokexiang/zhs_sign) ，并添加如下`Secret`到<b>`Setting -> Secret`</b>中：

| key                 | 作用                     |
| ------------------- | ------------------------ |
| <b>`ZHS_COOKIE`</b> | 用于科学上网签到的cookie |
| <b>`PUSH_KEY`</b>   | 用于推送到微信的密钥     |

### Step2

Cookie的复制方法，浏览器访问[网站（国内ip无法访问）](https://zhs.today/user)并登录，`F12`或`Ctrl + Shift + i`打开浏览器控制台，选择`Console`，输入命令：`copy(document.cookie)`并回车就会自动复制。

### TODO

- 基于Github Action的定时执行
- 基于账户密码的登录，Cookie具有一周的时效，免于定期替换Cookie