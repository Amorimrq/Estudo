#Persistent ; Mantém o script rodando
SetTimer, PressCtrl, 1000 ; Chama a função PressCtrl a cada 1000 ms (1 segundo)
return

PressCtrl:
Send, {Ctrl down}
Sleep, 50
Send, {Ctrl up}
return
