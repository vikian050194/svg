from datetime import datetime

from .abstract_time_manager import AbstractTimeManager


class TimeManager(AbstractTimeManager):
    def __init__(self, tz_name: str = None, tz_offset: int = None):
        self.timezone = None
        # self.timezone = datetime.now().astimezone().tzinfo
        # if tz_name and tz_offset:
        #     self.timezone = timezone(name=tz_name, offset=timedelta(seconds=tz_offset))

    def get_datetime(self) -> datetime:
        return datetime.now(tz=self.timezone).replace(microsecond=0)


__all__ = ["TimeManager"]
