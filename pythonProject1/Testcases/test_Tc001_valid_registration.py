from Base import Initiatedriver


def test_validregistration():
    driver = Initiatedriver.startbrowser()
    driver.find_element_by_name("fld_username").send_keys()
    driver.close()




