CONFIG_DIR = 'config'
DATA_DIR = 'data'
try:
    import sys
    import os
    sys.path.insert(0, CONFIG_DIR)
    from config import YOUR_BIRTHDAY, YOUR_GENDER, YOUR_PASSWORD, FIVESIM_API_KEY, FIVESIM_COUNTRY, FIVESIM_OPERATOR, USE_ARABIC_NAMES, NAMES_FILE
except ImportError:
    YOUR_BIRTHDAY = '2 4 1950'
    YOUR_GENDER = '1'
    YOUR_PASSWORD = ''
    FIVESIM_API_KEY = ''
    FIVESIM_COUNTRY = 'usa'
    FIVESIM_OPERATOR = 'any'
    USE_ARABIC_NAMES = True
    NAMES_FILE = os.path.join(DATA_DIR, 'names.txt')
if not YOUR_PASSWORD:
    try:
        password_file = os.path.join(CONFIG_DIR, 'password.txt')
        with open(password_file, 'r', encoding='utf-8') as f:
            your_password = f.read().strip()
    except FileNotFoundError:
        print('Error: config/password.txt file not found! Please create it.')
        your_password = ''
else:
    your_password = YOUR_PASSWORD
if not FIVESIM_API_KEY:
    try:
        fivesim_file = os.path.join(CONFIG_DIR, '5sim_config.txt')
        with open(fivesim_file, 'r', encoding='utf-8') as f:
            FIVESIM_API_KEY = f.read().strip()
    except FileNotFoundError:
        FIVESIM_API_KEY = ''
