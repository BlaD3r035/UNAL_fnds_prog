#config
import random
import time
import math
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"] 
# Los chistes tienen que ser igual de malos que la historia 😅
bad_jokes = ["Cancelaste una materia en tercera semana","Preparaste pizza con piña","Atropellaste a una abuelita con tu carruaje", "Te robaste el caballo real", "Besaste a la princesa 😏"] 
win_message = ["El rey encontrará otra manera de eliminarte...","Solo fue suerte..","Trabajas bien bajo presión...","No te metas en problemas de nuevo"]
lose_message = ["JAJAJA en serio creiste que le ganarías al rey? 😂", "Mejor suerte para la proxima... verdad que no hay 😂" ,"Para la proxima aprendete el abecedario 🤓"]
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
name = None
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
def gallows(trys, maxTrys, dead):
    if dead:
        
        
        print("      _______")
        print("     |/      |")
        print("     |      (_)")
        print("     |      \\|/")
        print("     |       |")
        print("     |      / \\")
        print("     |")
        print("  ___|___")
        time.sleep(2)

        
       
        print("      _______")
        print("     |/      |")
        print("     |      (_)")
        print("     |  " + colors["red"] +"     ." + colors["reset"])
        print("     |  " + colors["red"] +"     ." + colors["reset"])
        print("     |      \\|/")
        print("     |      / \\")
        print("  ___|___")
        time.sleep(1)

       
        print("      _______")
        print("     |/      |")
        print("     |      (_)")
        print("     |  " + colors["red"] +"     ." + colors["reset"])
        print("     |  " + colors["red"] +"     ." + colors["reset"])
        print("     |  " + colors["red"] +"     ." + colors["reset"])        
        print("     |      \\|/")
        print("     |      / \\")
        print("  ___|___")
        return
    
    steps = math.ceil((trys / maxTrys) * 7)

    print("      _______")
    print("     |/      |")
    
   
    print("     |      (_)" if steps >= 1 else "     |")

    
    if steps >= 2:
        if steps == 2:
            print("     |       |")
        elif steps == 3:
            print("     |      \\|")
        else:
            print("     |      \\|/")
    else:
        print("     |")
    
    
    if steps >= 5:
        if steps == 5:
            print("     |       |")
        elif steps == 6:
            print("     |      /")
        else:  
            print("     |      / \\")
    else:
        print("     |")
    
    print("     |")
    print("  ___|___")


def guillotine(trys, maxTrys, dead):
    if dead:
        print("   |=========|")
        print("   ||    /   |")
        print("   ||   /    |")
        print("   ||  /     |")
        print("   || /      |")
        print("   |=========|")
        print("   |         |")
        print("   |   (_)   |")
        print("   |_________|")
        print()
        time.sleep(2)

        print("   |=========|")
        print("   |  |      |")
        print("   | _|___   |")
        print("   ||    /   |")
        print("   ||   /    |")
        print("   ||  /     |")
        print("   |=========|")
        print("   |         |")
        print("   |   (_)   |")
        print("   |_________|")
        print()
        time.sleep(1)

        print("   |=========|")
        print("   |  |      |")
        print("   |  |      |")
        print("   |  |      |")
        print("   | _|___   |")
        print("   ||    /   |")
        print("   |=========|")
        print("   |         |")
        print("   |   ("+ colors["red"] + "." + colors["reset"] + ")   |")
        print("   |____"+ colors["red"] + "..(_)" + colors["reset"] + "|")
        print()
        return
    steps = math.ceil((trys / maxTrys) * 7)
    print(str(trys) + str(maxTrys) + str(steps))
   

  
    if steps >= 1:
        print("   |=========|")
    else:
        print("              ")

    
    if steps >= 2:
        print("   ||    /   |")
    else:
        print("              ")

  
    if steps >= 3:
        print("   ||   /    |")
    else:
        print("              ")

  
    if steps >= 4:
        print("   ||  /     |")
    else:
        print("              ")

    
    if steps >= 5:
        print("   || /      |")
        print("   |=========|")
    else:
        print("              ")
        print("              ")

   
    if steps >= 6:
        print("   |   (_)   |")
    else:
        print("   |         |")

    
    if steps >= 7:
        print("   |_________|")
    else:
        print("   |         |")

    print()

