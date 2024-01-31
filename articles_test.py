import pytest
from articles import Article


@pytest.fixture
def article():
    return Article("Test Article")


def test_article_init(article):
    assert article.title == "Test Article"
    assert article.content == ""


def test_article_slug(mocker, article):
    # given
    mock_slugify = mocker.patch("articles.slugify", return_value="test")

    # when
    got = article.slug

    # then
    assert got == "test"
    mock_slugify.assert_called_with(article.title)
