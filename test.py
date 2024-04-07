import unittest
import imageManipulator as im
import cv2

#small set of test cases to make sure the fuctions are actualy returing stuff 
class TestStringMethods(unittest.TestCase):
 
    def test_pixleateImage(self):
        path = 'photo of me.PNG'
        img=cv2.imread(path)
        img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        self.assertIsNotNone(cv2.imread(path))
        self.assertIsNotNone(im.pixleateImage(img))

    def test_sketchImage(self):
        path = 'photo of me.PNG'
        img=cv2.imread(path)
        img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        self.assertIsNotNone(cv2.imread(path))
        self.assertIsNotNone(im.imageToSketch(img))

    def test_comicImage(self):
        path = 'photo of me.PNG'
        img=cv2.imread(path)
        img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        self.assertIsNotNone(cv2.imread(path))
        self.assertIsNotNone(im.comicImage(img))

if __name__ == '__main__':
    unittest.main()