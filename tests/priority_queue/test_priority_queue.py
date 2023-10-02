from ting_file_management.priority_queue import PriorityQueue
import pytest


mock = [
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": []
    },
    {
        "nome_do_arquivo": "arquivo_teste.txt",
        "qtd_linhas": 10,
        "linhas_do_arquivo": []
    }
]


def test_basic_priority_queueing():
    pq = PriorityQueue()
    assert pq.is_priority(mock[1]) is False
    assert pq.is_priority(mock[0]) is True

    pq.enqueue(mock[0])
    pq.enqueue(mock[1])
    assert len(pq.high_priority) == 1
    assert len(pq.regular_priority) == 1

    assert pq.search(0) == mock[0]
    # assert pq.search(1) == mock[1]

    pq.dequeue()
    assert len(pq.high_priority) == 0
    # assert len(pq.regular_priority) == 1

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        pq.search(10)