your_birthday = YOUR_BIRTHDAY
your_gender = YOUR_GENDER
def load_user_agents():
    """Load user agents from config/user_agents.txt file"""
    # ***<module>.load_user_agents: Failure: Different control flow
    user_agents_list = []
    try:
        user_agents_file = os.path.join(CONFIG_DIR, 'user_agents.txt')
        with open(user_agents_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                user_agents_list.append(line)
        return user_agents_list if user_agents_list else get_default_user_agents()
    except FileNotFoundError:
        return get_default_user_agents()
def get_default_user_agents():
    """Default user agents fallback"""
    return ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36']
user_agents = load_user_agents()
def load_names_from_file():
    # irreducible cflow, using cdg fallback
    """Load names from names.txt file"""
    # ***<module>.load_names_from_file: Failure: Compilation Error
    names_list = []
    names_file = NAMES_FILE if os.path.exists(NAMES_FILE) else os.path.join(DATA_DIR, 'names.txt')
    with open(names_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            names_list.append(line) if ' ' in line else names_list.append(line)
            return names_list
            except FileNotFoundError:
            return []
names_list = load_names_from_file()
arabic_first_names = []
arabic_last_names = []
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import random
import time
import requests
from unidecode import unidecode
import uuid
from fp.fp import FreeProxy
import os
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.live import Live
from rich.text import Text
import json
import threading
from datetime import datetime
from selenium.webdriver import ActionChains
import re
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import platform
import sys
import subprocess
import zipfile
import shutil
import string
from selenium.webdriver.support.select import Select
console = Console()
CONFIG = {'version': '2.0.0', 'theme_color': 'cyan', 'secondary_color': 'magenta', 'success_color': 'green', 'error_color': 'red', 'warning_color': 'yellow'}
def get_matrix_animation():
    """Matrix-style code rain animation frames"""
    frames = []
    chars = '01█▓▒░'
    for i in range(4):
        frame = ''
        for _ in range(3):
            line = ''.join([random.choice(chars) for _ in range(40)])
            frame += f'[{CONFIG['success_color']}]{line}[/]\n'
        frames.append(frame)
    return frames
def show_beautiful_banner():
    """Display a beautiful banner with animations"""
    # ***<module>.show_beautiful_banner: Failure: Different bytecode
    banner = f'\n[{CONFIG['theme_color']}]\n██████╗ ███╗   ███╗ █████╗ ██╗██╗         ██████╗██████╗ ███████╗ █████╗ ████████╗ ██████╗ ██████╗ \n██╔════╝████╗ ████║██╔══██╗██║██║        ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗\n██║  ███╗██╔████╔██║███████║██║██║        ██║     ██████╔╝█████╗  ███████║   ██║   ██║   ██║██████╔╝\n██║   ██║██║╚██╔╝██║██╔══██║██║██║        ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗\n╚██████╔╝██║ ╚═╝ ██║██║  ██║██║███████╗   ╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║\n ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝\n[/]\n\n[{CONFIG['secondary_color']}]✨ The Ultimate Gmail Account Creator v{CONFIG['version']} ✨[/]\n'
    feature_text = ['🚀 Advanced Anti-Detection System', '🔒 Phone Verification Bypass', '🌐 Smart Proxy Integration', '🎨 Beautiful Modern Interface', '📊 Detailed Statistics', '💾 Auto-Save Accounts', '🔄 Auto-Retry on Failure', '⚡ Lightning Fast Creation']
    copyright_info = f'\n[{CONFIG['warning_color']}]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/]\n[{CONFIG['theme_color']}]© 2025 Shadow Hacker - All Rights Reserved[/]\n[{CONFIG['secondary_color']}]🌐 Website: https://www.shadowhackr.com[/]\n[{CONFIG['secondary_color']}]📘 Facebook: www.facebook.com/ShadowHackr[/]\n[{CONFIG['secondary_color']}]📱 WhatsApp: +962796668987[/]\n[{CONFIG['warning_color']}]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/]\n'
    console.print(Panel(f'{banner}\n\n{feature_text}\n{copyright_info}', border_style=CONFIG['theme_color'], padding=(1, 2), title='[bold]Welcome to Gmail Creator Pro[/]', subtitle='[bold]By SHADOWHACKER[/]'))
def show_beautiful_menu():
    """Display a beautiful menu with animations"""
    # ***<module>.show_beautiful_menu: Failure: Different bytecode
    menu_items = [('1', 'Create Gmail Accounts', '🚀 Start creating new Gmail accounts automatically'), ('2', 'View Statistics', '📊 View detailed creation statistics and success rates'), ('3', 'Settings', '⚙️ Configure proxy, user agents, and other settings'), ('4', 'View Saved Accounts', '📁 View all created accounts and their details'), ('5', 'Exit', '👋 Exit the application')]
def show_creation_progress(current, total):
    """Show beautiful progress bars for account creation"""
    # ***<module>.show_creation_progress: Failure: Different control flow
    with Progress(SpinnerColumn(), TextColumn('[progress.description]{task.description}'), BarColumn(complete_style=CONFIG['theme_color']), TaskProgressColumn(), console=console) as progress:
        overall_task = progress.add_task(f'[{CONFIG['theme_color']}]Overall Progress', total=total)
        account_task = progress.add_task(f'[{CONFIG['theme_color']}]Current Account', total=100)
        if current < total:
            progress.update(overall_task, completed=current)
            for step, desc in [(0, 'Initializing browser...'), (10, 'Opening Gmail signup...'), (20, 'Filling personal info...'), (40, 'Setting up email...'), (60, 'Creating password...'), (80, 'Bypassing verification...'), (90, 'Finalizing account...'), (100, 'Account created successfully!')]:
                progress.update(account_task, completed=step, description=f'[{CONFIG['theme_color']}]{desc}')
                time.sleep(0.5)
            current += 1
            progress.update(account_task, completed=0)
def save_account(email, password):
    """Save account details with encryption"""
    # ***<module>.save_account: Failure: Different control flow
    try:
        accounts_file = os.path.join(DATA_DIR, 'accounts.json')
        os.makedirs(DATA_DIR, exist_ok=True)
        accounts = []
        with open(accounts_file, 'r') as f, json.load(f) as accounts:
            pass
        accounts.append({'email': email, 'password': password, 'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'status': 'active'})
        with open(accounts_file, 'w') as f:
            json.dump(accounts, f, indent=4)
        console.print(f'[{CONFIG['success_color']}]✓ Account saved successfully![/]')
    except Exception as e:
        console.print(f'[{CONFIG['error_color']}]Error saving account: {str(e) / names.txt}[/]')
def view_statistics():
    """Show beautiful statistics dashboard"""
    # ***<module>.view_statistics: Failure: Different bytecode
    try:
        accounts_file = os.path.join(DATA_DIR, 'accounts.json')
        with open(accounts_file, 'r') as f:
            accounts = json.load(f)
        total = len(accounts)
        active = sum((1 for acc in accounts if acc['status'] == 'active'))
        success_rate = active / total * 100 if total > 0 else 0
        stats_table = Table(title=f'[{CONFIG['theme_color']}]Account Creation Statistics[/]', show_header=True, header_style='bold')
        stats_table.add_column('Metric', style=CONFIG['theme_color'])
        stats_table.add_column('Value', justify='right', style=CONFIG['success_color'])
        stats_table.add_row('Total Accounts Created', str(total))
        stats_table.add_row('Active Accounts', str(active))
        stats_table.add_row('Success Rate', f'{success_rate:.1f}%')
        stats_table.add_row('Last Creation', accounts[(-1)]['created_at'] if accounts else 'N/A')
        console.print(Panel(stats_table, border_style=CONFIG['theme_color']))
    except Exception as e:
        console.print(f'[{CONFIG['error_color']}]Error loading statistics: {str(e) / names.txt}[/]')
def human_typing(element, text, delay_range=(0.1, 0.3)):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(*delay_range))
def human_click(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element).pause(random.uniform(0.2, 0.5)).click().perform()
    time.sleep(random.uniform(0.5, 1.2))
def warm_up_session(driver):
    # ***<module>.warm_up_session: Failure: Compilation Error
    print('🔥 Warming up browsing session...')
    try:
        driver.get('https://www.google.com/')
        time.sleep(random.uniform(5, 8))
        search_box = driver.find_element(By.NAME, 'q')
        queries = ['today weather', 'sports news', 'dream interpretation', 'currency rates', 'best movies 2025', 'how to bake bread', 'tech news 2025']
        query = random.choice(queries)
        search_box.send_keys(query)
        search_box.submit()
        print(f'🔍 Searched: {query}')
        time.sleep(random.uniform(6, 10))
        links = driver.find_elements(By.XPATH, '//h3')
        random.choice(links).click() if links else None
            print('🌐 Browsed first result...')
            time.sleep(random.uniform(8, 12))
        driver.get('https://www.bbc.com/')
        time.sleep(random.uniform(6, 10))
        driver.get('https://www.wikipedia.org/')
        time.sleep(random.uniform(6, 10))
        driver.get('https://www.google.com/maps')
        print('🗺️ Opened Google Maps...')
        time.sleep(random.uniform(5, 8))
        driver.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        print('🎬 Watching YouTube video...')
        time.sleep(random.uniform(15, 25))
        print('✅ Session warmed up!')
    except Exception as e:
        print(f'⚠️ Error warming session: {e}')
def try_set_gender(driver, gender_values):
    # irreducible cflow, using cdg fallback
    # ***<module>.try_set_gender: Failure: Compilation Error
    for value in gender_values:
        pass
    gender_elem = driver.find_element(By.CSS_SELECTOR, 'select#gender, select[aria-label=\"Gender\"]')
    select = Select(gender_elem)
    select.select_by_value(value)
    if gender_elem.get_attribute('value') == value or gender_elem.get_attribute('value').lower() == value.lower():
        pass
    return True
    driver.execute_script('\n            let genderSelect = document.querySelector(\'select#gender\') || \n                                 document.querySelector(\'select[aria-label=\"Gender\"]\');\n            if (genderSelect) {\n                genderSelect.value = arguments[0];\n                genderSelect.dispatchEvent(new Event(\'change\', { bubbles: true }));\n            }\n        ', value)
    result = driver.execute_script('\n            let genderSelect = document.querySelector(\'select#gender\') || \n                                 document.querySelector(\'select[aria-label=\"Gender\"]\');\n            return genderSelect ? genderSelect.value : null;\n        ')
    if not result:
        continue
    else:
        if result == value or result.lower() == value.lower():
            return True
    return False
    select.select_by_visible_text(value)
    pass
def try_set_month(driver, month_values):
    # irreducible cflow, using cdg fallback
    # ***<module>.try_set_month: Failure: Compilation Error
    for value in month_values:
        pass
    month_elem = driver.find_element(By.CSS_SELECTOR, 'select#month, select[aria-label=\"Month\"], select[name=\"month\"]')
    select = Select(month_elem)
    select.select_by_value(value)
    if month_elem.get_attribute('value') == value or month_elem.get_attribute('value').lower() == value.lower():
        pass
    return True
    driver.execute_script('\n            function setMonthValue(value) {\n                let monthSelect = document.querySelector(\'select#month\') || \n                                  document.querySelector(\'select[aria-label=\"Month\"]\') ||\n                                  document.querySelector(\'select[name=\"month\"]\');\n                if (monthSelect) {\n                    monthSelect.value = arguments[0];\n                    monthSelect.dispatchEvent(new Event(\'change\', { bubbles: true }));\n                    for (let i = 0; i < monthSelect.options.length; i++) {\n                        if (monthSelect.options[i].value === arguments[0]) {\n                            monthSelect.selectedIndex = i;\n                            break;\n                        }\n                    }\n                    monthSelect.dispatchEvent(new Event(\'input\', { bubbles: true }));\n                    monthSelect.dispatchEvent(new Event(\'change\', { bubbles: true }));\n                }\n            }\n            setMonthValue(arguments[0]);\n        ', value)
    result = driver.execute_script('\n            let monthSelect = document.querySelector(\'select#month\') || \n                                  document.querySelector(\'select[aria-label=\"Month\"]\') ||\n                                  document.querySelector(\'select[name=\"month\"]\');\n            return monthSelect ? monthSelect.value : null;\n        ')
    if not result:
        continue
    else:
        if result == value or result.lower() == value.lower():
            return True
    return False
    select.select_by_visible_text(value)
    pass
def try_click_month_dropdown(driver, month_name):
    # ***<module>.try_click_month_dropdown: Failure: Compilation Error
    try:
        month_dropdown = driver.find_element(By.XPATH, '//*[@id=\"month\"]/div/div[1]/div')
        month_dropdown.click()
        time.sleep(1)
        options = driver.find_elements(By.XPATH, '//*[@id=\"month\"]/div/div[2]/ul/li')
        for option in options if month_name.strip() is not None.lower() in option.text.strip().lower():
            else:
                option.click()
                return True
    except Exception as e:
        return False
    return False
def try_click_gender_dropdown(driver, gender_text):
    # ***<module>.try_click_gender_dropdown: Failure: Compilation Error
    try:
        gender_dropdown = driver.find_element(By.XPATH, '//*[@id=\"gender\"]/div/div[1]/div')
        for option in options if gender_text.strip() is not None.lower() in option.text.strip().lower():
            else:
                option.click()
                return True
    except Exception as e:
        return False
    return False
def create_account(driver, wait, progress, task_id, your_username, your_password):
    # irreducible cflow, using cdg fallback
    # ***<module>.create_account: Failure: Compilation Error
    update_progress_with_animation(progress, task_id, 'Opening Gmail signup', 10)
    max_retries = 3
    success = False
    for attempt in range(max_retries):
        try:
            driver.delete_all_cookies()
            driver.execute_script('window.localStorage.clear();')
            driver.execute_script('window.sessionStorage.clear();')
            driver.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
            wait.until(EC.presence_of_element_located((By.NAME, 'firstName')))
            success = True
        except Exception as e:
            raise Exception(f'Could not load signup page: {str(e) / 1}') if attempt == max_retries - 1 else time.sleep(2)
                driver.refresh()
        else:
            break
    if not success:
        raise Exception('Failed to load signup page after multiple attempts')
    else:
        time.sleep(2)
        first_name = generate_realistic_name()
        last_name = generate_realistic_name()
        driver.execute_script('\n            let firstNameField = document.querySelector(\'input[name=\"firstName\"]\');\n            if (firstNameField) {\n                firstNameField.value = arguments[0];\n                firstNameField.dispatchEvent(new Event(\'input\', { bubbles: true }));\n                firstNameField.dispatchEvent(new Event(\'change\', { bubbles: true }));\n            }\n        ', first_name)
        driver.execute_script('\n            let lastNameField = document.querySelector(\'input[name=\"lastName\"]\');\n            if (lastNameField) {\n                lastNameField.value = arguments[0];\n                lastNameField.dispatchEvent(new Event(\'input\', { bubbles: true }));\n                lastNameField.dispatchEvent(new Event(\'change\', { bubbles: true }));\n            }\n        ', last_name)
        time.sleep(1.5)
        driver.execute_script('\n            let nextButton = Array.from(document.querySelectorAll(\'button\')).find(button => \n                button.textContent.toLowerCase().includes(\'next\'));\n            if (nextButton) nextButton.click();\n        ')
        time.sleep(3)
        month, day, year = validate_birthday(your_birthday)
        month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month_values = [month, str(int(month))]
        if month.isdigit() and 1 <= int(month) <= 12 and month_values.append(month_names[int(month) - 1]):
            pass
        month_selected = try_set_month(driver, month_values)
        try_click_month_dropdown(driver, month_names[int(month) - 1])
        time.sleep(2)
        driver.execute_script('\n            // Fill day\n            let dayField = document.querySelector(\'input[name=\"day\"]\');\n            if (dayField) {\n                dayField.value = arguments[0];\n                dayField.dispatchEvent(new Event(\'input\', { bubbles: true }));\n                dayField.dispatchEvent(new Event(\'change\', { bubbles: true }));\n            }\n            // Fill year\n            let yearField = document.querySelector(\'input[name=\"year\"]\');\n            if (yearField) {\n                yearField.value = arguments[1];\n                yearField.dispatchEvent(new Event(\'input\', { bubbles: true }));\n                yearField.dispatchEvent(new Event(\'change\', { bubbles: true }));\n            }\n        ', day, year)
        gender_values = [your_gender, '1', '2', '3', 'MALE', 'FEMALE', 'OTHER', 'ذكر', 'أنثى', 'اخرى']
        gender_texts = ['Male', 'Female', 'Other', 'ذكر', 'أنثى', 'اخرى']
        gender_selected = try_set_gender(driver, gender_values)
        if not gender_selected:
            for gtext in gender_texts:
                if try_click_gender_dropdown(driver, gtext):
                    break
        time.sleep(1)
        driver.execute_script('\n            function clickNext() {\n                // Try multiple methods to find the next button\n                let nextButton = Array.from(document.querySelectorAll(\'button\')).find(button => \n                    button.textContent.toLowerCase().includes(\'next\')) ||\n                    document.querySelector(\'button[type=\"submit\"]\') ||\n                    document.querySelector(\'button.VfPpkd-LgbsSe\');\n                \n                if (nextButton) {\n                    nextButton.click();\n                    return true;\n                }\n                return false;\n            }\n            return clickNext();\n        ')
        time.sleep(2)
        heading_xpaths = ['//div[contains(text(), \'Choose your Gmail address\')]', '//div[contains(text(), \'Create an email address\')]', '//h1[contains(text(), \'Create an email address\')]', '//h1[contains(text(), \'Choose your Gmail address\')]']
        heading_found = False
        for hx in heading_xpaths:
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, hx)))
                heading_found = True
            except Exception:
                continue
            else:
                break
        if not heading_found:
            raise Exception('Email-selection heading not found (UI text may have changed).')
        else:
            time.sleep(2)
            create_own_option = None
            xpath_selectors = ['//div[contains(text(), \'Create your own Gmail address\')]', '//span[contains(text(), \'Create your own Gmail address\')]', '//label[contains(text(), \'Create your own Gmail address\')]', '//div[contains(@class, \'VfPpkd-StrnGf-rymPhb\')]//span[contains(text(), \'Create your own\')]']
            for xpath in xpath_selectors:
                    elements = driver.find_elements(By.XPATH, xpath)
                    for element in elements:
                        if element.is_displayed() is None:
                            create_own_option = element
                            break
                    if create_own_option:
                        break
                if create_own_option and driver.execute_script('arguments[0].scrollIntoView(true);', create_own_option):
                    time.sleep(1)
                        create_own_option.click()
                            time.sleep(2)
                            username_field = None
                            field_selectors = ['//input[@type=\'text\']', '//input[@name=\'Username\']', '//input[@jsname=\'YPqjbf\']', '//input[contains(@class, \'whsOnd\')]', '//input[contains(@class, \'VfPpkd-fmcmS-wGMbrd\')]']
                            for selector in field_selectors:
                                        elements = driver.find_elements(By.XPATH, selector)
                                        for element in elements:
                                            if element.is_displayed() and element.is_enabled():
                                                    username_field = element
                                                    break
                                        if username_field:
                                            break
                                    if username_field:
                                        username_field.clear()
                                        time.sleep(0.5)
                                            username_field.send_keys(your_username)
                                                time.sleep(1)
                                                next_button = None
                                                button_selectors = ['//button[contains(text(), \'Next\')]', '//button[contains(@class, \'VfPpkd-LgbsSe\')]', '//button[@type=\'submit\']']
                                                for selector in button_selectors:
                                                            elements = driver.find_elements(By.XPATH, selector)
                                                            for element in elements:
                                                                if element.is_displayed() and element.is_enabled():
                                                                        next_button = element
                                                                        break
                                                            if next_button:
                                                                break
                                                        if next_button:
                                                            driver.execute_script('arguments[0].scrollIntoView(true);', next_button)
                                                            time.sleep(0.5)
                                                                next_button.click()
                                                                    time.sleep(2)
                                                                    update_progress_with_animation(progress, task_id, 'Entering password', 80)
                                                                    time.sleep(3)
                                                                        password_field = wait.until(EC.presence_of_element_located((By.NAME, 'Passwd')))
                                                                        confirm_field = wait.until(EC.presence_of_element_located((By.NAME, 'PasswdAgain')))
                                                                        wait.until(EC.element_to_be_clickable((By.NAME, 'Passwd')))
                                                                        wait.until(EC.element_to_be_clickable((By.NAME, 'PasswdAgain')))
                                                                        password_field.clear()
                                                                        confirm_field.clear()
                                                                        time.sleep(1)
                                                                        password_field.click()
                                                                        for char in your_password:
                                                                            password_field.send_keys(char)
                                                                        time.sleep(1)
                                                                        confirm_field.click()
                                                                        for char in your_password:
                                                                            confirm_field.send_keys(char)
                                                                        time.sleep(1)
                                                                        if password_field.get_attribute('value')!= your_password or confirm_field.get_attribute('value')!= your_password:
                                                                            driver.execute_script('\n                                    arguments[0].value = arguments[2];\n                                    arguments[0].dispatchEvent(new Event(\'input\', { bubbles: true }));\n                                    arguments[0].dispatchEvent(new Event(\'change\', { bubbles: true }));\n                                    arguments[1].value = arguments[2];\n                                    arguments[1].dispatchEvent(new Event(\'input\', { bubbles: true }));\n                                    arguments[1].dispatchEvent(new Event(\'change\', { bubbles: true }));\n                                ', password_field, confirm_field, your_password)
                                                                            time.sleep(1)
                                                                        try:
                                                                            show_password = driver.find_element(By.XPATH, '//input[@type=\'checkbox\']')
                                                                            if show_password and show_password.is_displayed() and show_password.click():
                                                                                    time.sleep(1)
                                                                        except:
                                                                            pass
                                                                        next_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(@class, \'VfPpkd-LgbsSe\') and contains(@class, \'VfPpkd-LgbsSe-OWXEXe-k8QpJ\')]')))
                                                                        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, \'VfPpkd-LgbsSe\') and contains(@class, \'VfPpkd-LgbsSe-OWXEXe-k8QpJ\')]')))
                                                                        driver.execute_script('arguments[0].scrollIntoView(true);', next_button)
                                                                        time.sleep(1)
                                                                        driver.execute_script('arguments[0].click();', next_button)
                                                                        time.sleep(3)
                                                                            wait.until(lambda driver: len(driver.find_elements(By.NAME, 'Passwd')) == 0)
                                                                            if handle_verification_smart(driver, wait, progress):
                                                                                update_progress_with_animation(progress, task_id, 'Account created successfully!', 100)
                                                                                save_account(f'{your_username}@gmail.com', your_password)
                                                                                    return True
                                                            console.print(f'[{CONFIG['error_color']}]Could not find password fields[/]')
                                        console.print(f'[{CONFIG['error_color']}]Could not find username field[/]')
                                                                                    return False
                    console.print(f'[{CONFIG['error_color']}]Could not find \'Create your own Gmail address\' option[/]')
                                                                return False
                            continue
                                radio_button = driver.find_element(By.XPATH, '//input[@type=\'radio\' and following-sibling::*[contains(text(), \'Create your own\')]]')
                                radio_button.click()
                                    driver.execute_script('arguments[0].click();', create_own_option)
                                                continue
                                                    driver.execute_script('arguments[0].value = arguments[1];', username_field, your_username)
                                                        ActionChains(driver).move_to_element(username_field).click().send_keys(your_username).perform()
                                                                    continue
                                                                        driver.execute_script('arguments[0].click();', next_button)
                                                                            ActionChains(driver).move_to_element(next_button).click().perform()
                                                                                    console.print(f'[{CONFIG['error_color']}]Failed to proceed after password entry[/]')
                                                                                        return False
                                                                                            except Exception as e:
                                                                                                    console.print(f'[{CONFIG['error_color']}]Error in password entry: {str(e)}[/]')
                                                                                                        return False
                    except Exception as e:
                                return False
        except Exception as e:
                    return False
