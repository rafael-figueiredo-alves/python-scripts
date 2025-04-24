from gamemainfunction import GameThread;
from consolehelpers import ClearConsole;
from gamemessages import ShowStartMessage, ShowGameOverMsg;

ClearConsole();
ShowStartMessage();

GameThread();

ShowGameOverMsg();