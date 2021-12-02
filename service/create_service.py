from service.video_to_text import VideoToTextService


def create_dummy_service():
    from infrastructure.audio_to_text.abstract import DummyModel

    audio_to_text_model = DummyModel()
    audio_to_text_service = VideoToTextService(audio_to_text_model)
    return audio_to_text_service

  
def create_transcrypt_service():
    from infrastructure.audio_to_text.models import TranscryptModel

    transcrypt_model = TranscryptModel()
    video_to_text_service = VideoToTextService(transcrypt_model)
    return video_to_text_service


services = {
    "dummy_service": create_dummy_service(),
    "transcrypt_service": create_transcrypt_service()
}

def get_service(service_name: str):
    service = services.get(service_name, None)
    return service
