ControlFocus("��", "","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("��", "", "Edit1", @ScriptDir & "\����1-ZDH.doc")
Sleep(1000)
ControlClick("��", "","Button1");