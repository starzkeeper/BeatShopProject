from django.contrib.auth import get_user_model
from django.test import TestCase

from beats.models import Beat


class BeatModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username="test_user", email='testemail@gmail.com')
        self.user2 = get_user_model().objects.create(username='test_user_2', email='testemail2@gmail.com')
        self.beat = Beat.objects.create(name='test1 test_', author=self.user,
                                        file='beats/tests/test_files/audio/test_audio.mp3',
                                        cover='beats/tests/test_files/img/test_img.jpg', bpm=120, key='Ab',
                                        genre='SynthPop', tags=['hashtag', 'hashtag2'], price=1200)
        self.beat.likes.set([self.user, self.user2])

    def test_beat_model_id_files(self):
        return self.assertTrue(self.beat.id)

    def test_beat_model_slug(self):
        return self.assertTrue(self.beat.slug)

    def test_beat_model_file_audio(self):
        with open(str(self.beat.file), 'rb') as file1:
            content1 = file1.read()

        with open('beats/tests/test_files/audio/test_audio.mp3', 'rb') as file2:
            content2 = file2.read()

        self.assertEqual(content1, content2)

    def test_beat_model_file_img(self):
        with open(str(self.beat.cover), 'rb') as file1:
            content1 = file1.read()

        with open('beats/tests/test_files/img/test_img.jpg', 'rb') as file2:
            content2 = file2.read()

        self.assertEqual(content1, content2)

    def test_beat_model_likes(self):
        liked = [liked for liked in self.beat.likes.all()]
        users = [self.user2, self.user]
        return self.assertCountEqual(liked, users)

    def test_beat_model_tags(self):
        tags = ['hashtag', 'hashtag2']
        return self.assertEqual(tags, self.beat.tags)

    def test_beat_model_genre(self):
        return self.assertTrue(self.beat.genre)

    def test_beat_model_key(self):
        return self.assertTrue(self.beat.key)
