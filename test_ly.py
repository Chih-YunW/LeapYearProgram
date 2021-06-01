import leapYear

def test_not_divisible_by_4():
	value = (1999)
        assert leapYear.leapYear(value) == "It is not a leap year"
def test_divisible_by_4_not_100():
        value = (2040)
        assert leapYear.leapYear(value) == "It is a leap year"


