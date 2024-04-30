from playwright.sync_api import Page, expect


def test_tie(page: Page):
    page.goto("https://samin005.github.io/Tic-Tac-Toe-AI/")
    expect(page.get_by_label("Hard  Easy  2 Players")).to_have_value("0")
    page.get_by_role("button", name="Start Game!").click()
    expect(page.locator("app-game")).to_contain_text("The AI lets you go first out of pity.")
    page.locator("[id=\"\\30 \"]").click()
    expect(page.locator("[id=\"\\34 \"]")).to_contain_text("O")
    expect(page.locator("app-game")).to_contain_text("X's turn.")
    page.locator("[id=\"\\33 \"]").click()
    expect(page.locator("[id=\"\\36 \"]")).to_contain_text("O")
    expect(page.locator("app-game")).to_contain_text("X's turn.")
    page.locator("[id=\"\\32 \"]").click()
    expect(page.locator("[id=\"\\31 \"]")).to_contain_text("O")
    expect(page.locator("app-game")).to_contain_text("X's turn.")
    page.locator("[id=\"\\37 \"]").click()
    expect(page.locator("[id=\"\\35 \"]")).to_contain_text("O")
    expect(page.locator("app-game")).to_contain_text("X's turn.")
    page.locator("[id=\"\\38 \"]").click()
    expect(page.locator("app-game")).to_contain_text("Game tied!")
