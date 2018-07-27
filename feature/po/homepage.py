__author__ = "Vivek Ganesan"


from page_objects import PageObject, MultiPageElement, PageElement


class HomePage(PageObject):

    http_homepage_header_hyperlinks = MultiPageElement(xpath="//div[@class='menu-header-menu-container']//li/a")
    subject_link = PageElement(xpath="//div[@class='menu-header-menu-container']//li/a[contains(text(),'Subjects')]")
    subject_article_sections = MultiPageElement(xpath="//a[@ng-if='data.section.name']")
    subject_article_section_articlelink = MultiPageElement(xpath="//a[@ng-if='data.link']")
    load_more = MultiPageElement(xpath="//button[@class='clear centre ng-scope']")
    login_button = PageElement(xpath="//button[@class='button clear login']")
    login_username = PageElement(id_='username')
    login_password  = PageElement(id_='password')
    logout_button  = PageElement(xpath="//button[contains(text(),'Logout')]")