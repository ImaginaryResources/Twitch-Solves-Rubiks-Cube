from pynput.keyboard import Key, Controller
import socket
import threading

keyboard = Controller()
message = ""

SERVER = "irc.twitch.tv"
PORT = 6667
PASS = "oauth token goes here"
BOT = "CubeBot"
CHANNEL = "channel name"
irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send(("PASS " + PASS + "\n" +
          "NICK " + BOT + "\n" +
          "JOIN #" + CHANNEL + "\n").encode())

# Face Rotations
# Right Moves
def R():
    global message
    keyboard.press('R')
    message = ""
    keyboard.release('R')
def Ri():
    global message
    keyboard.press('r')
    message = ""
    keyboard.release('r')
def R2():
    R()
    R()

def r():
    global message
    keyboard.press('R')
    message = ""
    keyboard.release('R')
    keyboard.press('m')
    message = ""
    keyboard.release('m')
def ri():
    global message
    keyboard.press('r')
    message = ""
    keyboard.release('r')
    keyboard.press('M')
    message = ""
    keyboard.release('M')
def r2():
    r()
    r()

# Left Moves
def L():
    global message
    keyboard.press('L')
    message = ""
    keyboard.release('L')
def Li():
    global message
    keyboard.press('l')
    message = ""
    keyboard.release('l')
def L2():
    L()
    L()

def l():
    global message
    keyboard.press('L')
    message = ""
    keyboard.release('L')
    keyboard.press('M')
    message = ""
    keyboard.release('M')
def li():
    global message
    keyboard.press('l')
    message = ""
    keyboard.release('l')
    keyboard.press('m')
    message = ""
    keyboard.release('m')
def l2():
    l()
    l()

# Front Moves
def F():
    global message
    keyboard.press('F')
    message = ""
    keyboard.release('F')
def Fi():
    global message
    keyboard.press('f')
    message = ""
    keyboard.release('f')
def F2():
    F()
    F()

def f():
    global message
    keyboard.press('F')
    message = ""
    keyboard.release('F')
    keyboard.press('S')
    message = ""
    keyboard.release('S')
def fi():
    global message
    keyboard.press('f')
    message = ""
    keyboard.release('f')
    keyboard.press('s')
    message = ""
    keyboard.release('s')
def f2():
    f()
    f()

# Back Moves
def B():
    global message
    keyboard.press('B')
    message = ""
    keyboard.release('B')
def Bi():
    global message
    keyboard.press('b')
    message = ""
    keyboard.release('b')
def B2():
    B()
    B()

def b():
    global message
    keyboard.press('B')
    message = ""
    keyboard.release('B')
    keyboard.press('s')
    message = ""
    keyboard.release('s')
def bi():
    global message
    keyboard.press('b')
    message = ""
    keyboard.release('b')
    keyboard.press('S')
    message = ""
    keyboard.release('S')
def b2():
    b()
    b()

# Down Moves
def D():
    global message
    keyboard.press('D')
    message = ""
    keyboard.release('D')
def Di():
    global message
    keyboard.press('d')
    message = ""
    keyboard.release('d')
def D2():
    D()
    D()

def d():
    global message
    keyboard.press('D')
    message = ""
    keyboard.release('D')
    keyboard.press('e')
    message = ""
    keyboard.release('e')
def di():
    global message
    keyboard.press('d')
    message = ""
    keyboard.release('d')
    keyboard.press('E')
    message = ""
    keyboard.release('E')
def d2():
    d()
    d()

# Up Moves
def U():
    global message
    keyboard.press('U')
    message = ""
    keyboard.release('U')
def Ui():
    global message
    keyboard.press('u')
    message = ""
    keyboard.release('u')
def U2():
    U()
    U()

def u():
    global message
    keyboard.press('U')
    message = ""
    keyboard.release('U')
    keyboard.press('E')
    message = ""
    keyboard.release('E')
def ui():
    global message
    keyboard.press('u')
    message = ""
    keyboard.release('u')
    keyboard.press('e')
    message = ""
    keyboard.release('e')
def u2():
    u()
    u()

# Middle Slices
# E Moves
def E():
    global message
    keyboard.press('E')
    message = ""
    keyboard.release('E')
def Ei():
    global message
    keyboard.press('e')
    message = ""
    keyboard.release('e')
def E2():
    E()
    E()

# S Moves
def S():
    global message
    keyboard.press('S')
    message = ""
    keyboard.release('S')
