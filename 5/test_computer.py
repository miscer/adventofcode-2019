from computer import get_opcode_modes, read_instruction


def test_get_opcode_modes():
    assert get_opcode_modes(1002, 3) == [0, 1, 0]
    assert get_opcode_modes(11102, 3) == [1, 1, 1]
    assert get_opcode_modes(10002, 3) == [0, 0, 1]
    assert get_opcode_modes(1101, 3) == [1, 1, 0]


def test_read_instruction():
    assert read_instruction([1, 2, 3, 4], 0) == (1, [(0, 2), (0, 3), (0, 4)], 4)
    assert read_instruction([1, 2, 3, 104, -1], 3) == (4, [(1, -1)], 5)
    assert read_instruction([99], 0) == (99, [], 1)
