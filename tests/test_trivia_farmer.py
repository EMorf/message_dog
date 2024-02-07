from src.trivia_farmer import TriviaAnswer

def test_trivia_object():
    """Simple test to verify behaviour of underlying data structure
    """    

    ta = TriviaAnswer("qa-pairs")
    ta.set_data("2 + 2 = ?", "4")
    assert ta.get_answer("2 + 2 = ?") == "4"


    assert ta.get_answer("Hello?") == ""

    t_q = "This is a test generator".split(" ")

    t_a = "This is a test answer".split(" ")

    for i, j in enumerate(t_q):
        assert ta.set_data(j, t_a[i])

    assert ta.get_answer("This") == "This"
