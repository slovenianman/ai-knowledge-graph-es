from src.knowledge_graph.main import main
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, help="Ruta del archivo .txt")
    parser.add_argument("--output", type=str, default="mi_grafo.html", help="Archivo de salida")
    args = parser.parse_args()
    main(args.input, args.output)
