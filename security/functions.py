def selected_to_controlled(applist, app_id):
    return True if applist.get_random().id == app_id else False


def quantities_are_equal(quantities: list):
    return True if len(set(quantities)) == 1 else False


def prices_are_equal(prices: list):
    return True if len(set(prices)) == 1 else False


def units_are_equal(units: list):
    return True if len(set(units)) == 1 else False
