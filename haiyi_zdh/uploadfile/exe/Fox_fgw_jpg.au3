ControlFocus("�ļ��ϴ�", "","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("�ļ��ϴ�", "", "Edit1", @ScriptDir & "\����2-ZDH.jpg")
Sleep(1000)
ControlClick("�ļ��ϴ�", "","Button1");