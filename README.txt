Project "Python for QA course"

There you see tasks code realization

Scope of this git, next:
	1. basic_theory.py - contain all that needed to be done in scope of "Basic theory" chapter
	2. Test_Book_Service/ - Exercise: Test Book Service
	3. UI_Tests_Selenium/ - Exercise: UI testing with Selenium


================================================================================================
Before running test install requirements.txt 
================================================================================================

Next files, additional for scope 1, include test data:
	Basic_text
	Basic_text_2


Tests from scope 2 - 3 could be runed, next:
	pytest Test_Book_Service/tests/api/test_put.py -vv
	pytest UI_Tests_Selenium/tests/test_case_1.py --alluredir logs  

For UI tests to see logs via Allure need to run next command: 
	allure serve logs

