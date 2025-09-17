#config
import random
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"] 
# Los chistes tienen que ser igual de malos que la historia 😅
bad_jokes = ["Cancelaste una materia en tercera semana","Preparaste pizza con piña","Atropellaste a una abuelita con tu carruaje", "Te robaste el caballo real", "Besaste a la princesa 😏"] 
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
    
    return

def guillotine(trys):
    return


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
    trys = None
    while(trys != "f" and trys != "i" and trys != "d"):
        print(colors["yellow"] + "Selecciona una dificultad: " + colors["blue"] +"Ingresa (f) para facil, (i) para intermedio o (d) para dificil" + colors["reset"])
        trys = str(input())
    if(trys == "f"):
        trys = 8
    elif(trys == "i"):
        trys = 6
    else:
        trys = 4
    print(trys)
    print()
    print(f"Conque {name}... Bueno {name}, haz cometido un crimen imperdonabile... {random.choice(bad_jokes)} y el rey 👑 te ha condenado a la" + colors["red"] + " PENA DE MUERTE... \n" + colors["reset"] +
          "Pero no te preocupes, Tu puedes elegir de que forma quieres morir; No es fantástico? 😂")
    print()
    print(f"Cuéntame {'camilo' if name.lower().startswith('carlos') else 'carlos'}.. o {name}? no importa.")
    game = None
    while(game != "g" and game != "h"):
        print(colors["yellow"] + "De que manera quieres morir?:" + colors["blue"] + " Ingresa (h) para Horca y (g) Para Guillotina" + colors["reset"])
        game = str(input())
    
    if(game == "g"):
        guillotine(trys)
    else:
        gallows(trys)
    
main()