def update_progress_with_animation(progress, task_id, message, percentage):
    """Update progress with smooth animation"""
    current = progress.tasks[task_id].completed
    steps = 10
    step_size = (percentage - current) / steps
    for i in range(steps):
        new_percentage = current + step_size * (i + 1)
        progress.update(task_id, description=f'[{CONFIG['theme_color']}]{message}...[/]', completed=new_percentage)
        time.sleep(0.05)
def click_next_button(driver):
    """Smart next button detection and click"""
    # ***<module>.click_next_button: Failure: Different control flow
    next_button_selectors = ['//span[contains(text(), \'Next\')]', '//button[contains(@class, \'VfPpkd-LgbsSe\')]', '//*[contains(text(), \'Next\')]']
    for selector in next_button_selectors:
        try:
            buttons = driver.find_elements(By.XPATH, selector)
            for button in buttons:
                if button.is_displayed() is None:
                    pass
                else:
                    return safe_click(driver, button)
        except:
            pass
    return False
def smart_find_element(driver, selectors):
    """Find element using multiple selectors"""
    # ***<module>.smart_find_element: Failure: Different control flow
    for by, value in selectors:
        try:
            element = wait_and_find_element(driver, by, value, timeout=5)
            return element if element and (not element.is_displayed()) else None
        except:
            pass
    return None
