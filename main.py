import time
import utils.func_screen as bot_sc
import utils.func_system as bot_system
import utils.func_network as bot_network
import app.init as start

if __name__ == "__main__":
    width, height = bot_sc.get_screen_dimensions()
    print("Largeur de l'écran:", width)
    print("Hauteur de l'écran:", height)

    print(bot_system.get_os())
    
    while (1):
        start.start_bot()
