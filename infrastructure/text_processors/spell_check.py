from infrastructure.audio_to_text.abstract import BaseModel

from deeppavlov import build_model, configs


class DummySpellCorrector(BaseModel):

    def __init__(self):
        pass

    def inference_model(self, model_input) -> str:
        return model_input


class SpellingCorrection(BaseModel):

    def __init__(self):
        self.config_path = configs.spelling_correction.brillmoore_kartaslov_ru
        self.model = build_model(self.config_path, download=True)

    def inference_model(self, model_input) -> str:
        print('spell checking')
        checked = self.model([model_input])[0]
        return checked
