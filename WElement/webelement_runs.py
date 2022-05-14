from WElement.webelement_class import *

driver = initialize_driver()
# #webelement_properties(driver)
# webelement_methods(driver)
# test_explicit_wait(driver)


# 5/14/22:
test_drag_and_drop(driver)
test_hover_over_action()

close_browser(driver)
