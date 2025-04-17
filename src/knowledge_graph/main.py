import os
from src.knowledge_graph.prompts import extraction_user_prompt
from src.knowledge_graph.config import load_config

def main(input_path, output_path):
    # Leer el texto de entrada
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Simular extracción de triples (en lugar de llamada a LLM real)
    simulated_triples = [
        {"subject": "actividades humanas", "predicate": "impactan", "object": "medio ambiente"},
        {"subject": "modelo productivo", "predicate": "genera", "object": "impacto ambiental"},
        {"subject": "emisiones", "predicate": "aumentan", "object": "cambio climático"},
    ]

    # Visualizar con pyvis
    from pyvis.network import Network
    net = Network(height="600px", width="100%", directed=True)

    for triple in simulated_triples:
        subj = triple["subject"]
        pred = triple["predicate"]
        obj = triple["object"]
        net.add_node(subj, label=subj)
        net.add_node(obj, label=obj)
        net.add_edge(subj, obj, label=pred)

    net.show(output_path)
