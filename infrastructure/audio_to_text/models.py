from typing import List

from asrecognition import ASREngine
import torch

from infrastructure.audio_to_text.abstract import BaseModel


class TranscryptModel(BaseModel):
    """
    Transcrypt works with audio paths
    """

    def __init__(self):
        self.device = self._select_device()
        self.asr = ASREngine("ru", model_path="jonatasgrosman/wav2vec2-large-xlsr-53-russian", device=self.device)

    def inference_model(self, rec_paths: List) -> str:
        transcriptions = []
        for rec_path in rec_paths:
            print(rec_path)
            transcription = self.asr.transcribe([rec_path])
            transcriptions.extend(transcription)
        text_from_audio = "".join([i['transcription'] for i in transcriptions])
        return text_from_audio

    def _select_device(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        return device
