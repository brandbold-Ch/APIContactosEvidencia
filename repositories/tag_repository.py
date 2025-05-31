from models.models import Tag
from repositories.base_repository import BaseRepository


class TagRepository(BaseRepository):

    def __init__(self):
        super().__init__(Tag)
