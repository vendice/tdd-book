from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Er kann ein to-do item eingeben
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # Er tippt einkaufen ein
        inputbox.send_keys('einkaufen')

        # Als er enter ein gibt wird die seite geupdated und er kann den ersten Punkt einkaufen sehen
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows =  table.find_elements_by_tag_name('tr')
        self.assertTrue(any (row.text == '1: einkaufen' for row in rows))

        
        # Die Textbox steht noch immer da, er kann einen zweiten Punkt eingeben

        self.fail('Finish the test!')
        # nach dem druecken von enter stehen beide Punkte unterhalb der Textbox

        # Die Liste ist ueber eine einyigartige url aufrufbar

        # nach dem aufrufen der url ist der Text noch da


if __name__ == '__main__':
    
    unittest.main(warnings='ignore')

