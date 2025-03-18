import pytest
from selenium import webdriver
from tests.pages.page_tags import TestTagsInputBoxPage


class TestTagsInputBox:
    def test_should_add_a_tag_successfully(self):
        driver = webdriver.Chrome()
        driver.get('https://qaplayground.dev/apps/tags-input-box/')
        tagsinput = TestTagsInputBoxPage(driver)
        tagsinput.add_tags_in_container()

    def test_should_remove_a_tag_successfully(self):
        driver = webdriver.Chrome()
        driver.get('https://qaplayground.dev/apps/tags-input-box/')
        delete_a_tag = TestTagsInputBoxPage(driver)
        delete_a_tag.remove_a_tag_in_container()

    def test_should_remove_all_tag_successfully(self):
        driver = webdriver.Chrome()
        driver.get('https://qaplayground.dev/apps/tags-input-box/')
        delete_all_tags = TestTagsInputBoxPage(driver)
        delete_all_tags.delete_all_tags_in_container()
        conteniner_tags = delete_all_tags.message.text
        assert conteniner_tags == '10'


if __name__ == "__main__":
    pytest.main()
