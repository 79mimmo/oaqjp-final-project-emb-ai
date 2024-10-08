from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionAnalyzer(unittest.TestCase):
   def test_emotion_analyzer(self):
        #Test for joy recognition
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        #Test for anger recognition
        result_1 = emotion_detector('I am really mad about this')
        self.assertEqual(result_1['dominant_emotion'], 'anger')
        #Test for disgust recognition
        result_1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_1['dominant_emotion'], 'disgust')
        #Test for sadness recognition
        result_1 = emotion_detector('I am so sad about this')
        self.assertEqual(result_1['dominant_emotion'], 'sadness')
        #Test for fear recognition
        result_1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_1['dominant_emotion'], 'fear')

unittest.main()
