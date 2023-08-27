def test_1 ():
    assert 2+2 == 4
def test_2 ():
    assert 2+3 == 4
def test_3():
    new_body = get_user_body("Ааааааааааааааа")
    tresp_2 = sender_stand_request.post_new_user(new_body)
    assert tresp_2.status_code == 201
    assert tresp_2.json()["authToken"] != ""
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert tresp_2.text.count(str_user) == 1