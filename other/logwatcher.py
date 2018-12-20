# encoding: utf-8
import select, paramiko

servers = ['',''], ['','']]


def print_log(sshcon, server_name):
    BUF_SIZE = 2048
    transport = sshcon.get_transport()
    transport.set_keepalive(1)
    # channel = transport.open_session()
    # channel.settimeout(10)
    # channel.exec_command( 'killall tail')
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
                        # report_error(line)
                        print 'error!!!!!!'
                        print line
                        # todo error
                    print line


def con_server(server_name):
    for i in servers:
        sshcon = paramiko.SSHClient()
        sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshcon.connect(i[0], 9800, 'root', i[1])
        cmd = 'docker ps|grep %s' % server_name
        # print cmd
        _, stdout, _ = sshcon.exec_command(cmd)
        res = stdout.readlines()
        if res:
            # print i[0]+ 'found'
            print_log(sshcon, server_name)
        else:
            print i[0]+'未找到服务'
            sshcon.close()


if __name__ == "__main__":
    server_name = raw_input()
    con_server(server_name)
