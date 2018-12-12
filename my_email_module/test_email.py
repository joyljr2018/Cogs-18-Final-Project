
#Test sending email but failed to log in with incorrect password
def test_send_receive_email():
    import email_functions as em
    # set up the email information
    user = "trysendemail01@gmail.com"
    password = '123123123Aa.'
    wrong_password = '123123123'
    message = 'Hello'
    from_address = user
    to_address = user
    
    #test if the funtion returns false if the password is incorrect
    fail = em.email_send (user,wrong_password,message,from_address,to_address)
    assert fail == False
    print("test for checking wrong password login passed") 

    #Test sending email function 

    success = em.email_send (user,password,message,from_address,to_address)

    assert success == True

    email_received = em.email_receive(user,password)
    content = email_received[2]
    # Test if the subject, from address, content are string
    assert isinstance(email_received[0], str)
    assert isinstance(email_received[1], str)
    assert isinstance(email_received[2], str)
    
    #Test if the contents of the email are correct
    assert email_received[0] == message
    assert email_received[1] == from_address
    assert email_received[2] == 'Hello\r\n'
    print("test for sending and receiving emails passed")