def fill_field_smart(driver, field, value):
    """Fill field using multiple methods"""
    methods = [lambda: field.send_keys(value), lambda: driver.execute_script('arguments[0].value = arguments[1]', field, value), lambda: ActionChains(driver).move_to_element(field).click().send_keys(value).perform()]
    for method in methods:
        try:
            method()
        except:
            pass
        else:
            return True
    return False
def validate_birthday(birthday_str):
    # irreducible cflow, using cdg fallback
    """Validate and parse birthday string"""
    # ***<module>.validate_birthday: Failure: Compilation Error
    month, day, year = birthday_str.split()
            month = '1'
                if not 1 <= int(day) <= 31:
                        day = '1'
                            if not 1900 <= int(year) <= 2010:
                                    year = '1990'
                                        return (month, day, year)
                                                return ('1', '1', '1990')
def generate_realistic_name():
    """Generate names from external file only - NO fallback"""
    if names_list:
        full_name = random.choice(names_list)
        return full_name if ' ' in full_name else full_name
    else:
        print('Error: names.txt is empty or not found! Please add names to names.txt')
        return f'User{random.randint(1000, 9999)}'
def bypass_phone_verification(driver, wait):
    # irreducible cflow, using cdg fallback
    """Enhanced phone verification bypass with multiple strategies"""
    # ***<module>.bypass_phone_verification: Failure: Compilation Error
    console.print(f'[{CONFIG['warning_color']}]Attempting to skip phone verification...[/]')
    skip_button_selectors = ['//button[contains(text(), \'Skip\')]', '//button[contains(text(), \'تخطي\')]', '//span[contains(text(), \'Skip\')]', '//span[contains(text(), \'تخطي\')]', '//div[contains(text(), \'Skip\')]', '//div[contains(text(), \'تخطي\')]', '//button[@aria-label=\'Skip\']', '//button[contains(@class, \'VfPpkd-LgbsSe\') and contains(text(), \'Skip\')]']
    for selector in skip_button_selectors:
                pass
                driver.execute_script('arguments[0].click();', skip_button)
                time.sleep(2)
                console.print(f'[{CONFIG['success_color']}]✓ Skipped phone verification![/]')
                    return True
                alternative_selectors = ['//button[contains(text(), \'Try another way\')]', '//button[contains(text(), \'Try a different way\')]', '//span[contains(text(), \'Try another way\')]', '//div[contains(text(), \'Try another way\')]']
                for selector in alternative_selectors:
                            alternative_button = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, selector)))
                            driver.execute_script('arguments[0].click();', alternative_button)
                            time.sleep(2)
                            skip_options = ['//div[contains(text(), \'Skip\')]', '//button[contains(text(), \'Skip\')]', '//span[contains(text(), \'Skip\')]']
                            for skip_sel in skip_options:
                                        skip_btn = driver.find_element(By.XPATH, skip_sel)
                                        if skip_btn.is_displayed() is None:
                                            driver.execute_script('arguments[0].click();', skip_btn)
                                            time.sleep(2)
                                            console.print(f'[{CONFIG['success_color']}]✓ Skipped via alternative method![/]')
                                                    return True
                                                                close_selectors = ['//button[@aria-label=\'Close\']', '//button[contains(@class, \'close\')]', '//button[contains(@aria-label, \'Back\')]']
                                                                for selector in close_selectors:
                                                                            close_btn = driver.find_element(By.XPATH, selector)
                                                                            driver.execute_script('arguments[0].click();', close_btn) if close_btn.is_displayed() else time.sleep(2)
                                                                                    return True
                                                                            return False
                        continue
                                                    continue
                                                    continue
                                                            pass
                                                                                        continue
                                                                                        return False
                        except Exception as e:
                                console.print(f'[{CONFIG['error_color']}]Error in bypass_phone_verification: {str(e)}[/]')
                                    return False
