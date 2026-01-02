"""Tests the functions in core module."""

# ruff: noqa: S101, DTZ001
# pylint: disable=W0612
import datetime
from unittest.mock import AsyncMock, patch

import pytest

from hamyar_paygah.services import get_missions_list


@pytest.mark.asyncio
async def test_get_missions_list_returns_response_text() -> None:
    """Tests the get_missions_list function."""
    server_url = "https://example.com"
    from_date = datetime.datetime(2025, 12, 28)
    to_date = datetime.datetime(2025, 12, 30)
    region_id = 5

    fake_response_text = "<soap>OK</soap>"

    # Mock response object
    mock_response = AsyncMock()
    mock_response.text.return_value = fake_response_text

    # Mock context manager returned by session.post
    mock_post_context = AsyncMock()
    mock_post_context.__aenter__.return_value = mock_response

    with patch("aiohttp.ClientSession.post", return_value=mock_post_context) as mock_post:
        result: str = await get_missions_list(
            server_url=server_url,
            from_date=from_date,
            to_date=to_date,
            region_id=region_id,
        )

    # Assert returned response
    assert result == fake_response_text

    # Assert request was made correctly
    mock_post.assert_called_once()

    _, called_kwargs = mock_post.call_args

    response_data = called_kwargs["data"]
    headers = called_kwargs["headers"]

    # Check URL
    assert called_kwargs["url"] == f"{server_url}/Report.svc"

    # Check Body
    assert "<fromDate>2025-12-28T00:00:00</fromDate>" in response_data
    assert "<toDate>2025-12-30T23:59:59</toDate>" in response_data
    assert "<regionId>5</regionId>" in response_data
    assert '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">' in response_data
    assert '<GetDocumentReportRegion xmlns="http://tempuri.org/">' in response_data

    # Check Headers
    assert headers["Content-Type"] == "text/xml; charset=utf-8"
    assert headers["SOAPAction"] == '"http://tempuri.org/IReport/GetDocumentReportRegion"'
