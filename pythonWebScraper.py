import os.path
import re
from datetime import datetime
from playwright.sync_api import sync_playwright

prodURLList = [
    # 'https://get4lessghana.com/product/samsung-galaxy-s24-ultra-256gb-12gb-ram-2/',
    # 'https://get4lessghana.com/product/samsung-galaxy-s24-ultra-512gb-12gb-ram/',
    # 'https://get4lessghana.com/product/samsung-galaxy-s24-ultra-1-tb-12gb-ram/',
    # 'https://frankotrading.com/product/samsung-s24-ultra-s928b-1tb12gb-tit/',
    # 'https://compughana.com/samsung-galaxy-sm-s928b-ds-s24-ultra.html',
    # 'https://www.jumia.com.gh/samsung-galaxy-s24-ultra-ai-6.8-5g-200mp12mp-1tb-hdd-12gb-ram-5000mah-titanium-gray-164468589.html',
    # 'https://www.jumia.com.gh/samsung-s24-galaxy-ai-128gb-hdd-8gb-ram-triple-50mp-camera-4000mah-onyx-black-164410104.html',
    # 'https://www.jumia.com.gh/samsung-s24-galaxy-ai-258gb-hdd-8gb-ram-tripple-50mp-camera-4000mah-onyx-black-164410192.html',
    # 'https://www.jumia.com.gh/samsung-s24-galaxy-ai-128gb-hdd-8gb-rm-tripple-50mp-camera-4000mah-marble-grey-164410116.html',
    # 'https://bestpricegh.com/products/copy-of-samsung-galaxy-s24-cell-phone-256gb-ai-smartphone-unlocked-android-50mp-camera-fastest-processor-long-battery-life-us-version-2024-amber-yellow',
    # 'https://bestpricegh.com/products/samsung-galaxy-s24-cell-phone-256gb-ai-smartphone-unlocked-android-50mp-camera-fastest-processor-long-battery-life-us-version-2024-amber-yellow',
    # 'https://compughana.com/samsung-galaxy-s24.html',
    # 'https://www.jumia.com.gh/samsung-galaxy-s24-ai-128gb-hdd-8gb-ram-tripple-50mp-camera-4000mah-black-165057886.html',
    # 'https://www.jumia.com.gh/samsung-s24-galaxy-ai-256gb-hdd-8gb-ram-tripple-50-mp-camera-4000mah-marble-gray-164410226.html',
    # 'https://www.jumia.com.gh/samsung-s24-galaxy-ai-128gb-hdd-8gb-ram-tripple-50mp-camera-4000mah-cobalt-violet-164410111.html',
    # 'https://telefonika.com/product/samsung-galaxy-s24/',
    # 'https://tonaton.com/a_new-samsung-galaxy-s24-128-gb-cvNE3KE7q1TDr0oYHva1W9wK.html',
    # 'https://frankotrading.com/product/samsung-s24-ultra-s928b-256gb12gb/',
    # 'https://frankotrading.com/product/samsung-s24-ultra-s928b-512gb12gb/',
    # 'https://www.jumia.com.gh/samsung-s24-plus-galaxy-ai-256gb-hdd-12gb-ram-tripple-50mp-camera-4900mah-onyx-black-164410250.html',
    # 'https://www.jumia.com.gh/samsung-s24-plus-galaxy-ai-512gb-hdd-12gb-ram-tripple-50mp-4900mah-amber-yellow-164417512.html',
    # 'https://telefonika.com/product/samsung-galaxy-s24-plus/',
    # 'https://tonaton.com/a_new-samsung-galaxy-s24-plus-256-gb-purple-hNxr8OEBKUzqm4cBLdWbZVmh.html',
    # 'https://tonaton.com/a_new-samsung-galaxy-a03-core-32-gb-black-m7aCQ4NohLvfJyFWkE0GNEVO.html',
    # 'https://www.ipmckart.com/phones-tablets/smart-phones/samsung-phones/samsung-galaxy-a04s-sm-a047fzkgafc.html',
    # 'https://www.jumia.com.gh/samsung-galaxy-a04s-128gb-hdd-4gb-ram-50mp-rear5-front-6.5-5000-mah-black-free-smart-watch-139947446.html',
    # 'https://www.jumia.com.gh/samsung-galaxy-a04s-32gb-3gb-ram-50mp-camera-6.5-5000-mah-green-24-months-warranty-144649440.html',
    # 'https://www.jumia.com.gh/samsung-galaxy-a04s-128gb-hdd-4gb-ram-50mp-rear5-front-6.5-5000-mah-black-72547976.html',
    # 'https://www.jumia.com.gh/samsung-galaxy-a04s-64gb-hdd-4gb-ram-50mp-rear5-front-6.5-5000-mah-black-free-booklet-cover-protector-129956898.html',
    # 'https://www.jumia.com.gh/samsung-galaxy-a04s-64gb-hdd-4gb-ram-50mp-rear5-front-6.5-5000-mah-black-72547943.html',
    # 'https://superlovekphones.com/product/samsung-galaxy-a04s-128gb-4gb/',
    # 'https://superlovekphones.com/product/samsung-galaxy-a04s-32gb-3gb/',
    # 'https://superlovekphones.com/product/samsung-galaxy-a04s-64gb-3gb/',
    # 'https://www.jumia.com.gh/samsung-galaxy-z-fold-4-dual-sim-5g-512gb-hdd-12gb-ram-50mp10mp12mp-rear10mp-front-4400mah-phantom-black-68415230.html',
    # 'https://www.jumia.com.gh/samsung-galaxy-s22-ultra-dual-sim-256gb-hdd-12gb-ram-50mp-rear-cream-free-earbud-12-months-warranty-144741837.html'
]

