from datetime import timedelta

from django.utils.timezone import now

from tests.factories.cycles import CycleFactory


def create_5_cycles_batch():
    start_date = now().date()
    end_date = start_date + timedelta(days=5)
    cycles = [
        (timedelta(days=-2 * 365), False),
        (timedelta(days=-365), False),
        (timedelta(days=0), True),
        (timedelta(days=365), False),
        (timedelta(days=2 * 365), False),
    ]
    for delta, is_active in cycles:
        CycleFactory(
            start_date=start_date + delta,
            end_date=end_date + delta,
            is_the_active_one=is_active,
        )
