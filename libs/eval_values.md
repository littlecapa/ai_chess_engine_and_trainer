EVAL Values:

- Classical Engine Evaluations like +1.22 are multiplied with 100
- Evaluations > EVAL_LIMIT (15.0) are cut down with LOG10 Function
- Evaluations and Distance to Mate are seperated.
-- Distance to Mate from Tablebases is converted to Evaluation with these rules:
--- Distance == 1: This actually means that the mate move has been played. Evaluation is set IS_MATE
--- Distance > 1: Min evaluation is MIN_FORCED_MATE (2500); for (Distances-1) < MAX_MATE_STEPS (100 Halfmoves) the bonus MATE_STEP (1) per step is added 

UNIT-Tests:
    tests_mate = [0, 1, 2, 3, 4, 52, 51, 50, 49, 18, 17, 16, 15, +22, -1, -2, -50, -51, -52, 98, 99, 100, 101, 102]
    tests_mate_results = [0.0, get_is_mate_value(), get_mate_in_one_value(), 12300, 12200, 7400, 7500, 7600, 7700, 10800, 10900, 11000, 11100, 10400, -get_is_mate_value(), -12500, -7600, -7500, -7400, 2800, 2700, 2600, 2500, 2500]


To Do: 
- Table Base is using half moves for distance to mate
- What is Stockfish using?