def Si():
    global message
    keyboard.press('s')
    message = ""
    keyboard.release('s')
def S2():
    S()
    S()

# M Moves
def M():
    global message
    keyboard.press('M')
    message = ""
    keyboard.release('M')
def Mi():
    global message
    keyboard.press('m')
    message = ""
    keyboard.release('m')
def M2():
    M()
    M()

# Cube Rotations
# X Moves
def X():
    global message
    keyboard.press('X')
    message = ""
    keyboard.release('X')
def Xi():
    global message
    keyboard.press('x')
    message = ""
    keyboard.release('x')
def X2():
    X()
    X()

# Y Moves
def Y():
    global message
    keyboard.press('Y')
    message = ""
    keyboard.release('Y')
def Yi():
    global message
    keyboard.press('y')
    message = ""
    keyboard.release('y')
def Y2():
    Y()
    Y()

# Z Moves
def Z():
    global message
    keyboard.press('Z')
    message = ""
    keyboard.release('Z')
def Zi():
    global message
    keyboard.press('z')
    message = ""
    keyboard.release('z')
def Z2():
    Z()
    Z()

# Triggers
def sexy():
    R(), U(), Ri(), Ui()
def inverseSexy():
    U(), R(), Ui(), Ri()
def sledge():
    Ri(), F(), R(), Fi()
def insert():
    R(), Ui(), Ri()
def remove():
    R(), U(), Ri()
def Su():
    R(), U(), Ri(), U()
def Ne():
    R(), U2(), Ri()
def trigger():
    R(), Ui(), Ri(), Ui()

# OLL Cases
def OCLL1OLL():
    R(), U2(), Ri(), Ui(), R(), U(), Ri(), Ui(), R(), Ui(), Ri()
def OCLL2OLL():
    R(), U2(), R2(), Ui(), R2(), Ui(), R2(), U2(), R()
def OCLL3OLL():
    R2(), D(), Ri(), U2(), R(), (), Di(), Ri(), U2(), Ri()
def OCLL4OLL():
    r(), U(), Ri(), Ui(), ri(), F(), R(), Fi()
def OCLL5OLL():
    Y(), Fi(), r(), U(), Ri(), Ui(), ri(), F(), R()
def OCLL6OLL():
    R(), U2(), Ri(), Ui(), R(), Ui(), Ri()
def OCLL7OLL():
    R(), U(), Ri(), U(), R(), U2(), Ri()
def T1OLL():
    R(), U(), Ri(), Ui(), Ri(), F(), R(), Fi()
def T2OLL():
    F(), sexy(), Fi()
def S1OLL():
    ri(), U2(), R(), U(), Ri(), U(), r()
def S2OLL():
    r(), U2(), Ri(), Ui(), R(), Ui(), ri()
def C1OLL():
    R(), U(), R2(), Ui(), Ri(), F(), R(), U(), R(), Ui(), Fi()
def C2OLL():
    Ri(), Ui(), Ri(), F(), R(), Fi(), U(), R()
def W1OLL():
    Ri(), Ui(), R(), Ui(), Ri(), U(), R(), U(), l(), Ui(), Ri(), U(), X()
def W2OLL():
    R(), U(), Ri(), U(), R(), Ui(), Ri(), Ui(), Ri(), F(), R(), Fi()
def E1OLL():
    r(), U(), Ri(), Ui(), M(), U(), R(), Ui(), Ri()
def E2OLL():
    R(), U(), Ri(), Ui(), Mi(), U(), R(), Ui(), ri()
def P1OLL():
    Ri(), Ui(), F(), U(), R(), Ui(), Ri(), Fi(), R()
def P2OLL():
    R(), U(), Bi(), Ui(), Ri(), U(), R(), B(), Ri()
def P3OLL():
    Y(), Ri(), Ui(), Fi(), U(), F(), R()
def P4OLL():
    f(), R(), U(), Ri(), Ui(), fi()
def I1OLL():
    f(), R(), U(), Ri(), Ui(), R(), U(), Ri(), Ui(), fi()
def I2OLL():
    Ri(), Ui(), R(), Ui(), Ri(), U(), Yi(), Ri(), U(), R(), B()
def I3OLL():
    Y(), Ri(), F(), R(), U(), R(), Ui(), R2(), Fi(), R2(), Ui(), Ri(), U(), R(), U(), Ri()
def I4OLL():
    ri(), Ui(), r(), Ui(), Ri(), U(), R(), Ui(), Ri(), U(), R(), ri(), U(), r()
