from states.states import UserState, create_state_machine


def test_state_machine():
    user = UserState(user_id=1)
    machine = create_state_machine(user)

    assert user.state == "init"

    user.start()
    assert user.state == "main_menu"

    user.view_category()
    assert user.state == "viewing_category"

    user.view_product()
    assert user.state == "viewing_product"

    user.back_to_menu()
    assert user.state == "init"
