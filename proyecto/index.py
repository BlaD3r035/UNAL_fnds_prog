#config
import random
import time
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"] 
# Los chistes tienen que ser igual de malos que la historia 😅
bad_jokes = ["Cancelaste una materia en tercera semana","Preparaste pizza con piña","Atropellaste a una abuelita con tu carruaje", "Te robaste el caballo real", "Besaste a la princesa 😏"] 
categories = [
    {
        "name":"ciudades",
        "words":["bogota","caracas","toronto","melbourne","abudabi","tokyo","nagasaki","pyongyang","beijing","oslo"]
    },
    
    {
        "name":"nombres de mujeres",
        "words":["camila","alejandra","piedad","socorro","sofia","marta","paulina","rafaela","brigitte","miranda"]
    },
    
    {
        "name":"organos del cuerpo en ingles",
        "words":["bladder","skin","gallbladder","liver","stomach","brain","bones","kidney","lungs","intestine"]
    },
    
    {
        "name":"paises",
        "words":["azerbaiyan","somalia","niger","japon","turquia","chipre","malasia","nepal","francia","italia"]
    },
    
    {
        "name":"idiomas",
        "words":["esperanto","ingles","español","catalan","mandarin","frances","italiano","hindi","ruso","aleman"]
    },
    
    {
        "name":"medios de transporte",
        "words":["tren","avion","barco","metro","teleferico","funicular","monorriel","tramvia","trolebus","bus"]
    },
    
]
graphic_game = False
colors ={
    "reset":"\033[0m",
    "red":"\033[31m",
    "green":"\033[32m",
    "yellow":"\033[33m",
    "blue":"\033[34m",
} # Estos son ANSI codes, los uso para darle mayor estilo a la app CLI. aquí está una documentación de como usarlos: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

# Se podría usar match/case para un mejor codigo, pero como esto no está en todas las versiones de python uso if/else :(
#draws
def gallows(trys):
    print("      _______")
    print("     |/      |")
    
    if trys >= 1:
        print("     |      (_)")
    else:
        print("     |")
        
    if trys >= 2:
        if trys == 2:
            print("     |       |")
        elif trys == 3:
            print("     |      \\|")
        elif trys == 4:
            print("     |      \\|/")
        else:
            print("     |      \\|/")
    else:
        print("     |")
    
    if trys >= 5:
        if trys == 5:
            print("     |       |")
        elif trys == 6:
            print("     |      /")
        elif trys >= 7:
            print("     |      / \\")
    else:
        print("     |")
    
    print("     |")
    print("  ___|___")


def guillotine(dif,trys):
    return

def game(name, trys):
    game = None
    while(game != "g" and game != "h"):
        print(colors["yellow"] + "De que manera quieres morir?:" + colors["blue"] + " Ingresa (h) para Horca y (g) Para Guillotina" + colors["reset"])
        game = str(input())
    print()
    print("así que quieres pasar tus ultimos momentos en la " + colors["red"] + f"{'GUILLOTINA...' if game.lower() == 'g' else 'HORCA...'}" + colors["reset"])
    print("Bueno, vamos a iniciar, no sentirás nada, espero. solo es....")
    time.sleep(1)
    print(colors["green"] + "... " + colors["reset"])
    time.sleep(1)
    print()


# main
def main():
    print()
    print("﹌﹌﹌﹌﹌  Bienvenido al juego de LA HORCA ☠️  ☠️  ﹌﹌﹌﹌﹌ ... y la guillotina 😅")
    print()
    print("Antes de iniciar...")
    name = None
    while(not name):
        print(colors["yellow"] + "Ingresa tu nombre: " + colors["reset"])
        name = str(input())
    print()
    dif = None
    while(dif != "f" and dif != "i" and dif != "d"):
        print(colors["yellow"] + "Selecciona una dificultad: " + colors["blue"] +"Ingresa (f) para facil, (i) para intermedio o (d) para dificil" + colors["reset"])
        dif = str(input())
    if(dif == "f"):
        trys = 8
    elif(dif == "i"):
        trys = 6
    else:
        trys = 4
    print()
    print(f"Conque {name}... Bueno {name}, haz cometido un crimen imperdonabile... {random.choice(bad_jokes)} y el rey 👑 te ha condenado a la" + colors["red"] + " PENA DE MUERTE... \n" + colors["reset"] +
          "Pero no te preocupes, Tu puedes elegir de que forma quieres morir; No es fantástico? 😂")
    time.sleep(2)
    print()
    print(f"Cuéntame {'camilo' if name.lower().startswith('carlos') else 'carlos'}.. o {name}? no importa.")
    game(name,trys)
    
main()

