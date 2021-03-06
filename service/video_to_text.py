"""
Сервис извлечения аудио дорожки из видео и первода в текстовый формат
"""

import os
from abc import ABC, abstractmethod
from pathlib import Path
from math import ceil
from typing import List
import numpy as np

from moviepy import editor as mp

from infrastructure.audio_to_text.abstract import BaseModel
from infrastructure.text_processors.ner import EntityExtractor


class BaseVideoToText(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def video_to_text(self, video_path: Path):
        pass 


class VideoToTextService(BaseVideoToText):

    def __init__(
        self, 
        audio_to_text_model: BaseModel, 
        spell_corrector: BaseModel, 
        ner: EntityExtractor,
        normalizer: BaseModel
        ):
        self.audio_to_text_model = audio_to_text_model
        self.spell_corrector = spell_corrector
        self.ner = ner
        self.normalizer = normalizer
    
    @staticmethod
    def _save_audio_from_video(
        video_path: str, 
        audio_save_path: str,
        filename: str, 
        clip_duration: int = 60
        ) -> str:

        chunk_paths = []

        audio = mp.AudioFileClip(video_path)
        chunks = ceil(audio.duration / clip_duration)

        start = 0
        for i in range(chunks):
            chunk_path = f"{audio_save_path}/{filename}_{i}.mp3"
            newsound = audio.subclip(start, np.clip(start+clip_duration, clip_duration, audio.duration))
            newsound.write_audiofile(chunk_path)
            start += clip_duration
            chunk_paths.append(chunk_path)

        return chunk_paths

    def video_to_text(self, video_path: Path) -> dict:
        audio_save_path = str(video_path.resolve().parent)
        filename = str(video_path.stem)
        video_path = str(video_path.absolute())
        # extract audio
        chunk_paths = VideoToTextService._save_audio_from_video(video_path, audio_save_path, filename)
        text_from_audio = self.audio_to_text_model.inference_model(chunk_paths)
        VideoToTextService._rm_audio_files(chunk_paths)
        text_from_audio = self.spell_corrector.inference_model(text_from_audio)
        text_from_audio = self.normalizer.inference_model(text_from_audio)
        entities = self.ner.get_entities(text_from_audio)
        return {
            'text': text_from_audio,
            'tags': entities
        }

    @staticmethod
    def _rm_audio_files(paths: List):
        for file_path in paths:
            os.remove(file_path)
    