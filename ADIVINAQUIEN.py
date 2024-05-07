import os
from PIL import Image

def main():
    # Cargar imagen
    menu_image_path = "menu.png"
    os.system("open " + menu_image_path)

    while True:
        genero = input("¿El personaje es hombre, mujer o extraterrestre?: ")
        edad = input("¿Es el personaje un adulto, un niño o no tiene edad?: ")
        color_ropa = input("¿De qué color es la ropa de tu personaje?: ")
        color_cabello = input("¿De qué color es el cabello del personaje?: ")

        if genero.lower() == "hombre" and edad.lower() == "adulto" and color_ropa.lower() == "blanco" and color_cabello.lower() == "no tiene":
            print("Tu personaje es Homero")
            mostrar_imagen("Homero.png")
        elif genero.lower() == "mujer" and edad.lower() == "adulto" and color_ropa.lower() == "verde" and color_cabello.lower() == "azul":
            print("Tu personaje es Marge")
            mostrar_imagen("Marge.png")
        elif genero.lower() == "hombre" and edad.lower() == "niño" and color_ropa.lower() == "rojo" and color_cabello.lower() == "amarillo":
            print("Tu personaje es Bart")
            mostrar_imagen("Bart.png")
        elif genero.lower() == "mujer" and edad.lower() == "niño" and color_ropa.lower() == "rojo" and color_cabello.lower() == "amarillo":
            print("Tu personaje es Lisa")
            mostrar_imagen("Lisa.png")
        elif genero.lower() == "mujer" and edad.lower() == "niño" and color_ropa.lower() == "azul" and color_cabello.lower() == "amarillo":
            print("Tu personaje es Maggie")
            mostrar_imagen("Maggie.png")
        elif genero.lower() == "hombre" and edad.lower() == "adulto" and color_ropa.lower() == "verde" and color_cabello.lower() == "castaño":
            print("Tu personaje es Flanders")
            mostrar_imagen("Flanders.png")
        elif genero.lower() == "hombre" and edad.lower() == "adulto" and color_ropa.lower() == "aqua" and color_cabello.lower() == "gris":
            print("Tu personaje es Burns")
            mostrar_imagen("Burns.png")
        elif genero.lower() == "hombre" and edad.lower() == "niño" and color_ropa.lower() == "rosa" and color_cabello.lower() == "azul":
            print("Tu personaje es Milhouse")
            mostrar_imagen("Milhouse.png")
        elif genero.lower() == "mujer" and edad.lower() == "adulto" and color_ropa.lower() == "verde" and color_cabello.lower() == "castaño":
            print("Tu personaje es Edna")
            mostrar_imagen("Edna.png")
        elif genero.lower() == "extraterrestre" and edad.lower() == "adulto" and color_ropa.lower() == "transparente" and color_cabello.lower() == "no tiene":
            print("Tu personaje es Kang")
            mostrar_imagen("Kang.png")
        else:
            print("No se puede determinar el personaje con las respuestas dadas.")

        respuesta = input("¿Quieres jugar de nuevo? (si/no): ")
        if respuesta.lower() != "si":
            print("¡Gracias por jugar! Hasta luego.")
            break

def mostrar_imagen(nombre_imagen):
    imagen = Image.open(nombre_imagen)
    imagen.show()

if __name__ == "__main__":
    main()

