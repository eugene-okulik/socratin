from playwright.sync_api import Page, expect


def test_1(page: Page):
    def confirm_alert(dialog):
        dialog.accept()

    page.on('dialog', confirm_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.click('a.a-button')
    result = page.locator('#result-text')
    expect(result).to_have_text('Ok')


def test_2(page: Page):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    with page.expect_popup() as second_page:
        page.click('a.a-button')
    second_page = second_page.value
    second_page.wait_for_load_state('load')
    result = second_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    page.is_enabled('a.a-button')


def test_3(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    page.wait_for_selector('.mt-4.text-danger.btn.btn-primary').click()
