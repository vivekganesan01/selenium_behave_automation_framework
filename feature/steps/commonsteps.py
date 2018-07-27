__author__ = "Vivek Ganesan"


from behave import given,then
import logging
from utilizer_selense import utilizer
from feature.po.homepage import HomePage


@given('Get the title of the current page "{Title}"')
def step_impl(context,Title):
    Title = str(Title).replace('-','')
    logging.info(" * - Title from feature file - {}".format(Title))
    TITLE = utilizer.get_title()
    assert TITLE == Title,"Doesn't match with the given title"


@then('Check the http response code for the site')
def step_impl(context):
    utilizer.get_http_response(context.url)


@given("Gather all the header link")
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    context.tag_http = {}
    for each_webelement in homepage.http_homepage_header_hyperlinks:
        context.tag_http[each_webelement.text] = each_webelement.get_attribute("href")


@then("Check the http response code for the link")
def step_impl(context):
    logging.info(" * - Total header link - {} ".format(len(list(context.tag_http.keys()))))
    context.headertags = []
    for tags in context.tag_http:
        context.headertags.append(tags)
    for http in context.headertags:
        logging.info(" * - {}".format(http))
        utilizer.get_http_response(context.tag_http[http])
        logging.info("")

@given("Navigate to subject category")
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    logging.info(" * - Checking subject category")
    utilizer.click_on_element(homepage.subject_link)
    utilizer.time_elapsed(6)

@then("Gather all the article-section header and check the status code")
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    total_article_section = homepage.subject_article_sections
    logging.info(" * - Total article section available - {} \n".format(len(total_article_section)))
    for each_article_section in total_article_section:
        tag = each_article_section.text
        http = each_article_section.get_attribute("href")
        logging.info( " * - {}".format(tag) )
        utilizer.get_http_response(http)

@then('Go to the "{section}" article section')
def step_impl(context,section):
    homepage = HomePage(utilizer.active_driver_instance())
    total_article_section = homepage.subject_article_sections
    for each_article_section in total_article_section:
        if each_article_section.text == section:
            logging.info(" <.> - Into the section {} page".format(section))
            utilizer.click_on_element(each_article_section)
            utilizer.time_elapsed(5)
        else:
            assert True == False, "Given section {} doesnt available in the TLS"

@then("Check all available article http link")
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    total_articlesection_articlelink = homepage.subject_article_section_articlelink
    for link in total_articlesection_articlelink:
        utilizer.get_http_response(link.get_attribute("href"))


@then('Make sure the default article count is not more than "{articlecount}"')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    total_articlesection_articlelink = homepage.subject_article_section_articlelink
    logging.info(" * - Total article count before load more operation - {}".format(len(total_articlesection_articlelink)))
    assert int(len(total_articlesection_articlelink)) >= 13 , "Default article should be 12 or less in single article section page"

@then("Check the load more button feature")
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    before_total_articlesection_articlelink = homepage.subject_article_section_articlelink
    logging.info(" * - Total article count before load more operation - {}".format(len(before_total_articlesection_articlelink)))
    logging.info(" * - Clicking on load more button")
    utilizer.click_on_element(homepage.load_more)
    utilizer.time_elapsed(7)
    after_total_articlesection_articlelink = homepage.subject_article_section_articlelink
    logging.info(" * - Total article count after load more operation - {}".format(len(after_total_articlesection_articlelink)))
    assert before_total_articlesection_articlelink <= after_total_articlesection_articlelink," Load more feature is not working effectively"

@given("As a user, Click on login")
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.click_on_element(homepage.login_button)
    utilizer.time_elapsed(6)
    login_url = utilizer.get_current_url()
    assert "login" not in login_url, "login screen is not opened . Try again"

@given('Enter "{username}" and "{password}" and login in')
def step_impl(context,username,password):
    homepage = HomePage(utilizer.active_driver_instance())
    logging.info(" * - Entering username password")
    utilizer.type_on_element(homepage.login_username,utilizer.ini_reader(context, username.split(".")[1]))
    utilizer.type_on_element(homepage.login_password, utilizer.ini_reader(context, password.split(".")[1]))
    utilizer.click_on_element(homepage.login_button)
    utilizer.time_elapsed(5)

@then("User should see the logged in screen")
def step_impl():
    logging.info(" * - Verifying after login")

