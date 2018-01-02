**目标网站：[http://best.zhaopin.com/?sid=121128100&site=sou](http://best.zhaopin.com/?sid=121128100&site=sou)**

#1.分析
- **先手动投票查看网页提交的请求**

![点击投票网页提交的请求](http://upload-images.jianshu.io/upload_images/6078268-36899f4851067a90.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![投票成功返回的json数据，可以看到是result：1](http://upload-images.jianshu.io/upload_images/6078268-2a8878448cd60e5b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


![为公司投票时提交的参数](http://upload-images.jianshu.io/upload_images/6078268-bc5ada41dc663898.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


---


![点击'为我点赞'网页提交的请求](http://upload-images.jianshu.io/upload_images/6078268-b793622ee5c47408.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



![点赞时提交的参数](http://upload-images.jianshu.io/upload_images/6078268-d5c313e5e796daf9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


>通过分析可以看到网页实际上并没有针对同一IP的投票进行限制，所以不需要进行使用代理IP，但是为了使我们的代码更加符合常规网站的对同一IP限制投票的机制，所以这里抓取一个代理IP的网站进行点击投票


![](http://upload-images.jianshu.io/upload_images/6078268-9ac7f4de4d62d5bb.gif?imageMogr2/auto-orient/strip)
>提供不错几个的短期代理IP网站
>- **[西刺免费代理IP](http://www.xicidaili.com/)**
>- **[快代理免费代理](http://www.kuaidaili.com/free/inha/)**
>- **[Proxy360代理](http://www.proxy360.cn/default.aspx)**
>- **[全网代理IP](http://www.goubanjia.com/free/index.shtml)**
>
>但是，这些免费开放代理一般会有很多人都在使用，而且代理有寿命短，速度慢，匿名度不高，HTTP/HTTPS支持不稳定等缺点（免费没好货）。
- 目标网址：**[西刺免费代理IP](http://www.xicidaili.com/nn)**


![查看网页结构每一个代理IP和端口都在一个<td></td>标签中，我们可以通过正则筛选出我们想要的结果](http://upload-images.jianshu.io/upload_images/6078268-e166098c6094a14a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



- 运行程序

![开启程序，可以看到每次投票的IP已不再是我们本机IP](http://upload-images.jianshu.io/upload_images/6078268-bde32b9cc749a46f.gif?imageMogr2/auto-orient/strip)