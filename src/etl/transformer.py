from functools import lru_cache
from typing import Iterator

from etl import models


class Transformer:
    def transform(
        self, raw_messages: Iterator[models.WatchingProgressKafkaSchema]
    ) -> models.WatchingProgressClickHouseSchema:
        for msg in raw_messages:
            yield self.transform_unit(raw_msg=msg)

    @staticmethod
    def transform_unit(
        raw_msg: models.WatchingProgressKafkaSchema,
    ) -> models.WatchingProgressClickHouseSchema:
        return models.WatchingProgressClickHouseSchema(
            user_id=raw_msg.user_id,
            film_id=raw_msg.movie_id,
            frame=raw_msg.frame,
            event_time=raw_msg.event_time,
        )


@lru_cache
def get_transformer() -> Transformer:
    return Transformer()
