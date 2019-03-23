from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class WebSearcher():

    def search_on_page_Chrome(self, portaladress, searchboxname, searchtext):
        driver = webdriver.Chrome()
        driver.get(portaladress)
        search_in_searchbox = driver.find_element_by_name(searchboxname)
        search_in_searchbox.clear()
        search_in_searchbox.send_keys(searchtext)
        search_in_searchbox.send_keys(Keys.RETURN)
    def