from abc import ABC, abstractmethod
import os
from pathlib import Path

from service.video_to_text import BaseVideoToText


class VideoToTextHandler:

    def __init__(self, video_to_text_service: BaseVideoToText):
        self.video_to_text_service = video_to_text_service

    def handle(self, video_bytes: bytes, video_id: str):
        """
        Takes responce a video converting to text responce
        - deserialize it (convert bytes to video)
        - process video in service
        - serialize results
        - return results to transport layer or frontend
        """
        save_dir = Path('tmp/')
        save_path = save_dir.joinpath(video_id)
        os.makedirs(save_dir, exist_ok=True)
        # save video from bytes
        VideoToTextHandler._save_video_from_bytes(video_bytes, save_path)
        # get transcrypt from video
        transcrypt = self.video_to_text_service.video_to_text(save_path)
        return transcrypt

    def _load_video_by_url(url: str):
        pass

    @staticmethod
    def _save_video_from_bytes(file_bytes: bytes, file_output: Path):
        with open(file_output, "wb") as out_file:
            out_file.write(file_bytes)
    

