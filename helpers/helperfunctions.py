def find_best_bid_in_outcomespace(self):
    """Finds the best bid available from the outcome space."""
    updated_outcomes = all_possible_bids_with_agreements_fixed(self)
    mn, mx = float("inf"), float("-inf")
    worst, best = None, None
    for o in updated_outcomes:
        u = self.ufun(o)
        if u < mn:
            worst, mn = o, u
        if u > mx:
            best, mx = o, u
    return best
