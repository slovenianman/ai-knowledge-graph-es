import argparse
import os
import sys

# Comprobamos que el módulo src.knowledge_graph está accesible
sys.path.append(os.path.abspath("."))

try:
    from src.knowledge_graph.main import main
except ImportError as e:
    print("❌ ERROR: No se puede importar el módulo principal.")
    print(e)
    sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generador de grafos de conocimiento desde texto.")
    parser.add_argument("--input", type=str, required=True, help="Ruta del archivo de texto (.txt)")
    parser.add_argument("--output", type=str, default="mi_grafo.html", help="Ruta del archivo HTML de salida")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"❌ ERROR: El archivo de entrada '{args.input}' no existe.")
        sys.exit(1)

    try:
        main(args.input, args.output)
    except KeyError as e:
        print("❌ ERROR: Fallo al formatear el prompt. Verifica que uses '{{' y '}}' en el JSON de ejemplo.")
        print(f"Detalle: {e}")
        sys.exit(1)
    except Exception as e:
        print("❌ ERROR durante la ejecución del grafo:")
        print(e)
        sys.exit(1)
