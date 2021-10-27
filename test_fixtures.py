# import pytest

# @pytest.fixture
# def empty_list():
#     return []

# def test_len_of_empty_list(empty_list):
#     #what is isinstance doing here? checking that empty_list is a list
#     assert isinstance(empty_list, list)
#     assert len(empty_list) == 0

# @pytest.fixture
# def one_item(empty_list):
#     #fixtures can be used as paramaters in subsequent fixtures (?)
#     #"by adding paramaters to our fixures we can modularize our fixture setup,
#     #letting us use same parts of our setup in different customized setups 
#     # for a greater variety of tests"
#     empty_list.append("item")
#     return empty_list

# def test_len_of_unary_list(one_item):
#     assert isinstance(one_item, list)
#     assert len(one_item) == 1
#     assert one_item[0] == "item"

# class FancyObject:
#     def __init__(self):
#         self.fancy = True
#         print(f"\nFancyObject: {self.fancy}")

#     def or_is_it(self):
#         self.fancy = not self.fancy 

#     def cleanup(self):
#         print(f"\ncleanup: {self.fancy}")

# @pytest.fixture
# def so_fancy():
#     fancy_object = FancyObject()
#     #what is yield? python keyword that lets functions 
#     #suspend themselves, optionally returning a value
#     #so they can resume from the same spot later
#     yield fancy_object
#     #yield used for working with generators and coroutines,
#     #should not be sued in regular functions
#     #only used in the context of fixtures (in the scope of this curriculum)
#     fancy_object.cleanup()

# def test_so_fancy(so_fancy):
#     assert so_fancy.fancy

#     so_fancy.or_is_it()

#     assert not so_fancy.fancy

