import itertools
from tqdm import tqdm
import numpy as np
import pandas as pd
import re
from matplotlib import pyplot as plt

class CrosswordGenerator:
    def __init__(self, word_list, size):
        print("Initializing Crossword Generator")
        self.word_list = word_list
        self.sort_words()
        self.placed_words = []
        self.n_rows, self.n_cols = size
        self.grid = None
        self.regexes_grid = None
        self.empty_grid = None
        self.column_preference = True
        self.grid = self.generate_grid()
        self.place_word_list()

    def sort_words(self):
        letters = {
            "a":0,
            "b":0,
            "c":0,
            "d":0,
            "e":0,
            "f":0,
            "g":0,
            "h":0,
            "i":0,
            "j":0,
            "k":0,
            "l":0,
            "m":0,
            "n":0,
            "o":0,
            "p":0,
            "q":0,
            "r":0,
            "s":0,
            "t":0,
            "u":0,
            "v":0,
            "w":0,
            "x":0,
            "y":0,
            "z":0
        }
        word_score = []
        for word in self.word_list:
            for character in word:
                letters[character] += 1
        for word in self.word_list:
            score = 0
            for character in word:
                score += letters[character]
            word_score.append((word, score))
        sorted_word_scores = sorted(word_score, key=lambda x: x[1], reverse=True)
        self.word_list = [word for word, score in sorted_word_scores]

    def place_word(self, word, req_crossings=True, preexisting_score=0):
        word = word.lower()

        def enlarge_grid(n):
            self.n_rows += n
            self.n_cols += n
            self.grid = self.generate_grid()
            print("new grid:")
            print(self.grid.to_string())

        def generate_fuzzy_regex(input_word):
            macro_regex = "(^"
            for character in input_word:
                micro_regex = f"({character}|0)"
                macro_regex += micro_regex
            macro_regex += ")"
            # print(macro_regex)
            return re.compile(macro_regex)

        def generate_exact_regex(input_word):
            macro_regex = f"[01]{input_word}[01]"
            return re.compile(macro_regex)

        def verify_series(series):
            import re
            s = "".join(series)

            # find every contiguous run of letters
            for m in re.finditer(r"[a-z]+", s):
                i, j = m.span()
                # must be bounded on both sides by 0/1 to be a placed word/clue fragment
                left = s[i - 1] if i > 0 else None
                right = s[j] if j < len(s) else None
                if left in "01" and right in "01":
                    inner = m.group(0)
                    if len(inner) == 1:
                        continue  # allow single-letter crossings
                    if inner.lower() not in self.word_list:
                        # print("INVALID WORD:", s[i - 1:j + 1])  # shows the [01]... [01] block
                        return False
            return True

        def verify_grid(changed_name, proposed_series, column=False):
            proposed_grid = self.grid.copy()
            if not column:
                proposed_grid.loc[changed_name] = proposed_series
            elif column:
                proposed_grid.loc[:, changed_name] = proposed_series
            else:
                raise ValueError("column must be True or False")

            for index, row in proposed_grid.iterrows():
                if not verify_series(row):
                    return False
            # print("PROPOSED_GRID:")
            # print(proposed_grid.to_string())
            for column_name, column in proposed_grid.items():
                if not verify_series(column):
                    return False
            return True

        def check_positions(series_name, word_size, column=False):
            if column:
                series = self.grid[series_name]
            else:
                series = self.grid.loc[series_name]

            # Get the values as a list
            values = series.values.tolist()
            possibles_searches = len(values) - 2 - word_size + 1

            if possibles_searches < 0:
                print("grid is too small for the word. grid must be enlarged.")
                enlarge_grid(word_size)
                return 0, None
            highest_score = preexisting_score
            best_position = None
            for x in range(possibles_searches):
                # Join the slice of values we want to check
                search = "".join(values[x:x + word_size])
                if not word_regex.fullmatch(search):
                    continue
                full_match = search
                zeros = full_match.count("0")
                ones = full_match.count("1")
                score = (2 - zeros / len(word)) * 100 + 1 - 20 * ones

                # NEW: count crossings (letters already present under the window)
                window_vals = values[x:x + word_size]
                crossings = sum(1 for c in window_vals if isinstance(c, str) and c.isalpha())

                # Check to see if it's a valuable position
                proposed_series = values[:x] + list(word) + values[x + word_size:]
                if verify_grid(series_name, proposed_series, column=column) is False:
                    continue

                # NEW: require at least one crossing once we’ve placed something
                if self.placed_words and crossings == 0 and req_crossings:
                    continue

                # NEW: reward crossings
                score += 100 * 1 ** crossings

                if score > highest_score:
                    # print(f"found a new highest score of {score} at position {x}")
                    highest_score = score
                    best_position = x

            return highest_score, best_position

        word_regex = generate_fuzzy_regex(word)
        word_size = len(word)

        highest_row_score = -100
        highest_row_position = None
        highest_column_score = -100
        highest_column_position = None

        if self.column_preference:
            # Check columns
            for col_name in self.grid.columns:
                score, position = check_positions(col_name, word_size, column=True)
                if score > highest_column_score:
                    highest_column_score = score
                    highest_column_position = (col_name, position)

            # Check rows
            for idx in self.grid.index:
                score, position = check_positions(idx, word_size, column=False)
                if score > highest_row_score:
                    highest_row_score = score
                    highest_row_position = (idx, position)
        else:
            # Check rows
            for idx in self.grid.index:
                score, position = check_positions(idx, word_size, column=False)
                if score > highest_row_score:
                    highest_row_score = score
                    highest_row_position = (idx, position)
            # Check columns
            for col_name in self.grid.columns:
                score, position = check_positions(col_name, word_size, column=True)
                if score > highest_column_score:
                    highest_column_score = score
                    highest_column_position = (col_name, position)

        # Place the word in the best position valid
        if highest_column_score > 0 or highest_row_score > 0:
            if (highest_column_position is not None and highest_column_score > highest_row_score) or \
               (highest_column_position is not None and highest_column_score == highest_row_score and self.column_preference):
                # Place vertically
                col, pos = highest_column_position
                if pos is not None:  # Add this check
                    word_in_position = [[col, pos+row, letter, highest_column_score] for row, letter in enumerate(word)]
                    self.placed_words.append(word_in_position)
                    return True
            elif highest_row_position is not None:  # Add this check
                # Place horizontally
                row, pos = highest_row_position
                if pos is not None:  # Add this check
                    word_in_position = [[pos+col, row, letter, highest_row_score] for col, letter in enumerate(word)]
                    self.placed_words.append(word_in_position)
                    return True
        return False

    def place_word_list(self):
        MAX_PLACEMENT_ATTEMPTS = 10
        # self.generate_regex_grid()
        number_of_attempts_made = [0 for _ in range(len(self.word_list))]
        unplaced_words = [[word, attempts] for word, attempts in zip(self.word_list.copy(), number_of_attempts_made)]
        print(unplaced_words)
        pbar = tqdm(total=len(self.word_list)+1)
        pbar.set_description("Placing Words")
        while unplaced_words:
            word = unplaced_words.pop(0)
            self.column_preference = not self.column_preference
            if self.place_word(word[0]):
                self.grid = self.generate_grid()
                pbar.update(1)
                continue
            else:
                if word[1] == MAX_PLACEMENT_ATTEMPTS:
                    print(f"unable to place {word[0]} after {MAX_PLACEMENT_ATTEMPTS} attempts, final chance...")
                    if self.place_word(word[0], req_crossings=False):
                        print("Updated Grid:")
                        self.grid = self.generate_grid()
                        print("successfully placed word! resetting tries on remaining words")
                        number_of_attempts_made = [0 for _ in range(len(self.word_list))]
                        unplaced_words = [[word, attempts] for word, attempts in zip(self.word_list.copy(), number_of_attempts_made)]
                    continue
                unplaced_words.append([word[0], word[1] + 1])

    def replace_word_list(self):
        local_word_list = self.placed_words.copy()
        for word in local_word_list:
            word_backup = word.copy()
            # Extract the score (position 3) from each letter's data
            score_to_beat = int(word[0][3])

            # Extract the letters (position 2) from each letter's data
            letters = [letter[2] for letter in word]
            complete_word = ''.join(letters)
            print(f"Word: {complete_word}, Score: {score_to_beat}")
            self.placed_words.remove(word)
            self.generate_grid()
            if not self.place_word(complete_word, req_crossings=True, preexisting_score=score_to_beat):
                self.placed_words.append(word_backup)
                self.generate_grid()
                print("Failed to replace word. Reverting to original word.")
                continue


    def generate_grid(self):
        grid = pd.DataFrame(np.zeros((self.n_rows + 2, self.n_cols + 2)), columns=range(self.n_cols + 2),
                            index=range(self.n_rows + 2)).map(int).map(str)
        grid.loc[0, :] = "1"
        grid.loc[-1, :] = "1"
        grid.loc[:, 0] = "1"
        grid.loc[:, -1] = "1"
        if self.placed_words:
            for word in self.placed_words:
                # word should be a list of letters and their positions
                for letters in word:
                    grid.loc[letters[1], letters[0]] = letters[2]
            # so now we've generated the grid and placed all the letters.
        return grid

    def render_grid(self, save_path=None, key = True):
        """
        Render the crossword grid using matplotlib

        Parameters:
            save_path (str, optional): If provided, saves the image to this path
        """
        plt.cla()
        # Convert grid to numpy array for plotting
        grid_array = self.grid.to_numpy()

        # Create figure and axis
        fig, ax = plt.subplots(figsize=(10, 10))

        # Hide the axes
        ax.set_xticks([])
        ax.set_yticks([])

        # Create the grid
        for i in range(grid_array.shape[0]):
            for j in range(grid_array.shape[1]):
                cell_value = grid_array[i, j]
                cell_color = 'black' if cell_value in ['1', '0'] else 'white'

                # Draw cell
                ax.add_patch(plt.Rectangle((j, -i-2), 1, 1, facecolor=cell_color, edgecolor='black'))

                # Add text if it's a letter
                if cell_value not in ['0', '1']:
                    ax.text(j + 0.5, - i - 1.5, cell_value.upper(),
                            ha='center', va='center', color='black',
                            fontsize=14, fontweight='bold')

        # Set the plot limits
        ax.set_xlim(0, grid_array.shape[1])
        ax.set_ylim(-grid_array.shape[0], 0)

        # Make sure the aspect ratio is equal
        ax.set_aspect('equal')

        # Add title
        plt.title('Crossword Grid', pad=20)

        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
            plt.close()
        else:
            plt.show()


if __name__ == "__main__":
    print("This is the crossword generator")
    word_list = [
        "apple", "river", "mountain", "shadow", "crystal", "ember", "storm", "lantern", "whisper", "garden", "velvet",
        "thunder", "canyon", "frost", "mirror", "flame", "willow", "ocean", "dusk", "horizon", "anchor", "bridge",
        "harbor", "island", "meadow", "prairie", "forest", "valley", "summit", "glacier", "breeze", "raven", "solace",
        "harvest", "voyage", "serpent", "beacon", "oracle", "cascade", "twilight", "aurora", "echo", "spire", "haven",
        "marble", "obsidian", "petal", "stream", "tidal", "gale", "copper", "amber", "onyx", "drift", "hollow", "grove",
        "ivory", "chorus", "meander", "wild", "bloom", "flint", "tundra", "delta", "luster", "rift", "plume", "cinder",
        "wander", "brine", "coral", "mirage", "solstice", "azure", "verdant", "opal", "bastion", "cavern"
    ]
    cg = CrosswordGenerator(word_list, (15, 15))
    cg.render_grid()
    # cg.replace_word_list()
    # cg.render_grid()
    print(cg.grid.to_string())