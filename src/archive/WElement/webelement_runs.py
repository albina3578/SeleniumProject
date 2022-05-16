from src.archive.WElement.webelement_class import initialize_chrome, test_hover_over_action, close_browser

driver = initialize_chrome()
# driver = initialize_firefox()

# 5/12/2022
# webelement_properties(driver)
# webelement_methods(driver)
# test_explicit_wait(driver)

# 5/14/2022
# test_drag_and_drop(driver)
test_hover_over_action(driver)
close_browser(driver)