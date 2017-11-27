## README
 
* 在request\_data.py里填写接口测试用到的相关信息（url,data,type）：
    
        参数url代表待测接口的url
        参数data代表待测接口的上行参数（json格式）
        参数type代表待测接口的请求方式（get/post两种）
 
* 在requester.log中记录接口测试日志
* 在logger.conf中进行日志配置
* 有test和test\_all两种方法（示例在requester.py的main函数中）
 
## What is this repository for? ###

* 以数据驱动接口测试的工具

## How do I get set up? ###

* 基于python3的request库进行封装开发
* 日志部分用到了logging模块