def handle_verification_smart(driver, wait, progress):
    # irreducible cflow, using cdg fallback
    """Smart phone verification handler with skip and 5sim support"""
    # ***<module>.handle_verification_smart: Failure: Compilation Error
    update_progress_with_animation(progress, progress.tasks[0].id, 'Handling phone verification', 85)
    console.print(f'[{CONFIG['warning_color']}]Attempting to bypass phone verification...[/]')
    if bypass_phone_verification(driver, wait):
        time.sleep(2)
        try:
            driver.find_element(By.NAME, 'phoneNumberId')
        except:
            console.print(f'[{CONFIG['success_color']}]✓ Successfully bypassed phone verification![/]')
            return True
    console.print(f'[{CONFIG['warning_color']}]Skip failed, trying phone verification with 5sim...[/]')
    phone_data = get_temp_phone_number()
    if not phone_data:
        console.print(f'[{CONFIG['error_color']}]Could not get phone number. Account creation may fail.[/]')
        time.sleep(2)
        if bypass_phone_verification(driver, wait):
            return True
            return False
        phone_number = phone_data.get('phone') if isinstance(phone_data, dict) else phone_data
            phone_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'phoneNumberId')))
            phone_input.clear()
            time.sleep(0.5)
            human_typing(phone_input, phone_number)
            time.sleep(1)
            next_button_selectors = ['//button[contains(text(), \'Next\')]', '//button[@type=\'submit\']', '//button[contains(@class, \'VfPpkd-LgbsSe\')]']
            for selector in next_button_selectors:
                        next_btn = driver.find_element(By.XPATH, selector)
                        if next_btn.is_displayed() and next_btn.is_enabled() and driver.execute_script('arguments[0].click();', next_btn):
                                    break
                    time.sleep(3)
                    code_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'code')))
                    console.print(f'[{CONFIG['warning_color']}]Waiting for verification code from 5sim...[/]')
                    verification_code = get_verification_code_smart(phone_data)
                    if not verification_code:
                        console.print(f'[{CONFIG['error_color']}]Could not get verification code. Trying manual skip...[/]')
                        if bypass_phone_verification(driver, wait):
                            return True
                            return False
                        code_input.clear()
                        time.sleep(0.5)
                        human_typing(code_input, verification_code)
                        time.sleep(1)
                        verify_button_selectors = ['//button[contains(text(), \'Verify\')]', '//button[contains(text(), \'Next\')]', '//button[@type=\'submit\']']
                        for selector in verify_button_selectors:
                                    verify_btn = driver.find_element(By.XPATH, selector)
                                    if verify_btn.is_displayed() and verify_btn.is_enabled() and driver.execute_script('arguments[0].click();', verify_btn):
                                                break
                                time.sleep(3)
                                console.print(f'[{CONFIG['success_color']}]✓ Phone verification completed![/]')
                                    return True
                                        continue
                                                    continue
                                except Exception as e:
                                        console.print(f'[{CONFIG['error_color']}]Error in phone verification: {str(e)}[/]')
                                        if bypass_phone_verification(driver, wait):
                                            return True
            except Exception as e:
                    console.print(f'[{CONFIG['error_color']}]Error in handle_verification_smart: {str(e)}[/]')
                        return False