def F1OLL():
    R(), U(), Ri(), Ui(), Ri(), F(), (), R2(), U(), Ri(), Ui(), Fi()
def F2OLL():
    R(), U(), Ri(), U(), Ri(), F(), R(), Fi(), R(), U2(), Ri()
def F3OLL():
    R(), U2(), R2(), F(), R(), Fi(), R(), U2(), Ri()
def F4OLL():
    F(), R(), Ui(), Ri(), Ui(), R(), U(), Ri(), Fi()
def K1OLL():
    r(), Ui(), ri(), Ui(), r(), U(), ri(), Yi(), Ri(), U(), R()
def K2OLL():
    Ri(), F(), R(), U(), Ri(), Fi(), R(), F(), Ui(), Fi()
def K3OLL():
    ri(), Ui(), r(), Ri(), Ui(), R(), U(), ri(), U(), r()
def K4OLL():
    r(), U(), ri(), R(), U(), Ri(), Ui(), r(), Ui(), ri()
def A1OLL():
    Y(), R(), U(), Ri(), Ui(), R(), Ui(), Ri(), Fi(), Ui(), F(), R(), U(), Ri()
def A2OLL():
    Yi(), F(), U(), R(), U2(), Ri(), Ui(), R(), U2(), Ri(), Ui(), Fi()
def A3OLL():
    R(), U(), Ri(), U(), R(), U2(), Ri(), F(), R(), U(), Ri(), Ui(), Fi()
def A4OLL():
    Ri(), Ui(), R(), Ui(), Ri(), U2(), R(), F(), R(), U(), Ri(), Ui(), Fi()
def L1OLL():
    Fi(), Li(), Ui(), L(), U(), Li(), Ui(), L(), U(), F()
def L2OLL():
    F(), R(), U(), Ri(), Ui(), R(), U(), Ri(), Ui(), Fi()
def L3OLL():
    r(), Ui(), r2(), U(), r2(), U(), r2(), Ui(), r()
def L4OLL():
    ri(), U(), r2(), Ui(), r2(), Ui(), r2(), U(), ri()
def L5OLL():
    ri(), Ui(), R(), Ui(), Ri(), U(), R(), Ui(), Ri(), U2(), r()
def L6OLL():
    r(), U(), Ri(), U(), R(), Ui(), Ri(), U(), R(), U2(), ri()
def B1OLL():
    r(), U(), Ri(), U(), R(), U2(), ri()
def B2OLL():
    ri(), Ui(), R(), Ui(), Ri(), U2(), r()
def B3OLL():
    ri(), R2(), U(), Ri(), U(), R(), U2(), Ri(), U(), Mi()
def B4OLL():
    Mi(), Ri(), Ui(), R(), Ui(), Ri(), U2(), R(), Ui(), M()
def B5OLL():
    L(), Fi(), Li(), Ui(), L(), U(), F(), Ui(), Li()
def B6OLL():
    Ri(), F(), R(), U(), Ri(), Ui(), Fi(), U(), R()
def O1OLL():
    R(), U2(), R2(), F(), R(), Fi(), U2(), Ri(), F(), R(), Fi()
def O2OLL():
    F(), R(), U(), Ri(), Ui(), Fi(), f(), R(), U(), Ri(), Ui(), fi()
def O3OLL():
    f(), R(), U(), Ri(), Ui(), fi(), Ui(), F(), (), R(), U(), Ri(), Ui(), Fi()
def O4OLL():
    f(), R(), U(), Ri(), Ui(), fi(), U(), F(), (), R(), U(), Ri(), Ui(), Fi()
def O5OLL():
    R(), U(), Ri(), U(), Ri(), F(), R(), Fi(), U2(), Ri(), F(), R(), Fi()
def O6OLL():
    Y(), R(), U2(), R2(), F(), R(), Fi(), U2(), Mi(), U(), R(), Ui(), ri()
def O7OLL():
    M(), U(), R(), U(), Ri(), Ui(), Mi(), Ri(), F(), R(), Fi()
def O8OLL():
    M(), U(), R(), U(), Ri(), Ui(), M2(), U(), R(), Ui(), ri()

# PLL Cases
def UbPerm():
    R2(), U(), sexy(), Ri(), Ui(), Ri(), U(), Ri()
def UaPerm():
    R(), Ui(), R(), U(), R(), U(), trigger(), R2()
def ZPerm():
    M2(), U2(), M(), U(), M2(), U(), M2(), U(), M(), Ui()
