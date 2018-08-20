__author__ = "Vivek Ganesan"


from behave import given,then
import logging
from utilizer_selense import utilizer
from feature.po.homepage import HomePage

@given('Get the title of the current page "{Title}"')
def step_impl(context,Title):
    title = str(Title).replace('-','')
    logging.info(" * - Title from feature file - {}".format(title))
    _title = utilizer.get_title()
    assert _title == title,"Doesn't match with the given title"


@then('Check the http response code for the site')
def step_impl(context):
    utilizer.get_http_response(context.url)


@given("Gather all the header link")
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    context.tag_http = {}  #  variable to hold all the TLS header links names and https links
    utilizer.time_elapsed(4)
    for each_webelement in homepage.http_homepage_header_hyperlinks:
        context.tag_http[each_webelement.text] = each_webelement.get_attribute("href")
        utilizer.time_elapsed(2)
    for x in context.tag_http.keys():
        logging.info(x)

@then("Check the http response code for the link")
def step_impl(context):
    logging.info(" * - Total header link - {} ".format(len(list(context.tag_http.keys()))))
    context.headertags = []  #  variable to hold all the TLS header links names
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
    utilizer.click_on_element(homepage.subject_link,"homepage.subject_link")
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
    utilizer.time_elapsed(5)
    total_article_section = homepage.subject_article_sections
    logging.info(" * - TOTAL - {}".format(len(total_article_section)))
    flag = True
    for each_article_section in total_article_section:
        if each_article_section.text == section:
            logging.info(" <.> - Into the section {} page".format(section))
            utilizer.click_on_element(each_article_section,str(each_article_section.text))
            utilizer.time_elapsed(5)
            flag = False
            break
    if flag:
        assert True == False, utilizer.log_it(" Page doesn't have {} section".format(section))


@then("Check all available article http link")
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    total_articlesection_articlelink = homepage.subject_article_section_articlelink
    for link in total_articlesection_articlelink:
        utilizer.get_http_response(link.get_attribute("href"))


@then('Make sure the default article count is not more than "{articlecount}"')
def step_impl(context,articlecount):
    homepage = HomePage(utilizer.active_driver_instance())
    total_articlesection_articlelink = homepage.subject_article_section_articlelink
    logging.info(" * - Total article count before load more operation - {}".format(len(total_articlesection_articlelink)))
    assert int(len(total_articlesection_articlelink)) <= 12 , "Default article should be 12 or less in single article section page"


@then("Check the load more button feature")
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    before_total_articlesection_articlelink = homepage.subject_article_section_articlelink
    logging.info(" * - Total article count before load more operation - {}".format(len(before_total_articlesection_articlelink)))
    utilizer.scroll_to_bottom()
    utilizer.time_elapsed(2)
    logging.info(" * - Clicking on load more button")
    utilizer.click_on_element(homepage.load_more,"homepage.load_more")
    utilizer.time_elapsed(5)
    after_total_articlesection_articlelink = homepage.subject_article_section_articlelink
    logging.info(" * - Total article count after load more operation - {}".format(len(after_total_articlesection_articlelink)))
    assert len(after_total_articlesection_articlelink) >= len(before_total_articlesection_articlelink), utilizer.log_it("Load more feature is not working effectively")


@given("As a user, Click on login")
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.click_on_element(homepage.login_button,"homepage.login_button")
    utilizer.time_elapsed(6)
    login_url = utilizer.get_current_url()
    assert "login" in login_url, utilizer.log_it("login screen is not opened . Try again : Current url :{}".format(login_url))


@given('Enter "{username}" and "{password}" and login in')
def step_impl(context,username,password):
    homepage = HomePage(utilizer.active_driver_instance())
    logging.info(" * - Entering username password")
    utilizer.type_on_element(homepage.login_username,utilizer.ini_reader(context, username.split(".")[1]))
    utilizer.type_on_element(homepage.login_password, utilizer.ini_reader(context, password.split(".")[1]))
    utilizer.scroll_to_bottom()
    utilizer.click_on_element(homepage.subscriber_login,"homepage.subscriber_login")
    utilizer.time_elapsed(5)

@then('Verify the login is success')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.page_element_validator(homepage.logout_button,"homepage.logout_button")
    logging.info(" * - User logged in successfully")


