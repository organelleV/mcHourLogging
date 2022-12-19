from mcrcon import MCRcon
serverName = "uwu.mine.nu"
serverRconPassword = "NHS5014pythoncut"

def getNumPlayers():
    try:
        with MCRcon(serverName, serverRconPassword) as mcr:
            resp = mcr.command("/list") # ex: "There are 0 of a max of 20 players online:"
            return int(resp[10])
    except:
        print('there was a problem running rcon')   