def game(name, maxTrys, his):
    game = None
    while(game != "g" and game != "h"):
        print(colors["yellow"] + "De que manera quieres morir?:" + colors["blue"] + " Ingresa (h) para Horca y (g) Para Guillotina" + colors["reset"])
        game = str(input())
    print()
    if(his):
        print("así que quieres pasar tus ultimos momentos en la " + colors["red"] + f"{'GUILLOTINA...' if game.lower() == 'g' else 'HORCA...'}" + colors["reset"])
        print("Bueno, vamos a iniciar, no sentirás nada, espero. solo es....")
        time.sleep(1)
        print(colors["green"] + "... " + colors["reset"])
        time.sleep(1)
        print("Parece que el rey 👑 te ha dado una oportunidad..")
        print("Tienes que adivinar su " + colors["green"] + "PALABRA SECRETA" + colors["reset"] +  " antes de que te maten!!!")

    cat_info = random.choice(categories)
    cat_name = cat_info["name"]
    wordList = cat_info["words"]
    word = random.choice(wordList)
    trys = 0
    crrntWord =[]
    for l in word:
        crrntWord.append("_")
    
    while trys < maxTrys and "".join(crrntWord) != word:

        print("\n" + "=" * 30)
        print(f" Categoría: {cat_name}")
        print(f" Palabra: {' '.join(crrntWord)}")
        print(f" Intentos restantes: {maxTrys - trys}")
        print("=" * 30)
        if(game == 'g'):
            guillotine(trys,maxTrys,dead=False)
        else:
            gallows(trys,maxTrys,dead=False)
        print( colors["yellow"] + "Adivina una letra: "+ colors ["blue"] + " (O pulsa Enter para elegir de manera aleatoria)" + colors["reset"])
        guess = str(input()).lower()
        if len(guess) != 1 or not guess.isalpha():
            print(colors["red"] + "Ingresa solo una letra. no hay afán 😁👍"+ colors["reset"])
            continue

        if guess in word:
            for i, l in enumerate(word):
                if l == guess:
                    crrntWord[i] = guess
                    
        else:
            trys += 1

    finishWord= "".join(crrntWord)
    if(finishWord == word):
        print(colors["green"] +"""
 ██████╗  █████╗ ███╗   ██╗ █████╗ ███████╗████████╗███████╗
██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝
██║  ███╗███████║██╔██╗ ██║███████║███████╗   ██║   █████╗  
██║   ██║██╔══██║██║╚██╗██║██╔══██║╚════██║   ██║   ██╔══╝  
╚██████╔╝██║  ██║██║ ╚████║██║  ██║███████║   ██║   ███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝
                                                            
""" +colors["reset"])
        print(colors["yellow"]+random.choice(win_message) + colors["reset"])
        print()
    elif (game == 'g'):
        guillotine(None,None,dead=True)
        print(colors["red"] + """
██████╗ ███████╗██████╗ ██████╗ ██╗███████╗████████╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██╔════╝
██████╔╝█████╗  ██████╔╝██║  ██║██║███████╗   ██║   █████╗  
██╔═══╝ ██╔══╝  ██╔══██╗██║  ██║██║╚════██║   ██║   ██╔══╝  
██║     ███████╗██║  ██║██████╔╝██║███████║   ██║   ███████╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝
                                                         
""" + colors["reset"])
        print(colors["red"]+random.choice(lose_message) + colors["reset"])
        print()
    else:
        gallows(None,None,dead=True)
        print(colors["red"] + """
██████╗ ███████╗██████╗ ██████╗ ██╗███████╗████████╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██╔════╝
██████╔╝█████╗  ██████╔╝██║  ██║██║███████╗   ██║   █████╗  
██╔═══╝ ██╔══╝  ██╔══██╗██║  ██║██║╚════██║   ██║   ██╔══╝  
██║     ███████╗██║  ██║██████╔╝██║███████║   ██║   ███████╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚══════╝
                                                            
""" + colors["reset"])
        print(colors["red"]+random.choice(lose_message) + colors["reset"])
        print()
    r = None
    while(r != "si" and r != "no"):
        print(colors["yellow"] + "Quieres jugar de nuevo? " + colors["blue"] + "(Ingresa (si) para jugar de nuevo y (no) para regresar al menú principal)" + colors["reset"])
        r = str(input())
    if(r == "si"):
        main(name,his=False)
    else:
        menu(name)


        