@given('As a user, Click on subcription button')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.click_on_element(homepage.subscribe_button,"homepage.subscribe_button")
    utilizer.time_elapsed(5)


@then('User should be in the "{title}" page')
def step_impl(context,title):
    homepage = HomePage(utilizer.active_driver_instance())
    logging.info(str(title))
    utilizer.verify_text_present(homepage.subscribe_to_times_literary_supplement, str(title))


@then('Try validating log out feature')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.click_on_element(homepage.logout_button,"homepage.logout_button")
    utilizer.page_element_validator(homepage.login_button,"homepage.login_button")


@given('Make sure user not logged in')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.page_element_validator(homepage.login_button,"homepage.login_button")


@then('Open a private article under any category')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.click_on_element(homepage.latest_edition, "homepage.latest_edition")
    utilizer.time_elapsed(5)
    utilizer.verify_text_present(homepage.subscriber_exclusive,"Subscriber Exclusive")
    utilizer.scroll_to_height(800)
    utilizer.time_elapsed(10)
    utilizer.navigate_to("https://www.the-tls.co.uk/article-section/letters/")
    utilizer.time_elapsed(8)
    current_url = utilizer.get_current_url()
    logging.info(current_url)
    assert "letters" in current_url, utilizer.log_it(" Current url is not opened properly it's should be letter's ")
    logging.info(" * - Opening the private article")
    for each in homepage.list_of_article_under_section:
        utilizer.move_to_element_click(each)
        break
    utilizer.time_elapsed(8)


@then('User should able to read the full article')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    for each in homepage.list_of_article_under_section:
        utilizer.move_to_element_click(each)
        break
    utilizer.time_elapsed(8)
    assert utilizer.element_should_not_visible(homepage.to_read_full_article_text) == None, utilizer.log_it("{To_read_full_article_text..} is present in page - Private article")


@then('User should not be able to read full article')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.scroll_to_bottom()
    utilizer.time_elapsed(5)
    utilizer.visibility_of_ele_located(homepage.to_read_full_article_text,"homepage.to_read_full_article_text")


@given('Click on search')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.click_on_element(homepage.search_button,"homepage.search_button")


@then('Enter Mary Beard and perform search')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.type_on_element(homepage.search_button,"MARY BEARD")
    utilizer.perform_enter()
    utilizer.time_elapsed(8)


@then('Search should return related article')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    logging.info(" * - Total search result article : {}".format(utilizer.get_text_webelement(homepage.search_result_count)))
    assert int(utilizer.get_text_webelement(homepage.search_result_count)) > 0,utilizer.log_it("Search result is ZERO. Please check")
    logging.info(" * - Search functionality is working")


@given('Click on latest edition')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.click_on_element(homepage.latest_edition,"homepage.latest_edition")
    utilizer.time_elapsed(4)


@then('Navigate to bottom and validate go to top button')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.scroll_to_bottom()
    Before_clicking_gototop = utilizer.active_driver_instance().execute_script('return window.pageYOffset;')
    utilizer.visibility_of_ele_located(homepage.go_to_top_button,"homepage.go_to_top_button")
    utilizer.click_on_element(homepage.go_to_top_button,"homepage.go_to_top_button")
    utilizer.time_elapsed(6)
    After_clicking_gototop = utilizer.active_driver_instance().execute_script('return window.pageYOffset;')
    logging.info("Before_gototop :{}, After_gototop: {}".format(Before_clicking_gototop,After_clicking_gototop))
    assert After_clicking_gototop == 0 ,utilizer.log_it("GO TO TOP might not be worked as expected. "
                                                        "Before_gototop:{} After_gototop:{}".format(Before_clicking_gototop,After_clicking_gototop))


@given('Open subjects page')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.click_on_element(homepage.subject_link,"homepage.subject_link")
    utilizer.time_elapsed(8)


@then('Open any section')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.move_to_element_click(homepage.return_single_section())
    utilizer.time_elapsed(8)


@then('Open any article inside the section')
def step_impl(context):
    homepage = HomePage(utilizer.active_driver_instance())
    utilizer.move_to_element_click(homepage.return_single_article_under_subjects())
    utilizer.time_elapsed(8)