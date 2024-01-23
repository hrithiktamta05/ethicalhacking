set x = wscript.CreateObject("wscript.shell")
	dim a:a=1
	For i = a to 2 step 1
	wscript.sleep 50
	MsgBox("This is suspicious")
next
MsgBox("You clicked 2 times")
wscript.Quit