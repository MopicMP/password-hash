"""Tests for password-hash."""

import pytest
from password_hash import hash


class TestHash:
    """Test suite for hash."""

    def test_basic(self):
        """Test basic usage."""
        result = hash("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            hash("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = hash(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
