from negmas import Outcome, ResponseType
from anl2025.negotiator import ANL2025Negotiator
from helpers.helperfunctions import set_id_dict, did_negotiation_end, get_target_bid_at_current_index, is_edge_agent, find_best_bid_in_outcomespace

class Group3Agent(ANL2025Negotiator):
    def init(self):
        """Executed when the agent is created. Initializes negotiation parameters."""
        self.current_neg_index = -1
        self.target_bid = None
        self.id_dict = {}
        set_id_dict(self)

    def propose(self, negotiator_id: str, state, dest: str = None) -> Outcome | None:
        """Proposes to the given partner using the side negotiator."""
        if did_negotiation_end(self):
            self._update_strategy()

        bid = get_target_bid_at_current_index(self)
        return bid

    def respond(self, negotiator_id: str, state, source: str = None) -> ResponseType:
        """Responds to the partner's offer."""
        if did_negotiation_end(self):
            self._update_strategy()

        if state.current_offer is get_target_bid_at_current_index(self):
            return ResponseType.ACCEPT_OFFER
        return ResponseType.REJECT_OFFER

    def _update_strategy(self):
        """Updates the agent's strategy after each negotiation."""
        if is_edge_agent(self):
            _, best_bid = self.ufun.extreme_outcomes()
        else:
            best_bid = find_best_bid_in_outcomespace(self)
        self.target_bid = best_bid
