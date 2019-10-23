接口测试步骤
    需求分析---需求文档
        1.梳理业务流程
        2.需要测试哪些功能？
        3.测试周期，任务安排
    用例设计---接口文档，数据库设计
    代码编写
    持续集成
    

unittest
    单元测试作为整个项目核心
    断言
    数据驱动-ddt
    使用测试套件批量执行测试用例
    生成测试报告
    
excel
    保存测试数据，用例信息
    
配置文件
    保存不常修改的数据信息
    
日志器
    记录测试过程中的日志信息，方便查看错误记录
    
requests
    http请求库，模拟客户端向服务器发起请求
    
pymysql
    连接mysql
    执行sql
    数据校验
正则
    参数化，类似jmeter
    
接口依赖
    动态创建获取属性，setattr(), getattr
