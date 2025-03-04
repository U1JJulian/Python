import flet as ft #Importamos la libreria
def main (page: ft.Page):
    page.bgcolor=ft.colors.BLUE_GREY_800 #Cambiar color de la interfaz
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER #Centrar los elementos CrossAxisAligment.???
    page.title="Mi app basado en POO" #Titulo de la ventana
    texto=ft.Text("Mi primera app con flet") #Mostrar Texto
    texto2=ft.Text("Este es un ejemplo para mi canal de Youtube")
    textbox = ft.TextField(label="Escribe algo", width=300) #Creacion del textbox
    
    def cambiar_texto(self):
        texto2.value="Hola como estas"
        page.update()
    boton = ft.FilledButton(text="Cambiar texto", on_click=cambiar_texto)

    page.add(texto,texto2,textbox,boton) #Agregarlo en mi pagina
    

ft.app(target=main)
#ft.app(target=main, view=ft.WEB_BROWSER) #Para abrirlo en web