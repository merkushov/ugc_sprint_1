from pydantic import UUID4

from models.base import BaseModel


class InputEvent(BaseModel):
    movie_id: UUID4
    frames: int


class KafkaEvent(BaseModel):
    key: bytes
    value: bytes


class WatchProgressEvent(BaseModel):
    movie_id: UUID4
    user_id: UUID4
    frames: str

    def convert_to_kafka_event(self) -> KafkaEvent:
        key = f"{self.user_id}_{self.movie_id}".encode("utf-8")
        value = self.frames.encode("utf-8")
        return KafkaEvent(key=key, value=value)
