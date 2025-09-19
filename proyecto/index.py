#config
import random # Para las elecciones aleatorias
import time # para los sleeps en el codigo
import math # para el calculo de los dibujos
import json # para operar los JSON
from pathlib import Path # para verificar la existencia de los archivos entre otras cosas
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"] 
# Los chistes tienen que ser igual de malos que la historia 😅
bad_jokes = ["Cancelaste una materia en tercera semana","Preparaste pizza con piña","Atropellaste a una abuelita con tu carruaje", "Te robaste el caballo real", "Besaste a la princesa 😏"] 
win_message = ["El rey encontrará otra manera de eliminarte...","Solo fue suerte...","Trabajas bien bajo presión...","No te metas en problemas de nuevo"]
lose_message = ["JAJAJA en serio creiste que le ganarías al rey? 😂", "Mejor suerte para la próxima... ¿verdad que no hay? 😂" ,"Para la proxima aprendete el abecedario 🤓", "No te tenia fe la verdad...", "Tal vez es muy dificil para ti 🍼"]
default_categories = [
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
categories_path = Path("categories.txt")
users_path = Path("users.txt")
config_path = Path("config.txt")
if(not categories_path.exists()):
    with categories_path.open("x",encoding="utf-8") as f:
        json.dump(default_categories,f,ensure_ascii=False,indent=3)
    

#Se guarda por default las categorias del juego en un archivo .txt con formato json para hacerlo facil de manipular
name = None
rememberName = False
if(config_path.exists()): # Se verifica si el usuario tiene la configuración de guardar usuario activada
    with config_path.open("r",encoding='utf-8') as f:
        config = json.load(f)
        if(config["remember_name"]):
            name = config["name"]
            rememberName = True


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
    # animación para la muerte
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
        time.sleep(2)
        return
    
    steps = math.ceil((trys / maxTrys) * 7) 
    # se calcula que paso del esquema es según la cantidad de intentos con el limite de intentos. esto se multiplica por el maximo de animaciones y finalmente
    # se aproxima al entero mas grande
    # ahora se arma el esquema segun el paso
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

# igual que con el ahorcado
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
# funcion donde corre la partida
def game(name, maxTrys, his):
    game = None
    while(game != "g" and game != "h"):
        print(colors["yellow"] + "De que manera quieres morir?:" + colors["blue"] + " Ingresa (h) para Horca y (g) Para Guillotina" + colors["reset"])
        game = str(input())
    print()
    if(his):
        print("así que quieres pasar tus ultimos momentos en la " + colors["red"] + f"{'GUILLOTINA...' if game.lower() == 'g' else 'HORCA...'}" + colors["reset"])
        print("Bueno, vamos a iniciar, no sentirás nada, espero. solo es....")
        time.sleep(2)
        print(colors["green"] + "... " + colors["reset"])
        time.sleep(2)
        print("Parece que el rey 👑 te ha dado una oportunidad..")
        print("Tienes que adivinar su " + colors["green"] + "PALABRA SECRETA" + colors["reset"] +  " antes de que te maten!!!")
        time.sleep(2)
    # se hace un random de las categorias y palabras, tambien se verifica que no se repita la palabra con la ultima palabra que tuvo el usuario
    # se usa shuffle para darle un poco mas de "aleatoriedad" 
    with categories_path.open("r", encoding='utf-8') as f:
        categories = json.load(f)
    random.shuffle(categories)
    cat_info = random.choice(categories)
    cat_name = cat_info["name"]
    wordList = cat_info["words"]
    random.shuffle(wordList)
    word = random.choice(wordList)
    if users_path.exists():
        with users_path.open("r", encoding="utf-8") as f:
            users = json.load(f)

        
        user = None 
        for u in users:
            if u["name"] == name:
                user = u
                break  

        if(user):
            
            while (word == user["last_word"]):
                word = random.choice(wordList)
    trys = 0
    crrntWord =[]
    for l in word:
        crrntWord.append("_")
    fail_letters = []
    while trys < maxTrys and "".join(crrntWord) != word:
        
        print("\n" + "=" * 30)
        print(f" Categoría: {cat_name}")
        print(f" Palabra: {' '.join(crrntWord)}")
        print(f" Intentos restantes: {maxTrys - trys}")
        print(f" Letras fallidas: " + " ".join(fail_letters))
        print("=" * 30)
        if(game == 'g'):
            guillotine(trys,maxTrys,dead=False)
        else:
            gallows(trys,maxTrys,dead=False)
        print( colors["yellow"] + "Adivina una letra: "+ colors ["blue"] + " (O pulsa Enter para elegir de manera aleatoria)" + colors["reset"])
        guess = str(input()).lower()
        if(not guess):
            random.shuffle(letters)
            guess = random.choice(letters)
        if len(guess) != 1 or not guess.isalpha():
            print(colors["red"] + "Ingresa solo una letra. no hay afán 😁👍"+ colors["reset"])
            continue

        if guess in word:
            for i, l in enumerate(word):
                if l == guess:
                    crrntWord[i] = guess
                    
        else:
            fail_letters.append(guess)
            trys += 1

    finishWord= "".join(crrntWord)
    # guarda los resultados del usuario
    if(not users_path.exists()):
        with users_path.open("w",encoding='utf-8') as f:
            json.dump([{"name":name,"wins":1 if finishWord == word else 0,"loses":1 if finishWord != word else 0,"rounds":1,"last_word":word}],f,ensure_ascii=False,indent=3)
    else:
        with users_path.open("r", encoding="utf-8") as f:
            data = json.load(f) 
            exists = False
            for p in data:
                if(p["name"] == name):
                    p["wins"] += 1 if finishWord == word else 0
                    p["loses"] += 1 if finishWord != word else 0
                    p["rounds"] += 1
                    p["last_word"] = word
                    exists = True
                    break
            if(not exists):
                data.append({"name":name,"wins":1 if finishWord == word else 0,"loses":1 if finishWord != word else 0,"rounds":1,"last_word":word})
            with users_path.open("w",encoding='utf-8') as f:
                json.dump(data,f,ensure_ascii=False,indent=3)
    # muestra los resulrados y carga la animación de muerte en caso de perder
    if(finishWord == word):
        print(colors["green"] +"""
 ██████╗  █████╗ ███╗   ██╗ █████╗ ███████╗████████╗███████╗
██╔════╝ ██╔══██╗████╗  ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝
██║  ███╗███████║██╔██╗ ██║███████║███████╗   ██║   █████╗  
██║   ██║██╔══██║██║╚██╗██║██╔══██║╚════██║   ██║   ██╔══╝  
╚██████╔╝██║  ██║██║ ╚████║██║  ██║███████║   ██║   ███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝
                                                            
""" +colors["reset"])
        random.shuffle(win_message)
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
        random.shuffle(lose_message)
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
        random.shuffle(lose_message)
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
        random.shuffle(bad_jokes)
        print(f"Conque {name}... Bueno {name}, haz cometido un crimen imperdonabile... {random.choice(bad_jokes)} y el rey 👑 te ha condenado a la" + colors["red"] + " PENA DE MUERTE... \n" + colors["reset"] +
            "Pero no te preocupes, tú puedes elegir de qué forma quieres morir. No es fantástico? 😂")
        time.sleep(2)
        print()
       
    game(name,maxTrys,his)
# se manejan todas las opciones del menú
def optionsMenu(option, name):
    if(option == 1):
        main(name, his=True)
    elif(option == 2):
        main(name,his=False)
    elif(option == 3):
        if users_path.exists():
            with users_path.open("r", encoding='utf-8') as f:
                registration = json.load(f)
                
            topPlayers = sorted(registration, key=lambda x: x["wins"], reverse=True)[:3]

            print()
            print(colors["blue"] + "🏆 TOP JUGADORES 🏆" + colors["reset"])
            print(colors["yellow"] + "=====================" + colors["reset"])

            for i, player in enumerate(topPlayers, start=1):
                print(
                    colors["green"]
                    + f"{i}. {player['name']}"
                    + colors["reset"]
                    + f" | 🏅 Victorias: {player['wins']} | ☠️ Partidas perdidas: {player['loses']} | 📂 Total de partidas: {player['rounds']}"
                )

            print(colors["yellow"] + "=====================" + colors["reset"])
            input(colors["blue"] + "\nPresiona ENTER para regresar al menú..." + colors["reset"])
            menu(name)

        else:
            print()
            print(colors["red"] + "No existen partidas registradas" + colors["reset"])
            time.sleep(1)
            menu(name)
    elif (option == 4):
        newCatName = None
        newCatWords = []
        while(not newCatName):
            print()
            print(colors["yellow"] + "Ingrese el nombre de la nueva categoria de palabras" + colors["reset"])
            newCatName = str(input())
        print()
        print( colors["blue"] +"ahora ingrese palabra por palabra que desee agregar a esta categoria. al finalizar pulse ENTER (sin nada escrito)" + colors["reset"])
        indexWords = 1
        while(True):
            newWord = str(input(colors["yellow"] +f"Ingrese la palabra " + colors["green"] + str(indexWords) + ": " + colors["reset"]))
            indexWords = indexWords + 1 
            if(not newWord):
                break

            newCatWords.append(newWord.lower())
        print()
        print(colors["yellow"] + "============" + colors["reset"])
        print(colors["yellow"] + "Nombre de la categoria: " + colors["reset"] + newCatName)
        print(colors["yellow"] + "Palabras: " + colors["reset"])
        print("   " + " ".join(newCatWords))
        print(colors["yellow"] + "============" + colors["reset"])
        print()
        print(colors["yellow"] + "Deseas guardár esta categoria?"+ colors["reset"])
        r = None
        while(r != "si" and r != "no"):
            print(colors["blue"] + "Ingresa (si) para guardarla y (no) para cancelar" + colors["reset"])
            r = str(input())
        if(r == "si"):
            with categories_path.open("r",encoding='utf-8') as f:
                categoriesResult = json.load(f)
            catExists = False
            for cat in categoriesResult:
                if(cat["name"] == newCatName):
                    catExists = True
                    break
            if(not catExists):
                categoriesResult.append({"name":newCatName,"words":newCatWords})
                with categories_path.open('w',encoding='utf-8') as f:
                    json.dump(categoriesResult,f,ensure_ascii=False,indent=3)
                print()
                print(colors["green"] + f"Categoría {newCatName} guardada con exito!! ahóra podrá aparecer en las partidas")
                time.sleep(2)
                menu(name)
            else:
                print(colors["red"] + "Error, ya existe una categoría con este nombre")
                time.sleep(2)
                menu(name)
                    
                
        else:
            print()
            print(colors["red"] + "Se canceló el registro " + colors["reset"])
            menu(name)
        



    elif(option == 5):
        change =False
        while(not change):
            print()
            name = str(input(colors["yellow"] + "Ingresa tu nombre: "+ colors["reset"]))
            if(name):
                change = True
            else:
                print(colors["red"]+"El nombre no es valido" + colors["reset"])

        menu(name)
    elif(option == 6):
        print()
        print("- Cuando la opción de Recordar usuario está activa, siempre se va a cargar el usuario al iniciar el programa.")
        print()
        print("- Si Cambia de usuario sin desactivar la opción, podrá usar el nuevo usuario, pero siempre va a cargar el usuario configurado cuando se inicia el programa")
        print()
        time.sleep(4)
        
        remember_response = None
        while(remember_response != "activar" and remember_response != "desactivar"):
            print(colors["yellow"] + "Desea activar o desactivar la opcion de recordar usuario?")
            print(colors["blue"] + "Escriba (activar) para activar la opción y (desactivar) para desactivarla" + colors["reset"])
            remember_response = str(input())
        if(remember_response == "activar"):
            config_name = None
            while(not config_name):
                print(colors["yellow"]+ "Ingrese el nombre del usuario a recordar: " + colors["reset"])
                config_name = str(input())
            if(config_path.exists()):
                with config_path.open("r",encoding='utf-8') as f:
                    config_data = json.load(f)
                config_data["name"] = config_name
                config_data["remember_name"] = True
                with config_path.open("w",encoding='utf-8') as f:
                    json.dump(config_data,f,ensure_ascii=False,indent=3)
    
            else:
                with config_path.open("w",encoding='utf-8') as f:
                    json.dump({"name":config_name,"remember_name":True},f,ensure_ascii=False,indent=3)


        else:

            if(config_path.exists()):
                with config_path.open("r",encoding='utf-8') as f:
                    config_data = json.load(f)
                config_data["name"] = None
                config_data["remember_name"] = False
                with config_path.open("w",encoding='utf-8') as f:
                    json.dump(config_data,f,ensure_ascii=False,indent=3)
    
            else:
                with config_path.open("w",encoding='utf-8') as f:
                    json.dump({"name":None,"remember_name":False},f,ensure_ascii=False,indent=3)
    
        print()
        print(colors["green"] + "Se realizó el cambio correctamente. Es necesario reiniciar el programa." + colors["reset"])
        input(colors["yellow"] + "Pulse ENTER para cerrar el programa" + colors["reset"])
    
    elif(option == 7):
        print()
        print(colors["red"] + "ESTÁS SEGURO DE REINICIAR LA CONFIGURACIÓN COMO PREDETERMINADA ?")
        print(colors["blue"] + "Esto borrará todos los registros y configuraciones, esta acción no se puede deshacer" + colors["reset"])
        reset = None
        while(reset != "si" and reset != "no"):
            print()
            print(colors["yellow"] + "Desea reiniciar la configuración?: " + colors["blue"] + "¨Ingrese " + colors["red"] + "(si) " + colors["blue"] + "para reiniciar la configuración y (no) para cancelar la acción" + colors["reset"])
            reset = str(input())
        if(reset == "si"):
            if(config_path.exists()):
                config_path.unlink()

            if(users_path.exists()):
                users_path.unlink()

            if(categories_path.exists()):
                categories_path.unlink()

            print()
            print(colors["green"] + "Registros borrados con exito. es necesario reiniciar el programa" + colors["reset"])
            input(colors["yellow"] + "Pulse ENTER para cerrar el programa" + colors["reset"])

                          
        else:
            print()
            print("Se ha cancelado la opción")
            time.sleep(1)
            menu(name)
    elif(option == 8):
        print()
        print(colors["green"] + "Gracias por jugar 💕" + colors["reset"])


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
    print(colors["yellow"] + "3." + colors["blue"] + "Ver los mejores jugadores")
    print(colors["yellow"] + "4." + colors["blue"] + "Agregar mas palabras")
    print(colors["yellow"] + "5." + colors["blue"] + "Cambiar Usuario")
    print(colors["yellow"] + "6." + colors["blue"] + "Recordar usuario "+((colors["green"] + "(Activado)" + colors["reset"]) if rememberName else ( colors["red"] + "(Desactivado)"+colors["reset"])) )
    print(colors["yellow"] + "7." + colors["red"] + "Resetear configuración "+ colors['reset'])
    print(colors["yellow"] + "8." + colors["red"] + "Salir"+ colors['reset'])
    print()
    option = None
    while( option != "1" and option != "2"and option != "3"and option != "4"and option != "5" and option !="6" and option != "7" and option !=  "8"):
        option = input(colors['yellow'] + "Ingresa una opción: " + colors["reset"])
    option = int(option)
    optionsMenu(option, name)
    

        
    
menu(name)