# main
def main(name, his):
    print()
    dif = None
    while(dif != "f" and dif != "i" and dif != "d"):
        print(colors["yellow"] + "Selecciona una dificultad: " + colors["blue"] +"Ingresa (f) para facil, (i) para intermedio o (d) para dificil" + colors["reset"])
        dif = str(input())
    if(dif == "f"):
        maxTrys = 8
    elif(dif == "i"):
        maxTrys = 6
    else:
        maxTrys = 4
    print()
    if(his):
        print(f"Conque {name}... Bueno {name}, haz cometido un crimen imperdonabile... {random.choice(bad_jokes)} y el rey 👑 te ha condenado a la" + colors["red"] + " PENA DE MUERTE... \n" + colors["reset"] +
            "Pero no te preocupes, Tu puedes elegir de que forma quieres morir; No es fantástico? 😂")
        time.sleep(2)
        print()
        print(f"Cuéntame {'camilo' if name.lower().startswith('carlos') else 'carlos'}.. o {name}? no importa.")
    game(name,maxTrys,his)

def menu(name):
    print()
    print(colors["yellow"] + r"""
 _                                 _                        _      _                  
| |                               | |                      | |    | |                 
| |     __ _    ___ ___  _ __   __| | ___ _ __   __ _    __| | ___| |  _ __ ___ _   _ 
| |    / _` |  / __/ _ \| '_ \ / _` |/ _ \ '_ \ / _` |  / _` |/ _ \ | | '__/ _ \ | | |
| |___| (_| | | (_| (_) | | | | (_| |  __/ | | | (_| | | (_| |  __/ | | | |  __/ |_| |
\_____/\__,_|  \___\___/|_| |_|\__,_|\___|_| |_|\__,_|  \__,_|\___|_| |_|  \___|\__, |
                                                                                 __/ |
                                                                                |___/ 
""" + colors["reset"])
    print()
    while(not name):
        print("Antes de iniciar...")
        print(colors["yellow"] + "Ingresa tu nombre: " + colors["reset"])
        name = str(input())
    print()
    print("Hola " + colors["yellow"] + name + colors["reset"])
    print()
    print(colors["green"] + "Menú principal" + colors["reset"])
    print(colors["yellow"] + "1." + colors["blue"] + "Jugar")
    print(colors["yellow"] + "2." + colors["blue"] + "Jugar (sin historia) ")
    print(colors["yellow"] + "3." + colors["blue"] + "Ver registro de mejores puntajes")
    print(colors["yellow"] + "4." + colors["blue"] + "Cambiar nombre")
    print(colors["yellow"] + "5." + colors["red"] + "Salir"+ colors['reset'])
    print()
    option = None
    while( option != "1" and option != "2"and option != "3"and option != "4"and option != "5"):
        option = input(colors['yellow'] + "Ingresa una opción: " + colors["reset"])
    option = int(option)
    if(option == 1):
        main(name, his=True)
    elif(option == 2):
        main(name,his=False)
    elif(option == 3):
        ""
    elif(option == 4):
        change =False
        while(not change):
            print()
            name = str(input(colors["yellow"] + "Ingresa tu nombre: "+ colors["reset"]))
            if(name):
                change = True
            else:
                print(colors["red"]+"El nombre no es valido" + colors["reset"])

        menu(name)
    

menu(name)