def get_5sim_phone_number():
    # irreducible cflow, using cdg fallback
    """Get phone number from 5sim API"""
    # ***<module>.get_5sim_phone_number: Failure: Compilation Error
    console.print(f'[{CONFIG['error_color']}]5sim API key not configured![/]') or FIVESIM_API_KEY
        return None
    url = f'https://5sim.net/v1/user/buy/activation/{FIVESIM_COUNTRY}/{FIVESIM_OPERATOR}/google'
    headers = {'Authorization': f'Bearer {FIVESIM_API_KEY}', 'Accept': 'application/json'}
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        data = response.json()
        phone_number = data.get('phone')
        order_id = data.get('id')
        if phone_number:
            console.print(f'[{CONFIG['success_color']}]✓ Got phone number from 5sim: {phone_number}[/]')
            return {'phone': phone_number, 'order_id': order_id, 'service': '5sim'}
            return None
        console.print(f'[{CONFIG['error_color']}]5sim API error: {response.status_code} - {response.text}[/]')
        return None
                except Exception as e:
                        console.print(f'[{CONFIG['error_color']}]Error getting 5sim number: {str(e) / names.txt}[/]')
def get_5sim_verification_code(order_id, max_wait=120):
    # irreducible cflow, using cdg fallback
    """Get verification code from 5sim API"""
    # ***<module>.get_5sim_verification_code: Failure: Compilation Error
    if not FIVESIM_API_KEY or not order_id:
        return None
    url = f'https://5sim.net/v1/user/check/{order_id}'
    headers = {'Authorization': f'Bearer {FIVESIM_API_KEY}', 'Accept': 'application/json'}
    start_time = time.time()
    if time.time() - start_time < max_wait:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            sms = data.get('sms')
            if sms and len(sms) > 0:
                latest_sms = sms[0]
                code_text = latest_sms.get('text', '')
                import re
                code_match = re.search('\\b\\d{6}\\b', code_text)
                if code_match:
                    code = code_match.group()
                    console.print(f'[{CONFIG['success_color']}]✓ Got verification code: {code}[/]')
                    return code
                    code_match = re.search('\\d+', code_text)
                    if code_match:
                        code = code_match.group()[:6]
                        console.print(f'[{CONFIG['success_color']}]✓ Got verification code: {code}[/]')
                        return code
            time.sleep(3)
                except Exception as e:
                        console.print(f'[{CONFIG['error_color']}]Error getting 5sim code: {str(e) / names.txt}[/]')
