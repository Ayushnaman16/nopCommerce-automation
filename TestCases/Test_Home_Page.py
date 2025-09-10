from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.homePage import HomePage
import os

class Test_HomePage:

    def test_012(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)
        # self.hp.build_your_computer_text()

        if self.hp.build_your_computer_text():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_012.png")
            self.driver.close()
            assert False

    def test_013(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.build_your_own_computer_url()=="https://demo.nopcommerce.com/build-your-own-computer":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_013.png")
            self.driver.close()
            assert False

    def test_014(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        self.driver.implicitly_wait(5)

        if self.hp.build_your_own_computer_cart_click_header():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_014.png")
            self.driver.close()
            assert False

    def test_015(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.build_your_computer_compare_click():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_015.png")
            self.driver.close()
            assert False

    def test_016(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.build_your_own_computer_wishlist_header():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_016.png")
            self.driver.close()
            assert False

    def test_017(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)
        # self.hp.build_your_computer_text()

        if self.hp.apple_macbook_pro_text():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_012.png")
            self.driver.close()
            assert False

    def test_018(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.apple_macbook_pro_url()=="https://demo.nopcommerce.com/apple-macbook-pro":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_013.png")
            self.driver.close()
            assert False

    def test_019(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        self.driver.implicitly_wait(5)

        if self.hp.apple_macbook_pro_cart_click_header():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_019.png")
            self.driver.close()
            assert False

    def test_020(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.apple_macbook_pro_compare_click():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_019.png")
            self.driver.close()
            assert False

    def test_021(self, setup):
        self.driver = setup

        self.hp = HomePage(self.driver)

        if self.hp.apple_macbook_pro_wishlist_header():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_021.png")
            self.driver.close()
            assert False

    def test_022(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)
        # self.hp.build_your_computer_text()

        if self.hp.htc_smartphone_text():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_022.png")
            self.driver.close()
            assert False

    def test_023(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.htc_smartphone_url()=="https://demo.nopcommerce.com/htc-smartphone":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_013.png")
            self.driver.close()
            assert False

    def test_024(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        self.driver.implicitly_wait(5)

        if self.hp.htc_smartphone_cart_click():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_024.png")
            self.driver.close()
            assert False

    def test_025(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.htc_smartphone_compare_click():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_024.png")
            self.driver.close()
            assert False

    def test_026(self, setup):
        self.driver = setup

        self.hp = HomePage(self.driver)

        if self.hp.htc_smartphone_wishlist_click():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_026.png")
            self.driver.close()
            assert False

    def test_027(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)
        # self.hp.build_your_computer_text()

        if self.hp.virtual_gift_card_text():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_027.png")
            self.driver.close()
            assert False

    def test_028(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.virtual_gift_card_url()=="https://demo.nopcommerce.com/25-virtual-gift-card":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_013.png")
            self.driver.close()
            assert False

    def test_029(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        self.driver.implicitly_wait(5)

        if self.hp.virtual_gift_card_cart_click_header():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_014.png")
            self.driver.close()
            assert False

    def test_030(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.virtual_gift_card_compare_click():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir+"\\ScreenShots\\test_029.png")
            self.driver.close()
            assert False

    def test_031(self, setup):
        self.driver = setup

        self.hp = HomePage(self.driver)

        if self.hp.virtual_gift_card_wishlist_header():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_031.png")
            self.driver.close()
            assert False

    def test_040(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.welcome_store_title_text():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_040.png")
            self.driver.close()
            assert False

    def test_041(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.welcome_store_body_text():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_041.png")
            self.driver.close()
            assert False

    def test_042(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.documentation_link_header():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_042.png")
            self.driver.close()
            assert False

    def test_043(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.forums_link_header():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_043.png")
            self.driver.close()
            assert False

    def test_044(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.nopCommerce_link_header():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_044.png")
            self.driver.close()
            assert False

    def test_045(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.electronics_title_text():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_045.png")
            self.driver.close()
            assert False

    def test_046(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.electronics_title_header("title"):
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_046.png")
            self.driver.close()
            assert False

    def test_047(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.electronics_image_display():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_047.png")
            self.driver.close()
            assert False

    def test_048(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.electronics_title_header("image"):
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_048.png")
            self.driver.close()
            assert False

    def test_049(self, setup):
        self.driver = setup

        self.hp = HomePage(self.driver)

        if self.hp.apparel_title_text():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_049.png")
            self.driver.close()
            assert False

    def test_050(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.apparel_title_header("title"):
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_050.png")
            self.driver.close()
            assert False

    def test_051(self, setup):
        self.driver = setup

        self.hp = HomePage(self.driver)

        if self.hp.apparel_image_display():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_051.png")
            self.driver.close()
            assert False

    def test_052(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.electronics_title_header("image"):
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_052.png")
            self.driver.close()
            assert False

    def test_053(self, setup):
        self.driver = setup

        self.hp = HomePage(self.driver)

        if self.hp.digital_downloads_title_text():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_053.png")
            self.driver.close()
            assert False

    def test_054(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.digital_downloads_title_header("title"):
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_054.png")
            self.driver.close()
            assert False

    def test_055(self, setup):
        self.driver = setup

        self.hp = HomePage(self.driver)

        if self.hp.digital_downloads_image_display():
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_055.png")
            self.driver.close()
            assert False

    def test_056(self,setup):
        self.driver=setup

        self.hp=HomePage(self.driver)

        if self.hp.electronics_title_header("image"):
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot(os.curdir + "\\ScreenShots\\test_056.png")
            self.driver.close()
            assert False