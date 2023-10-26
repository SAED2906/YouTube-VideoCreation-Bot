from PIL import Image, ImageEnhance
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

# Config
screenshotDir = "Screenshots"
screenWidth = 400
screenHeight = 800


def getPostScreenshots(filePrefix, script):
    print("Taking screenshots...")
    driver, wait = __setupDriver(script.url)
    script.titleSCFile = __takeScreenshot(filePrefix, driver, wait)
    for commentFrame in script.frames:
        commentFrame.screenShotFile = __takeScreenshot(
            filePrefix, driver, wait, f"t1_{commentFrame.commentId}")
    driver.quit()


def __takeScreenshot(filePrefix, driver, wait, handle="Post"):
    method = By.CLASS_NAME if (handle == "Post") else By.ID
    search = wait.until(EC.presence_of_element_located((method, handle)))
    driver.execute_script("window.focus();")

    fileName = f"{screenshotDir}/{filePrefix}-{handle}.png"
    fp = open(fileName, "wb")
    fp.write(search.screenshot_as_png)
    fp.close()
    change_opacity(fileName)
    return fileName


def __setupDriver(url: str):
    options = webdriver.FirefoxOptions()
    options.headless = False
    options.enable_mobile = False
    profile_path = "C:/Users/*YOU*/AppData/Roaming/Mozilla/Firefox/Profiles/6ze46et0.Reddit"
    firefox_profile = FirefoxProfile(profile_path)
    driver = webdriver.Firefox(
        firefox_profile=firefox_profile, options=options)
    wait = WebDriverWait(driver, 10)

    driver.set_window_size(width=screenWidth, height=screenHeight)
    driver.get(url)

    return driver, wait


def change_opacity(input_image_path):
    image = Image.open(input_image_path).convert('RGBA')
    alpha = image.split()[3]
    enhancer = ImageEnhance.Brightness(alpha)
    new_alpha = enhancer.enhance(0.8)
    new_image = Image.merge('RGBA', image.split()[:3] + (new_alpha,))
    new_image.save(input_image_path)
