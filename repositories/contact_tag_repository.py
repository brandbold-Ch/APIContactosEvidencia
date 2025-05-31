from models.models import ContactTag
from repositories.base_repository import BaseRepository


class ContactTagRepository(BaseRepository):

    def __init__(self):
        super().__init__(ContactTag)
