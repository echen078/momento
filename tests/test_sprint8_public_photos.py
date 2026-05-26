"""
E2E tests for Sprint 8 — Public Photos & Community Feed.

Requires the Express backend to be running on port 5001.
"""

import io
import requests
import pytest


def make_test_image(filename="test.jpg", content_type="image/jpeg"):
    """Create a minimal valid JPEG file-like object for upload."""
    jpeg_bytes = (
        b"\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00"
        b"\xff\xd9"
    )
    return (filename, io.BytesIO(jpeg_bytes), content_type)


def upload_photo(base_url, auth_header, *, is_public=None, caption="Test photo"):
    """Helper to upload a photo and return the response JSON."""
    files = {"photo": make_test_image()}
    data = {
        "lat": "34.0522",
        "lng": "-118.2437",
        "caption": caption,
    }
    if is_public is not None:
        data["isPublic"] = "true" if is_public else "false"

    resp = requests.post(
        f"{base_url}/api/photos", headers=auth_header, files=files, data=data
    )
    assert resp.status_code == 201, resp.text
    return resp.json()


class TestUploadIsPublic:
    """Tests for isPublic flag on POST /api/photos"""

    def test_upload_public_photo(self, base_url, auth_header):
        """Upload with isPublic=true returns 201 with isPublic: true."""
        body = upload_photo(
            base_url, auth_header, is_public=True, caption="Public upload"
        )
        assert body["isPublic"] is True

    def test_upload_private_photo_default(self, base_url, auth_header):
        """Upload without isPublic returns 201 with isPublic: false."""
        body = upload_photo(
            base_url, auth_header, caption="Private upload"
        )
        assert body["isPublic"] is False


class TestGetPublicPhotos:
    """Tests for GET /api/photos/public"""

    def test_get_public_photos_shape(self, base_url, auth_header):
        """GET /api/photos/public returns paginated response shape."""
        upload_photo(base_url, auth_header, is_public=True, caption="Public shape test")

        resp = requests.get(f"{base_url}/api/photos/public")
        assert resp.status_code == 200
        body = resp.json()
        assert "photos" in body
        assert "page" in body
        assert "totalPages" in body
        assert "totalPhotos" in body
        assert isinstance(body["photos"], list)

    def test_public_photos_include_username(
        self, base_url, auth_header, test_user_credentials
    ):
        """Public photos list includes populated username."""
        upload_photo(
            base_url, auth_header, is_public=True, caption="Username populate test"
        )

        resp = requests.get(f"{base_url}/api/photos/public")
        assert resp.status_code == 200
        photos = resp.json()["photos"]
        assert len(photos) >= 1

        matching = [
            p for p in photos if p.get("caption") == "Username populate test"
        ]
        assert len(matching) == 1
        assert matching[0]["user"]["username"] == test_user_credentials["username"]

    def test_public_photos_exclude_private(self, base_url, auth_header):
        """Public photos list does not include private photos."""
        public = upload_photo(
            base_url, auth_header, is_public=True, caption="Visible public photo"
        )
        private = upload_photo(
            base_url, auth_header, is_public=False, caption="Hidden private photo"
        )

        resp = requests.get(f"{base_url}/api/photos/public")
        assert resp.status_code == 200
        photo_ids = {p["_id"] for p in resp.json()["photos"]}

        assert public["_id"] in photo_ids
        assert private["_id"] not in photo_ids

    def test_public_photos_pagination(self, base_url, auth_header):
        """Pagination returns correct page size and totalPages."""
        for i in range(3):
            upload_photo(
                base_url,
                auth_header,
                is_public=True,
                caption=f"Pagination photo {i}",
            )

        resp = requests.get(
            f"{base_url}/api/photos/public", params={"page": 1, "limit": 2}
        )
        assert resp.status_code == 200
        body = resp.json()
        assert len(body["photos"]) == 2
        assert body["page"] == 1
        assert body["totalPhotos"] >= 3
        assert body["totalPages"] >= 2

    def test_get_public_photos_without_auth(self, base_url, auth_header):
        """GET /api/photos/public works without auth."""
        upload_photo(base_url, auth_header, is_public=True, caption="No auth public")

        resp = requests.get(f"{base_url}/api/photos/public")
        assert resp.status_code == 200


class TestGetPhotoByIdOptionalAuth:
    """Tests for GET /api/photos/:id with optionalAuth"""

    def test_get_public_photo_without_auth(self, base_url, auth_header):
        """Public photo is viewable without auth."""
        photo = upload_photo(
            base_url, auth_header, is_public=True, caption="Public by id"
        )

        resp = requests.get(f"{base_url}/api/photos/{photo['_id']}")
        assert resp.status_code == 200
        assert resp.json()["_id"] == photo["_id"]
        assert resp.json()["isPublic"] is True

    def test_get_private_photo_without_auth(self, base_url, auth_header):
        """Private photo returns 403 without auth."""
        photo = upload_photo(
            base_url, auth_header, is_public=False, caption="Private by id"
        )

        resp = requests.get(f"{base_url}/api/photos/{photo['_id']}")
        assert resp.status_code == 403

    def test_get_private_photo_with_owner_auth(self, base_url, auth_header):
        """Private photo is viewable by owner."""
        photo = upload_photo(
            base_url, auth_header, is_public=False, caption="Owner private view"
        )

        resp = requests.get(
            f"{base_url}/api/photos/{photo['_id']}", headers=auth_header
        )
        assert resp.status_code == 200
        assert resp.json()["_id"] == photo["_id"]
        assert resp.json()["isPublic"] is False
