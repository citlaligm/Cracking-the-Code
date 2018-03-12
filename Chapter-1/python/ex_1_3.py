def URLify(str_in,n):
    ulr_part = str_in.split()
    return "%20".join(ulr_part)


def test_URLify():
    str_in = "Mr John Smith"
    str_out = "Mr%20John%20Smith"
    assert URLify(str_in,13) == str_out

