class SearchPage:
    search_box = '//*[@id="search_query_top"]'
    # List suggest in HOmePage
    list_suggest_xpath = '//*[@id="index"]/div[2]/ul/li'
    title_xpath = '//div[@class="pb-center-column col-xs-12 col-sm-4"]/h1'
    button_search_xpath = '//*[@id="searchbox"]/button'
    list_search_xpath = '//*[@id="center_column"]/ul/li'
    title_result_class_name = 'heading-counter'

    price_txt = 'our_price_display'

    # wrong tittle
    tittle_wrong_xpath = '//*[@id="center_column"]/p'

    # List suggest in Product Page
    list_product_xpath = '//*[@id="product"]/div[@class="ac_results"]/ul/li'


class Contact:
    # locator newletter
    letter = 'newsletter-input'
    button_letter = 'submitNewsletter'
    message_notice = "//p[@class='alert alert-success']"

    # locator contactus
    button_contact = '//a[@title="Contact Us"]'
    subject = 'id_contact'
    email = 'email'
    order = 'id_order'
    file_upload = 'fileUpload'
    message = 'message'
    button_send_contact = 'submitMessage'
    notice = '//*[@id="center_column"]/p'


class Login:
    # Login locator
    sign_in = "//a[normalize-space()='Sign in']"
    email_input_id = 'email_create'
    button_login_id = 'SubmitCreate'
    error_message = "//li[normalize-space()='Invalid email address.']"

    # Locator element personal
    first_name = "//input[@id='customer_firstname']"
    last_name = '//input[@id="customer_lastname"]'
    pass_word = 'passwd'
    address = 'address1'
    city = 'city'
    state = 'id_state'
    zip = 'postcode'
    country = 'id_country'
    phone = 'phone_mobile'
    alias = 'alias'
    button_register = 'submitAccount'


class Order:
    # Locator
    # Test order Success
    continue_shopping_xpath = "//span[@title='Continue shopping']//span[1]"
    checkout_out_xpath = '//a[@class="btn btn-default button button-medium"]'

    price_product = '//td[@class="cart_total"]/span'

    total_product = '//*[@id="total_product"]'

    proceed_checkout_xpath = '//a[@class="button btn btn-default standard-checkout button-medium"]'

    email_checkout_xpath = '//*[@id="email"]'

    pass_checkout_xpath = '//*[@id="passwd"]'

    button_signin_xpath = '//*[@id="SubmitLogin"]'

    proceed_checkout2_xpath = '//*[@id="center_column"]/form/p/button'  # checkout after signIN

    click_term_xpath = '//*[@id="cgv"]'

    proceed_checkout3_xpath = '//*[@id="form"]/p/button'  # check after Shipping

    payment_method = '//a[@class="bankwire"]'

    confirm_order_xpath = '//*[@id="cart_navigation"]/button'

    notice_order_success = '//p/strong[@class="dark"]'

    # test change Order Detail
    change_quantity = '//input[@class="cart_quantity_input form-control grey"]'
    delete_quantity = '//i[@class="icon-trash"]'

    alert_term_xpath = "//p[@class='fancybox-error']"
    close_alert_term = "//a[@title='Close']"

    # test_sale_product
    list_product_xpath = '//*[@id="homefeatured"]/li'
    sale_product_xpath = '//*[@id="homefeatured"]/li/div/div[2]/div[1]/span[3]'

    # check sale order
    button_addtoCart = '//*[@id="add_to_cart"]/button'
    proceed_checkout = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a'

    # List product
    lst_pro = '//ul[@id="homefeatured"]//a[@class="button ajax_add_to_cart_button btn btn-default"]'
    # List add to cart
    list_pro = '//ul[@id="homefeatured"]//li[{}]//a[@title="Add to cart"]'
    # List hover img
    img = '//ul[@id="homefeatured"]//li[{}]//div[@class="left-block"]'


class Product:
    # Locator

    # check viewlarge when clicking image
    lst_product = '//*[@id="homefeatured"]/li'
    normal_image = '//*[@id="bigpic"]'
    big_image = '//div[@class="fancybox-wrap fancybox-desktop fancybox-type-image fancybox-opened"]'
    title_xpath = '//span[@class = "child"]'

    # check viewlarge when clicking button view large
    button_close = '//a[@class="fancybox-item fancybox-close"]'

    button_viewlarge = '//span[@class="span_link no-print"]'

    # add to cart with quantity =0

    quantity_xpath = '//input[@id="quantity_wanted"]'

    buton_addtocart = '//*[@id="add_to_cart"]/button/span'

    alert_quantity = '//p[@class="fancybox-error"]'

    # add to cart with quantity >0

    close_alert_xpath = '//a[@class="fancybox-item fancybox-close"]'
    alert_success_xpath = "//h2[normalize-space()='Product successfully added to your shopping cart']"
    button_close_popup = '//span[@title="Close window"]'
    button_cart_xpath = '//a[@title="View my shopping cart"]'

    get_name_detail_xpath = '//div[@class="pb-center-column col-xs-12 col-sm-4"]//h1'
    get_quantity_detail_xpath = '//p//input[@id="quantity_wanted"]'
    get_name_cart_xpath = '//tr//td//p[@class="product-name"]/a'
    get_quantity_cart_xpath = '//input[@size="2"]'

    #test share twitter
    twitter = '//button[@class="btn btn-default btn-twitter"]'
    # test write comment
    click_sign = '//a[@title="Log in to your customer account"]'
    user_xpath = '//*[@id="email"]'
    pw_xpath = '//*[@id="passwd"]'
    button_signIn = '//*[@id="SubmitLogin"]'
    button_backHome = '//a[@title="Home"]'
    click_write_cmt = '//a[@class="open-comment-form"]'
    input_title = '//*[@id="comment_title"]'
    input_comment = '//*[@id="content"]'
    button_send_cmt = '//*[@id="submitNewMessage"]'
    check_title = "//div[@class='fancybox-inner']/p[contains(text(),'Your')]"
    close_notice = '//button[@class="button btn-default button-medium"]'

    # test send to friend
    send_to_friend = '//*[@id="send_friend_button"]'
    name_xpath = '//*[@id="friend_name"]'
    email_xpath = '//*[@id="friend_email"]'
    button_send_mail = '//*[@id="sendEmail"]'
    notice_send_mail = '//div[@class="fancybox-inner"]/p[contains(text(),"Your")]'
    close_send_email = '//p[@class="submit"]/input'
