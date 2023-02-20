import re
import typing
from datetime import timedelta
from enum import Enum
from itertools import count
from typing import Any, List, Optional, Union

from Browser import Browser
from Browser.assertion_engine import AssertionOperator as AO
from Browser.utils.data_types import *
from robot.api.deco import keyword, library
from robot.libraries.BuiltIn import BuiltIn
from robot.utils import DotDict

EQUALS = AO["=="]
NOT_EQUALS = AO["!="]
CONTAINS = AO["*="]
NOT_CONTAINS = AO["not contains"]
STARTS_WITH = AO["^="]
ENDS_WITH = AO["$="]
THEN = AO["then"]


class WebElement(str):
    # self._key_attrs = {
    #         None: ["@id", "@name"],
    #         "a": [
    #             "@id",
    #             "@name",
    #             "@href",
    #             "normalize-space(descendant-or-self::text())",
    #         ],
    #         "img": ["@id", "@name", "@src", "@alt"],
    #         "input": ["@id", "@name", "@value", "@src"],
    #         "button": [
    #             "@id",
    #             "@name",
    #             "@value",
    #             "normalize-space(descendant-or-self::text())",
    #         ],
    #     }

    # def _get_tag_and_constraints(self, tag):
    #     if tag is None:
    #         return None, {}
    #     tag = tag.lower()
    #     constraints = {}
    #     if tag == "link":
    #         tag = "a"
    #     if tag == "partial link":
    #         tag = "a"
    #     elif tag == "image":
    #         tag = "img"
    #     elif tag == "list":
    #         tag = "select"
    #     elif tag == "radio button":
    #         tag = "input"
    #         constraints["type"] = "radio"
    #     elif tag == "checkbox":
    #         tag = "input"
    #         constraints["type"] = "checkbox"
    #     elif tag == "text field":
    #         tag = "input"
    #         constraints["type"] = [
    #             "date",
    #             "datetime-local",
    #             "email",
    #             "month",
    #             "number",
    #             "password",
    #             "search",
    #             "tel",
    #             "text",
    #             "time",
    #             "url",
    #             "week",
    #             "file",
    #         ]
    #     elif tag == "file upload":
    #         tag = "input"
    #         constraints["type"] = "file"
    #     elif tag == "text area":
    #         tag = "textarea"
    #     return tag, constraints

    LOCATORS = {
        "id": "id={loc}",
        "name": "css=[name={loc}]",
        "identifier": "css=[id={loc}], [name={loc}]",
        "class": "css=.{loc}",
        "tag": "css={loc}",
        "xpath": "xpath={loc}",
        "css": "css={loc}",
        "link": 'css=a >> text="{loc}"',
        "partial link": "css=a >> text={loc}",
        "default": "[id={loc}], [name={loc}]",
        "text": "text={loc}",
    }

    @classmethod
    def from_string(cls, locator: str) -> "WebElement":
        for strategy, selector in cls.LOCATORS.items():
            match = re.match(f"{strategy} ?[:=] ?", locator)
            if match:
                loc = locator[match.end() :]
                return cls(selector.format(loc=loc))
        if locator.startswith("/"):
            return cls(f"xpath={locator}")
        return cls("[id={loc}], [name={loc}]".format(loc=locator))

    @staticmethod
    def is_default(locator: str) -> bool:
        m = re.fullmatch("\[id=(.*)], \[name=(.*)]", locator)
        if m and m.group(1) == m.group(2):
            return m.group(1)
        return None


BROWSERS = {
    "firefox": (SupportedBrowsers.firefox, False),
    "ff": (SupportedBrowsers.firefox, False),
    "headlessfirefox": (SupportedBrowsers.firefox, True),
    "chromium": (SupportedBrowsers.chromium, False),
    "chrome": (SupportedBrowsers.chromium, False),
    "googlechrome": (SupportedBrowsers.chromium, False),
    "headlesschrome": (SupportedBrowsers.chromium, True),
    "gc": (SupportedBrowsers.chromium, False),
    "edge": (SupportedBrowsers.chromium, False),
    "webkit": (SupportedBrowsers.webkit, False),
    "safari": (SupportedBrowsers.webkit, False),
}


