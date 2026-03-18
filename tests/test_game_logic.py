from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Tests targeting the off-by-one bug in update_score win bonus:
# The bug was `100 - 10 * (attempt_number + 1)` instead of `100 - 10 * attempt_number`,
# which silently deducted 10 extra points from every winning score.

def test_win_score_attempt_1():
    # Winning on attempt 1: should earn 100 - 10*1 = 90 points, not 80 (the bugged value)
    score = update_score(current_score=0, outcome="Win", attempt_number=1)
    assert score == 90

def test_win_score_attempt_3():
    # Winning on attempt 3: should earn 100 - 10*3 = 70 points, not 60 (the bugged value)
    score = update_score(current_score=0, outcome="Win", attempt_number=3)
    assert score == 70

def test_win_score_accumulates_correctly():
    # Score from previous guesses should be preserved and the correct win bonus added
    score = update_score(current_score=25, outcome="Win", attempt_number=2)
    # expected: 25 + (100 - 10*2) = 25 + 80 = 105
    assert score == 105
