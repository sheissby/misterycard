ControlFocus("文件上传", "","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("文件上传", "", "Edit1", @ScriptDir & "\附件2-ZDH.jpg")
Sleep(1000)
ControlClick("文件上传", "","Button1");