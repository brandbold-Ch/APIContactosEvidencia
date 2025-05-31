from models.models import Contact
from repositories.base_repository import BaseRepository


class ContactRepository(BaseRepository):

    def __init__(self):
        super().__init__(Contact)
