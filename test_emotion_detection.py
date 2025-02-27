from EmotionDetection import emotion_detection as emt
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for anger emotion
        result2 = emt.emotion_detector("I am really mad about this")
        self.assertEqual(result2['dominant_emotion'], 'anger')

        # Test case for disgust emotion
        result3 = emt.emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3['dominant_emotion'], 'disgust')

        # Test case for sadness emotion
        result4 = emt.emotion_detector("I am so sad about this")
        self.assertEqual(result4['dominant_emotion'], 'sadness')

        # Test case for fear emotion
        result5 = emt.emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5['dominant_emotion'], 'fear')
        
unittest.main()