def HPerm():
    M2(), U(), M2(), U2(), M2(), U(), M2()
def AaPerm():
    X(), Ri(), U(), Ri(), D2(), insert(), D2(), R2(), Xi()
def AbPerm():
    X(), R2(), D2(), remove(), D2(), R(), Ui(), R(), Xi()
def EPerm():
    Xi(), R(), Ui(), Ri(), D(), R(), U(), Ri(), Di(), R(), U(), Ri(), D(), R(), Ui(), Ri(), Di(), X()
def RaPerm():
    R(), Ui(), Ri(), Ui(), R(), U(), R(), D(), Ri(), Ui(), R(), Di(), Ri(), U2(), Ri(), Ui()
def RbPerm():
    Ri(), U2(), R(), U2(), Ri(), F(), R(), U(), Ri(), Ui(), Ri(), Fi(), R2(), Ui()
def JaPerm():
    Ri(), U(), Li(), U2(), R(), Ui(), Ri(), U2(), R(), L(), Ui()
def JbPerm():
    R(), U(), Ri(), Fi(), R(), U(), Ri(), Ui(), Ri(), F(), R2(), Ui(), Ri(), Ui()
def TPerm():
    R(), U(), Ri(), Ui(), Ri(), F(), R2(), Ui(), Ri(), Ui(), R(), U(), Ri(), Fi()
def FPerm():
    Ri(), Ui(), Fi(), R(), U(), Ri(), Ui(), Ri(), F(), R2(), Ui(), Ri(), Ui(), R(), U(), Ri(), U(), R()
def VPerm():
    Ri(), U(), Ri(), Ui(), Y(), Ri(), Fi(), R2(), Ui(), Ri(), U(), Ri(), F(), R(), F()
def YPerm():
    F(), R(), Ui(), Ri(), Ui(), R(), U(), Ri(), Fi(), R(), U(), Ri(), Ui(), Ri(), F(), R(), Fi()
def NaPerm():
    R(), U(), Ri(), U(), R(), U(), Ri(), Fi(), R(), U(), Ri(), Ui(), Ri(), F(), R2(), Ui(), Ri(), U2(), R(), Ui(), Ri()
def NbPerm():
    Ri(), U(), R(), Ui(), Ri(), Fi(), Ui(), F(), R(), U(), Ri(), F(), Ri(), Fi(), R(), Ui(), R()
def GaPerm():
    R2(), U(), Ri(), U(), Ri(), Ui(), R(), Ui(), R2(), D(), Ui(), Ri(), U(), R(), Di(), U()
def GbPerm():
    Fi(), Ui(), F(), R2(), u(), Ri(), U(), R(), Ui(), R(), ui(), R2()
def GcPerm():
    R2(), Ui(), R(), Ui(), R(), U(), Ri(), U(), R2(), Di(), U(), R(), Ui(), Ri(), D(), Ui()
def GdPerm():
    Di(), R(), U(), Ri(), Ui(), D(), R2(), Ui(), R(), Ui(), Ri(), U(), Ri(), U(), R2(), U()

