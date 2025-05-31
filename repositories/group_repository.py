from models.models import Group
from repositories.base_repository import BaseRepository


class GroupRepository(BaseRepository):

    def __init__(self):
        super().__init__(Group)
