from handlers.video import VideoToTextHandler
from service.video_to_text import VideoToTextService


def create_dummy_handler() -> VideoToTextHandler:
    from infrastructure.audio_to_text.abstract import DummyModel
    from infrastructure.text_processors.spell_check import DummySpellCorrector
    from infrastructure.text_processors.ner import DummyEntityExtractor


    audio_to_text_model = DummyModel()
    spell_corrector = DummySpellCorrector()
    ner = DummyEntityExtractor()
    video_to_text_service = VideoToTextService(audio_to_text_model, spell_corrector, ner)
    handler = VideoToTextHandler(video_to_text_service)
    return handler

  
def create_transcrypt_handler() -> VideoToTextHandler:
    from infrastructure.audio_to_text.models import TranscryptModel
    from infrastructure.text_processors.spell_check import SpellingCorrection
    from infrastructure.text_processors.ner import EntityExtractor

    transcrypt_model = TranscryptModel()
    spell_corrector = SpellingCorrection()
    ner = EntityExtractor()
    video_to_text_service = VideoToTextService(transcrypt_model, spell_corrector, ner)
    
    handler = VideoToTextHandler(video_to_text_service)
    return handler


handlers = {
    "dummy_handler": create_dummy_handler,
    "transcrypt_handler": create_transcrypt_handler
}


def get_handler(handler_name: str):
    handler = handlers.get(handler_name, None)()
    return handler
