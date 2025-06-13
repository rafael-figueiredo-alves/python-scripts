from gamemainfunction import GameThread;
from consolehelpers import ClearConsole;
from gamemessages import ShowStartMessage, ShowGameOverMsg;
import sys;


ClearConsole();

if(len(sys.argv) > 1):
    ValorMaximo = sys.argv[1]
else:
    ValorMaximo = 10;

ShowStartMessage(ValorMaximo);

GameThread(ValorMaximo);

ShowGameOverMsg();