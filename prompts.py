extraction_user_prompt = """
Tu tarea es leer el texto (en español) y extraer todas las relaciones en formato Sujeto–Predicado–Objeto (S–P–O), expresadas también en español.

Sigue estas reglas:

- SOLO extrae relaciones significativas. Evita términos genéricos como "situación", "caso", "tema", "elemento", "cosa".
- Escribe todas las entidades y relaciones en minúsculas.
- Los predicados deben tener entre 1 y 3 palabras, y estar en español.
- Sustituye los pronombres por nombres si se puede inferir.
- Usa formas consistentes ("inteligencia artificial", no mezclar con "IA").

Devuelve únicamente un array JSON con los triples. Ejemplo:

```json
[
  {"subject": "ciudades inteligentes", "predicate": "mejoran", "object": "calidad de vida"},
  {"subject": "movilidad sostenible", "predicate": "reduce", "object": "emisiones"}
]
```

Aquí está el texto a procesar:
```{text}```
"""
