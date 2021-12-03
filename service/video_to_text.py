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


class BaseVideoToText(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def video_to_text(self, video_path: Path):
        pass 


class VideoToTextService(BaseVideoToText):

    def __init__(self, audio_to_text_model: BaseModel):
        self.audio_to_text_model = audio_to_text_model
    
    @staticmethod
    def _save_audio_from_video(
        video_path: str, 
        audio_save_path: str,
        filename: str, 
        clip_duration: int = 110
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

    def video_to_text(self, video_path: Path) -> str:
        audio_save_path = str(video_path.resolve().parent)
        filename = str(video_path.stem)
        video_path = str(video_path.absolute())
        # extract audio
        chunk_paths = VideoToTextService._save_audio_from_video(video_path, audio_save_path, filename)
        transcrypts = self.audio_to_text_model.inference_model(chunk_paths)
        text_from_audio = "".join([i['transcription'] for i in transcrypts])
        self._rm_audio_files(chunk_paths)
        return text_from_audio

    def _rm_audio_files(paths: List):
        for file_path in paths:
            os.remove(file_path)
    