@library(converters={WebElement: WebElement.from_string})
class SeleniumLibraryToBrowser:
    def __init__(
        self,
        timeout=timedelta(seconds=5.0),
        implicit_wait=timedelta(seconds=0.0),
        run_on_failure="Capture Page Screenshot",
        screenshot_root_directory: Optional[str] = None,
        plugins: Optional[str] = None,
        event_firing_webdriver: Optional[str] = None,
        browser_args: Optional[List[str]] = None,
    ):
        self.timeout = timeout
        self.implicit_wait = implicit_wait
        self.run_on_failure = run_on_failure
        self.screenshot_root_directory = screenshot_root_directory
        self.plugins = plugins
        self.event_firing_webdriver = event_firing_webdriver
        self._browser: Optional[Browser] = None
        self._browser_args = browser_args or []
        self._browser_indexes = {}
        self._browser_aliases = {}
        self._browser_index = count()

    @property
    def b(self) -> Browser:
        if self._browser is None:
            BuiltIn().import_library(name="Browser", *self._browser_args)
            self._browser = BuiltIn().get_library_instance("Browser")
            self._browser.set_strict_mode(False, Scope.Global)
            BuiltIn().set_library_search_order("SeleniumLibraryToBrowser")
        return self._browser

    @keyword
    def add_cookie(
        self,
        name: str,
        value: str,
        path: Optional[str] = None,
        domain: Optional[str] = None,
        secure: Optional[bool] = None,
        expiry: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def add_location_strategy(
        self, strategy_name: str, strategy_keyword: str, persist: bool = False
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def alert_should_be_present(
        self,
        text: str = "",
        action: str = "ACCEPT",
        timeout: Optional[timedelta] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def alert_should_not_be_present(
        self, action: str = "ACCEPT", timeout: Optional[timedelta] = None
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def assign_id_to_element(self, locator: WebElement, id: str):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword(tags=("IMPLEMENTED",))
    def capture_element_screenshot(
        self,
        locator: Union[WebElement, None, str],
        filename: str = "selenium-element-screenshot-{index}.png",
    ):
        self.b.take_screenshot(filename=re.sub(".png$", "", filename), selector=locator)

    @keyword(tags=("IMPLEMENTED",))
    def capture_page_screenshot(self, filename: str = "selenium-screenshot-{index}.png"):
        self.b.take_screenshot(filename=re.sub(".png$", "", filename))

    @keyword(tags=("IMPLEMENTED",))
    def checkbox_should_be_selected(self, locator: WebElement):
        self.b.get_checkbox_state(locator, EQUALS, True)

    @keyword(tags=("IMPLEMENTED",))
    def checkbox_should_not_be_selected(self, locator: WebElement):
        self.b.get_checkbox_state(locator, EQUALS, False)

    @keyword(tags=("IMPLEMENTED",))
    def choose_file(self, locator: WebElement, file_path: str):
        self.b.upload_file_by_selector(locator, file_path)

    @keyword(tags=("IMPLEMENTED",))
    def clear_element_text(self, locator: WebElement):
        self.b.clear_text(locator)

    @keyword(tags=("IMPLEMENTED",))
    def click_button(self, locator: WebElement, modifier: Union[bool, str] = False):
        if modifier:
            raise NotImplementedError("Modifier is not implemented")
        loc = WebElement.is_default(locator)
        if loc:
            locator = (
                "css="
                f'button[id="{loc}"],'
                f'button[name="{loc}"],'
                f'button[value="{loc}"],'
                f'input[id="{loc}"],'
                f'input[name="{loc}"],'
                f'input[value="{loc}"]'
            )
        self.b.click(selector=locator)

    @keyword(tags=("IMPLEMENTED",))
    def click_element(
        self,
        locator: WebElement,
        modifier: Union[bool, str] = False,
        action_chain: bool = False,
    ):
        if modifier:
            raise NotImplementedError("Modifier is not implemented")
        self.b.click(selector=locator)

    @keyword(tags=("IMPLEMENTED",))
    def click_element_at_coordinates(self, locator: WebElement, xoffset: int, yoffset: int):
        bbox = self.b.get_boundingbox(selector)  # {x, y, width, height}
        # calculates the half of the width and height of the element
        x = bbox["width"] / 2 + xoffset
        y = bbox["height"] / 2 + yoffset
        self.b.click(selector=locator, position_x=x, position_y=y)

    @keyword(tags=("IMPLEMENTED",))
    def click_image(self, locator: WebElement, modifier: Union[bool, str] = False):
        """See the Locating elements section for details about the locator syntax.
        When using the default locator strategy, images are searched using id, name, src and alt.
        """
        if modifier:
            raise NotImplementedError("Modifier is not implemented")
        loc = WebElement.is_default(locator)
        if loc:
            locator = (
                f'xpath=//img[@id="{loc}"] | '
                f'//img[@name="{loc}"] | '
                f'//img[@src="{loc}"] | '
                f'//img[@alt="{loc}"]'
            )
        self.b.click(selector=locator)

    @keyword(tags=("IMPLEMENTED",))
    def click_link(self, locator: WebElement, modifier: Union[bool, str] = False):
        """See the Locating elements section for details about the locator syntax.
        When using the default locator strategy, links are searched using id, name, href and the link text.
        """
        if modifier:
            raise NotImplementedError("Modifier is not implemented")
        loc = WebElement.is_default(locator)
        if loc:
            locator = (
                f'xpath=//a[@id="{loc}"] | '
                f'//a[@name="{loc}"] | '
                f'//a[@href="{loc}"] | '
                f'//a[normalize-space(descendant-or-self::text())="{loc}"]'
            )
        self.b.click(selector=locator)

    @keyword(tags=("IMPLEMENTED",))
    def close_all_browsers(self):
        self.b.close_browser(SelectionType.ALL)
        self._browser_aliases = {}
        self._browser_indexes = {}

    @keyword(tags=("IMPLEMENTED",))
    def close_browser(self):
        current_id = self.b.get_browser_ids(SelectionType.ACTIVE)
        for index, id in self._browser_indexes.items():
            if id == current_id:
                self._browser_indexes.pop(index)
                for alias, idx in self._browser_aliases.items():
                    if idx == index:
                        self._browser_aliases.pop(alias)
                        break
                break
        self.b.close_browser(SelectionType.CURRENT)

    @keyword(tags=("IMPLEMENTED",))
    def close_window(self):
        self.b.close_page(SelectionType.CURRENT)

    @keyword
    def cover_element(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def create_webdriver(
        self, driver_name: str, alias: Optional[str] = None, kwargs={}, **init_kwargs
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def current_frame_should_contain(self, text: str, loglevel: str = "TRACE"):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def current_frame_should_not_contain(self, text: str, loglevel: str = "TRACE"):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword(tags=("IMPLEMENTED",))
    def delete_all_cookies(self):
        self.b.delete_all_cookies()

    @keyword
    def delete_cookie(self, name):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword(tags=("IMPLEMENTED",))
    def double_click_element(self, locator: WebElement):
        self.b.click(locator, clickCount=2, delay=timedelta(milliseconds=100))

    @keyword(tags=("IMPLEMENTED",))
    def drag_and_drop(self, locator: WebElement, target: WebElement):
        self.b.drag_and_drop(locator, target, steps=10)

    @keyword(tags=("IMPLEMENTED",))
    def drag_and_drop_by_offset(self, locator: WebElement, xoffset: int, yoffset: int):
        self.b.drag_and_drop_relative_to(locator, xoffset, yoffset, steps=10)

    @keyword(tags=("IMPLEMENTED",))
    def element_attribute_value_should_be(
        self,
        locator: WebElement,
        attribute: str,
        expected: Optional[str],
        message: Optional[str] = None,
    ):
        self.b.get_attribute(locator, attribute, EQUALS, expected, message)

    @keyword(tags=("IMPLEMENTED",))
    def element_should_be_disabled(self, locator: WebElement):
        self.b.get_element_states(locator, CONTAINS, "disabled")

    @keyword(tags=("IMPLEMENTED",))
    def element_should_be_enabled(self, locator: WebElement):
        self.b.get_element_states(locator, CONTAINS, "enabled")

    @keyword(tags=("IMPLEMENTED",))
    def element_should_be_focused(self, locator: WebElement):
        self.b.get_element_states(locator, CONTAINS, "focused")

    @keyword(tags=("IMPLEMENTED",))
    def element_should_be_visible(self, locator: WebElement, message: Optional[str] = None):
        self.b.get_element_states(locator, CONTAINS, "visible", message=message)

    @keyword(tags=("IMPLEMENTED",))
    def element_should_contain(
        self,
        locator: WebElement,
        expected: Optional[str],
        message: Optional[str] = None,
        ignore_case: bool = False,
    ):
        if ignore_case:
            self.b.get_text(locator, THEN, f"'''{expected}'''.lower() in value.lower()", message)
        else:
            self.b.get_text(locator, CONTAINS, expected, message)

    @keyword(tags=("IMPLEMENTED",))
    def element_should_not_be_visible(self, locator: WebElement, message: Optional[str] = None):
        self.b.get_element_states(locator, NOT_CONTAINS, "visible", message=message)

    @keyword(tags=("IMPLEMENTED",))
    def element_should_not_contain(
        self,
        locator: WebElement,
        expected: Optional[str],
        message: Optional[str] = None,
        ignore_case: bool = False,
    ):
        self.b.get_text(locator, NOT_CONTAINS, expected, message)

    @keyword(tags=("IMPLEMENTED",))
    def element_text_should_be(
        self,
        locator: WebElement,
        expected: Optional[str],
        message: Optional[str] = None,
        ignore_case: bool = False,
    ):
        self.b.get_text(locator, EQUALS, expected, message)

    @keyword(tags=("IMPLEMENTED",))
    def element_text_should_not_be(
        self,
        locator: WebElement,
        not_expected: Optional[str],
        message: Optional[str] = None,
        ignore_case: bool = False,
    ):
        if ignore_case:
            self.b.get_text(
                locator, THEN, f"'''{not_expected}'''.lower() not in value.lower()", message
            )
        else:
            self.b.get_text(locator, NOT_EQUALS, not_expected, message)

    @keyword
    def execute_async_javascript(self, *code: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def execute_javascript(self, *code: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def frame_should_contain(self, locator: WebElement, text: str, loglevel: str = "TRACE"):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword(tags=("IMPLEMENTED",))
    def get_all_links(self):
        return [
            self.b.get_attribute(element, "id")
            if "id" in self.b.get_attribute_names(element)
            else ""
            for element in self.b.get_elements(selector="css=a")
        ]

    @keyword(tags=("IMPLEMENTED",))
    def get_browser_aliases(self):
        return DotDict(self._browser_aliases)

    @keyword(tags=("IMPLEMENTED",))
    def get_browser_ids(self):
        return list(self._browser_indexes.keys())

    @keyword(tags=("IMPLEMENTED",))
    def get_cookie(self, name: str):
        return DotDict(self.b.get_cookie(name, CookieType.dict))

    @keyword(tags=("IMPLEMENTED",))
    def get_cookies(self, as_dict: bool = False):
        if as_dict:
            return DotDict(self.b.get_cookies(CookieType.dictionary))
        return self.b.get_cookies(CookieType.str)

    @keyword(tags=("IMPLEMENTED",))
    def get_element_attribute(self, locator: WebElement, attribute: str):
        return self.b.get_attribute(locator, attribute)

    @keyword(tags=("IMPLEMENTED",))
    def get_element_count(self, locator: WebElement):
        return self.b.get_element_count(locator)

    @keyword(tags=("IMPLEMENTED",))
    def get_element_size(self, locator: WebElement):
        value = self.b.get_boundingbox(locator, BoundingBoxFields.ALL)
        return value["width"], value["height"]

    @keyword(tags=("IMPLEMENTED",))
    def get_horizontal_position(self, locator: WebElement):
        return self.b.get_boundingbox(locator, BoundingBoxFields.x)

    @keyword(tags=("IMPLEMENTED",))
    def get_list_items(self, locator: WebElement, values: bool = False):
        options = self.b.get_select_options(locator)
        if values:
            return [option["value"] for option in options]
        return [option["label"] for option in options]

    @keyword(tags=("IMPLEMENTED",))
    def get_location(self):
        return self.b.get_url()

    @keyword(tags=("IMPLEMENTED",))
    def get_locations(self, browser: str = "CURRENT"):
        current_page = self.b.get_page_ids(
            page=SelectionType.CURRENT, context=SelectionType.CURRENT, browser=SelectionType.CURRENT
        )[0]
        try:
            return list(self._generate_locations(browser))
        finally:
            self.b.switch_page(current_page, context=SelectionType.ALL, browser=SelectionType.ALL)

    def _generate_locations(self, browser: str):
        if browser.upper() == "CURRENT":
            page_ids = self.b.get_page_ids(browser=SelectionType.CURRENT)
        elif browser.upper() == "ALL":
            page_ids = self.b.get_page_ids()
        else:
            print(1, self._browser_indexes.get(browser, None))
            print(2, self._browser_aliases.get(browser))
            print(3, self._browser_indexes.get(self._browser_aliases.get(browser), None))
            id = self._browser_indexes.get(browser, None) or self._browser_indexes.get(
                self._browser_aliases.get(browser), None
            )
            if id is None:
                raise ValueError(f"Browser '{browser}' not found")
            self.b.switch_browser(id)
            page_ids = self.b.get_page_ids(browser=SelectionType.CURRENT)
        for page_id in page_ids:
            self.b.switch_page(page_id, context=SelectionType.ALL, browser=SelectionType.ALL)
            yield self.b.get_url()

    @keyword
    def get_selected_list_label(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def get_selected_list_labels(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def get_selected_list_value(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def get_selected_list_values(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def get_selenium_implicit_wait(self):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def get_selenium_speed(self):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def get_selenium_timeout(self):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def get_session_id(self):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def get_source(self):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def get_table_cell(
        self,
        locator: Union[WebElement, None, str],
        row: int,
        column: int,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword(tags=("IMPLEMENTED",))
    def get_text(self, locator: WebElement):
        return self.b.get_text(locator)

    @keyword(tags=("IMPLEMENTED",))
    def get_title(self):
        return self.b.get_title()

    @keyword(tags=("IMPLEMENTED",))
    def get_value(self, locator: WebElement):
        return self.b.get_text(locator)

    @keyword(tags=("IMPLEMENTED",))
    def get_vertical_position(self, locator: WebElement):
        return self.b.get_boundingbox(locator, BoundingBoxFields.y)

    @keyword(tags=("IMPLEMENTED",))
    def get_webelement(self, locator: WebElement):
        return self.b.get_element(locator)

    @keyword(tags=("IMPLEMENTED",))
    def get_webelements(self, locator: WebElement):
        return self.b.get_elements(locator)

    @keyword
    def get_window_handles(self, browser: str = "CURRENT"):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def get_window_identifiers(self, browser: str = "CURRENT"):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def get_window_names(self, browser: str = "CURRENT"):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def get_window_position(self):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def get_window_size(self, inner: bool = False):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def get_window_titles(self, browser: str = "CURRENT"):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def go_back(self):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def go_to(self, url):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def handle_alert(self, action: str = "ACCEPT", timeout: Optional[timedelta] = None):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword(tags=("IMPLEMENTED",))
    def input_password(self, locator: WebElement, password: str, clear: bool = True):
        org_level = BuiltIn().set_log_level(level="NONE")
        try:
            self.input_text(locator, password, clear)
        finally:
            BuiltIn().set_log_level(level=org_level)

    @keyword(tags=("IMPLEMENTED",))
    def input_text(self, locator: WebElement, text: str, clear: bool = True):
        self.b.type_text(locator, text, clear=clear)

    @keyword
    def input_text_into_alert(
        self, text: str, action: str = "ACCEPT", timeout: Optional[timedelta] = None
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def list_selection_should_be(self, locator: WebElement, *expected: str):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def list_should_have_no_selections(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def location_should_be(self, url: str, message: Optional[str] = None):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def location_should_contain(self, expected: str, message: Optional[str] = None):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def log_location(self):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def log_source(self, loglevel: str = "INFO"):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def log_title(self):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def maximize_browser_window(self):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def mouse_down(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def mouse_down_on_image(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def mouse_down_on_link(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def mouse_out(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def mouse_over(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def mouse_up(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword(tags=("IMPLEMENTED",))
    def open_browser(
        self,
        url: Optional[str] = None,
        browser: str = "firefox",
        alias: Optional[str] = None,
        remote_url: Union[bool, str] = False,
        desired_capabilities: Union[dict, None, str] = None,
        ff_profile_dir: Optional[str] = None,
        options: Any = None,
        service_log_path: Optional[str] = None,
        executable_path: Optional[str] = None,
    ):
        browser_enum, headless = BROWSERS.get(browser, (SupportedBrowsers.chromium, False))
        ids = self.b.new_persistent_context(
            url=url, browser=browser_enum, args=options, headless=headless
        )
        identifier = str(next(self._browser_index))
        self._browser_indexes[identifier] = ids[0]
        if alias:
            self._browser_aliases[alias] = identifier
        return identifier

    @keyword
    def open_context_menu(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_contain(self, text: str, loglevel: str = "TRACE"):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_contain_button(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_contain_checkbox(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_contain_element(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
        limit: Optional[int] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_contain_image(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_contain_link(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_contain_list(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_contain_radio_button(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_contain_textfield(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_not_contain(self, text: str, loglevel: str = "TRACE"):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_not_contain_button(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_not_contain_checkbox(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_not_contain_element(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_not_contain_image(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_not_contain_link(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_not_contain_list(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_not_contain_radio_button(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def page_should_not_contain_textfield(
        self,
        locator: WebElement,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def press_key(self, locator: WebElement, key: str):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def press_keys(self, locator: Union[WebElement, None, str] = None, *keys: str):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def radio_button_should_be_set_to(self, group_name: str, value: str):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def radio_button_should_not_be_selected(self, group_name: str):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def register_keyword_to_run_on_failure(self, keyword: Optional[str]):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def reload_page(self):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def remove_location_strategy(self, strategy_name: str):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def scroll_element_into_view(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def select_all_from_list(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword(tags=("IMPLEMENTED",))
    def select_checkbox(self, locator: WebElement):
        self.b.check_checkbox(locator)

    @keyword
    def select_frame(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword(tags=("IMPLEMENTED",))
    def select_from_list_by_index(self, locator: WebElement, *indexes: str):
        self.b.select_options_by(locator, SelectAttribute.index, *indexes)

    @keyword(tags=("IMPLEMENTED",))
    def select_from_list_by_label(self, locator: WebElement, *labels: str):
        self.b.select_options_by(locator, SelectAttribute.label, *labels)

    @keyword(tags=("IMPLEMENTED",))
    def select_from_list_by_value(self, locator: WebElement, *values: str):
        self.b.select_options_by(locator, SelectAttribute.value, *values)

    @keyword
    def select_radio_button(self, group_name: str, value: str):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def set_browser_implicit_wait(self, value: timedelta):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def set_focus_to_element(self, locator: WebElement):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def set_screenshot_directory(self, path: Optional[str]):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def set_selenium_implicit_wait(self, value: timedelta):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def set_selenium_speed(self, value: timedelta):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def set_selenium_timeout(self, value: timedelta):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def set_window_position(self, x: int, y: int):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def set_window_size(self, width: int, height: int, inner: bool = False):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def simulate_event(self, locator: WebElement, event: str):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def submit_form(self, locator: Union[WebElement, None, str] = None):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def switch_browser(self, index_or_alias: str):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def switch_window(
        self,
        locator: Union[list, str] = "MAIN",
        timeout: Optional[str] = None,
        browser: str = "CURRENT",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def table_cell_should_contain(
        self,
        locator: Union[WebElement, None, str],
        row: int,
        column: int,
        expected: str,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def table_column_should_contain(
        self,
        locator: Union[WebElement, None, str],
        column: int,
        expected: str,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def table_footer_should_contain(
        self,
        locator: Union[WebElement, None, str],
        expected: str,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def table_header_should_contain(
        self,
        locator: Union[WebElement, None, str],
        expected: str,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def table_row_should_contain(
        self,
        locator: Union[WebElement, None, str],
        row: int,
        expected: str,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def table_should_contain(
        self,
        locator: Union[WebElement, None, str],
        expected: str,
        loglevel: str = "TRACE",
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def textarea_should_contain(
        self,
        locator: WebElement,
        expected: str,
        message: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def textarea_value_should_be(
        self,
        locator: WebElement,
        expected: str,
        message: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def textfield_should_contain(
        self,
        locator: WebElement,
        expected: str,
        message: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def textfield_value_should_be(
        self,
        locator: WebElement,
        expected: str,
        message: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def title_should_be(self, title: str, message: Optional[str] = None):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword(tags=("IMPLEMENTED",))
    def unselect_all_from_list(self, locator: WebElement):
        self.b.select_options_by(locator, SelectAttribute.index)

    @keyword(tags=("IMPLEMENTED",))
    def unselect_checkbox(self, locator: WebElement):
        self.b.uncheck_checkbox(locator)

    @keyword
    def unselect_frame(self):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def unselect_from_list_by_index(self, locator: WebElement, *indexes: str):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def unselect_from_list_by_label(self, locator: WebElement, *labels: str):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def unselect_from_list_by_value(self, locator: WebElement, *values: str):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def wait_for_condition(
        self,
        condition: str,
        timeout: Optional[timedelta] = None,
        error: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def wait_until_element_contains(
        self,
        locator: Union[WebElement, None, str],
        text: str,
        timeout: Optional[timedelta] = None,
        error: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def wait_until_element_does_not_contain(
        self,
        locator: Union[WebElement, None, str],
        text: str,
        timeout: Optional[timedelta] = None,
        error: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def wait_until_element_is_enabled(
        self,
        locator: Union[WebElement, None, str],
        timeout: Optional[timedelta] = None,
        error: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def wait_until_element_is_not_visible(
        self,
        locator: Union[WebElement, None, str],
        timeout: Optional[timedelta] = None,
        error: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def wait_until_element_is_visible(
        self,
        locator: Union[WebElement, None, str],
        timeout: Optional[timedelta] = None,
        error: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def wait_until_location_contains(
        self,
        expected: str,
        timeout: Optional[timedelta] = None,
        message: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def wait_until_location_does_not_contain(
        self,
        location: str,
        timeout: Optional[timedelta] = None,
        message: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def wait_until_location_is(
        self,
        expected: str,
        timeout: Optional[timedelta] = None,
        message: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def wait_until_location_is_not(
        self,
        location: str,
        timeout: Optional[timedelta] = None,
        message: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def wait_until_page_contains(
        self,
        text: str,
        timeout: Optional[timedelta] = None,
        error: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def wait_until_page_contains_element(
        self,
        locator: Union[WebElement, None, str],
        timeout: Optional[timedelta] = None,
        error: Optional[str] = None,
        limit: Optional[int] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def wait_until_page_does_not_contain(
        self,
        text: str,
        timeout: Optional[timedelta] = None,
        error: Optional[str] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")

    @keyword
    def wait_until_page_does_not_contain_element(
        self,
        locator: Union[WebElement, None, str],
        timeout: Optional[timedelta] = None,
        error: Optional[str] = None,
        limit: Optional[int] = None,
    ):
        "*NOT IMPLEMENTED YET*"
        raise NotImplementedError("keyword is not implemented")
