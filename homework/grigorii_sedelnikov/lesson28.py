import json

from playwright.async_api import Route
from playwright.sync_api import Page


def test_1(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = 'Яблокофон15Про'
        body = json.dumps(body)
        route.fulfill(response=response, body=body)

    page.route('https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat', handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('//h3[text()="iPhone 15 Pro &"]').click()
    assert page.wait_for_selector('#rf-digitalmat-overlay-label-0').text_content() == 'Яблокофон15Про'
