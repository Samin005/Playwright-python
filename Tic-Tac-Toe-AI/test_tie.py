from playwright.sync_api import Playwright, sync_playwright, expect


def test_tie(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://samin005.github.io/Tic-Tac-Toe-AI/")
    expect(page.locator("#typedText")).to_contain_text("Mode Details: You will play against an AI that uses the Minimax Alpha Beta Pruning Algorithm to make the best move possible. You won't win, the best thing you can do is a tie!")
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

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_tie(playwright)
