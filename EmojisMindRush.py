import os
import random
import time


# ==============================
#        EMOJIS HUNT
# ==============================

EMOJIS = ["😀", "🔥", "🚀", "🎮", "⭐"]

START_TIME = 5.0
MIN_TIME = 1.0
TIME_DECREASE = 0.5
POINTS_PER_ROUND = 10


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def create_arrays():
    """Create two independently shuffled emoji arrays."""
    array1 = EMOJIS.copy()
    array2 = EMOJIS.copy()

    random.shuffle(array1)
    random.shuffle(array2)

    return array1, array2


def display_array(array, name):
    """Display an emoji array with numbered positions."""
    print(f"\n{name}:")

    for position, emoji in enumerate(array, start=1):
        print(f"{position}: {emoji}", end="   ")

    print()


def display_arrays(array1, array2):
    """Display both emoji arrays."""
    print("\n🎯 EMOJIS HUNT")
    print("=" * 40)

    display_array(array1, "Array 1")
    display_array(array2, "Array 2")

    print()


def get_position(emoji, array_number, array_length):
    """Get and validate the player's position input."""
    while True:
        try:
            position = int(
                input(
                    f"📍 Position of {emoji} "
                    f"in Array {array_number}: "
                )
            )

            if 1 <= position <= array_length:
                return position

            print(
                f"⚠️ Please enter a position "
                f"between 1 and {array_length}."
            )

        except ValueError:
            print("⚠️ Please enter a valid number.")


def play_round(display_time, score):
    """Play one complete round."""
    array1, array2 = create_arrays()

    clear_screen()

    display_arrays(array1, array2)

    print("🧠 Memorize the emoji positions!")
    print(f"⏱️ You have {display_time:.1f} seconds...")

    time.sleep(display_time)

    clear_screen()

    # Target is intentionally revealed AFTER the arrays disappear.
    target = random.choice(EMOJIS)

    print("=" * 40)
    print("🎯 MEMORY CHALLENGE")
    print("=" * 40)

    print(f"\nFind the position of: {target}\n")

    array_length = len(array1)

    position1 = get_position(
        target,
        1,
        array_length
    )

    position2 = get_position(
        target,
        2,
        array_length
    )

    correct_position1 = array1.index(target) + 1
    correct_position2 = array2.index(target) + 1

    if (
        position1 == correct_position1
        and position2 == correct_position2
    ):
        score += POINTS_PER_ROUND

        print("\n✅ CORRECT!")
        print(f"🏆 Score: {score}")

        return True, score

    print("\n❌ WRONG ANSWER!")

    print(
        f"📍 Correct position in Array 1: "
        f"{correct_position1}"
    )

    print(
        f"📍 Correct position in Array 2: "
        f"{correct_position2}"
    )

    print(f"\n🏆 Final Score: {score}")

    return False, score


def show_start_screen():
    """Display the game's start screen."""
    clear_screen()

    print("=" * 40)
    print("          🎯 EMOJIS HUNT")
    print("=" * 40)

    print("\n🧠 Test your short-term memory!")
    print("👀 Memorize the emoji positions.")
    print("🎯 A target emoji will be shown after")
    print("   the arrays disappear.")
    print("❌ One wrong answer ends the game.")

    input("\nPress ENTER to start...")


def show_game_over(score, rounds_completed):
    """Display the final game-over screen."""
    print("\n" + "=" * 40)
    print("             💀 GAME OVER")
    print("=" * 40)

    print(f"\n🏆 Final Score: {score}")
    print(f"🎯 Rounds Completed: {rounds_completed}")

    print("\nThanks for playing Emojis Hunt! 🧠🎯")


def main():
    """Main game loop."""
    score = 0
    round_number = 1
    display_time = START_TIME

    try:
        show_start_screen()

        while True:
            clear_screen()

            print("=" * 40)
            print(f"              ROUND {round_number}")
            print("=" * 40)

            time.sleep(1)

            success, score = play_round(
                display_time,
                score
            )

            if not success:
                break

            round_number += 1

            # Reduce display time after every successful round.
            display_time = max(
                MIN_TIME,
                display_time - TIME_DECREASE
            )

            print("\n🚀 Next round is starting...")
            print(
                f"⏱️ Next memorization time: "
                f"{display_time:.1f} seconds"
            )

            time.sleep(2)

        show_game_over(
            score,
            round_number - 1
        )

    except KeyboardInterrupt:
        clear_screen()

        print("\n" + "=" * 40)
        print("        👋 GAME INTERRUPTED")
        print("=" * 40)

        print(f"\n🏆 Score: {score}")
        print(f"🎯 Rounds Completed: {round_number - 1}")

        print("\nThanks for playing Emojis Hunt! 🎯")


if __name__ == "__main__":
    main()
    
