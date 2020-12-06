import importlib


def test_day(test_number, file_details, test_details, benchmark):
    input_filename, part_one_answer, part_two_answer = file_details
    person_name, test_name = test_details

    test = importlib.import_module(test_name)
    part_one, part_two = benchmark(test.main, input_filename)

    assert part_one == part_one_answer
    assert part_two == part_two_answer
