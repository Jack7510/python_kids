# -*- coding: utf-8 -*-
#!/usr/bin/python3

import unittest
import exercise
import jack_ex

class TestExercise(unittest.TestCase):

    def test_joint_2_string(self):
        a = "hello"
        b = "world"
        self.assertEqual("helloworld", \
            exercise.joint_2_string(a, b))

    def test_polynomial(self):
        sum1 = jack_ex.calc_polynomial(1, 2, 3, 4, 5)
        sum2 = exercise.calc_polynomial(1, 2, 3, 4, 5)
        self.assertEqual(sum1, sum2)

    def test_str_times(self):
        self.assertEqual(jack_ex.str_times('hello', 2), \
                         exercise.str_times('hello', 2))

    def test_str_get_char(self):
        self.assertEqual(jack_ex.str_get_char('windows', 3), \
                         exercise.str_get_char('windows', 3))

        self.assertNotEqual(jack_ex.str_get_char('windows', 4), \
                            exercise.str_get_char('windows', 5))

    def test_str_list_add(self):
        names = ['Jack', 'Margret', 'Songsong']
        jobs_name = 'Cici'
        names_ex = ['Jack', 'Margret', 'Songsong']
        jack_ex.str_list_add(names, jobs_name)
        exercise.str_list_add(names_ex, jobs_name)
        self.assertEqual(names, names_ex)

    def test_str_list_del(self):
        names = ['Jack', 'Margret', 'Songsong','Cici']
        jobs_name = 'Cici'
        names_ex = ['Jack', 'Margret', 'Songsong', 'Cici']
        jack_ex.str_list_del(names, jobs_name)
        exercise.str_list_del(names_ex, jobs_name)
        self.assertEqual(names, names_ex)

if __name__ == '__main__':
    unittest.main()
