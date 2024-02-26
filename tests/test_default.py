from lib.messages import error, success


def test_s1_ch2(a, b, number):
    messages = [
        'це на так',
        'то не так!'
    ]
    if a + b == number:
        print(success())
    else:
        print(error(error_descriptions=[messages]))

