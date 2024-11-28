import requests
import pytest
from src.helpers.api_requests_wrapper import post_requests, put_requests
from src.constants.api_constants import create_booking_url, create_token_url
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.common_verification import verify_response, verify_http_status_code, verify_json_key_for_not_null


class TestCreateBooking(object):
    @pytest.mark.positive
    def test_create_booking_positive(self):
        response = post_requests(url=create_booking_url(), headers=common_headers_json(), auth=None,
                                 payload=payload_create_booking(), in_json=False)
        print(response)
        booking_id = response.json()["bookingid"]
        print(booking_id)
        verify_response(response.json()["bookingid"])
        verify_http_status_code(response, 200)

    def test_create_token(self):
        response = post_requests(url=create_token_url(), auth=None, headers=common_headers_json(),
                                 payload=payload_create_token(), in_json=False)
        print(response)
        token = response.json()["token"]
        print(token)
        verify_response(response.json()["token"])
        verify_http_status_code(response, 200)

    def test_update_booking(self):
        booking_id = "/8"
        token = "6ab2be5ddc0eaf0"
        full_url = create_booking_url() + booking_id
        auth = ("admin", "password123")
        response_update = put_requests(url=full_url, auth=auth, headers=common_headers_json(),
                                       payload=payload_create_booking(), in_json=False)
        print(response_update.json())
