#!/usr/bin/env python3
"""Unit and integration tests for the client module."""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json) -> None:
        """Test that GithubOrgClient.org calls get_json once with the
        expected org URL and returns its result.
        """
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name))

    def test_public_repos_url(self) -> None:
        """Test that _public_repos_url returns the repos_url from the
        (mocked) org payload.
        """
        known_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos",
        }
        with patch.object(
                GithubOrgClient, 'org', new_callable=PropertyMock) as m_org:
            m_org.return_value = known_payload
            client = GithubOrgClient("google")
            self.assertEqual(
                client._public_repos_url, known_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json) -> None:
        """Test that public_repos returns the expected repo names based on
        the mocked payload.
        """
        test_payload = [
            {"name": "episodes.dart", "license": {"key": "bsd-3-clause"}},
            {"name": "dagger", "license": {"key": "apache-2.0"}},
        ]
        mock_get_json.return_value = test_payload
        with patch.object(
                GithubOrgClient, '_public_repos_url',
                new_callable=PropertyMock) as mock_url:
            mock_url.return_value = (
                "https://api.github.com/orgs/google/repos")
            client = GithubOrgClient("google")
            self.assertEqual(
                client.public_repos(), ["episodes.dart", "dagger"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected) -> None:
        """Test that has_license correctly matches a repo's license key."""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD,
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos."""

    @classmethod
    def setUpClass(cls) -> None:
        """Start a patcher for requests.get that serves fixture payloads
        based on the requested URL.
        """
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            cls.org_payload["repos_url"]: cls.repos_payload,
        }

        def get_payload(url):
            """Return a Mock whose .json() yields the fixture for url."""
            return Mock(json=lambda: route_payload[url])

        cls.get_patcher = patch('requests.get', side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop the requests.get patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Test public_repos returns all expected repo names."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Test public_repos filters correctly by license."""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"), self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
