ControlFocus("ѡ��Ҫ���ص��ļ�", "","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("ѡ��Ҫ���ص��ļ�", "", "Edit1", @ScriptDir & "\����1-ZDH.doc")
Sleep(1000)
ControlClick("ѡ��Ҫ���ص��ļ�", "","Button1");