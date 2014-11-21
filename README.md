iNodeReverseVerification
========================================================================================================================

KeyWords：iNode Reverse; Verification ;Simple Script

关键词：iNode逆向；验证；简单脚本


###Introduction
------------------------------------------------------------------------
####[1]Purpose of iNodeReverseVerification:

######(1.1) My honor to predecessors including liuqun, humiaozuzu and bitdust in Github. My work about iNode reversing verification inherits from the policies and emulate the style of predecessors.

`FORK FROM their great work`

*https://github.com/liuqun/njit8021xclient

*https://github.com/humiaozuzu/YaH3C

*https://github.com/bitdust/njit8021xclient

*https://github.com/bitdust/YaH3C

#####(1.2) I want to help you if you are interested in reversing iNode so that these iNodeReverseVerification just hold a simple introduction by Python scripts to guide you to analyze iNode.

####[2]Content of iNodeReverseVerification:

#####(2.1) If you want to reverse iNode, you will read files about 802.1x authentication of iNode how to work and the follow URL must be read.

https://github.com/liuqun/njit8021xclient/blob/master/Documents.html

#####(2.2) After you have a fair idea of iNode how to work, I make a simple reversing verification about Base64 in request packet.

#####(2.3) I also simulate a MD5 code packet forward to verification if MD5 can be produced by us and cheat server or not

#####(2.4) There are no struct of packet in this file or my Python scripts.And I have told that these files are just simple experiment, even just a test. 

###引言
------------------------------------------------------------------------
####[1]本分支文档存在的主要目的有两个：

#####（1.1）致敬前辈，包括Github平台原分支liuqun/njit8021xclient，humiaozuzu/YaH3C。以及修改跟进分支bitdust/njit8021xclient和bitdust/YaH3C。向他们学习。

#####（1.2）为使用iNode校园客户端，并想从网络数据包层面逆向分析他的同学，铺下一层简单的道路，便于入门者的后续探索。

####[2]本文档完成的一些工作内容有：

#####（2.1）若想逆向分析iNode校园客户端，先应该预习一下iNode相关的知识，可参看liuqun/njit8021xclient的原理文档

https://github.com/liuqun/njit8021xclient/blob/master/Documents.html

#####（2.2）在了解相关知识后，我介绍我的工作，主要完成了iNode中请求认证包里Base64编码的逆向验证工作。

#####（2.3）还完成了iNode中MD5认证包的正向MD5加密验证工作，模仿制作数据，看看能不能实现仿制。

#####（2.4）本分支文档或脚本没有涉及到数据包构造，只是个简单的验证脚本，仅为仿制数据包和验证编码的简单实验，甚至连实验都算不上。