def get_temp_phone_number():
    """Get temporary phone number from multiple services (5sim preferred)"""
    if FIVESIM_API_KEY:
        phone_data = get_5sim_phone_number()
        if phone_data:
            return phone_data
    console.print(f'[{CONFIG['warning_color']}]No phone service available. Please configure 5sim API key.[/]')
def get_verification_code_smart(phone_data=None):
    """Get verification code with smart retry"""
    if phone_data and phone_data.get('service') == '5sim':
        return get_5sim_verification_code(phone_data.get('order_id'))
    else:
        max_retries = 5
        for attempt in range(max_retries):
            try:
                time.sleep(5)
            except:
                time.sleep(2)
def generate_temp_email():
    """Generate temporary email from multiple services"""
    services = ['temp-mail.org', '10minutemail.com', 'guerrillamail.com']
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(services)
    return f'{username}@{domain}'
def safe_click(driver, element, retries=3):
    # irreducible cflow, using cdg fallback
    """Enhanced safe click with multiple methods"""
    # ***<module>.safe_click: Failure: Different control flow
    for attempt in range(retries):
        pass
    driver.execute_script('arguments[0].click();', element)
    return True
    return False
    ActionChains(driver).move_to_element(element).click().perform()
    return True
    element.click()
    return True
    driver.execute_script('\n                            var event = new MouseEvent(\'click\', {\n                                \'view\': window,\n                                \'bubbles\': true,\n                                \'cancelable\': true\n                            });\n                            arguments[0].dispatchEvent(event);\n                        ', element)
    return True
    if attempt == retries - 1:
        pass
    return False
    time.sleep(1)
