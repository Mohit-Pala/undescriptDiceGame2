from dice import Die
from enums.sides import DiceFaces
import unittest


class TestDie(unittest.TestCase):
    
    def test_init_default_num_sides(self):
        die = Die()
        self.assertEqual(die.num_sides, 6)
    
    def test_init_default_dice_sides_length(self):
        die = Die()
        self.assertEqual(len(die.dice_sides), 6)
    
    def test_init_dice_sides_structure(self):
        die = Die()
        for side in die.dice_sides:
            self.assertIn('side_id', side)
            self.assertIn('die_side', side)
            self.assertIn('weight', side)
    
    def test_init_auto_increment_id(self):
        die = Die()
        self.assertEqual(die.auto_increment_id, 7)
    
    def test_init_dice_sides_values(self):
        die = Die()
        expected_faces = [DiceFaces.ONE, DiceFaces.TWO, DiceFaces.THREE, 
                         DiceFaces.FOUR, DiceFaces.FIVE, DiceFaces.SIX]
        actual_faces = [side['die_side'] for side in die.dice_sides]
        self.assertEqual(actual_faces, expected_faces)

    def test_add_side_default_wildcard(self):
        die = Die()
        initial_count = len(die.dice_sides)
        die.add_side()
        self.assertEqual(len(die.dice_sides), initial_count + 1)
        self.assertEqual(die.dice_sides[-1]['die_side'], DiceFaces.WILDCARD)
    
    def test_add_side_custom_face(self):
        die = Die()
        die.add_side(DiceFaces.ONE)
        self.assertEqual(die.dice_sides[-1]['die_side'], DiceFaces.ONE)
    
    def test_add_side_custom_weight(self):
        die = Die()
        die.add_side(weight=2.5)
        self.assertEqual(die.dice_sides[-1]['weight'], 2.5)
    
    def test_add_side_increments_auto_id(self):
        die = Die()
        initial_id = die.auto_increment_id
        die.add_side()
        self.assertEqual(die.auto_increment_id, initial_id + 1)
    
    def test_add_side_assigns_correct_id(self):
        die = Die()
        expected_id = die.auto_increment_id
        die.add_side()
        self.assertEqual(die.dice_sides[-1]['side_id'], expected_id)

    def test_remove_side_existing_id(self):
        die = Die()
        initial_count = len(die.dice_sides)
        die.remove_side(1)
        self.assertEqual(len(die.dice_sides), initial_count - 1)
        self.assertNotIn(1, [side['side_id'] for side in die.dice_sides])
    
    def test_remove_side_nonexistent_id(self):
        die = Die()
        initial_count = len(die.dice_sides)
        die.remove_side(999)
        self.assertEqual(len(die.dice_sides), initial_count)
    
    def test_remove_side_multiple_sides(self):
        die = Die()
        die.remove_side(1)
        die.remove_side(2)
        remaining_ids = [side['side_id'] for side in die.dice_sides]
        self.assertNotIn(1, remaining_ids)
        self.assertNotIn(2, remaining_ids)
    
    def test_remove_side_all_sides(self):
        die = Die()
        for i in range(1, 7):
            die.remove_side(i)
        self.assertEqual(len(die.dice_sides), 0)
    
    def test_remove_side_preserves_other_sides(self):
        die = Die()
        die.remove_side(3)
        remaining_ids = [side['side_id'] for side in die.dice_sides]
        expected_ids = [1, 2, 4, 5, 6]
        self.assertEqual(sorted(remaining_ids), expected_ids)

    def test_modify_side_existing_id(self):
        die = Die()
        die.modify_side(1, DiceFaces.WILDCARD, 2.0)
        modified_side = next(side for side in die.dice_sides if side['side_id'] == 1)
        self.assertEqual(modified_side['die_side'], DiceFaces.WILDCARD)
        self.assertEqual(modified_side['weight'], 2.0)
    
    def test_modify_side_nonexistent_id(self):
        die = Die()
        original_sides = die.dice_sides.copy()
        die.modify_side(999, DiceFaces.WILDCARD, 2.0)
        self.assertEqual(die.dice_sides, original_sides)
    
    def test_modify_side_only_face(self):
        die = Die()
        original_weight = die.dice_sides[0]['weight']
        die.modify_side(1, DiceFaces.SIX, original_weight)
        modified_side = next(side for side in die.dice_sides if side['side_id'] == 1)
        self.assertEqual(modified_side['die_side'], DiceFaces.SIX)
        self.assertEqual(modified_side['weight'], original_weight)
    
    def test_modify_side_only_weight(self):
        die = Die()
        original_face = die.dice_sides[0]['die_side']
        die.modify_side(1, original_face, 3.5)
        modified_side = next(side for side in die.dice_sides if side['side_id'] == 1)
        self.assertEqual(modified_side['die_side'], original_face)
        self.assertEqual(modified_side['weight'], 3.5)
    
    def test_modify_side_multiple_modifications(self):
        die = Die()
        die.modify_side(1, DiceFaces.WILDCARD, 1.5)
        die.modify_side(1, DiceFaces.TWO, 2.5)
        modified_side = next(side for side in die.dice_sides if side['side_id'] == 1)
        self.assertEqual(modified_side['die_side'], DiceFaces.TWO)
        self.assertEqual(modified_side['weight'], 2.5)

    def test_roll_returns_dice_face(self):
        die = Die()
        result = die.roll()
        self.assertIsInstance(result, DiceFaces)
    
    def test_roll_returns_valid_face(self):
        die = Die()
        result = die.roll()
        valid_faces = [side['die_side'] for side in die.dice_sides]
        self.assertIn(result, valid_faces)
    
    def test_roll_weighted_dice(self):
        die = Die()
        die.dice_sides = [{'side_id': 1, 'die_side': DiceFaces.ONE, 'weight': 100}]
        for _ in range(10):
            result = die.roll()
            self.assertEqual(result, DiceFaces.ONE)
    
    def test_roll_empty_dice_raises_error(self):
        die = Die()
        die.dice_sides = []
        with self.assertRaises(IndexError):
            die.roll()
    
    def test_roll_distribution_approximation(self):
        die = Die()
        results = [die.roll() for _ in range(1000)]
        unique_results = set(results)
        self.assertGreaterEqual(len(unique_results), 3)


if __name__ == '__main__':
    unittest.main()