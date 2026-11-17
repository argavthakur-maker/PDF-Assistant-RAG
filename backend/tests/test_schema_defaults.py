from app.schemas import DocumentResponse, ErrorEnvelope


def test_error_envelope_collection_defaults_are_independent():
    first = ErrorEnvelope(code="bad_request", message="Invalid request")
    second = ErrorEnvelope(code="not_found", message="Missing resource")

    first.details["field"] = "email"

    assert second.details == {}


def test_document_response_list_defaults_are_independent():
    first = DocumentResponse(id="document-1")
    second = DocumentResponse(id="document-2")

    first.keywords.append("retrieval")
    first.extracted_urls.append("https://example.com")

    assert second.keywords == []
    assert second.extracted_urls == []
