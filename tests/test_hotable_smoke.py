# tests/test_hotable_smoke.py
import re
import allure
from playwright.sync_api import Page, expect

@allure.title("Wejście na stronę, wybór restauracji wybranie stolika i pobranie kodu rabatowego")
def test_wybor_restauracji_i_stolikow(page: Page):
    with allure.step("Otwórz stronę główną"):
        page.goto("https://hotable.pl", wait_until="domcontentloaded")

    with allure.step("Akceptuj cookies (jeśli widoczne)"):
        btn = page.get_by_role("button", name=re.compile("Akceptuj|Zgadzam|Accept", re.I))
        if btn.is_visible():
            btn.click()

    with allure.step("Wybierz restaurację"):
        page.get_by_role("link", name="Porto Azzurro").click()

    with allure.step("Przewiń do sekcji 'Stoliki' i kliknij stolik"):
        page.get_by_test_id("table-t20").locator("div").first.click()

    with allure.step("Pobierz kod rabatowy"):
        page.get_by_role("button", name="Zdobądź zniżkę →").click()
        page.get_by_role("button", name="Kopiuj kod").click()
