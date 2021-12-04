from infrastructure.audio_to_text.abstract import BaseModel
from nemo_text_processing.inverse_text_normalization.inverse_normalize import InverseNormalizer


class DummyNormalization(BaseModel):

    def __init__(self):
        pass

    def inference_model(self, model_input) -> str:
        return model_input


class NvidiaInverseNormalizer(BaseModel):

    def __init__(self):
        self.inverse_normalizer = InverseNormalizer(lang='ru')

    def inference_model(self, model_input) -> str:
        print('normalization')
        normed = self.inverse_normalizer.inverse_normalize(model_input, verbose=False)
        return normed
