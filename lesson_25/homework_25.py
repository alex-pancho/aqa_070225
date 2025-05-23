import requests
from lxml import html 
"""
Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
"""

username = "guest"
passwd = "welcome2qauto"
url = f"https://{username}:{passwd}@qauto2.forstudy.space"

class Locators:
    HOME_BUTTON_XPATH = "//a[text() = 'Home']" 
    ABOUT_BUTTON_XPATH = "//button[@appscrollto='aboutSection']"
    CONTACTS_BUTTON_XPATH = '//button[@appscrollto="contactsSection"]' 
    GUEST_LOG_IN_XPATH = '//button[@class="header-link -guest"]'
    SIGN_IN_BUTTON_XPATH = '//button[@class="btn btn-outline-white header_signin"]' 
    LOGIN_EMAIL_INPUT_FIELD_XPATH = '//input[@id="signinEmail"]'
    LOGIN_PASSWORD_INPUT_FIELD_XPATH = '//input[@id="signinPassword"]' 
    LOGIN_REMEMBER_ME_CHECKBOX_XPATH = '//input[@id="remember"]'
    LOGIN_FORGOT_PASSWORD_XPATH = '//button[.="Forgot password"]'
    LOGIN_REGISTRATION_BUTTON_XPATH = '//button[.="Registration"]'
    LOGIN_LOGIN_BUTTON_XPATH = '//button[.="Login"]'
    GUEST_ADD_CAR_BUTTON_XPATH = '//button[.="Add car"]'
    ADD_CAR_BRAND_DROP_DOWN_XPATH = '//select[@id="addCarBrand"]'
    ADD_CAR_BRAND_DROP_DOWN_VALUE_XPATH = '//option[.="Audi"]'
    ADD_CAR_MILEAGE_INPUT_XPATH = '//input[@id="addCarMileage"]'
    ADD_CAR_MODEL_DROP_DOWN_XPATH = '//select[@id="addCarModel"]'
    ADD_CAR_CANCEL_BUTTON_XPATH = '//button[.="Cancel"]'
    ADD_CAR_ADD_BUTTON_XPATH = '//button[.="Add"]'
    ADD_FUEL_EXPENSE_BUTTON_XPATH = '//button[.="Add fuel expense"]'
    UPDATE_MILAGE_XPATH = '//p[.="Update mileage • 23.05.2025"]'
    PAGE_TITLE_XPATH = '//h1[@class="hero-descriptor_title display-2"]'
    SIGN_UP_BUTTON_XPATH = '//button[@class="hero-descriptor_btn btn btn-primary"]'
    HILLEL_LINK_XPATH = '//a[@href="https://ithillel.ua"]'
    CALENDAR_ICON_XPATH = '//span[@class="icon icon-calendar"]'
    SUPPORT_EMAIL_XPATH = '//a[@href="mailto:developer@ithillel.ua"]'
    CONTACTS_FACEBOOK_BUTTON_XPATH = '//span[@class="socials_icon icon icon-facebook"]'
    
    HOME_BUTTON_CSS = "a.btn header-link -active"
    ABOUT_BUTTON_CSS = "button[appscrollto='aboutSection']"
    CONTACTS_BUTTON_CSS = 'button[appscrollto="contactsSection"]'
    GUEST_LOG_IN_CSS =  'button.header-link -guest'
    SIGN_IN_BUTTON_CSS = 'button.btn btn-outline-white header_signin'
    LOGIN_EMAIL_INPUT_FIELD_CSS = 'input#signinEmail'
    LOGIN_PASSWORD_INPUT_FIELD_CSS = 'input#signinPassword"]'
    LOGIN_REMEMBER_ME_CHECKBOX_CSS = 'input#remember'
    LOGIN_FORGOT_PASSWORD_CSS = 'button.btn btn-link'
    LOGIN_REGISTRATION_BUTTON_CSS = 'button.btn.btn-link[type="button"]'
    LOGIN_LOGIN_BUTTON_CSS = 'button[class="btn btn-primary"]'
    ADD_CAR_BRAND_DROP_DOWN_CSS = 'select#addCarBrand'
    ADD_CAR_MILEAGE_INPUT_CSS= 'input#addCarMileage'
    ADD_CAR_MODEL_DROP_DOWN_CSS = 'select#id="addCarModel'
    ADD_CAR_CANCEL_BUTTON_CSS = 'select#addCarModel'
    ADD_FUEL_EXPENSE_BUTTON_CSS = 'button[class="car_add-expense btn btn-success"]'
    UPDATE_MILAGE_CSS = 'p[class="car_update-mileage"]'
    PAGE_TITLE_CSS = 'h1.hero-descriptor_title display-2'
    SIGN_UP_BUTTON_CSS = 'button#hero-descriptor_btn btn btn-primary'
    HILLEL_LINK_CSS = 'a[href="https://ithillel.ua"]'
    CALENDAR_ICON_CSS = 'span.icon icon-calendar'
    SUPPORT_EMAIL_CSS = 'a[href="mailto:developer@ithillel.ua"]'
    CONTACTS_FACEBOOK_BUTTON_CSS = 'span#socials_icon icon icon-facebook'
    
    
    
   
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    