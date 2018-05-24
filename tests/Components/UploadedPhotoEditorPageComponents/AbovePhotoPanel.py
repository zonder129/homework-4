from selenium.webdriver.support.wait import WebDriverWait

from tests.Components.Component import Component


class AbovePhotoPanel(Component):
    CONFIRM_PHOTO_UPLOADED = '//li[@id="uploadingCompleteMsg"]'

    def wait_until_photo_will_be_downloaded(self):
        WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_xpath(self.CONFIRM_PHOTO_UPLOADED)
        )