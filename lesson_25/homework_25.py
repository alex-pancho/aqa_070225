import requests

"""
Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
"""

username = "guest"
passwd = "welcome2qauto"
url = f"https://{username}:{passwd}@qauto2.forstudy.space"

header_contacts = '//div[@class="section contacts"] //text()[.="Contacts"]'
p_year = '//footer //p[.="© 2021 Hillel IT school"]'
contact_link_hillel = '//a[@class="contacts_link display-4"="https://ithillel.ua"]'
contact_link_mail = '//a[@class="contacts_link h4"="mailto:developer@ithillel.ua"]'
button_sign_up = '//section[@class="section hero"] //button[.="Sign up"]'
button_sign_in = '//div[@class="header_right d-flex align-items-center"] //button[.="Sign In"]'
button_guest_log_in = '//div[@class="header_right d-flex align-items-center"] //button[.="Guest log in"]'
logo = '//header //a[@class="header_logo"]'
link_home = '//header //a[@class="btn header-link -active"]'
button_about = '//header //button[.="About"]'
button_contacts = '//header //button[.="Contacts"]'
footer_logo = '//footer //a[@class="footer_logo"]'
facebook_icon = '//span[@class="socials_icon icon icon-facebook"]'
telegram_icon = '//span[@class="socials_icon icon icon-telegram"]'
youtube_icon = '//span[@class="socials_icon icon icon-youtube"]'
instagram_icon = '//span[@class="socials_icon icon icon-instagram"]'
linkedin_icon = '//span[@class="socials_icon icon icon-linkedin"]'
p_auto_developed = ('//footer //text()[.="Hillel auto developed in Hillel IT school for '
                    'educational purposes of QA courses."]')
p_about_block_title_1 = '//div[@class="about-block"] //text()[.="Log fuel expenses"]'
p_about_block_descr_1 = ('//div[@class="about-block"] //text()[.="Keep track of your replacement schedule and '
                         'plan your vehicle maintenance expenses in advance."]')
p_about_block_title_2 = '//div[@class="about-block"] //text()[.="Instructions and manuals"]'
p_about_block_descr_2 = ('//div[@class="about-block"] //text()[.="Watch over 100 instructions and repair your car '
                         'yourself."]')
img_about_info_1 = '//img[@class="about-picture_img"][@src="/assets/images/homepage/info_1.jpg"]'
img_about_info_2 = '//img[@class="about-picture_img"][@src="/assets/images/homepage/info_2.jpg"]'
div_youtube_thumbnail = '//div[@id="player"] //div[@class="ytp-cued-thumbnail-overlay-image"]'

header_contacts_css = '#contactsSection h2:first-child'
p_year_css = 'div.footer_item p:first-child'
contact_link_hillel_css = '#contactsSection .row :last-child a.contacts_link[href="https://ithillel.ua"]'
contact_link_mail_css = '#contactsSection .row :last-child a.contacts_link[href="mailto:developer@ithillel.ua"]'
button_sign_up_css = 'app-home section.section.hero .hero-descriptor button.hero-descriptor_btn'
button_sign_in_css = 'header .header_right button.header_signin'
button_guest_log_in_css = 'header .header_right button.header-link.-guest'
logo_css = 'header a.header_logo'
link_home_css = 'header nav.header_nav a.header-link'
button_about_css = 'header nav.header_nav button.header-link[appscrollto="aboutSection"]'
button_contacts_css = 'header nav.header_nav button.header-link[appscrollto="contactsSection"]'
footer_logo_css = 'footer .footer_item a.footer_logo'
facebook_icon_css = '#contactsSection .contacts_socials span.icon-facebook'
telegram_icon_css = '#contactsSection .contacts_socials span.icon-telegram'
youtube_icon_css = '#contactsSection .contacts_socials span.icon-youtube'
instagram_icon_css = '#contactsSection .contacts_socials span.icon-instagram'
linkedin_icon_css = '#contactsSection .contacts_socials span.icon-linkedin'
p_auto_developed_css = 'div.footer_item p:nth-child(2)'
p_about_block_title_1_css = '#aboutSection .row :first-child .about-block p.about-block_title'
p_about_block_descr_1_css = '#aboutSection .row :first-child .about-block p.about-block_descr'
p_about_block_title_2_css = '#aboutSection .row :last-child .about-block p.about-block_title'
p_about_block_descr_2_css = '#aboutSection .row :last-child .about-block p.about-block_descr'
img_about_info_1_css = '#aboutSection .row :first-child .about-block img.about-picture_img'
img_about_info_2_css = '#aboutSection .row :last-child .about-block img.about-picture_img'
div_youtube_thumbnail_css = '#player .ytp-cued-thumbnail-overlay button.ytp-button'
