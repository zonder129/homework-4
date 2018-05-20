from tests.Components.AlbumPageComponents.AlbumActionPanel import AlbumActionPanel
from tests.Components.AlbumPageComponents.AlbumMainTopContentBar import AlbumMainTopContentBar
from tests.Components.AlbumPageComponents.ListOfPhotos import ListOfPhotos
from tests.Pages.Page import Page


class AlbumPage(Page):
    PATH = ''

    @property
    def main_top_content_bar(self):
        return AlbumMainTopContentBar(self.driver)

    @property
    def action_panel(self):
        return AlbumActionPanel(self.driver)

    @property
    def list_of_photos(self):
        return ListOfPhotos(self.driver)