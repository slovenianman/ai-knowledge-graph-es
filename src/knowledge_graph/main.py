from src.knowledge_graph.config import load_config
from src.knowledge_graph.prompts import extraction_user_prompt

def main(input_path, output_path):
    with open(input_path, "r") as f:
        text = f.read()
    print("Ejecutando con el siguiente prompt:")
    print(extraction_user_prompt.format(text=text[:300] + "..."))
    # Aquí se llamaría al modelo y se generaría el grafo (omitido para simplificar)
    with open(output_path, "w") as out:
        out.write("<html><body><h1>Grafo generado</h1></body></html>")
