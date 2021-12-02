"""
Сервис извлечения аудио дорожки из видео и первода в текстовый формат
"""

from abc import ABC, abstractmethod
from pathlib import Path

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
    def _save_audio_from_video(video_path: str, audio_save_path: str) -> str:
        mp.AudioFileClip(video_path).write_audiofile(audio_save_path)


    def video_to_text(self, video_path: Path) -> str:
        video_path = str(video_path.absolute())
        audio_save_path = video_path.replace('mp4', 'mp3')

        VideoToTextService._save_audio_from_video(video_path, audio_save_path)

        transcrypt = self.audio_to_text_model.inference_model(audio_save_path)
        return transcrypt
