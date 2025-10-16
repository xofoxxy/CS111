import itertools

import numpy as np
import pandas as pd
import regex as re
from pandas import Index


class CrosswordGenerator:
    def __init__(self, word_list):
        print("Initializing Crossword Generator")
        self.word_list = word_list
        self.placed_words = None
        self.n_rows = 2
        self.n_cols = 2
        self.grid = None
        self.regexes_grid = None
        self.empty_grid = None
        self.grid = self.generate_grid()
        self.place_word_list()

    def place_word(self, word):
        def enlarge_grid(n):
            self.n_rows += n
            self.n_cols += n
            self.grid = self.generate_grid()
            print("new grid:")
            print(self.grid.to_string())

        # def verify_grid():
        #     for row in self.grid:
        #         string = "".join(row)
        #         string_list = string.split("0").remove("0")
        #         if string

        def generate_regex(input_word):
            macro_regex = "("
            for character in input_word:
                micro_regex = f"({character}|0)"
                macro_regex += micro_regex
            macro_regex += ")"
            print(macro_regex)
            return re.compile(macro_regex)

        def check_positions(series, word_size):
            highest_score = 0
            best_position = None
            
            # Get the values as a list
            values = series.values.tolist()
            possibles_searches = len(values) - word_size + 1
            
            if possibles_searches < 0:
                print("grid is too small for the word. grid must be enlarged.")
                enlarge_grid(word_size)
                return 0, None
            
            for x in range(possibles_searches):
                # Join the slice of values we want to check
                search = "".join(values[x:x + word_size])
                reg_match = re.findall(word_regex, search)
                # print(reg_match)
                if reg_match:
                    score = len(reg_match)
                    if score > highest_score:
                        highest_score = score
                        best_position = x
                    
            return highest_score, best_position

        word_regex = generate_regex(word)
        word_size = len(word)
        
        # Check columns
        highest_column_score = 0
        highest_column_position = None
        
        for col_name in self.grid.columns:
            score, position = check_positions(self.grid[col_name], word_size)
            if score > highest_column_score:
                highest_column_score = score
                highest_column_position = (col_name, position)
        
        # Check rows
        highest_row_score = 0
        highest_row_position = None
        
        for idx in self.grid.index:
            score, position = check_positions(self.grid.loc[idx], word_size)
            if score > highest_row_score:
                highest_row_score = score
                highest_row_position = (idx, position)
        
        # Place the word in the best position found
        # print(f"highest column score: {highest_column_score}")
        # print(f"highest row score: {highest_row_score}")
        if highest_column_score > 0 or highest_row_score > 0:
            if highest_column_score >= highest_row_score:
                # Place vertically
                col, pos = highest_column_position
                for i, letter in enumerate(word):
                    self.grid.loc[pos + i, col] = letter
                return True
            else:
                # Place horizontally
                row, pos = highest_row_position
                for i, letter in enumerate(word):
                    self.grid.loc[row, pos + i] = letter
                return True
        return False


    def place_word_list(self):
        MAX_PLACEMENT_ATTEMPTS = 10
        # self.generate_regex_grid()
        number_of_attempts_made = [0 for _ in range(len(self.word_list))]
        unplaced_words = [[word, attempts] for word, attempts in zip(self.word_list.copy(), number_of_attempts_made)]
        print(unplaced_words)
        while unplaced_words:
            word = unplaced_words.pop(0)
            if self.place_word(word[0]):
                #self.generate_regex_grid()
                # self.placed_words.append(constructed_regex)
                continue
            else:
                if word[1] == MAX_PLACEMENT_ATTEMPTS:
                    print(f"unable to place {word[0]} after {MAX_PLACEMENT_ATTEMPTS} attempts")
                    continue
                unplaced_words.append([word[0], word[1] + 1])

    def generate_grid(self):
        grid = pd.DataFrame(np.zeros((self.n_rows, self.n_cols)), columns=range(self.n_cols),
                            index=range(self.n_rows)).map(int).map(str)
        if self.placed_words:
            for word in self.placed_words:
                # word should be a list of letters and their positions
                for letters in word:
                    grid.loc[letters[1], letters[0]] = letters[2]
            # so now we've generated the grid and placed all the letters.
            return grid
        else:
            return grid


if __name__ == "__main__":
    print("This is the crossword generator")
    cg = CrosswordGenerator(["hello", "world", "this", "is", "a", "test"])
    print(cg.grid.to_string())