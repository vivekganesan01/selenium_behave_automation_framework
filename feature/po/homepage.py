__author__ = "Vivek Ganesan"

from page_objects import PageObject, MultiPageElement, PageElement


class HomePage(PageObject):

    http_homepage_header_hyperlinks = MultiPageElement(xpath = "//div[@class='menu-header-menu-container']//li/a")
    subject_link = PageElement(xpath = "//div[@class='menu-header-menu-container']//li/a[contains(text(),'Subjects')]")
    subject_article_sections = MultiPageElement(xpath = "//a[@ng-if='data.section.name']")
    subject_article_section_articlelink = MultiPageElement(xpath = "//a[@ng-if='data.link']")
    load_more = PageElement(xpath = "//button[@class='clear centre ng-scope']")
    login_button = PageElement(xpath = "//button[@class='button clear login']")
    login_username = PageElement(id_ = 'username')
    login_password  = PageElement(id_ = 'password')
    logout_button  = PageElement(xpath = "//button[contains(text(),'Logout')]")
    subscribe_button = PageElement(xpath = "//button[@class='button subscribe']")
    latest_edition = PageElement(xpath = "//a[contains(text(),'Latest Edition')]")
    subscriber_exclusive = PageElement(xpath = "//h2[text()='Subscriber Exclusive']")
    arts = PageElement(xpath = "//a[text()='Arts']")
    list_of_article_under_section = MultiPageElement(xpath = "//div[@tls-scroll='scrollState']//div[@class='padded']//a")
    to_read_full_article_text = PageElement(xpath = "//div[@class='form-subtitle futura' and contains(text(),'To read')]")
    search_button = PageElement(xpath = "//input[@type='search']")
    search_result_count = PageElement(xpath = "//span[@ng-bind='results.count_total']")
    subscriber_login = PageElement(xpath = "//input[@type='submit' and @value='Login']")
    subscribe_to_times_literary_supplement = PageElement(xpath = "// h2[text() = 'Subscribe to The Times Literary Supplement']")
    list_of_editor_section = MultiPageElement(xpath = "//div[@class='editions-bottom fadeIn ng-scope']//h3[@class='futura']")
    go_to_top_button = PageElement(xpath = "//a[@id='return-to-top']")


    def return_single_article(self):
        return self.list_of_article_under_section[1]


    def return_single_editor_section(self):
        return self.list_of_editor_section[0]


    def return_single_section(self):
        return self.subject_article_sections[0]


    def return_single_article_under_subjects(self):
        return self.subject_article_section_articlelink[0]