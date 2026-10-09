# Наталья Сидорова 48-я когорта - Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request as request

def test_get_order_by_track():
    order_responce = request.post_new_order(data.order_body)

    track_number_order = order_responce.json()['track']

    get_order_responce = request.get_order_by_track(track_number_order)

    assert get_order_responce.status_code == 200
