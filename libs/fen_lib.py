CASTLING_OPTIONS = ["k", "q", "K", "Q"]

def split_fen(fen_str):
    parts = fen_str.split()

    # Extracting individual components
    position = parts[0]
    color_to_move = parts[1]
    castling_options = parts[2]
    en_passant_square = parts[3]
    halfmove_clock = int(parts[4])
    fullmove_clock = int(parts[5])

    return position, color_to_move, castling_options, en_passant_square, halfmove_clock, fullmove_clock

def flip_color_to_move(color_to_move):
    if color_to_move == "w":
        return "b"
    return "w"

def get_ranks_from_fen(position_string):
    return position_string.split('/')

def flip_color_position(position_string):
    new_position_string = ""
    for rank in reversed(get_ranks_from_fen(position_string)):
        if new_position_string != "":
            new_position_string += "/"
        new_rank = flip_color_rank(rank)
        new_position_string += new_rank
    return new_position_string 

def flip_color_rank(rank_string):
    new_string = ""
    for char in rank_string:
        if char.islower():
            new_string += char.upper()
        elif char.isupper():
            new_string += char.lower()
        else:
            new_string += char
    return new_string

def flip_castling_options(castling_options):
    flip_str =""
    for index, option in enumerate(CASTLING_OPTIONS):
        if option in castling_options:
            flip_str += option.swapcase()
        else:
            flip_str += "-"    
    return flip_str

def split_chess_square(square_str):
    file = square_str[0]
    rank = int(square_str[1])
    return file, rank

def flip_en_passant_square(square_string):
    if square_string == "-":
        return "-"
    file, rank = split_chess_square(square_string)
    return file + str(9-rank)

def flip_color(fen_string):
    position, color_to_move, castling_options, en_passant_square, halfmove_clock, fullmove_clock = split_fen(fen_string)
    return flip_color_position(position) + " " + \
            flip_color_to_move(color_to_move) + " " + \
            flip_castling_options(castling_options) + " " + \
            flip_en_passant_square(en_passant_square) + " " + \
            str(halfmove_clock) + " " + str(fullmove_clock)
