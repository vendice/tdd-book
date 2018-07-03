from selenium import webdriver
import unittest

class NewVisitorTest (unittest.TestCase):

    def setUp(self):
        self.browser =  webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):


        # der user hat von einer neuen to-do app geh;rt und besucht sie
        self.browser.get('http://localhost:8000')

        # er schaut sich den Titel der Seite an, und sieht To-Do                                                 
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!"')

        # Er kann ein to-do item eingeben

        # Er tippt einkaufen ein

        # Als er enter ein gibt wird die seite geupdated und er kann den ersten Punkt einkaufen sehen

        # Die Textbox steht noch immer da, er kann einen zweiten Punkt eingeben

        # nach dem druecken von enter stehen beide Punkte unterhalb der Textbox

        # Die Liste ist ueber eine einyigartige url aufrufbar

        # nach dem aufrufen der url ist der Text noch da


if __name__ == '__main__':
    
    unittest.main(warnings='ignore')

