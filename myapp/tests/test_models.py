from django.test import TestCase
from page.models import Page, Tag
from user.models import User


class TestHomePageModels(TestCase):
    def setUp(self):
        pass

    def test_page(self):
        user1 = User.objects.create(title="test user")

        followers = [
            User.objects.create(
                title=f"follower user {index}",
                email=f"follower{index}@gmail.com",
                username=f"follower{index}",
            )
            for index in range(10)
        ]

        page1 = Page.objects.create(
            name="1",
            uuid=1,
            description="...",
            owner=user1,
            is_private=True,
        )
        for index in range(5):
            page1.followers.add(followers[index])

        all_users_from_db = User.objects.all()
        self.assertIn(user1.id, [user.id for user in all_users_from_db])

    def test_post(self):
        user1 = User.objects.create(title="test user1")

        page1 = Page.objects.create(name="1", uuid=1, description="...", owner=user1)

    def test_tag(self):
        tag1 = Tag.objects.create(name="test_tag")

    def test_followers(self):
        user1 = User.objects.create(title="test user")
        followers = [
            User.objects.create(
                title=f"follower user {index}",
                email=f"follower{index}@gmail.com",
                username=f"follower{index}",
            )
            for index in range(10)
        ]

        page1 = Page.objects.create(name="", uuid=1, description="...", owner=user1)

        for index in range(5):
            page1.followers.add(followers[index])

        assert True


class UserTest(TestCase):
    def test_user(self):
        user1 = User.objects.create(
            email="roma@mai.com", role="user", title="roma", is_blocked=False
        )
