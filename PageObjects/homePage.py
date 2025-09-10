from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver

class HomePage:

    build_your_computer=(By.XPATH,"//a[text()='Build your own computer']")
    apple_macbook_pro=(By.XPATH,"//a[text()='Apple MacBook Pro']")
    htc_smartphone=(By.XPATH,"//a[text()='HTC smartphone']")
    virtual_gift_card=(By.XPATH,"//a[text()='$25 Virtual Gift Card']")
    build_your_computer_compare_button=( By.XPATH,"//div[@data-productid='1']//button[text()='Add to compare list']")
    apple_macbook_pro_compare_button=(By.XPATH,"//div[@data-productid='4']//button[text()='Add to compare list']")
    htc_smartphone_compare_button=(By.XPATH,"//div[@data-productid='18']//button[text()='Add to compare list']")
    virtual_gift_card_compare_button=(By.XPATH,"//div[@data-productid='45']//button[text()='Add to compare list']")
    successful_compare_message=(By.XPATH,"//div[@class='bar-notification success']/p")
    build_your_computer_heading=(By.XPATH,"//h1[text()='Build your own computer']")
    apple_macbook_pro_heading=(By.XPATH,"//h1[text()='Apple MacBook Pro']")
    successful_added_to_cart=(By.XPATH,"//div[@id='bar-notification']")
    virtual_gift_card_heading=(By.XPATH,"//h1[text()='$25 Virtual Gift Card']")
    build_your_computer_cart_button=(By.XPATH,"//div[@data-productid='1']//button[text()='Add to cart']")
    apple_macbook_pro_cart_button=(By.XPATH,"//div[@data-productid='4']//button[text()='Add to cart']")
    htc_smartphone_cart_button=(By.XPATH,"//div[@data-productid='18']//button[text()='Add to cart']")
    virtual_gift_card_cart_button=(By.XPATH,"//div[@data-productid='45']//button[text()='Add to cart']")
    successful_wishlist_message=(By.XPATH,"//div[@class='bar-notification success']/p")
    build_your_computer_wishlist_button=(By.XPATH,"//div[@data-productid='1']//button[text()='Add to wishlist']")
    apple_macbook_pro_wishlist_button=(By.XPATH,"//div[@data-productid='4']//button[text()='Add to wishlist']")
    htc_smartphone_wishlist_button=(By.XPATH,"//div[@data-productid='18']//button[text()='Add to wishlist']")
    virtual_gift_card_wishlist_button=(By.XPATH,"//div[@data-productid='45']//button[text()='Add to wishlist']")
    welcome_store_title=(By.CSS_SELECTOR,"div.topic-block-title")
    welcome_store_body=(By.CSS_SELECTOR,"div.topic-block-body")
    documentation_link=(By.CSS_SELECTOR,"a[href='http://docs.nopcommerce.com/']")
    documentation_link_heading=(By.CSS_SELECTOR,"h1#nopcommerce-documentation")
    forums_link=(By.CSS_SELECTOR,"a[href='https://www.nopcommerce.com/boards/']")
    forums_link_heading=(By.CSS_SELECTOR,"div.page-title")
    nopCommerce_link=(By.CSS_SELECTOR,"a[href='https://www.nopcommerce.com']")
    nopCommerce_link_heading=(By.XPATH,"//h1[text()='Free and open-source eCommerce platform']")
    electronics_title=(By.XPATH,"//a[text()=' Electronics ']")
    apparel_title=(By.XPATH,"//a[text()=' Apparel ']")
    digital_downloads_title=(By.XPATH,"//a[text()=' Digital downloads ']")
    electronics_image=(By.CSS_SELECTOR,"img[alt='Picture for category Electronics']")
    apparel_image=(By.CSS_SELECTOR,"img[alt='Picture for category Apparel']")
    digital_downloads_image=(By.CSS_SELECTOR,"img[alt='Picture for category Digital downloads']")
    electronics_apparel_digital_heading=(By.CSS_SELECTOR,"div.page-title")

    def __init__(self,driver:WebDriver):
        self.driver=driver

    def build_your_computer_text(self):
        # text=self.driver.find_element(*self.build_your_computer).text
        return self.driver.find_element(*self.build_your_computer).is_displayed()

    def apple_macbook_pro_text(self):
        return self.driver.find_element(*self.apple_macbook_pro).is_displayed()

    def htc_smartphone_text(self):
        return self.driver.find_element(*self.htc_smartphone).is_displayed()

    def virtual_gift_card_text(self):
        return self.driver.find_element(*self.virtual_gift_card).is_displayed()

    def build_your_computer_click(self):
        self.driver.find_element(*self.build_your_computer).click()

    def apple_macbook_pro_click(self):
        self.driver.find_element(*self.apple_macbook_pro).click()

    def htc_smartphone_click(self):
        self.driver.find_element(*self.htc_smartphone).click()

    def virtual_gift_card_click(self):
        self.driver.find_element(*self.virtual_gift_card).click()

    def build_your_own_computer_url(self):
        self.build_your_computer_click()
        return self.driver.current_url

    def apple_macbook_pro_url(self):
        self.apple_macbook_pro_click()
        return self.driver.current_url

    def htc_smartphone_url(self):
        self.htc_smartphone_click()
        return self.driver.current_url

    def virtual_gift_card_url(self):
        self.virtual_gift_card_click()
        return self.driver.current_url

    # def compare_message(self):
    #     wait=WebDriverWait(self.driver,10)
    #     message=wait.until(EC.visibility_of_element_located(self.successful_compare_message))
    #     # return self.driver.find_element(*self.successful_compare_message).is_displayed()
    #     return message.is_displayed()

    def compare_message(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            message = wait.until(EC.presence_of_element_located(self.successful_compare_message))
            return message.is_displayed()
        except:
            return False

    def build_your_computer_compare_click(self):
        self.driver.find_element(*self.build_your_computer_compare_button).click()
        # return self.driver.find_element(*self.successful_compare_message).is_displayed()
        return self.compare_message()

    def apple_macbook_pro_compare_click(self):
        self.driver.find_element(*self.apple_macbook_pro_compare_button).click()
        return self.compare_message()

    def htc_smartphone_compare_click(self):
        self.driver.find_element(*self.htc_smartphone_compare_button).click()
        return self.compare_message()

    def virtual_gift_card_compare_click(self):
        self.driver.find_element(*self.virtual_gift_card_compare_button).click()
        return self.compare_message()

    # def added_to_cart_message(self):
    #     wait=WebDriverWait(self.driver,10)
    #     message=wait.until(EC.visibility_of_element_located(self.successful_added_to_cart))
    #     return message.is_displayed()
    def added_to_cart_message(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            message = wait.until(EC.visibility_of_element_located(self.successful_added_to_cart))
            return message.is_displayed()
        except:
            return False

    def build_your_own_computer_cart_click(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.build_your_computer_cart_button)).click()

    def build_your_own_computer_cart_click_header(self):
        self.build_your_own_computer_cart_click()
        return self.driver.find_element(*self.build_your_computer_heading).is_displayed()

    def apple_macbook_pro_cart_click(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.apple_macbook_pro_cart_button)).click()

    def apple_macbook_pro_cart_click_header(self):
        self.apple_macbook_pro_cart_click()
        return self.driver.find_element(*self.apple_macbook_pro_heading).is_displayed()

    def htc_smartphone_cart_click(self):
        self.driver.find_element(*self.htc_smartphone_cart_button).click()
        return self.added_to_cart_message()

    def virtual_gift_card_cart_click(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.virtual_gift_card_cart_button)).click()

    def virtual_gift_card_cart_click_header(self):
        self.virtual_gift_card_cart_click()
        return self.driver.find_element(*self.virtual_gift_card_heading).is_displayed()

    def wishlist_message(self):
        wait=WebDriverWait(self.driver,10)
        try:
            message=wait.until(EC.presence_of_element_located(self.successful_wishlist_message))
            return message.is_displayed()
        except:
            assert False

    def build_your_own_computer_wishlist_click(self):
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable(self.build_your_computer_wishlist_button)).click()

    def build_your_own_computer_wishlist_header(self):
        self.build_your_own_computer_wishlist_click()
        wait=WebDriverWait(self.driver,10)
        message=wait.until(EC.presence_of_element_located(self.build_your_computer_heading))
        return message.is_displayed()
        # return self.driver.find_element(*self.build_your_computer_heading).is_displayed()

    def apple_macbook_pro_wishlist_click(self):
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable(self.apple_macbook_pro_wishlist_button)).click()

    def apple_macbook_pro_wishlist_header(self):
        self.apple_macbook_pro_wishlist_click()
        wait=WebDriverWait(self.driver,10)
        message=wait.until(EC.presence_of_element_located(self.apple_macbook_pro_heading))
        return message.is_displayed()
        # return self.driver.find_element(*self.apple_macbook_pro_heading).is_displayed()

    def htc_smartphone_wishlist_click(self):
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable(self.htc_smartphone_wishlist_button)).click()
        return self.successful_wishlist_message

    def virtual_gift_card_wishlist_click(self):
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable(self.virtual_gift_card_wishlist_button)).click()

    def virtual_gift_card_wishlist_header(self):
        self.virtual_gift_card_wishlist_click()
        wait=WebDriverWait(self.driver,10)
        message=wait.until(EC.presence_of_element_located(self.virtual_gift_card_heading))
        return message.is_displayed()
        # return self.driver.find_element(*self.virtual_gift_card_heading).is_displayed()

    def welcome_store_title_text(self):
        return self.driver.find_element(*self.welcome_store_title).is_displayed()

    def welcome_store_body_text(self):
        return self.driver.find_element(*self.welcome_store_body).is_displayed()

    def documentation_link_click(self):
        self.driver.find_element(*self.documentation_link).click()

    def documentation_link_header(self):
        self.documentation_link_click()
        return self.driver.find_element(*self.documentation_link_heading).is_displayed()

    def forums_link_click(self):
        self.driver.find_element(*self.forums_link).click()

    def forums_link_header(self):
        self.forums_link_click()
        return self.driver.find_element(*self.forums_link_heading).is_displayed()

    def nopCommerce_link_click(self):
        self.driver.find_element(*self.nopCommerce_link).click()

    def nopCommerce_link_header(self):
        self.nopCommerce_link_click()
        return self.driver.find_element(*self.nopCommerce_link_heading).is_displayed()

    def electronics_title_text(self):
        return self.driver.find_element(*self.electronics_title).is_displayed()

    def apparel_title_text(self):
        return self.driver.find_element(*self.apparel_title).is_displayed()

    def digital_downloads_title_text(self):
        return self.driver.find_element(*self.digital_downloads_title).is_displayed()

    def electronics_image_display(self):
        return self.driver.find_element(*self.electronics_image).is_displayed()

    def apparel_image_display(self):
        return self.driver.find_element(*self.apparel_image).is_displayed()

    def digital_downloads_image_display(self):
        return self.driver.find_element(*self.digital_downloads_image).is_displayed()

    def electronics_title_click(self):
        self.driver.find_element(*self.electronics_title).click()

    def electronics_image_click(self):
        self.driver.find_element(*self.electronics_image).click()

    def electronics_apparel_digital_header(self):
        return self.driver.find_element(*self.electronics_apparel_digital_heading).is_displayed()

    def electronics_title_header(self,click_type="title"):
        # self.electronics_title_click()
        if click_type.lower() == "title":
            self.electronics_title_click()
        elif click_type.lower() == "image":
            self.electronics_image_click()
        return self.electronics_apparel_digital_header()

    def apparel_title_click(self):
        self.driver.find_element(*self.apparel_title).click()

    def apparel_image_click(self):
        self.driver.find_element(*self.apparel_image).click()

    def apparel_title_header(self,click_type="title"):
        # self.apparel_title_click()
        if click_type.lower() == "title":
            self.apparel_title_click()
        elif click_type.lower() == "image":
            self.apparel_image_click()
        return self.electronics_apparel_digital_header()

    def digital_downloads_title_click(self):
        self.driver.find_element(*self.digital_downloads_title).click()

    def digital_downloads_image_click(self):
        self.driver.find_element(*self.digital_downloads_image).click()

    def digital_downloads_title_header(self,click_type="title"):
        # self.digital_downloads_title_click()
        if click_type.lower() == "title":
            self.digital_downloads_title_click()
        elif click_type.lower() == "image":
            self.digital_downloads_image_click()
        return self.electronics_apparel_digital_header()