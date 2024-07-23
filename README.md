# Besty Webshop Remake
*Expres gemankeerde webshop*

## Deploy
App stond op Google App Engine, maar is inmiddels weggehaald.
[(dode link)](https://betsy-webshop-remake.ew.r.appspot.com) op Google App Engine.

## STARR

### Situatie
Webshop met disfunctionele login

Er klopt iets niet met de login, iedereen is welkom. Wat is hier aan de hand?

### Taken
Testen schrijven - BDD

Mijn taak: login testen. 

### Actie
Uitgezocht: welke test tools zijn geschikt (app = Python webapp met Flask FE en sqlite database):
- Cucumber BDD
- Selenium Webdriver

Gedaan:
- Python Behave install + eerste script (trial)
- Flask integratie met Behave
- Selenium install + eerste script (trial) - title printen
- Selenium login test script - o.a. welkomstboodschap printen

### Resultaat
Eerste kennismaking met Cucumber + Selenium WebDriver. Script op proef geschreven en gerund, met succes. (Behave test pass, Selenium test print titel van webapp in CLI). Vervolg: scripts schrijven om werkelijk de login te testen.
