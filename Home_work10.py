import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_position(2000, 600)
driver.maximize_window()

sites = "https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html"
driver.get(sites)

q1_element = driver.find_element(By.NAME, "q1")
q1_element.send_keys("k")

q2_element = driver.find_element(By.NAME, "q2")
q2_element.send_keys("13")

q3_element = driver.find_element(By.NAME, "q3")
q3_element.send_keys("9")

q4_element = driver.find_element(By.NAME, "q4")
q4_element.send_keys("15")

q5_element = driver.find_element(By.NAME, "q5")
q5_element.send_keys("8")

q6_element = driver.find_element(By.NAME, "q6")
q6_element.send_keys("256")

q7_element = driver.find_element(By.NAME, "q7")
q7_element.send_keys("0")

q8_element = driver.find_element(By.NAME, "q8")
q8_element.send_keys("3")

q9_element = driver.find_element(By.XPATH, '//input[@name="q9" and @value="b"]')

q9_element.click()

q10_element = driver.find_element(By.XPATH, '//input[@name="q10" and @value="a"]')
q10_element.click()

q11_element = driver.find_element(By.XPATH, '//input[@name="q11" and @value="d"]')
q11_element.click()

q12_element = driver.find_element(By.XPATH, '//input[@name="q12" and @value="a"]')
q12_element.click()

q13_element = driver.find_element(By.XPATH, '//input[@name="q13" and @value="a"]')
q13_element.click()

q14_element = driver.find_element(By.XPATH, '//input[@name="q14" and @value="d"]')
q14_element.click()

q15_element = driver.find_element(By.XPATH, '//input[@name="q15" and @value="c"]')
q15_element.click()

q16_element = driver.find_element(By.XPATH, '//input[@name="q16" and @value="c"]')
q16_element.click()

q17_element = driver.find_element(By.XPATH, '//input[@name="q17" and @value="a"]')
q17_element.click()

q18_element = driver.find_element(By.XPATH, '//input[@name="q18" and @value="b"]')
q18_element.click()

q19_b_element = driver.find_element(By.XPATH, '//input[@name="q19" and @value="e"]')
q19_b_element.click()

q20_b_element = driver.find_element(By.XPATH, '//input[@name="q20" and @value="a"]')
q20_b_element.click()

q21_b_element = driver.find_element(By.XPATH, '//input[@name="q21" and @value="d"]')
q21_b_element.click()

q22_b_element = driver.find_element(By.XPATH, '//input[@name="q22" and @value="c"]')
q22_b_element.click()

q23_b_element = driver.find_element(By.XPATH, '//input[@name="q23" and @value="d"]')
q23_b_element.click()

q24_b_element = driver.find_element(By.XPATH, '//input[@name="q24" and @value="c"]')
q24_b_element.click()

q25_b_element = driver.find_element(By.XPATH, '//input[@name="q25" and @value="b"]')
q25_b_element.click()

q26_b_element = driver.find_element(By.XPATH, '//input[@name="q26" and @value="a"]')
q26_b_element.click()

q27_b_element = driver.find_element(By.XPATH, '//input[@name="q27" and @value="b"]')
q27_b_element.click()

q28_b_element = driver.find_element(By.XPATH, '//input[@name="q28" and @value="a"]')
q28_b_element.click()

q29_b_element = driver.find_element(By.XPATH, '//input[@name="q29" and @value="c"]')
q29_b_element.click()

q30_b_element = driver.find_element(By.XPATH, '//input[@name="q30" and @value="d"]')
q30_b_element.click()

q31_b_element = driver.find_element(By.XPATH, '//input[@name="q31" and @value="c"]')
q31_b_element.click()

q32_b_element = driver.find_element(By.XPATH, '//input[@name="q32" and @value="a"]')
q32_b_element.click()

q33_b_element = driver.find_element(By.XPATH, '//input[@name="q33" and @value="b"]')
q33_b_element.click()

finish_b_element = driver.find_element(By.XPATH, '//input[@type="BUTTON" and @value="FINISHED"]')
finish_b_element.click()

url = "https://test.mensa.no/"

driver.get(url)
age_1850 = driver.find_element(By.CLASS_NAME, 'ageselect_1850')
age_1850.click()
time.sleep(5)

start_test = driver.find_element(By.XPATH, '//*[@id="startTest"]')
start_test.click()
time.sleep(5)

exercise1 = driver.find_element(By.XPATH, '//*[@id="question_0"]/div[3]/div[5]/div/img')
exercise1.click()
time.sleep(1)

exercise2 = driver.find_element(By.XPATH, '//*[@id="question_1"]/div[3]/div[5]/div/img')
exercise2.click()
time.sleep(5)

exercise3 = driver.find_element(By.XPATH, '//*[@id="question_2"]/div[3]/div[3]/div')
exercise3.click()
time.sleep(5)

exercise4 = driver.find_element(By.XPATH, '//*[@id="question_3"]/div[3]/div[5]/div/img')
exercise4.click()
time.sleep(5)

exercise5 = driver.find_element(By.XPATH, '//*[@id="question_4"]/div[3]/div[6]/div/img')
exercise5.click()
time.sleep(5)

exercise6 = driver.find_element(By.XPATH, '//*[@id="question_5"]/div[3]/div[1]/div/img')
exercise6.click()
time.sleep(5)

exercise7 = driver.find_element(By.XPATH, '//*[@id="question_6"]/div[3]/div[1]/div/img')
exercise7.click()
time.sleep(5)

exercise8 = driver.find_element(By.XPATH, '//*[@id="question_7"]/div[3]/div[2]/div/img')
exercise8.click()
time.sleep(5)

exercise9 = driver.find_element(By.XPATH, '//*[@id="question_8"]/div[3]/div[5]/div')
exercise9.click()
time.sleep(5)

exercise10 = driver.find_element(By.XPATH, '//*[@id="question_9"]/div[3]/div[2]/div')
exercise10.click()
time.sleep(5)

exercise11 = driver.find_element(By.XPATH, '//*[@id="question_10"]/div[3]/div[2]/div/img')
exercise11.click()
time.sleep(5)

exercise12 = driver.find_element(By.XPATH, '//*[@id="question_11"]/div[3]/div[4]/div')
exercise12.click()

exercise13 = driver.find_element(By.XPATH, '//*[@id="question_12"]/div[3]/div[6]/div')
exercise13.click()
time.sleep(5)

finish_test = driver.find_element(By.XPATH, '//*[@id="question_12"]/div[5]/div/button[3]')
finish_test.click()
time.sleep(5)

finish_test2 = driver.find_element(By.XPATH, '//*[@id="endTestDialog"]/div/div/div[3]/button[2]')
finish_test2.click()
time.sleep(5)

time.sleep(300)
