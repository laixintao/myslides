---
title: Awesome Commandline!
author: laixintao
...

# 欢迎！


上大学初学计算机的时候，我们觉得自己只能写出来黑乎乎的命令行，不太酷。一直想做出漂亮的软件，或者优美的网页。然而写程序多年，才发现最喜欢的还是命令行，在命令行中能事半功倍的完成任务，能轻松的结合命令行完成不同的工作。是什么让命令行如此高效，如何利用好命令行？如果你是 ipython 粉，是否想知道如何只通过几行代码，就可以写出具有 ipython 体验的工具？

本期线上分享 iredis 开发的几位同学和大家分享下开发命令行的经验和难点，以及命令行的乐趣。

*分享在 14:00 准时开始...*

---

# 为什么命令行 Awesome ???

---

## The First Power of Command Line

-> **Editor! (Vim/Emacs/etc)**  

- 如何删除多余的 git 分支？
- 如何格式化 json？
- 实用的Ctrl-X Ctrl-E
- 改变一个文件的编码？
- 查看二进制文件(xxd)?

---

## The Second Power of Command Line

-> **Pipe!**

- Tools like fpp/jq
- 连接不同的工具...
- Works every where

将一个文件夹拷贝到远程的服务器:
```bash
tar c . | ssh root@myserver.com "tar xv"
```

---

备份数据库而不占本地的磁盘:

```bash
$ mysqldump --single-transaction -u backuper mydb | \
ssh root@backup.myserver.com "cat - > /var/mysql_back.sql"
```

更多将 ssh 与 pipe 结合的操作: <https://www.kawabangga.com/posts/3416>

---

## What's wrong with GUI??

- GUI 与其他工具交互太难了，你不能像shell一样，将一个GUI程序的输出作为另一个程序的输入;
- 鼠标操作太慢了；
- 跨平台。我只用终端和浏览器，那么我的工具栈基本上都是跨平台的；
- 服务器上，难以使用GUI程序，比如在 docker 中 debug 的时候；
- GUI消耗资源太多了，尤其是越来越多的 Electron 应用；

---

网友：

> 自从用了 SwiftUI 后，我每天都活在噪声中。你们知道 15寸的 MBP 俩风扇全速转起来有多响吗？
>  知道，每开3个goland、2个vscode和chrome，再外接个4k显示器就可以比双开门冰箱全功率制冷还要吵

source: <https://twitter.com/keaising/status/1241774766265995264?s=20>

---

在终端工作，我们大部分时候都在接触几种类型的工具：

- 命令行工具: find/grep/awk/sed/git ...
- 编辑器
- 全屏工具：py-spy/htop/ncdu …
- REPL: mongo/mysql/redis/python

---

# 命令行工具

每一个工具干一件事，通过 Pipe 连接配合，Awesome!

---

# 编辑器

经过配置之后媲美 IDE，Awesome！

---

# 全屏工具

开箱即用，傻瓜说明，Awesome！

---

# REPL

REPL … REPL Sucks!

Why?

I show you why.

---

数据库，编程语言等的 REPL，基本上只提供了很基本的功能。
但是如果开发者每天要和这些工具交互, 这些基本的功能是不够的...

---

**你值得更好的 REPL！**

---

# Demo

我们可以怎么做的更好?

iredis VS redis-cli

---

# 如何开发 REPL？

我们现在就写一个吧...

---

这个 REPL 有什么问题呢？

- 没有处理信号；
- 没有命令历史；
- Emacs 快捷键不能用，← 也不能用；
- …

---

# 我们需要库/框架！

首先，区分一下不同的框架，都是在做什么的：

- click: 命令行工具 (argparse等等其他的库也是)
- 全屏TUI工具: curses urwid <https://www.kawabangga.com/posts/2761>  (pingtop)
- REPL prompt-toolkit!

---

# prompt-tookit

- Pure Python
- Completely type annotated
- Key bindings
- No global state
- Auto suggestions
- etc.

---

# 我们用它来写一个吧！

---

# 增加细节：IRedis 简化版

---

# What's more

- 去 example 发现更多Feature/可以使用的功能;
- 查看 prompt 接口的参数;
- 浏览 mycli/pgcli/iredis 的代码；


---

# 核心要点：FormattedText

```python
  FormattedText(
      [
          ("class:dockey", "value: "),
          ("class:value", "hello world"),
      ]
  )
```

---

# 核心要点: Lexer & Completer

编译正则的难题?

<https://www.kawabangga.com/posts/3877>

---

# 开发技巧

- 日志输出;


---

# 如何测试？

- 单元测试；
- 黑盒测试（集成测试），pexpect;

---

# Pexpect 的原理

- spawn 出来一个新的进程测试，模拟用户的行为；
- 向这个进程，模拟发送按键的过程；
- `expect()` 函数验证output（正则）;
- 直到 Timeout 还没有 expect 到的话，Timeout 异常;
- 使用 `logfile_read` 来输出真实的 REPL;

---

# BDD: 行为驱动的开发?

- 读起来像英语，更能表达出在测的是什么;
- 面向老板的开发方式？
- 像是一个DSL，引入了复杂度。

**mycli/pgcli 使用了这种测试方式.**

资料：
- What is BDD? <https://youtu.be/VS6EEUVZGLE>
- Python behave <https://behave.readthedocs.io/en/latest/>

---

# 如何发布 ?

- 推荐poetry；
- 推荐使用CI，尽量频繁的发布，因为接口兼容性要求不高；
- 推荐发布 binary(PyOxidizer);

---

# dbcli 的开发理念

<https://www.dbcli.com/about/>

* Be nice.
* Be courteous.
* Be respectful.
* Have an open mind.
* Never be condescending.
* Never discriminate (even if you like Emacs and Java).

---

# What's next?

* mongo cli? ES cli?
* 参与到 dbcli 的开发?

---

Happy Hacking!

slide: <https://github.com/laixintao/myslides>
slide播放工具: [patat](https://github.com/jaspervdj/patat)
