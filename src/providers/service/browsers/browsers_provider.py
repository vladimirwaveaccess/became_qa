from src.providers.service.browsers.browsers_library.chrome_browser import ChromeBrowser
from src.providers.service.browsers.browsers_library.ff_browser import FFBrowser
from src.providers.service.browsers.browsers_library.ie_browser import IEBrowser


class BrowsersProvider:

    BROWSER_MAPPER = {
        'chrome': ChromeBrowser,
        'ff': FFBrowser,
        'ie': IEBrowser
    }

    def get_driver(browser_name):
        """
        browser_name -> 'chrome, ff, edge'
        """

        browser = BrowsersProvider.BROWSER_MAPPER.get(browser_name)
        if browser is None:
            raise NotImplementedError(f"Browser name {browser_name} is not supported for UI tests. Please register it in BrowsersProvider class")

        driver = browser.get_driver()
        return driver

