from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    data = [
        {'qtd_linhas': 7}, {'qtd_linhas': 6}, {'qtd_linhas': 1},
        {'qtd_linhas': 2}, {'qtd_linhas': 3},
    ]

    q = PriorityQueue()

    q.enqueue(data[1])
    q.enqueue(data[2])
    q.enqueue(data[3])
    q.enqueue(data[4])
    q.enqueue(data[0])

    assert len(q) == 5
    assert q.search(2) == data[4]
    assert q.search(3) == data[1]

    with pytest.raises(IndexError):
        q.search(10)

    assert q.dequeue() == data[2]
    assert q.dequeue() == data[3]
    assert q.dequeue() == data[4]
    assert q.dequeue() == data[1]
    assert q.dequeue() == data[0]

    assert len(q) == 0

    q.enqueue(data[0])
    q.enqueue(data[1])

    assert len(q) == 2
