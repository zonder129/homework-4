from tests.Components.EditAlbumPageComponents.DeleteAlbumPopUp import DeleteAlbumPopUp
from tests.Components.EditAlbumPageComponents.EditAlbumActionPanel import EditAlbumActionPanel
from tests.Pages.Page import Page


class EditAlbumPage(Page):
    PATH = ''

    @property
    def action_panel(self):
        return EditAlbumActionPanel(self.driver)

    @property
    def delete_album_popup(self):
        return DeleteAlbumPopUp(self.driver)