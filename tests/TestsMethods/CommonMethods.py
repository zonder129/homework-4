from tests.Pages.AuthPage import AuthPage
from tests.Pages.CommonPage import CommonPage
from tests.Pages.FeedPage import FeedPage
from tests.Utils import Constants


class CommonMethods:

    def __init__(self, driver):
        self.driver = driver

    def authorize(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_login(Constants.USERNAME)
        auth_form.set_password(Constants.PASSWORD)
        auth_form.submit()

    def redirect_to_photo_section_from_feed_page(self):
        feed_page = FeedPage(self.driver)

        feed_left_bar = feed_page.left_bar
        feed_left_bar.click_on_link_to_photo_section()

    def quit_profile_from_any_page(self):
        common_page = CommonPage(self.driver)

        navigation_toolbar = common_page.navigation_toolbar
        navigation_toolbar.open_profile_menu()
        navigation_toolbar.try_quit_profile()

        quit_popup = common_page.quit_popup
        quit_popup.definitely_quit_profile()