from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"c:\users\bhavy\pycharmprojects\amazon\drivers\chromedriver.exe")
url = 'https://www.amazon.com'
search_text ='headphones'

def search_best_selling_item(drvr,url,search_text):
    best_sellers = [] #set for collecting product links
    driver.get(url)
    time.sleep(3) # Let the user actually see something!
    try:

        if drvr.find_element_by_id('twotabsearchtextbox').is_displayed() : #if the search bar visible
            drvr.find_element_by_id('twotabsearchtextbox').send_keys(search_text)
            drvr.find_element_by_class_name('nav-input').click()
            time.sleep(3) # Let the user actually see something!

            # finding tags which contains Best Seller, its <span> tag in the page
            tags = drvr.find_elements_by_link_text('Best Seller')
            for tag in tags:

                #the item to be found is in nested divs
                #grand parent
                    #parent
                        #best seller tag

                #sibling
                    # h2 tag
                        # actual url of the image

                # finding parent tag of best seller 1 level up
                parent_tag = tag.find_element_by_xpath('..')
                # finding grand parent tag of best seller 2 level up
                grand_parent_tag = parent_tag.find_element_by_xpath('..')

                # finding the next sibling which contain the url
                sib_tag = grand_parent_tag.find_element_by_xpath('./following-sibling::div')

                # getting all the titles in sibling
                titles = sib_tag.find_elements_by_tag_name('h2')
                count =0

                #check of link in h2
                for title in titles:
                    prod_link = title.find_elements_by_tag_name('a')
                    for link in prod_link:
                        print(count+1, link.text)
                        print(link.get_attribute('href'))
                        print('\n')
                        best_sellers.append(link.get_attribute('href'))


        return best_sellers

    except Exception as e:
        print("++WRN:Not able to process ....",str(e))

def add_to_cart(prod_links,drvr):
    # for i in prod_links:
    #     print(i)

    if prod_links:
        for link in prod_links:
            drvr.get(link)
            print(link)
            driver.find_element_by_id("add-to-cart-button").click()
            print("Your Item is added to cart\n")
            time.sleep(5)


bs_prod_links = search_best_selling_item(driver,url,search_text)

add_to_cart(bs_prod_links,driver)