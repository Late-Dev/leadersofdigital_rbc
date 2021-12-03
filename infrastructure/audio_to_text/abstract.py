from abc import ABC, abstractmethod
from typing import List


class BaseModel(ABC):

    @abstractmethod
    def __init__(self):
        """
        Initialize model path or som input parameters
        """
        pass

    @abstractmethod
    def inference_model(self, model_input) -> str:
        """
        Make a model nference
        :return:
        """
        pass


class DummyModel(BaseModel):

    def __init__(self):
        pass

    def inference_model(self, model_input=None):
        transcrypt = "Это тестовый текст с видео"
        return transcrypt
