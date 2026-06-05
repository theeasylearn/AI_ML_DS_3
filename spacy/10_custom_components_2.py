import spacy as sa 
from spacy.language import Language
from spacy.tokens import Doc
import re 
#property 
Doc.set_extension("coordinates",default=[])
text = """The modern field of geospatial analysis relies heavily on the precise extraction of coordinate data from unstructured text, a task perfectly suited for custom natural language processing pipelines. When building a specialized Named Entity Recognition component in spaCy, providing diverse syntactic contexts is critical for model accuracy. Consider a global logistics firm tracking assets across various terrain types and shipping lanes. A shipping vessel departing from Europe might report its initial anchoring position in the Mediterranean Sea at 34°05'N, 12°15'E, where standard maritime notations are heavily utilized by automated logging systems. As the vessel transitions into open waters, the NLP pipeline must remain resilient to shifts in text structure, adapting to both formal logs and casual radio transcripts. Meanwhile, a terrestrial research team operating in the dense wilderness of South America might log their base camp coordinates using standard decimal formats, documenting their exact biological survey starting point at -3.1019, -60.0250 deep within the Amazon basin. Because spaCy models rely on tokenization patterns, exposing the custom component to negative signs, decimals, and degree symbols within the same training block prevents overfitting to a single layout. Moving across the globe to urban infrastructure management, a city planning committee in Australia might analyze transit congestion by pinning a central metropolitan hub located precisely at 37.8136° S, 144.9631° E, mixing decimal precision with directional cardinal suffixes. This variation forces the transition-based parser in spaCy to look at surrounding tokens, such as prepositions and adjacent nouns, rather than relying solely on rigid regular expressions. Furthermore, aviation logs introduce another layer of textual complexity, often embedding coordinates directly into dense, rapid-fire flight telemetry reports. An international cargo flight crossing northern airspace might log a critical waypoint over the high-altitude terrain of Central Asia, marking their position at 39.9042° N, 116.4074° E during a routine atmospheric data collection sweep. If the NER model is trained only on clean, isolated tables, it will inevitably fail when encountering these coordinates buried deep within long-form prose. Finally, environmental monitoring stations tracking volcanic activity in Iceland require extreme precision, often broadcasting telemetry strings that place a specific seismic sensor at 64.1466, -21.9426 amid a flurry of geological metrics. By combining all five of these distinct spatial anchors into a single, cohesive narrative framework, the spaCy pipeline learns to recognize the semantic boundaries of geographic entities regardless of regional formatting habits. Software engineers can tokenize this text, apply precise character-level offsets for the entity spans, and feed the annotated annotations into the standard spaCy training loop. Through iterative epochs, the convolutional layers of the model will successfully weight these diverse numerical expressions, ultimately resulting in a robust, production-ready custom component capable of parsing global coordinate data with high accuracy..
"""
COORDINATE_PATTERNS = {
    # 1. Decimal Degrees (DD): Captures signed floats or floats followed by N,S,E,W
    # Examples: -37.8136, 144.9631 or 37.8136° S, 144.9631° E
    "COORD_DD": re.compile(
        r'(?:-?\d{1,3}\.\d+)\s*°?\s*[NS]?[\s,]+(?:-?\d{1,3}\.\d+)\s*°?\s*[EW]?'
    ),
    
    # 2. Degrees, Minutes, Seconds (DMS): Captures standard maritime/aviation layout
    # Examples: 40° 42' 46" N, 74° 00' 21" W or 40°42'N, 12°15'E
    "COORD_DMS": re.compile(
        r'\d{1,3}°\s*\d{1,2}\'(?:\s*\d{1,2}(?:\.\d+)?[”"])?\s*[NS][\s,]+\d{1,3}°\s*\d{1,2}\'(?:\s*\d{1,2}(?:\.\d+)?[”"])?\s*[EW]',
        re.IGNORECASE
    ),
    
    # 3. UTM Coordinates: Captures Grid Zone Designator + Easting/Northing meters
    # Example: 18T 583960m E 4507340m N or 18T 583960 E 4507340 N
    "COORD_UTM": re.compile(
        r'\b\d{1,2}[C-X]\s+\d{5,7}m?\s*[EA]\s+\d{6,8}m?\s*[NO]\b',
        re.IGNORECASE
    ),
    
    # 4. Geohash: Captures standard base32 geohashes (5 to 12 alphanumeric characters, excluding a, i, l, o)
    # Uses a lookahead barrier to avoid matching random lowercase dictionary words
    # "COORD_GEOHASH": re.compile(
    #     r'\b[0-9b-hjkmnp-z]{5,12}\b'
    # )
}
@Language.component("getCoordinates")
def getCoordinates(doc):
    doc_text = doc.text
    list = []
    for label, pattern in COORDINATE_PATTERNS.items():
        for match in pattern.finditer(doc.text):
            start_char, end_char = match.span()
            
            # Align the regex character offsets cleanly with spaCy token boundaries
            span = doc.char_span(start_char, end_char, label=label, alignment_mode="contract")
            
            if span is not None:
               list.append(span)
    doc._.coordinates = list
    return doc

nlp = sa.load('en_core_web_sm')
nlp.add_pipe("getCoordinates",last=True)
doc = nlp(text)
print(doc._.coordinates)

