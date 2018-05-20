import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from tests.Components.AlbumPageComponents.AlbumActionPanel import AlbumActionPanel
from tests.Components.AlbumPageComponents.AlbumMainTopContentBar import AlbumMainTopContentBar
from tests.Pages.AlbumPage import AlbumPage
from tests.Pages.PhotoSectionPage import PhotoSectionPage
from tests.Pages.UploadedPhotoEditorPage import UploadedPhotoEditorPage
from tests.TestsMethods.CommonMethods import CommonMethods
from tests.Utils import Constants


class AddImageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = os.environ.get('BROWSER', 'CHROME')

        cls.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        cls.common_methods = CommonMethods(cls.driver)

    def setUp(self):
        self.common_methods.authorize()
        self.common_methods.redirect_to_photo_section_from_feed_page()

    def tearDown(self):
        self.common_methods.quit_profile_from_any_page()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def upload_image(self, name):

        photo_section_page = PhotoSectionPage(self.driver)
        add_photo_button = photo_section_page.add_photo_button
        add_photo_button.upload_file(name)

    def get_image_id_on_uploaded_photo_editor_page(self):
        uploaded_photo_editor_page = UploadedPhotoEditorPage(self.driver)
        uploaded_image_card = uploaded_photo_editor_page.uploaded_image_card
        return uploaded_image_card.get_uploaded_photo_id()

    def test_addSimpleImageTest(self):
        self.upload_image(Constants.TEST_IMAGE_NAME)

        add_photo_button = PhotoSectionPage(self.driver).add_photo_button
        self.assertTrue(add_photo_button.check_upload_start_successfully())

        uploaded_image_id = self.get_image_id_on_uploaded_photo_editor_page()

        #TODO:change to common page
        album_page = AlbumPage(self.driver)
        album_page.main_top_content_bar.redirect_to_foto_section()

        photo_section_page = PhotoSectionPage(self.driver)
        photo_albums_list_bar = photo_section_page.photo_albums_list_bar
        photo_albums_list_bar.open_album_with_name(Constants.DEFAULT_ALBUM_NAME)

        self.assertTrue(album_page.list_of_photos.check_photo_in_album_by_id(uploaded_image_id))