def gamecontrol():
    global message
    while True:
        # Face Rotations
        # Right Moves
        if "R" == message:
            R()
        elif "R'" == message:
            Ri()
        elif "R‘" == message:
            Ri()
        elif "R2" == message:
            R2()
        elif "r" == message:
            r()
        elif "r'" == message:
            ri()
        elif "r‘" == message:
            ri()
        elif "r2" == message:
            r2()
        # Left Moves
        elif "L" == message:
            L()
        elif "L'" == message:
            Li()
        elif "L‘" == message:
            Li()
        elif "L2" == message:
            L2()
        elif "l" == message:
            l()
        elif "l'" == message:
            li()
        elif "l‘" == message:
            li()
        elif "l2" == message:
            l2()
        # Front Moves
        elif "F" == message:
            F()
        elif "F'" == message:
            Fi()
        elif "F‘" == message:
            Fi()
        elif "F2" == message:
            F2()
        elif "f" == message:
            f()
        elif "f'" == message:
            fi()
        elif "f‘" == message:
            fi()
        elif "f2" == message:
            f2()
        # Back Moves
        elif "B" == message:
            B()
        elif "B'" == message:
            Bi()
        elif "B‘" == message:
            Bi()
        elif "B2" == message:
            B2()
        elif "b" == message:
            b()
        elif "b'" == message:
            bi()
        elif "b‘" == message:
            bi()
        elif "b2" == message:
            b2()
        # Down Moves
        elif "D" == message:
            D()
        elif "D'" == message:
            Di()
        elif "D‘" == message:
            Di()
        elif "D2" == message:
            D2()
        elif "d" == message:
            d()
        elif "d'" == message:
            di()
        elif "d‘" == message:
            di()
        elif "d2" == message:
            d2()
        # Up Moves
        elif "U" == message:
            U()
        elif "U'" == message:
            Ui()
        elif "U‘" == message:
            Ui()
        elif "U2" == message:
            U2()
        elif "u" == message:
            u()
        elif "u'" == message:
            ui()
        elif "u‘" == message:
            ui()
        elif "u2" == message:
            u2()
        # Middle Slices
        # E Moves
        elif "E" == message:
            E()
        elif "E'" == message:
            Ei()
        elif "E‘" == message:
            Ei()
        elif "E2" == message:
            E2()
        # S Moves
        elif "S" == message:
            S()
        elif "S'" == message:
            Si()
        elif "S‘" == message:
            Si()
        elif "S2" == message:
            S2()
        # M Moves
        elif "M" == message:
            M()
        elif "M'" == message:
            Mi()
        elif "M‘" == message:
            Mi()
        elif "M2" == message:
            M2()
        # Cube Rotations
        # X Moves
        elif "X" == message:
            X()
        elif "X'" == message:
            Xi()
        elif "X‘" == message:
            Xi()
        elif "X2" == message:
            X2()
        elif "x" == message:
            X()
        elif "x'" == message:
            Xi()
        elif "x‘" == message:
            Xi()
        elif "x2" == message:
            X2()
        # Y Moves
        elif "Y" == message:
            Y()
        elif "Y'" == message:
            Yi()
        elif "Y‘" == message:
            Yi()
        elif "Y2" == message:
            Y2()
        elif "y" == message:
            Y()
        elif "y'" == message:
            Yi()
        elif "y‘" == message:
            Yi()
        elif "y2" == message:
            Y2()
        # Z Moves
        elif "Z" == message:
            Z()
        elif "Z'" == message:
            Zi()
        elif "Z‘" == message:
            Zi()
        elif "Z2" == message:
            Z2()
        elif "z" == message:
            Z()
        elif "z'" == message:
            Zi()
        elif "z‘" == message:
            Zi()
        elif "z2" == message:
            Z2()
        # Triggers
        elif "sexy" == message:
            sexy()
        elif "SEXY" == message:
            sexy()
        elif "invSexy" == message:
            inverseSexy()
        elif "sledge" == message:
            sledge()
        elif "insert" == message:
            insert()
        elif "remove" == message:
            remove()
        elif "su" == message:
            Su()
        elif "ne" == message:
            Ne()
        # OLL Cases
        elif "OCLL1 OLL" == message:
            OCLL1OLL()
        elif "OCLL2 OLL" == message:
            OCLL2OLL()
        elif "OCLL3 OLL" == message:
            OCLL3OLL()
        elif "OCLL4 OLL" == message:
            OCLL4OLL()
        elif "OCLL5 OLL" == message:
            OCLL5OLL()
        elif "OCLL6 OLL" == message:
            OCLL6OLL()
        elif "OCLL7 OLL" == message:
            OCLL7OLL()
        elif "T1 OLL" == message:
            T1OLL()
        elif "T2 OLL" == message:
            T2OLL()
        elif "S1 OLL" == message:
            S1OLL()
        elif "S2 OLL" == message:
            S2OLL()
        elif "C1 OLL" == message:
            C1OLL()
        elif "C2 OLL" == message:
            C2OLL()
        elif "W1 OLL" == message:
            W1OLL()
        elif "W2 OLL" == message:
            W2OLL()
        elif "E1 OLL" == message:
            E1OLL()
        elif "E2 OLL" == message:
            E2OLL()
        elif "P1 OLL" == message:
            P1OLL()
        elif "P2 OLL" == message:
            P2OLL()
        elif "P3 OLL" == message:
            P3OLL()
        elif "P4 OLL" == message:
            P4OLL()
        elif "I1 OLL" == message:
            I1OLL()
        elif "I2 OLL" == message:
            I2OLL()
        elif "I3 OLL" == message:
            I3OLL()
        elif "I4 OLL" == message:
            I4OLL()
        elif "F1 OLL" == message:
            F1OLL()
        elif "F2 OLL" == message:
            F2OLL()
        elif "F3 OLL" == message:
            F3OLL()
        elif "F4 OLL" == message:
            F4OLL()
        elif "K1 OLL" == message:
            K1OLL()
        elif "K2 OLL" == message:
            K2OLL()
        elif "K3 OLL" == message:
            K3OLL()
        elif "K4 OLL" == message:
            K4OLL()
        elif "A1 OLL" == message:
            A1OLL()
        elif "A2 OLL" == message:
            A2OLL()
        elif "A3 OLL" == message:
            A3OLL()
        elif "A4 OLL" == message:
            A4OLL()
        elif "L1 OLL" == message:
            L1OLL()
        elif "L2 OLL" == message:
            L2OLL()
        elif "L3 OLL" == message:
            L3OLL()
        elif "L4 OLL" == message:
            L4OLL()
        elif "L5 OLL" == message:
            L5OLL()
        elif "L6 OLL" == message:
            L6OLL()
        elif "B1 OLL" == message:
            B1OLL()
        elif "B2 OLL" == message:
            B2OLL()
        elif "B3 OLL" == message:
            B3OLL()
        elif "B4 OLL" == message:
            B4OLL()
        elif "B5 OLL" == message:
            B5OLL()
        elif "B6 OLL" == message:
            B6OLL()
        elif "O1 OLL" == message:
            O1OLL()
        elif "O2 OLL" == message:
            O2OLL()
        elif "O3 OLL" == message:
            O3OLL()
        elif "O4 OLL" == message:
            O4OLL()
        elif "O5 OLL" == message:
            O5OLL()
        elif "O6 OLL" == message:
            O6OLL()
        elif "O7 OLL" == message:
            O7OLL()
        elif "O8 OLL" == message:
            O8OLL()
        # PLL Cases
        elif "Ub Perm" == message:
            UbPerm()
        elif "Ua Perm" == message:
            UaPerm()
        elif "Z Perm" == message:
            ZPerm()
        elif "H Perm" == message:
            HPerm()
        elif "Aa Perm" == message:
            AaPerm()
        elif "Ab Perm" == message:
            AbPerm()
        elif "E Perm" == message:
            EPerm()
        elif "Ra Perm" == message:
            RaPerm()
        elif "Rb Perm" == message:
            RbPerm()
        elif "Ja Perm" == message:
            JaPerm()
        elif "Jb Perm" == message:
            JbPerm()
        elif "T Perm" == message:
            TPerm()
        elif "F Perm" == message:
            FPerm()
        elif "V Perm" == message:
            VPerm()
        elif "Y Perm" == message:
            YPerm()
        elif "Na Perm" == message:
            NaPerm()
        elif "Nb Perm" == message:
            NbPerm()
        elif "Ga Perm" == message:
            GaPerm()
        elif "Gb Perm" == message:
            GbPerm()
        elif "Gc Perm" == message:
            GcPerm()
        elif "Gd Perm" == message:
            GdPerm()
        else:
            pass

