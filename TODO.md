#2017-11-30
    1. 修改bubblesort 及 binarySearch的代码风格问题
    2. 为bubblesort写三个以上测试case
    3. 写一个选择排序的函数
    
#2017-12-7

我们系统中经常产生各种消息，这些消息需要以各种方式通知给用户。
消息产生的频率可能很高，由于邮件服务器/短信服务器等的限制，对外发送需排队发送。
 
请设计并实现“消息中心“模块，主要功能：
1、支持各种消息（现有邮件、短信、hi）发送，可支持消息种类扩充。
2、邮件服务器等每分钟只能发送M条信息，请考虑缓存/队列等的使用，对消息发送进行限流。设计的时候，请考虑性能因素

 
其他：
1、消息发送模拟实现即可