import tornado.ioloop  # 封装了linux的epoll和BSD的kqueue，是tornado高效的基础
import tornado.web  # tornado的web基础
import tornado.httpserver
import tornado.options
from tornado.options import options

tornado.options.define('port', default=8000, type=int)
tornado.options.define('list', default=[], type=str, multiple=True)


# 一个业务处理类
class IndexHandler(tornado.web.RequestHandler):
    # 处理get请求的，不能处理post请求
    def get(self, *args, **kwargs):
        self.write('sunck is not a good man')


if __name__ == '__main__':
    tornado.options.parse_command_line()  # 转换命令行参数
    print(tornado.options.options.list)

    app = tornado.web.Application([
        (r'/', IndexHandler)
    ])

    # app.listen(8000)
    # 实例化一个http服务器对象
    httpServer = tornado.httpserver.HTTPServer(app)
    # httpServer.listen(8000)
    httpServer.bind(options.port)  # 绑定8000端口
    httpServer.start(5)  # 启动多个进程

    tornado.ioloop.IOLoop.current().start()
