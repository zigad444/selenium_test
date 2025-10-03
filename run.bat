@echo off
python -m pytest -s -v -m "regression" --html .\reports\test_report_chrome.html --browser chrome

