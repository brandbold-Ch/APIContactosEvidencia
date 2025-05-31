from models.models import ContactGroup
from repositories.base_repository import BaseRepository


class ContactGroupRepository(BaseRepository):

    def __init__(self):
        super().__init__(ContactGroup)
