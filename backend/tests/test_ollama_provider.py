@'
import pytest

from app.llm.exceptions import MalformedResponseError
from app.llm.providers.ollama_provider import _decode_ollama_payload


def test_valid_ollama_payload():
    result = _decode_ollama_payload('{"response": "Hello"}')
    assert result["response"] == "Hello"


def test_invalid_ollama_json():
    with pytest.raises(MalformedResponseError):
        _decode_ollama_payload("not valid json")


def test_non_object_ollama_payload():
    with pytest.raises(MalformedResponseError):
        _decode_ollama_payload('["unexpected"]')
'@ | Set-Content backend/tests/test_ollama_provider.py -Encoding utf8