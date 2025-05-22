from anl2025 import anl2025_tournament
from helpers.helperfunctions import make_multideal_scenario

def run_a_tournament(TestedNegotiator, n_repetitions=5, debug=False, nologs=False, small=False):
    """Runs a tournament to test the agent."""
    scenarios = [make_multideal_scenario(nedges=3, nissues=2, nvalues=2) for _ in range(1)]
    scenariosbig = [make_multideal_scenario(nedges=3) for _ in range(2)]

    if small:
        anl2025_tournament(
            competitors=tuple([TestedNegotiator]),
            scenarios=scenarios,
            n_repetitions=1,
            n_jobs=-1 if debug else 0,
            verbose=False,
        ).final_scores
    else:
        anl2025_tournament(
            competitors=tuple([TestedNegotiator]),
            scenarios=scenariosbig,
            n_repetitions=n_repetitions,
            n_jobs=-1 if debug else 0,
            verbose=True,
        ).final_scores
