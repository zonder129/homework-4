from tests.Components.Component import Component


class UploadedImageCard(Component):
    PHOTO_ID_DIV = '//div[@data-module="PhotoEdit"]'

    def get_uploaded_photo_id(self):
        element = self.driver.find_element_by_xpath(self.PHOTO_ID_DIV)
        return element.getAttribute('data-id')
