import requests
import pytest
from src.constants.api_constants import create_booking_url,base_url
from src.helpers.api_requests_wrapper import post_requests
from src.helpers.utils import common_headers_json
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import verify_response,verify_http_status_code
class TestCreateBooking(object):
    @pytest.mark.negative
    def test_create_booking_tc1(self):
        response=post_requests(url=create_booking_url(),auth=None,headers=common_headers_json(),payload=None,in_json=False)
        print(response)
        verify_http_status_code(response,400)

    def test_create_booking_tc2(self):
        response=post_requests(url=base_url(),auth=None,headers=common_headers_json(),payload=payload_create_booking(),in_json=False)
        print(response)
        verify_http_status_code(response,404)

    def test_create_booking_tc3(self):
        response=post_requests(url=create_booking_url(),auth=None,headers=None,payload=payload_create_booking(),in_json=False)
        print(response)
        verify_http_status_code(response,500)

    def test_create_booking_tc4(self):
        response=post_requests(url=create_booking_url(),auth=None,headers=common_headers_json(),payload="This is a Text File",in_json=False)
        print(response)
        verify_http_status_code(response,400)