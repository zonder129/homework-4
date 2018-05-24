import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from tests.Pages.AlbumPage import AlbumPage
from tests.Pages.EditAlbumPage import EditAlbumPage
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

    def delete_photo_from_album_by_id(self, photo_id):
        album_page = AlbumPage(self.driver)
        action_panel = album_page.action_panel
        action_panel.edit_album()

        edit_album_page = EditAlbumPage(self.driver)
        list_of_photos = edit_album_page.list_of_photos
        list_of_photos.delete_photo_by_id(photo_id)

    def redirect_to_album_page_from_photo_section_page(self, album_name):
        photo_section_page = PhotoSectionPage(self.driver)
        photo_albums_list_bar = photo_section_page.photo_albums_list_bar
        photo_albums_list_bar.open_album_with_name(album_name)

    def wait_until_photo_downloaded(self):
        uploaded_photo_editor_page = UploadedPhotoEditorPage(self.driver)
        above_photo_panel = uploaded_photo_editor_page.above_photo_panel
        above_photo_panel.wait_until_photo_will_be_downloaded()

    def restore_photo_after_delete(self):
        edit_album_page = EditAlbumPage(self.driver)
        list_of_photos = edit_album_page.list_of_photos
        list_of_photos.restore_last_deleted_photo()

    def wait_until_photo_deleted(self):
        edit_album_page = EditAlbumPage(self.driver)
        list_of_photos = edit_album_page.list_of_photos
        list_of_photos.wait_until_photo_deleted()

    def redirect_from_edit_page_to_album_page(self):
        edit_album_page = EditAlbumPage(self.driver)
        list_of_photos = edit_album_page.list_of_photos
        list_of_photos.redirect_back_to_album_page()

    # READY
    def test_image_add_in_default_album(self):
        self.upload_image(Constants.TEST_IMAGE_NAME)

        add_photo_button = PhotoSectionPage(self.driver).add_photo_button
        self.assertTrue(add_photo_button.check_upload_start_successfully())

        self.wait_until_photo_downloaded()

        uploaded_image_id = self.get_image_id_on_uploaded_photo_editor_page()

        self.common_methods.redirect_to_photo_section_with_main_top_content_bar()

        self.redirect_to_album_page_from_photo_section_page(Constants.DEFAULT_ALBUM_NAME)

        album_page = AlbumPage(self.driver)
        self.assertTrue(album_page.list_of_photos.check_photo_in_album_by_id(uploaded_image_id))

        self.delete_photo_from_album_by_id(uploaded_image_id)

    # READY
    def test_restore_image_after_delete(self):
        self.upload_image(Constants.TEST_IMAGE_NAME)

        self.wait_until_photo_downloaded()

        uploaded_image_id = self.get_image_id_on_uploaded_photo_editor_page()

        self.common_methods.redirect_to_photo_section_with_main_top_content_bar()

        self.redirect_to_album_page_from_photo_section_page(Constants.DEFAULT_ALBUM_NAME)

        self.delete_photo_from_album_by_id(uploaded_image_id)

        self.wait_until_photo_deleted()

        self.restore_photo_after_delete()

        self.redirect_from_edit_page_to_album_page()

        album_page = AlbumPage(self.driver)
        self.assertTrue(album_page.list_of_photos.check_photo_in_album_by_id(uploaded_image_id))







