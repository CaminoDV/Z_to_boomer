"""Punto de entrada de la aplicación de traducción."""

from traductor import traducir_a_boomer


def iniciar_programa() -> None:
    """Ejecuta la interfaz por consola del traductor."""
    print("=== TRADUCTOR GEN Z -> BOOMER ===")
    
    texto_usuario: str = input("Escribe una frase: ")
    traduccion: str = traducir_a_boomer(texto_usuario)
    
    print(f"Traducción: {traduccion}")


if __name__ == "__main__":
    iniciar_programa()
