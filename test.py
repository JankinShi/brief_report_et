# 使用tornado
# from tornado.wsgi import WSGIContainer
# from tornado.httpserver import HTTPServer
# from tornado.ioloop import IOLoop
# from myapp import create_app
# import config
 
# # app = create_app('config')
# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
 
# http_server = HTTPServer(WSGIContainer(app))
# http_server.listen(5500)
# IOLoop.instance().start()


# import config
from app import create_app  # app 是自己打的包
import os
import time

 
# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app = create_app('production')




@app.route('/test')
def maintest():
    return 'hello world'
    
@app.route('/sleep')
def mainsleep():
    time.sleep(15)
    return 'wake up'

if __name__ == '__main__':
	# app.run(port='5201')
	app.run(port='5201', threaded=True)


