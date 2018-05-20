from tests.Components.Component import Component


class ListOfPhotos(Component):
    PHOTOS_UL = '//ul[contains(class, "ugrid_cnt")]'

    def check_photo_in_album_by_id(self, new_photo_id):
        links = self.driver.find_element_by_xpath(self.PHOTOS_UL).find_elements_by_xpath('/li')
        for link in links:
            current_photo_id = link.find_element_by_xpath('/img').getAttribute('id')
            result_id = current_photo_id.split('_')[1]
            if result_id == new_photo_id:
                return True
        return False
