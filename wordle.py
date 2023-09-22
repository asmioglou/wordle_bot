import re
import time

from random import choice
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from words import words


class Wordle:
    """This is a class to simulate a game of wordle, with greek words. 
    Inspired by dspinellis word-master game which it uses. Makes use
    of regular expressions to successively narrow the wordlist pool"""

    def __init__(self):
        """Set as instance variables for no obvious reason."""
        self.browser = webdriver.Firefox()
        self.letters = {}   # letter buttons
        self.must_have_letters = set()
        self.regexp = ["[^]","[^]","[^]","[^]","[^]"]
        self.url = "https://dspinellis.github.io/word-master/"
        self.wait = WebDriverWait(self.browser, 10)
        self.wordlist = words.keys()

    def initialize(self):
        """Open webpage, close first modal and get the keyboard 
        buttons from webpage and store in dict."""
        self.browser.get(self.url)
        # close the first modal
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 
            'button.top-4.right-4'))).click()
        # get letters
        self.letters['Ε'] = \
            self.browser.find_element("xpath", "//*[contains(text(), 'Ε')]")
        self.letters['Ρ'] = \
            self.browser.find_element("xpath", "//*[contains(text(), 'Ρ')]")
        self.letters['Τ'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Τ')]")
        self.letters['Υ'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Υ')]")
        self.letters['Θ'] = self.browser. \
            find_element("xpath", "//*[contains(text(),'Θ')]")
        self.letters['Ι'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Ι')]")
        self.letters['Ο'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Ο')]")
        self.letters['Π'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Π')]")
        self.letters['Α'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Α')]")
        self.letters['Σ'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Σ')]")
        self.letters['Δ'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Δ')]")
        self.letters['Φ'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Φ')]")
        self.letters['Γ'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Γ')]")
        self.letters['Η'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Η')]")
        self.letters['Ξ'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Ξ')]")
        self.letters['Κ'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Κ')]")
        self.letters['Λ'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Λ')]")
        self.letters['Ζ'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Ζ')]")
        self.letters['Χ'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Χ')]")
        self.letters['Ψ'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Ψ')]")
        self.letters['Ω'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Ω')]")
        self.letters['Β'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Β')]")
        self.letters['Ν'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Ν')]")
        self.letters['Μ'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'Μ')]")
        self.letters['enter'] = self.browser. \
            find_element("xpath", "//*[contains(text(), 'ENTER')]")
    
    def manual_type(self, word):
        """Simulate typing in the browser keyboard, as clicks.
        Wait 1s between clicks. First, check if won!"""
        try:
            # This does not work, but shouldn't rely on exception
            self.browser.find_element(By.CSS_SELECTOR, "div.ReactModal__Overlay")
            print("Success! You won!")
            return
        except:
            pass
        # If not won, click the buttons
        for letter in word:
            self.letters[letter].click()
            time.sleep(1)
        self.letters['enter'].click()
    
    def check_letters(self, n):
        """Check each letter from webpage, and update the regular expression
        accordingly."""
        # 5 items of each row
        round_letters = self.browser.   \
                find_elements(By.CSS_SELECTOR, "span.rounded-full")[5*n:5*(n+1)]
        for letter in enumerate(round_letters):
            if "nm-inset-n-gray" in letter[1].get_attribute("class"):
                for counter in range(5):
                    if (self.regexp[counter].startswith("[^")):
                        self.regexp[counter] = \
                                self.regexp[counter][:-1]+letter[1].text + "]"
                continue
            if "nm-inset-yellow-500" in letter[1].get_attribute("class"):
                self.must_have_letters.add(letter[1].text)
                self.regexp[letter[0]] = self.regexp[letter[0]][:-1]+\
                                                     letter[1].text + "]"
                continue
            if "nm-inset-n-green" in letter[1].get_attribute("class"):
                self.regexp[letter[0]] = "[" + letter[1].text + "]"
                continue
    
    def update_pool(self):
        """Update wordlist pool according to results."""
        print("regx: " + "^" + "".join(self.regexp) + "$")
        regx = re.compile("^" + "".join(self.regexp) + "$")
        self.wordlist = list(filter(regx.match, self.wordlist))
        self.wordlist = list(filter(lambda item: 
            all([x in item for x in self.must_have_letters]), self.wordlist))

    def play(self):
        """Simulate 5 games and let the last one for the player."""
        for count in range(5):
            first = choice(list(self.wordlist))
            self.manual_type(first)
            self.check_letters(count)
            self.update_pool()

if __name__ == "__main__":
    game = Wordle()
    game.initialize()
    game.play()
