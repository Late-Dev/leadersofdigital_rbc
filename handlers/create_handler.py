from handlers.video import VideoToTextHandler
from service.video_to_text import VideoToTextService


def create_dummy_handler() -> VideoToTextHandler:
    from infrastructure.audio_to_text.abstract import DummyModel

    audio_to_text_model = DummyModel()
    video_to_text_service = VideoToTextService(audio_to_text_model)
    handler = VideoToTextHandler(video_to_text_service)
    return handler

  
def create_transcrypt_handler() -> VideoToTextHandler:
    from infrastructure.audio_to_text.models import TranscryptModel
    from infrastructure.audio_to_text.spell_check import SpellingCorrection

    transcrypt_model = TranscryptModel()
    video_to_text_service = VideoToTextService(transcrypt_model)
    spell_corrector = SpellingCorrection()
    handler = VideoToTextHandler(video_to_text_service, spell_corrector)
    return handler


handlers = {
    "dummy_handler": create_dummy_handler(),
    "transcrypt_handler": create_transcrypt_handler()
}


def get_handler(handler_name: str):
    handler = handlers.get(handler_name, None)
    return handler
