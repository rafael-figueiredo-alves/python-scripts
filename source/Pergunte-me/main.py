import lib.console
import lib.inputs
import lib.core

resetScreen = True

while True:

    if(resetScreen):
        lib.console.ClearConsole()
        lib.console.PrintAppTitle("Pergunte-me o que quiser", "0.0.1")
        resetScreen = False

    if(lib.inputs.InputSair()):
        resetScreen = True
        lib.core.MostrarResposta()
        continue
    else:
        lib.console.CloseApp()