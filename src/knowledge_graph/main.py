from pyvis.network import Network

def main(input_path, output_path):
    # Leer el texto de entrada
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Simulación básica de extracción de triples
    triples = [
        {"subject": "impacto ambiental", "predicate": "es causado por", "object": "actividades humanas"},
        {"subject": "emisiones", "predicate": "afectan", "object": "cambio climático"}
    ]

    if not triples:
        print("❌ No se encontraron triples para generar el grafo.")
        return

    # Crear el grafo
    net = Network(height="600px", width="100%", directed=True)

    for triple in triples:
        subj = triple["subject"]
        pred = triple["predicate"]
        obj = triple["object"]
        net.add_node(subj, label=subj)
        net.add_node(obj, label=obj)
        net.add_edge(subj, obj, label=pred)

    # Guardar visualización
    net.show(output_path)
