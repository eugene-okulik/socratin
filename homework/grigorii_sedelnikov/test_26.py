import time

from playwright.sync_api import Page, expect


def test_1(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication").click()
    page.get_by_role('textbox', name='username').fill("tomsmith")
    page.get_by_role('textbox', name='password').fill("SuperSecretPassword!")
    page.get_by_role('button', name='Login').click()


def test_2(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_role('textbox', name='First Name').fill("Johnyy")
    page.get_by_role('textbox', name='Last Name').fill("Vendor")
    page.get_by_role('textbox', name='name@example.com').fill("Vendor@in.er")
    page.locator('label.custom-control-label', has_text='Other').click()
    page.get_by_role('textbox', name='Mobile Number').fill("0999098888")
    page.locator('#dateOfBirthInput').fill("22 Jun 1996")
    page.locator('#subjectsInput').fill('Maths')
    page.keyboard.press("Enter")
    page.locator('label[for="hobbies-checkbox-2"]').click()
    page.locator('#currentAddress').type("New York")
    page.locator('#react-select-3-input').fill("NCR")
    page.keyboard.press("Enter")
    page.locator('#react-select-4-input').type("Gurgaon")
    page.keyboard.press("Enter")
    page.locator('#submit').click()
    time.sleep(5)
    expect(page.locator('div.modal-title.h4#example-modal-sizes-title-lg')).to_have_text(
        "Thanks for submitting the form")