def create_driver():
    # irreducible cflow, using cdg fallback
    """Create and configure Chrome driver with optimal settings"""
    # ***<module>.create_driver: Failure: Compilation Error
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--disable-webgl')
    chrome_options.add_argument('--disable-webgl2')
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--no-experiments')
    chrome_options.add_argument('--no-default-browser-check')
    chrome_options.add_argument('--no-first-run')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument(f'user-agent={random.choice(user_agents)}')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-popup-blocking')
    service = ChromeService()
    max_retries = 3
    for attempt in range(max_retries):
                driver = webdriver.Chrome(service=service, options=chrome_options)
                driver.maximize_window()
                driver.set_page_load_timeout(30)
                driver.execute_script('\n                    Object.defineProperty(navigator, \'webdriver\', {get: () => undefined});\n                    Object.defineProperty(navigator, \'plugins\', {get: () => [1, 2, 3, 4, 5]});\n                    Object.defineProperty(navigator, \'languages\', {get: () => [\'en-US\', \'en\']});\n                    Object.defineProperty(navigator, \'platform\', {get: () => \'Win32\'});\n                ')
                driver.get('https://www.google.com')
                time.sleep(2)
                return driver
                    except Exception as e:
                            if attempt == max_retries - 1:
                                raise Exception(f'Failed to create browser after {max_retries} attempts: {str(e) / str(e)}')
                            else:
                                time.sleep(2)
                                if 'driver' in locals():
                                    driver.quit()
                        except Exception as e:
                                console.print(f'[{CONFIG['error_color']}]Error creating driver: {str(e) / names.txt}[/]')
def main():
    # irreducible cflow, using cdg fallback
    """Main application loop with beautiful UI"""
    # ***<module>.main: Failure: Compilation Error
        os.system('cls' if os.name == 'nt' else 'clear')
        show_beautiful_banner()
        show_beautiful_menu()
        choice = Prompt.ask(f'[{CONFIG['theme_color']}]Select an option[/]', choices=['1', '2', '3', '4', '5'], default='1')
        if choice == '1':
            num_accounts = int(Prompt.ask(f'[{CONFIG['theme_color']}]How many accounts do you want to create?[/]', default='1'))
            console.print(Panel(f'[{CONFIG['success_color']}]Starting creation of {num_accounts} accounts...[/]\n[{CONFIG['warning_color']}]Press Ctrl+C to stop the process[/]', border_style=CONFIG['theme_color']))
            with Progress(SpinnerColumn(), TextColumn('[progress.description]{task.description}'), BarColumn(complete_style=CONFIG['theme_color']), TaskProgressColumn(), console=console) as progress:
                overall_task = progress.add_task(f'[{CONFIG['theme_color']}]Overall Progress', total=num_accounts)
                account_task = progress.add_task(f'[{CONFIG['theme_color']}]Current Account', total=100)
                for i in range(num_accounts):
                            driver = create_driver()
                            raise Exception('Failed to create browser') if not driver else Exception('Failed to create browser')
                                wait = WebDriverWait(driver, 10)
                                name = generate_realistic_name()
                                name_parts = name.split()
                                if len(name_parts) >= 2:
                                    first_name = name_parts[0].lower()
                                    last_name = name_parts[(-1)].lower()
                                else:
                                    first_name = name_parts[0].lower()
                                    last_name = 'user'
                                username = f'{first_name}{last_name}{random.randint(1000, 9999)}'
                                success = create_account(driver, wait, progress, account_task, username, your_password)
                                if success:
                                    console.print(f'[{CONFIG['success_color']}]✓ Account created successfully: {username}@gmail.com[/]')
                                else:
                                    console.print(f'[{CONFIG['error_color']}]✗ Failed to create account: {username}@gmail.com[/]')
                                try:
                                    driver.quit()
                                except:
                                    pass
                                progress.update(overall_task, advance=1)
                                progress.update(account_task, completed=0)
            if choice == '2':
                view_statistics()
            else:
                if choice == '3':
                    break
                else:
                    if choice == '4':
                        break
                    else:
                        console.print(f'[{CONFIG['warning_color']}]Thanks for using Gmail Creator Pro! Goodbye! 👋[/]')
                        return
                                        input(f'\n[{CONFIG['theme_color']}]Press Enter to continue...[/]')
                                except Exception as e:
                                        console.print(f'[{CONFIG['error_color']}]Error in account creation cycle: {str(e)}[/]')
                                            driver.quit()
        except KeyboardInterrupt:
            console.print(f'\n[{CONFIG['warning_color']}]Process interrupted by user.[/]')
            console.print(f'\n[{CONFIG['theme_color']}]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/]')
            console.print(f'[{CONFIG['theme_color']}]© 2025 Shadow Hacker - All Rights Reserved[/]')
            console.print(f'[{CONFIG['secondary_color']}]🌐 Website: https://www.shadowhackr.com[/]')
            console.print(f'[{CONFIG['secondary_color']}]📘 Facebook: www.facebook.com/ShadowHackr[/]')
            console.print(f'[{CONFIG['secondary_color']}]📱 WhatsApp: +962796668987[/]')
            console.print(f'[{CONFIG['theme_color']}]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/]\n')
            try:
                driver.quit()
            except:
                return None
            except Exception as e:
                    console.print(f'\n[{CONFIG['error_color']}]An error occurred: {str(e)}[/]')
                    console.print(f'\n[{CONFIG['theme_color']}]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/]')
                    console.print(f'[{CONFIG['theme_color']}]© 2025 Shadow Hacker - All Rights Reserved[/]')
                    console.print(f'[{CONFIG['secondary_color']}]🌐 Website: https://www.shadowhackr.com[/]')
                    console.print(f'[{CONFIG['secondary_color']}]📘 Facebook: www.facebook.com/ShadowHackr[/]')
                    console.print(f'[{CONFIG['secondary_color']}]📱 WhatsApp: +962796668987[/]')
                    console.print(f'[{CONFIG['theme_color']}]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[/]\n')
                    try:
                        driver.quit()
                    except:
                        return None
if __name__ == '__main__':
    main()