def twitch():
    def joinchat():
        loading = True
        while loading:
            readbuffer_join = irc.recv(1024)
            readbuffer_join = readbuffer_join.decode()
            for line in readbuffer_join.split("\n")[0:-1]:
                print(line)
                loading = loadingComplete(line)

    def loadingComplete(line):
        if ("End of /NAMES list" in line):
            print("Bot has joined " + CHANNEL + "'s Channel!")
            sendMessage(irc, "CubeBot Joined")
            return False
        else:
            return True

    def sendMessage(irc, message):
        messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
        irc.send((messageTemp + "\n").encode())

    def getUser(line):
        separate = line.split(":", 2)
        user = separate[1].split("!", 1)[0]
        return user

    def getMessage(line):
        global message
        try:
            message = (line.split(":", 2))[2]
        except:
            message = ""
        return message

    def Console(line):
        if "PRIVMSG" in line:
            return False
        else:
            return True

    joinchat()

    while True:
        try:
            readbuffer = irc.recv(1024).decode()
        except:
            readbuffer = ""
        for line in readbuffer.split("\r\n"):
            if line == "":
                continue
            if "PING" in line and Console(line):
                msg = "PONG tmi.twitch.tv\r\n".encode()
                irc.send(msg)
                print(msg)
                continue
            else:
                user = getUser(line)
                message = getMessage(line)
                print(user + ": " + message)

if __name__ == '__main__':
    t1 = threading.Thread(target= twitch)
    t1.start()
    t2 = threading.Thread(target= gamecontrol)
    t2.start()