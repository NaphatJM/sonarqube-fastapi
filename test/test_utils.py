# test/test_utils.py

import pytest
from app.utils import calculate_average, reverse_string


class TestCalculateAverage:
    def test_calculate_average_positive_numbers(self):
        """ทดสอบการคำนวณค่าเฉลี่ยของตัวเลขบวก"""
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        result = calculate_average(numbers)
        assert result == 3.0

    def test_calculate_average_negative_numbers(self):
        """ทดสอบการคำนวณค่าเฉลี่ยของตัวเลขลบ"""
        numbers = [-1.0, -2.0, -3.0]
        result = calculate_average(numbers)
        assert result == -2.0

    def test_calculate_average_mixed_numbers(self):
        """ทดสอบการคำนวณค่าเฉลี่ยของตัวเลขผสม"""
        numbers = [-1.0, 0.0, 1.0]
        result = calculate_average(numbers)
        assert result == 0.0

    def test_calculate_average_single_number(self):
        """ทดสอบการคำนวณค่าเฉลี่ยของตัวเลขเดียว"""
        numbers = [5.0]
        result = calculate_average(numbers)
        assert result == 5.0

    def test_calculate_average_empty_list(self):
        """ทดสอบ error เมื่อ list ว่าง"""
        with pytest.raises(ValueError, match="Numbers list must not be empty"):
            calculate_average([])

    def test_calculate_average_float_precision(self):
        """ทดสอบความแม่นยำของ float"""
        numbers = [1.1, 2.2, 3.3]
        result = calculate_average(numbers)
        assert abs(result - 2.2) < 0.0001


class TestReverseString:
    def test_reverse_string_normal(self):
        """ทดสอบการกลับข้อความปกติ"""
        text = "hello"
        result = reverse_string(text)
        assert result == "olleh"

    def test_reverse_string_empty(self):
        """ทดสอบการกลับข้อความว่าง"""
        text = ""
        result = reverse_string(text)
        assert result == ""

    def test_reverse_string_single_char(self):
        """ทดสอบการกลับตัวอักษรเดียว"""
        text = "a"
        result = reverse_string(text)
        assert result == "a"

    def test_reverse_string_palindrome(self):
        """ทดสอบการกลับ palindrome"""
        text = "racecar"
        result = reverse_string(text)
        assert result == "racecar"

    def test_reverse_string_with_spaces(self):
        """ทดสอบการกลับข้อความที่มีช่องว่าง"""
        text = "hello world"
        result = reverse_string(text)
        assert result == "dlrow olleh"

    def test_reverse_string_with_numbers(self):
        """ทดสอบการกลับข้อความที่มีตัวเลข"""
        text = "abc123"
        result = reverse_string(text)
        assert result == "321cba"

    def test_reverse_string_thai_text(self):
        """ทดสอบการกลับข้อความภาษาไทย"""
        text = "สวัสดี"
        result = reverse_string(text)
        assert result == "ีดัสวส"
