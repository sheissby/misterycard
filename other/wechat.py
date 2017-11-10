# encoding: utf-8
import itchat
from itchat.content import *
itchat.auto_login()
print itchat.get_QRuuid()

@itchat.msg_register(TEXT)
def text_reply(msg):
    ToUserNickName = itchat.search_friends(userName=msg['ToUserName'])['NickName']
    FromUserNickName = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    print FromUserNickName, msg['Text']
    # returnmsg = u'%s对%s说：%s' % (FromUserNickName, ToUserNickName, msg['Text'])
    if FromUserNickName != u'灰特':
        itchat.send(msg['Text'], toUserName=msg['FromUserName'])

itchat.run()
