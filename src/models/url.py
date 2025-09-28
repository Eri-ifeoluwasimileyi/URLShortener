from datetime import datetime
from typing import Optional

from pydantic import BaseModel, AnyUrl


class ShortenedURLRequest(BaseModel):
    user_id: str
    long_url: AnyUrl
    expires_in: Optional[datetime] = None


class ShortenedUrlInfo(BaseModel):
    user_id: str
    short_url: str
    long_url: str
    clicks_count: int = 0
    created_at: datetime = datetime.now()
    expires_in: Optional[datetime] = None
    last_accessed: datetime|str = 'Not used'