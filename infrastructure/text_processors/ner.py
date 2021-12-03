from typing import List

from natasha import (
       Segmenter,
       MorphVocab,
       NewsEmbedding,
       NewsMorphTagger,
       NewsSyntaxParser,
       NewsNERTagger,
       NamesExtractor,
       Doc
)


class EntityExtractor:
    def __init__(self):
        self.segmenter = Segmenter()
        self.morph_vocab = MorphVocab()

        self.emb = NewsEmbedding()
        self.morph_tagger = NewsMorphTagger(self.emb)
        self.syntax_parser = NewsSyntaxParser(self.emb)
        self.ner_tagger = NewsNERTagger(self.emb)

        self.names_extractor = NamesExtractor(self.morph_vocab)

    def get_entities(self, text: str) -> List[str]:
        doc = Doc(text)

        doc.segment(self.segmenter)
        doc.parse_syntax(self.syntax_parser)
        doc.tag_morph(self.morph_tagger)
        doc.tag_ner(self.ner_tagger)
        for span in doc.spans:
            span.normalize(self.morph_vocab)
        entities = [span.normal for span in doc.spans]

        return entities
