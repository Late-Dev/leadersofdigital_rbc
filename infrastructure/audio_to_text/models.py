from asrecognition import ASREngine

from infrastructure.audio_to_text.abstract import BaseModel


class TranscryptModel(BaseModel):
    """
    Transcrypt works with audio paths
    """

    def __init__(self):
        self.asr = ASREngine("ru", model_path="jonatasgrosman/wav2vec2-large-xlsr-53-russian")

    def inference_model(self, audio_rec) -> str:
        rec_paths = [audio_rec]
        transcriptions = self.asr.transcribe(rec_paths)
        return transcriptions
