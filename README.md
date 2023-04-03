# FinalAutoTestesProject по <a href='https://stepik.org/course/575/info'>курсу.</a>

## Установка:

<div>

    git clone git@github.com:jeffrixxxon/FinalSeleniumProject.git

</div>

<div>

    cd FinalSeleniumProject

</div>

<div>
    
    pip install -r requirements.txt

</div>

## Запуск:

<div>

    pytest -s -v --tb=line test_product_page.py

</div>

### Или:

<div>

    pytest -s -v --tb=line test_main_page.py

</div>

## Опцианально можно выбрать язык страницы:
> по умолчанию стоит en: English

<div>

    pytest -s -v --tb=line --language=язык название_теста

</div>