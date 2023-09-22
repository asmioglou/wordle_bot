This mini project is inspired by **dspinellis** [word game](https://github.com/dspinellis/word-master)

Makes use of Regular Expressions and Selenium with Python.
So, in order to use it, one should install Selenium and include Selenium Webdriver in an appopriate directory. I used [geckodriver](https://github.com/mozilla/geckodriver/releases) and so, I included it in the repo but should one want to use another browser, the relevant webdriver file should be included.

Also, the revelant directory should be included in user's PATH variable. This is normally done on Linux Systems with:

```
export PATH=$PATH:/path/to/directory 

```

Further details on Selenium can be found on [Selenium website](https://selenium.dev) or [Selenium Github](https://github.com/SeleniumHQ).

## Demonstration

Here is a video that shows an example Game Play.

1. User executes the wordle script which opens a Firefox browser 
2. Browser visits the relevant webpage
3. Closes the initial modal
4. Proceeds to pay the game according to the rules

The bot tries to guess the word in 5 games, effectively leaving a last one for the user-human.


[![Wordle game](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fispeakalittlegreek.files.wordpress.com%2F2022%2F01%2Fwordle.png&f=1&nofb=1&ipt=913d97ead7a4c6a62d238c2fe900dd514466b65d672cebf2f7c8e60127c1d661&ipo=images)](https://youtu.be/Fz59uDBFxD8 "Greek Wordle gameplay")
