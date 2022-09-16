import pytest


@pytest.mark.parametrize(
    argnames='total_height, day_displacement, night_displacement, days_to_go_correct',
    argvalues=[
        (10, 3, 2, 8),
        (20, 7, 3, 5),
        (19, 7, 3, 4),
        (10, 6, 0, 2),
        (10, 10, 0, 1),
        (10, 100, 0, 1),
        (31, 10, 5, 6),
        (29, 10, 5, 5),
        (93, 17, 5, 8),
        (98, 17, 5, 8)
    ]
)
def test_snail(total_height, day_displacement, night_displacement, days_to_go_correct):
    whole_days_distance = total_height - day_displacement
    one_day_displacement = day_displacement - night_displacement
    # number of complete days of forward and back motion
    # +
    # 1 for day in which snail will approach finish line
    # +
    # 1 for last day, which was subtracted from whole_days_distance
    total_days = (whole_days_distance // one_day_displacement) + int(
        whole_days_distance % one_day_displacement != 0) + 1
    assert total_days == days_to_go_correct
