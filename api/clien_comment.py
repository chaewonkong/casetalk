'''Clien Comment Posting Program

Automatically log in and post comments at clien.net'''

from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/ChaewonKong/Desktop/pyWeb/chromedriver")


def clien_login():
	'''Get id, pw as an input and post id, password to clien site'''

	user_id = input("Enter ID -->")
	user_pw = input("Enter Password -->")

	# Sign in process
	try:
		driver.get("https://www.clien.net/service/")
		driver.find_element_by_name("userId").send_keys(user_id)
		driver.find_element_by_name("userPassword").send_keys(user_pw)
		driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/button').click()
		time.sleep(2)
	except Exception as e:
		print(e)

	else:
		if driver.current_url == "https://www.clien.net/service/":
			print("Successfully logged in!")
			time.sleep(2)
		else:
			print("Login Failed: Please try again!")
			driver.close()
		


def clien_post_comment():
	'''Post given comment input to articles in clien'''
	
	clien_login() # Sign in Clien.net

	try:
		# Navigate to newly posted "Today's Recommandations"
		driver.find_element_by_xpath('//*[@id="div_content"]/div[2]/div[2]/div[1]/div/a[1]/span[2]').click()

		# Write and post a comment
		driver.find_element_by_xpath('//*[@id="commentToogleBtn"]/button').click()
		driver.find_element_by_xpath('//*[@id="froala-editor"]/div[3]/div').send_keys("그렇군요...")
		driver.find_element_by_xpath('//*[@id="rewrite_height"]').click()
		time.sleep(2)
		driver.close()

	except Exception as e:
		print(e)

	else:
		print("Successfully posted a comment!")


clien_post_comment()