import tkinter as tk

# constantes
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50

# nuestra "Base de Datos"
VOCABULARY = [
    {
        "word": "Actually", 
        "correct": "En realidad", 
        "wrong": "Actualmente"
    },
    {
        "word": "Sensible", 
        "correct": "Sensato", 
        "wrong": "Sensible"
    },
    {
        "word": "Embarrassed",
        "correct": "Avergonzado",
        "wrong": "Embarazada"
    }
]

# estado global
current_index = 0

def draw_interface():
    """Dibuja la interfaz leyendo los datos actuales. Es como el render de un componente."""
    canvas.delete("all")  # Limpiamos el lienzo completo
    
    # comprobamos si hemos terminado
    if current_index >= len(VOCABULARY):
        canvas.create_text(200, 200, text="¡Completado!", font=("Arial", 30))
        return

    word_data = VOCABULARY[current_index]
    
    # dibujar la palabra principal
    canvas.create_text(200, 100, text=word_data["word"], font=("Arial", 30))
    
    # dibujar el botón izquierdo (Correcto)
    # Nota: En Tkinter, los rectángulos se rellenan con 'fill'
    canvas.create_rectangle(30, 250, 30 + BUTTON_WIDTH, 250 + BUTTON_HEIGHT, fill="lightblue")
    canvas.create_text(105, 275, text=word_data["correct"], font=("Arial", 12))

    # dibujar el botón derecho (Incorrecto)
    canvas.create_rectangle(220, 250, 220 + BUTTON_WIDTH, 250 + BUTTON_HEIGHT, fill="lightblue")
    canvas.create_text(295, 275, text=word_data["wrong"], font=("Arial", 12))

def handle_click(event):
    """Esta función es nuestro Event Listener. Se dispara solo al hacer clic."""
    global current_index
    
    # si el juego ha terminado, ignoramos los clics
    if current_index >= len(VOCABULARY):
        return

    mouse_x = event.x
    mouse_y = event.y
    word_data = VOCABULARY[current_index]
    
    #  BOTÓN IZQUIERDO (CORRECTO)
    if (30 <= mouse_x <= 180) and (250 <= mouse_y <= 300):
        # Feedback verde
        canvas.create_rectangle(30, 250, 30 + BUTTON_WIDTH, 250 + BUTTON_HEIGHT, fill="green")
        canvas.create_text(105, 275, text=word_data["correct"], font=("Arial", 12))
        
        # Avanzamos el estado y usamos root.after() en lugar de time.sleep()
        # root.after(500, funcion) ejecuta la función tras 500 milisegundos (medio segundo)
        current_index += 1
        root.after(500, draw_interface)
        
    #  BOTÓN DERECHO (INCORRECTO)
    elif (220 <= mouse_x <= 370) and (250 <= mouse_y <= 300):
        # feedback rojo
        canvas.create_rectangle(220, 250, 220 + BUTTON_WIDTH, 250 + BUTTON_HEIGHT, fill="red")
        canvas.create_text(295, 275, text=word_data["wrong"], font=("Arial", 12))
        
        # volvemos a pintar la misma palabra tras medio segundo para quitar el rojo
        root.after(500, draw_interface)

# INICIALIZACIÓN DE LA APLICACIÓN 

# creamos la ventana base
root = tk.Tk()
root.title("App de Vocabulario")

# creamos el lienzo y lo empaquetamos en la ventana
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# añadimos el Event Listener del ratón (Clic Izquierdo = <Button-1>)
canvas.bind("<Button-1>", handle_click)

# pintamos la primera palabra
draw_interface()

# iniciamos el bucle principal de la aplicación
root.mainloop()