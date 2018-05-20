from tests.Components.CommonComponents.NavigationToolBar import NavigationToolBar
from tests.Components.CommonComponents.QuitPopUp import QuitPopUp
from tests.Pages.Page import Page


class CommonPage(Page):
    PATH = ''

    @property
    def navigation_toolbar(self):
        return NavigationToolBar(self.driver)

    @property
    def quit_popup(self):
        return QuitPopUp(self.driver)