for prodURL in prodURLList:
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(prodURL)

        prod_brand = "samsung"
        prod_model = "galaxy s24 ultra"

        ramMemory = "12GB"
        network = "5G"

        table_name = prod_brand + " " + prod_model
        table_name_string = table_name.replace(" ","_")
        sql_file_name = table_name_string + ".sql"
        sql_file_path = "./db/" + sql_file_name
        print
        check_sql_file = os.path.exists(sql_file_path)

        if ("-8gb" in prodURL) or ("-8-gb" in prodURL):
            ssdStorage = "8GB"
            print("link is for 8GB product")
        elif ("-16gb" in prodURL) or ("-16-gb" in prodURL):
            ssdStorage = "16GB"
            print("link is for 16GB product")
        elif ("-32gb" in prodURL) or ("-32-gb" in prodURL):
            ssdStorage = "32GB"
            print("link is for 32GB product")
        elif ("-64gb" in prodURL) or ("-64-gb" in prodURL):
            ssdStorage = "64GB"
            print("link is for 64GB product")
        elif ("-128gb" in prodURL) or ("-128-gb" in prodURL):
            ssdStorage = "128GB"
            print("link is for 128GB product")
        elif ("-256gb" in prodURL) or ("-256-gb" in prodURL):
            ssdStorage = "256GB"
            print("link is for 256GB product")
        elif ("-512gb" in prodURL) or ("-512-gb" in prodURL):
            ssdStorage = "512GB"
            print("link is for 512GB product")
        elif ("-1tb" in prodURL) or ("-1-tb" in prodURL):
            ssdStorage = "1TB"
            print("link is for 1TB product")
        else:
            ssdStorage = "NotAStorage"
            print("Storage not specified")

        if "bestpricegh" in prodURL:
            store_name_string = prodURL[8:19]
            store_name = store_name_string[:4].capitalize() + store_name_string[4:9].capitalize() + " Ghana"
            filler_text = "Free delivery above GH₵90 * 1 week return policy * 3 months warranty"

            ### Price selector for BestPrice Ghana ###
            price_element = page.query_selector('div .detail-price span')
            price_string_raw = price_element.inner_html()
            price_string = price_string_raw.replace(",","")
            price = price_string.replace("GH₵","")
            ### Price selector for BestPrice Ghana ###

        elif "compughana" in prodURL:
            store_name_string = prodURL[8:18]
            store_name = store_name_string[:5].capitalize() + store_name_string[5].capitalize() + store_name_string[6:]
            filler_text = "Free delivery * 1 week return policy * Warranty info unavailable"

            ### Price selector for CompuGhana ###
            price_element = page.query_selector('span .price')
            price_string_raw = price_element.inner_html()
            price_string = price_string_raw.replace(",","")
            price = price_string.replace("₵","")
            ### Price selector for CompuGhana ###

        elif "easybuygh" in prodURL:
            store_name_string = prodURL[8:17]
            store_name = store_name_string[:4].capitalize() + store_name_string[4:7].capitalize() + " Ghana"
            filler_text = "Delivery between 2 - 5 working days * 7 days return policy * Warranty info unavailable"

            ### Price selector for EasyBuy Ghana ###
            price_element = page.query_selector('p bdi')
            price_string_raw = price_element.inner_html()
            price_string = price_string_raw.replace(",","")
            price = price_string.replace("<span class=\"woocommerce-Price-currencySymbol\">₵</span>","")
            ### Price selector for EasyBuy Ghana ###
            
        elif "electromart" in prodURL:
            store_name_string = prodURL[12:23]
            store_name = store_name_string.capitalize() + " Ghana"
            filler_text = "Delivery between 2 - 5 working days * 7 days return policy * Warranty info unavailable"

            ### Price selector for Electromart Ghana ###
            price_element = page.query_selector('.price')
            price_string_raw = price_element.inner_html()
            if re.search("<del aria-hidden=\"true\">", price_string_raw):
                price_element = page.query_selector('.price ins bdi')
                price_string_raw = price_element.inner_html()
            else:
                price_element = page.query_selector('.price')
                price_string_raw = price_element.inner_html()

            price_string = price_string_raw.replace(",","")
            price = price_string.replace("<span class=\"woocommerce-Price-currencySymbol\">₵</span>","")
            ### Price selector for Electromart Ghana ###

        elif "frankotrading" in prodURL:
            store_name_string = prodURL[8:21]
            store_name_string = store_name_string + "enterprise"
            store_name = store_name_string[:6].capitalize() + " " + store_name_string[6:13].capitalize() + " " + store_name_string[13:].capitalize()
            filler_text = "A day delivery in Accra for GH₵20 * 1 week return policy * Warranty info unavailable"

            ### Price selector for Franko Trading Enterprise ###
            price_element = page.query_selector('.price')
            price_string_raw = price_element.inner_html()
            if re.search("<del aria-hidden=\"true\">", price_string_raw):
                price_element = page.query_selector('.price ins bdi')
                price_string_raw = price_element.inner_html()
            else:
                price_element = page.query_selector('.price')
                price_string_raw = price_element.inner_html()

            price_string = price_string_raw.replace(",","")
            price = price_string.replace("<span class=\"woocommerce-Price-currencySymbol\">₵</span>","")
            ### Price selector for Franko Trading Enterprise ###

        elif "freddiescorneronline" in prodURL:
            store_name_string = prodURL[8:22]
            store_name = store_name_string[:8].capitalize() + " " + store_name_string[8:14].capitalize()
            filler_text = "A day delivery in Accra for GH₵20 * 1 week return policy * Warranty info unavailable"

            ### Price selector for Freddies Corner ###
            price_element = page.query_selector('p bdi')
            price_string_raw = price_element.inner_html()
            price_string = price_string_raw.replace(",","")
            price = price_string.replace("<span class=\"woocommerce-Price-currencySymbol\">₵</span>","")
            ### Price selector for Freddies Corner ###

        elif "get4lessghana" in prodURL:
            store_name_string = prodURL[8:21]
            store_name = store_name_string[:4].capitalize() + store_name_string[4:8].capitalize() + " " + store_name_string[8:].capitalize()
            filler_text = "Delivery info unavailable * Return policy unavailable * Warranty info unavailable"

            ### Price selector for Get4Less Ghana ###
            price_element = page.query_selector('bdi')
            price_string_raw = price_element.inner_html()
            price_string = price_string_raw.replace(",","")
            price = price_string.replace("<span class=\"woocommerce-Price-currencySymbol\">₵</span>","")
            ### Price selector for Get4Less Ghana ###

        elif "ipmckart" in prodURL:
            store_name_string = prodURL[12:20]
            store_name = store_name_string[:4].upper() + " Ghana"
            filler_text = "Delivery info unavailable * Return policy unavailable * Warranty info unavailable"

            ### Price selector for Get4Less Ghana ###
            price_element = page.query_selector('.price-wrapper .price')
            price_string_raw = price_element.inner_html()
            price_string = price_string_raw.replace(",","")
            price = price_string.replace("GHS ","")
            ### Price selector for Get4Less Ghana ###

        elif "jiji" in prodURL:
            store_name_string = prodURL[8:12]
            store_name = store_name_string[:5].capitalize() + " Ghana"
            filler_text = "Standard delivery between 3 - 10 days * 15 days return policy * Warranty info unavailable"

            ### Price selector for Jiji Ghana ###
            price_element = page.locator('span[itemprop="price"]')
            price_string_raw = price_element.text_content()
            price_string = price_string_raw.replace(",","")
            price = price_string.replace("GH₵ ","").rstrip()
            ## Price selector for Jiji Ghana ###

        elif "jumia" in prodURL:
            store_name_string = prodURL[12:17]
            store_name = store_name_string[:5].capitalize() + " Ghana"
            filler_text = "Standard delivery between 3 - 10 days * 15 days return policy * Warranty info unavailable"

            ### Price selector for Jumia Ghana ###
            price_element = page.locator('span[data-price="true"]')
            price_string_raw = price_element.text_content()
            price_string = price_string_raw.replace(",","")
            price = price_string.replace("GH₵ ","")
            ## Price selector for Jumia Ghana ###

        elif "melcom" in prodURL:
            store_name_string = prodURL[8:14]
            store_name = store_name_string[:6].capitalize()
            filler_text = "Delivery info unavailable * 48 hours return policy * 1 year warranty"

            ### Price selector for Melcom Ghana ###
            price_element = page.locator('span[data-price-type="finalPrice"] .price')
            price_string_raw = price_element.text_content()
            price_string = price_string_raw.replace(",","")
            price = price_string.replace("₵","")
            ## Price selector for Melcom Ghana ###

        elif "ololoexpress" in prodURL:
            store_name_string = prodURL[8:20]
            store_name = store_name_string[:5].capitalize() + store_name_string[5:].capitalize()
            filler_text = "Delivery info unavailable * 7 days return policy * Warranty info unavailable"

            ### Price selector for OloloExpress ###
            price_element = page.query_selector('div .rtin-price')
            price_string_raw = price_element.inner_html()
            price_string = price_string_raw.replace(",","").replace("₵","")
            price = price_string.replace("(Fixed)","")
            ## Price selector for OloloExpress ###
        elif "superlovekphones" in prodURL:
            store_name_string = prodURL[8:18]
            store_name = store_name_string.capitalize()
            filler_text = "Free delivery in 48 hours * Refund within 10 and 30 days * 1 year warranty"

            ### Price selector for Telefonika ###
            price_element = page.query_selector('p span bdi')
            price_string_raw = price_element.inner_html()
            price_string = price_string_raw.replace(",","")
            price = price_string.replace("<span class=\"woocommerce-Price-currencySymbol\">₵</span>","")
            ### Price selector for Telefonika ###

        elif "telefonika" in prodURL:
            store_name_string = prodURL[8:18]
            store_name = store_name_string.capitalize()
            filler_text = "Free delivery in 48 hours * Refund within 10 and 30 days * 1 year warranty"

            ### Price selector for Telefonika ###
            price_element = page.query_selector('p[class="price"]')
            price_string_raw = price_element.inner_html()
            if re.search("<del aria-hidden=\"true\">", price_string_raw):
                price_element = page.query_selector('ins bdi')
                price_string_raw = price_element.inner_html()
            else:
                price_element = page.query_selector('p[class="price"] span bdi')
                price_string_raw = price_element.inner_html()

            price_string = price_string_raw.replace(",","")
            price = price_string.replace("<span class=\"woocommerce-Price-currencySymbol\">₵</span>","")
            ### Price selector for Telefonika ###

        elif "tonaton" in prodURL:
            store_name_string = prodURL[8:15]
            store_name = store_name_string.capitalize()
            filler_text = "Standard delivery between 3 - 10 days * 15 days return policy * Warranty info unavailable"

            ### Price selector for Tonaton ###
            price_element = page.locator('span[itemprop="price"]')
            price_string_raw = price_element.text_content()
            price_string = price_string_raw.replace(",","")
            price = price_string.replace("GH₵ ","")
            ## Price selector for Tonaton ###

        if check_sql_file == False:
            with open("./db/" + sql_file_name, "w", encoding="utf-8") as file:
                b = """ (
    id int(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
    storelogo varchar(255) NOT NULL,
    storename varchar(255) NOT NULL,
    storetype varchar(255) NOT NULL,
    storage_capacity varchar(255) NOT NULL,
    product_desc varchar(255) NOT NULL,
    product_price varchar(255) NOT NULL,
    product_link varchar(255) NOT NULL
);"""
                sql_declaration = "CREATE TABLE IF NOT EXISTS " + table_name_string + b
                file.write(sql_declaration)
                file.write("\n\n")
                store_logo_str = store_name_string + "-logo.png"

                filler_one = """ (storelogo, storename, storetype, storage_capacity, product_desc, product_price, product_link) VALUES (
    '""" + store_logo_str + """', '""" + store_name + """', 'Online', '""" + ssdStorage + """', '* """ + ramMemory + """ RAM; """ + network + """; Dual SIM * Colours: Not specified * """ + filler_text + """', '""" + price + """', '""" + prodURL + """'
);"""

                str1 = "INSERT INTO " + table_name_string + filler_one
                file.write(str1)
        else:
            with open("./db/" + sql_file_name,"r", encoding="utf-8") as file:

                store_logo_str = store_name_string + "-logo.png"
                file_content = file.read()

                url_match = re.search(prodURL, file_content)

                if url_match:
                    price_match = re.search(price, file_content)

                    if price_match:
                        print("Product link already exist. There might be possible duplication.")
                    else:
                        with open("pricedrop.sql", "a", encoding="utf-8") as file2:
                            time_now_s = datetime.now()
                            time_now_us = time_now_s.strftime("%Y-%m-%d %H:%M:%S")

                            matches = re.search(r"'(\d+).(\d+)', '" + prodURL + "'", file_content)

                            old_price = float(price)
                            new_price = float(matches.group(1))

                            print(old_price)
                            print(type(old_price))

                            print(new_price)
                            print(type(new_price))

                            pd_filler_str = """INSERT INTO pricedrop (productimage, storelogo, productbrand, productmodel, product_desc, oldprice, newprice, percent_drop, product_link, dropdate) VALUES (
    '""" + table_name.replace(" ","-") + "-front.webp', '" + store_logo_str + "', '" + prod_brand.capitalize() + "', '" + prod_model.capitalize() + "', '" + table_name.title() + " - " + ssdStorage + " HHD - " + ramMemory + " RAM', '" + matches.group(1) + "', '" + price + "', '" + str(round(100 * ((new_price - old_price)/new_price))) + "', '" + prodURL + "', '" + time_now_us + "'""""
);"""
                            file2.write("\n\n")
                            file2.write(pd_filler_str)
                            # file2.write(matches.group())
                            # file2.write(price)
                else:
                    with open("./db/" + sql_file_name,"a", encoding="utf-8") as file:

                        filler_one = """ (storelogo, storename, storetype, storage_capacity, product_desc, product_price, product_link) VALUES (
    '""" + store_logo_str + """', '""" + store_name + """', 'Online', '""" + ssdStorage + """', '* """ + ramMemory + """ RAM; """ + network + """; Dual SIM * Colours: Not specified * """ + filler_text + """', '""" + price + """', '""" + prodURL + """'
);"""

                        str1 = "INSERT INTO " + table_name_string + filler_one
                        file.write("\n\n")
                        file.write(str1)

                        browser.close()