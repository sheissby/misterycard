ControlFocus("�ļ��ϴ�", "","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("�ļ��ϴ�", "", "Edit1", @ScriptDir & "\����1-ZDH.doc")
Sleep(1000)
ControlClick("�ļ��ϴ�", "","Button1");