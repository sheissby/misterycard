ControlFocus("选择要加载的文件", "","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("选择要加载的文件", "", "Edit1", @ScriptDir & "\附件2-ZDH.jpg")
Sleep(1000)
ControlClick("选择要加载的文件", "","Button1");