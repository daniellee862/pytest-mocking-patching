from cruncher import NumberCruncher
import pytest


#>>> from cruncher import NumberCruncher
#>>> nc = NumberCruncher(3) # a NumberCruncher that can store 3 facts
#>>> nc.crunch()
#'Yum! 8100'   # stored 8100. NumberRequester is invoked from within NumberCruncher
#>>> nc.crunch()
#'Yuk! 5335'


def test_number_cruncher_likes_even_numbers():
    """Test that the crunch method saves number facts for even numbers.

    Given:
         A Number cruncher instance getting an even result for its "crunch" method (eg 42)

    Result:
        Method returns "Yum! 42"
        The tummy attribute contains a dict such as {'number': 42, "fact": "42 is the meaning of life."}
    """
    def mock_call():
        return {'number': 42, "fact": "42 is the meaning of life."}
    nc = NumberCruncher(3)
    nc.requester.call = mock_call
    assert nc.crunch() == "Yum! 42"
    assert {'number': 42, "fact": "42 is the meaning of life."} in nc.tummy
  
  
def test_number_cruncher_hates_odd_numbers():
    """Test that the crunch method rejects number facts for odd numbers.
    
    Given:
         A Number cruncher instance getting an odd result for its "crunch" method eg 13

    Result:
        Method returns "Yuk! 13"
        The tummy attribute is unchanged.
    
    """

    def mock_call():
        return {'number': 13, "fact": "13 is the meaning of life."}
    nc = NumberCruncher(3)
    nc.requester.call = mock_call
    assert nc.crunch() == "Yuk! 13"
    assert nc.tummy == []


def test_number_cruncher_discards_oldest_item_when_tummy_full():
    """Test that the crunch method maintains a maximum number of facts.
    
    Given:
         A Number cruncher instance with tummy size 3 having 3 items in tummy getting 
         an even result for its "crunch" method, eg 24.

    Result:
        Method deletes oldest result from tummy (eg 42)
        Method returns "Burp! 42"
        The tummy attribute contains 24 but not 42.
    
    """

    nc = NumberCruncher(3)
    def mock_call():
        return {'number': 12, "fact": "12 is the meaning of life."}
    nc.requester.call = mock_call
    nc.crunch()
    def mock_call():
        return {'number': 14, "fact": "14 is the meaning of laziness."}
    nc.requester.call = mock_call
    nc.crunch()
    def mock_call():
        return {'number': 16, "fact": "16 is the meaning of boredom."}
    nc.requester.call = mock_call
    nc.crunch()
    def mock_call():
        return {'number': 18, "fact": "18 is the meaning of tiredness."}
    nc.requester.call = mock_call
    nc.crunch()
    assert {'number': 12, "fact": "12 is the meaning of life."} not in nc.tummy
    assert nc.tummy[0] == {'number': 14, "fact": "14 is the meaning of laziness."}
    assert nc.tummy[2] == {'number': 18, "fact": "18 is the meaning of tiredness."}


def test_number_cruncher_raises_runtime_error_if_invalid_number_request():
    """Test that there is a runtime error if NumberRequester response is
        invalid

        Given:
            A NumberCruncher instance, receiving an invalid NumberRequester
            response (eg an AttributeError)

        Result: 
            Raises RuntimeError
    """
    with pytest.raises(RuntimeError):
        nc = NumberCruncher(3)
        nc.requester.endpoint = ''
        nc.crunch()