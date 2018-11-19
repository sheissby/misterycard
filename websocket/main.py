# encoding: utf-8

import paramiko
import select
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


servers = ['192.9.100.50', '$2a$10$D'], ['192.9.100.51', '$3a$10$D'], ['192.9.100.53', '$4a$10$D']


def print_log(sshcon, server_name, ws):
    BUF_SIZE = 1024
    transport = sshcon.get_transport()
    transport.set_keepalive(1)
    channel = transport.open_session()
    channel.settimeout(100)
    cmd = "docker ps|grep %s|awk '{print $1}'|xargs docker logs --tail 10 -f" % server_name
    channel.exec_command(cmd)
    while transport.is_active():
        LeftOver = ''
        rl, wl, xl = select.select([channel], [], [], 0.0)
        if len(rl) > 0:
            buf = channel.recv(BUF_SIZE)
            if len(buf) > 0:
                lines_to_process = LeftOver + buf
                EOL = lines_to_process.rfind("\n")
                if EOL != len(lines_to_process) - 1:
                    LeftOver = lines_to_process[EOL + 1:]
                    lines_to_process = lines_to_process[:EOL]
                else:
                    LeftOver = ""
                for line in lines_to_process.splitlines():
                    if "error" in line:
                        ws.send(u'未知错误：' + line.decode('utf-8'))
                    print line
                    ws.send(line.decode('utf-8'))


def con_server(server_name, ws):
    for i in servers:
        try:
            ws.send(u'开始连接' + i[0])
            sshcon = paramiko.SSHClient()
            sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sshcon.connect(i[0], 9800, 'root', i[1])
            ws.send(u'已连接' + i[0])
        except Exception, e:
            ws.send(u'连接' + i[0] + u'出错：' + e)
            break
        cmd = 'docker ps|grep %s' % server_name
        # print cmd
        _, stdout, _ = sshcon.exec_command(cmd)
        res = stdout.readlines()
        if res:
            ws.send(i[0] + u'上已找到服务')
            print_log(sshcon, server_name, ws)
        else:
            ws.send(i[0] + u'上未找到服务')
            sshcon.close()


@app.route('/')
def index():
    return render_template('index.html')


WS_LIST = []


@app.route('/logwatcher')
def test():
    ws = request.environ.get('wsgi.websocket')
    if not ws:
        return '请使用WebSocket协议' # websocket连接已经成功

    WS_LIST.append(ws)
    while True:
        # 等待用户发送消息，并接受
        server_name = ws.receive()
        print server_name

        # 关闭：message=None
        if not server_name:
            print("ws.close")
            WS_LIST.remove(ws)
            ws.close()
            break

        for item in WS_LIST:
            con_server(server_name, item)


if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.1', 5001), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
