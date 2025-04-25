
import ply.lex as lex
from tokens import tokens

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Función para reconocer palabras clave (keywords)
def t_KEYWORD(t):
    r'[WwVv]{2}'  # Dos caracteres W, w, V, o v
    if t.value in keyword_lexemes:
        t.type = keyword_lexemes[t.value]  # Asigna el tipo basado en el lexema
    return t

# Función para números hexadecimales


def t_HEX(t):
    r'[OoCc]{2}'  # Dos caracteres O, o, C, o c
    if t.value in hex_lexemes:
        t.type = hex_lexemes[t.value]
    return t

# Función para operadores definidos por combinaciones de I, L, T


def t_OPERATOR(t):
    r'[ILT]{2}'  # Dos caracteres I, L, o T
    if t.value in operator_lexemes:
        t.type = operator_lexemes[t.value]
    return t

# Función para caracteres especiales definidos por combinaciones de Z, z


def t_CHAR(t):
    r'[zZ]{8}'  # Captura combinaciones de 8 caracteres z/Z
    # Asigna el tipo correspondiente o 'UNKNOWN_CHAR'
    t.type = char_lexemes.get(t.value, 'UNKNOWN_CHAR')
    return t


# Función para caracteres especiales definidos por combinaciones de Z, z


def t_SPECIALSYMBOL(t):
    r'[();{}\[\]]'  # Corresponde a los símbolos especiales definidos
    if t.value in specialSymbol_lexemes:
        t.type = specialSymbol_lexemes[t.value]
    return t


# Regla genérica para identificadores
def t_IDENTIFIER(t):
    r'[bd][bd]*'
    return t

# Manejo de errores


def t_error(t):
    print(f"Token inválido: {t.value[0]} en línea {t.lineno}")
    t.lexer.skip(1)

# Manejo de nuevas líneas


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Construir el lexer
lexer = lex.lex()

# Diccionarios de lexemas
keyword_lexemes = {
    'WW': 'ENTERO',
    'Ww': 'FLOTANTE',
    'WV': 'STRING',
    'Wv': 'IF',
    'wW': 'WHILE',
    'ww': 'RETURN',
    'wV': 'NULL',
    'wv': 'BREAK',
    'Vv': 'ELSE',
    'Vw': 'SWITCH',
    'VV': 'CASE',
    'Vv': 'DEFAULT',
    'vW': 'Array',
    'vw': 'PRINT',
    'vV': 'TRUE',
    'vv': 'FALSE'
}

hex_lexemes = {
    'OO': 'HEX_0',
    'Oo': 'HEX_1',
    'OC': 'HEX_2',
    'Oc': 'HEX_3',
    'oO': 'HEX_4',
    'oo': 'HEX_5',
    'oC': 'HEX_6',
    'oc': 'HEX_7',
    'CO': 'HEX_8',
    'Co': 'HEX_9',
    'CC': 'HEX_A',
    'cO': 'HEX_C',
    'co': 'HEX_D',
    'cC': 'HEX_E',
    'cc': 'HEX_F'
}

operator_lexemes = {
    'II': 'PLUS_OP',
    'IL': 'MINUS_OP',
    'IT': 'MULT_OP',
    'LI': 'DIV_OP',
    'LL': 'ASSIGN_OP',
    'LT': 'EQ_OP',
    'TI': 'MORE_OP',
    'TL': 'LESS_OP',
    'TT': 'NE_OP'
}

char_lexemes = {
    'zzzzzzzz': 'NULL_CHAR',
    'zzzzzzzZ': 'SOH_CHAR',
    'zzzzzzZz': 'STX_CHAR',
    'zzzzzzZZ': 'ETX_CHAR',
    'zzzzzZzz': 'EOT_CHAR',
    'zzzzzZzZ': 'ENQ_CHAR',
    'zzzzzZZz': 'ACK_CHAR',
    'zzzzzZZZ': 'BEL_CHAR',
    'zzzzZzzz': 'BS_CHAR',
    'zzzzZzzZ': 'HT_CHAR',
    'zzzzZzZz': 'LF_CHAR',
    'zzzzZzZZ': 'VT_CHAR',
    'zzzzZZzz': 'FF_CHAR',
    'zzzzZZzZ': 'CR_CHAR',
    'zzzzZZZz': 'SO_CHAR',
    'zzzzZZZZ': 'SI_CHAR',
    'zzzZzzzz': 'DLE_CHAR',
    'zzzZzzzZ': 'DC1_CHAR',
    'zzzZzzZz': 'DC2_CHAR',
    'zzzZzzZZ': 'DC3_CHAR',
    'zzzZzZzz': 'DC4_CHAR',
    'zzzZzZzZ': 'NAK_CHAR',
    'zzzZzZZz': 'SYN_CHAR',
    'zzzZzZZZ': 'ETB_CHAR',
    'zzzZZzzz': 'CAN_CHAR',
    'zzzZZzzZ': 'EM_CHAR',
    'zzzZZzZz': 'SUB_CHAR',
    'zzzZZzZZ': 'ESC_CHAR',
    'zzzZZZzz': 'FS_CHAR',
    'zzzZZZzZ': 'GS_CHAR',
    'zzzZZZZz': 'RS_CHAR',
    'zzzZZZZZ': 'US_CHAR',
    'zzZzzzzz': 'SPACE_CHAR',
    'zzZzzzzZ': 'EXCLAMATION_CHAR',
    'zzZzzzZz': 'DOUBLE_QUOTE_CHAR',
    'zzZzzzZZ': 'HASH_CHAR',
    'zzZzzZzz': 'DOLLAR_CHAR',
    'zzZzzZzZ': 'PERCENT_CHAR',
    'zzZzzZZz': 'AMPERSAND_CHAR',
    'zzZzzZZZ': 'SINGLE_QUOTE_CHAR',
    'zzZzZzzz': 'LPAREN_CHAR',
    'zzZzZzzZ': 'RPAREN_CHAR',
    'zzZzZzZz': 'ASTERISK_CHAR',
    'zzZzZzZZ': 'PLUS_CHAR',
    'zzZzZZzz': 'COMMA_CHAR',
    'zzZzZZzZ': 'MINUS_CHAR',
    'zzZzZZZz': 'DOT_CHAR',
    'zzZzZZZZ': 'SLASH_CHAR',
    'zzZZzzzz': 'ZERO_CHAR',
    'zzZZzzzZ': 'ONE_CHAR',
    'zzZZzzZz': 'TWO_CHAR',
    'zzZZzzZZ': 'THREE_CHAR',
    'zzZZzZzz': 'FOUR_CHAR',
    'zzZZzZzZ': 'FIVE_CHAR',
    'zzZZzZZz': 'SIX_CHAR',
    'zzZZzZZZ': 'SEVEN_CHAR',
    'zzZZZzzz': 'EIGHT_CHAR',
    'zzZZZzzZ': 'NINE_CHAR',
    'zzZZZzZz': 'COLON_CHAR',
    'zzZZZzZZ': 'SEMICOLON_CHAR',
    'zzZZZZzz': 'LESS_THAN_CHAR',
    'zzZZZZzZ': 'EQUALS_CHAR',
    'zzZZZZZz': 'GREATER_THAN_CHAR',
    'zzZZZZZZ': 'QUESTION_MARK_CHAR',
    'zZzzzzzz': 'AT_CHAR',
    'zZzzzzzZ': 'A_CHAR',
    'zZzzzzZz': 'B_CHAR',
    'zZzzzzZZ': 'C_CHAR',
    'zZzzzZzz': 'D_CHAR',
    'zZzzzZzZ': 'E_CHAR',
    'zZzzzZZz': 'F_CHAR',
    'zZzzzZZZ': 'G_CHAR',
    'zZzzZzzz': 'H_CHAR',
    'zZzzZzzZ': 'I_CHAR',
    'zZzzZzZz': 'J_CHAR',
    'zZzzZzZZ': 'K_CHAR',
    'zZzzZZzz': 'L_CHAR',
    'zZzzZZzZ': 'M_CHAR',
    'zZzzZZZz': 'N_CHAR',
    'zZzzZZZZ': 'O_CHAR',
    'zZzZzzzz': 'P_CHAR',
    'zZzZzzzZ': 'Q_CHAR',
    'zZzZzzZz': 'R_CHAR',
    'zZzZzzZZ': 'S_CHAR',
    'zZzZzZzz': 'T_CHAR',
    'zZzZzZzZ': 'U_CHAR',
    'zZzZzZZz': 'V_CHAR',
    'zZzZzZZZ': 'W_CHAR',
    'zZzZZzzz': 'X_CHAR',
    'zZzZZzzZ': 'Y_CHAR',
    'zZzZZzZz': 'Z_CHAR',
    'zZzZZzZZ': 'LBRACKET_CHAR',
    'zZzZZZzz': 'BACKSLASH_CHAR',
    'zZzZZZzZ': 'RBRACKET_CHAR',
    'zZzZZZZz': 'CARET_CHAR',
    'zZzZZZZZ': 'UNDERSCORE_CHAR',
    'zZZzzzzz': 'BACKTICK_CHAR',
    'zZZzzzzZ': 'a_CHAR',
    'zZZzzzZz': 'b_CHAR',
    'zZZzzzZZ': 'c_CHAR',
    'zZZzzZzz': 'd_CHAR',
    'zZZzzZzZ': 'e_CHAR',
    'zZZzzZZz': 'f_CHAR',
    'zZZzzZZZ': 'g_CHAR',
    'zZZzZzzz': 'h_CHAR',
    'zZZzZzzZ': 'i_CHAR',
    'zZZzZzZz': 'j_CHAR',
    'zZZzZzZZ': 'k_CHAR',
    'zZZzZZzz': 'l_CHAR',
    'zZZzZZzZ': 'm_CHAR',
    'zZZzZZZz': 'n_CHAR',
    'zZZzZZZZ': 'o_CHAR',
    'zZZZzzzz': 'p_CHAR',
    'zZZZzzzZ': 'q_CHAR',
    'zZZZzzZz': 'r_CHAR',
    'zZZZzzZZ': 's_CHAR',
    'zZZZzZzz': 't_CHAR',
    'zZZZzZzZ': 'u_CHAR',
    'zZZZzZZz': 'v_CHAR',
    'zZZZzZZZ': 'w_CHAR',
    'zZZZZzzz': 'x_CHAR',
    'zZZZZzzZ': 'y_CHAR',
    'zZZZZzZz': 'z_CHAR',
    'zZZZZzZZ': 'LBRACE_CHAR',
    'zZZZZZzz': 'PIPE_CHAR',
    'zZZZZZzZ': 'RBRACE_CHAR',
    'zZZZZZZz': 'TILDE_CHAR',
    'zZZZZZZZ': 'SUPR_CHAR',
    'Zzzzzzzz': 'CEDILLA_UPPER_CHAR',
    'ZzzzzzzZ': 'UMLAUT_LOWER_u_CHAR',
    'ZzzzzzZz': 'ACUTE_LOWER_e_CHAR',
    'ZzzzzzZZ': 'CIRCUMFLEX_LOWER_a_CHAR',
    'ZzzzzZzz': 'UMLAUT_LOWER_a_CHAR',
    'ZzzzzZzZ': 'GRAVE_LOWER_a_CHAR',
    'ZzzzzZZz': 'RING_LOWER_a_CHAR',
    'ZzzzzZZZ': 'CEDILLA_LOWER_c_CHAR',
    'ZzzzZzzz': 'CIRCUMFLEX_LOWER_e_CHAR',
    'ZzzzZzzZ': 'UMLAUT_LOWER_e_CHAR',
    'ZzzzZzZz': 'GRAVE_LOWER_e_CHAR',
    'ZzzzZzZZ': 'UMLAUT_LOWER_i_CHAR',
    'ZzzzZZzz': 'CIRCUMFLEX_LOWER_i_CHAR',
    'ZzzzZZzZ': 'GRAVE_LOWER_i_CHAR',
    'ZzzzZZZz': 'UMLAUT_UPPER_A_CHAR',
    'ZzzzZZZZ': 'RING_UPPER_A_CHAR',
    'ZzzZzzzz': 'ACUTE_UPPER_E_CHAR',
    'ZzzZzzzZ': 'DIPHTHONG_LOWER_ae_CHAR',
    'ZzzZzzZz': 'DIPHTHONG_UPPER_AE_CHAR',
    'ZzzZzzZZ': 'CIRCUMFLEX_LOWER_o_CHAR',
    'ZzzZzZzz': 'UMLAUT_LOWER_o_CHAR',
    'ZzzZzZzZ': 'GRAVE_LOWER_o_CHAR',
    'ZzzZzZZz': 'CIRCUMFLEX_LOWER_u_CHAR',
    'ZzzZzZZZ': 'GRAVE_LOWER_u_CHAR',
    'ZzzZZzzz': 'UMLAUT_LOWER_y_CHAR',
    'ZzzZZzzZ': 'UMLAUT_UPPER_O_CHAR',
    'ZzzZZzZz': 'UMLAUT_UPPER_U_CHAR',
    'ZzzZZzZZ': 'SLASH_LOWER_o_CHAR',
    'ZzzZZZzz': 'POUND_SIGN_CHAR',
    'ZzzZZZzZ': 'SLASH_UPPER_O_CHAR',
    'ZzzZZZZz': 'MULTIPLICATION_SIGN_CHAR',
    'ZzzZZZZZ': 'FLORIN_CHAR',
    'ZzZzzzzz': 'ACUTE_LOWER_a_CHAR',
    'ZzZzzzzZ': 'ACUTE_LOWER_i_CHAR',
    'ZzZzzzZz': 'ACUTE_LOWER_o_CHAR',
    'ZzZzzzZZ': 'ACUTE_LOWER_u_CHAR',
    'ZzZzzZzz': 'TILDE_LOWER_n_CHAR',
    'ZzZzzZzZ': 'TILDE_UPPER_N_CHAR',
    'ZzZzzZZz': 'ORDINAL_FEMININE_CHAR',
    'ZzZzzZZZ': 'ORDINAL_MASCULINE_CHAR',
    'ZzZzZzzz': 'INVERTED_QUESTION_MARK_CHAR',
    'ZzZzZzzZ': 'REGISTERED_SIGN_CHAR',
    'ZzZzZzZz': 'NOT_SIGN_CHAR',
    'ZzZzZzZZ': 'HALF_CHAR',
    'ZzZzZZzz': 'QUARTER_CHAR',
    'ZzZzZZzZ': 'INVERTED_EXCLAMATION_MARK_CHAR',
    'ZzZzZZZz': 'LEFT_ANGLE_QUOTE_CHAR',
    'ZzZzZZZZ': 'RIGHT_ANGLE_QUOTE_CHAR',
    'ZzZZzzzz': 'LOW_DENSITY_SHADE_CHAR',
    'ZzZZzzzZ': 'MEDIUM_DENSITY_SHADE_CHAR',
    'ZzZZzzZz': 'HIGH_DENSITY_SHADE_CHAR',
    'ZzZZzzZZ': 'VERTICAL_BAR_CHAR',
    'ZzZZzZzz': 'RIGHT_TEE_CHAR',
    'ZzZZzZzZ': 'ACUTE_UPPER_A_CHAR',
    'ZzZZzZZz': 'CIRCUMFLEX_UPPER_A_CHAR',
    'ZzZZzZZZ': 'GRAVE_UPPER_A_CHAR',
    'ZzZZZzzz': 'COPYRIGHT_SIGN_CHAR',
    'ZzZZZzzZ': 'DOUBLE_VERTICAL_LINE_CHAR',
    'ZzZZZzZz': 'DOUBLE_VERTICAL_BAR_CHAR',
    'ZzZZZzZZ': 'TOP_RIGHT_CORNER_CHAR',
    'ZzZZZZzz': 'BOTTOM_RIGHT_DOUBLE_CORNER_CHAR',
    'ZzZZZZzZ': 'CENT_SIGN_CHAR',
    'ZzZZZZZz': 'YEN_SIGN_CHAR',
    'ZzZZZZZZ': 'TOP_LEFT_CORNER_CHAR',
    'ZZzzzzzz': 'BOTTOM_LEFT_CORNER_CHAR',
    'ZZzzzzzZ': 'BOTTOM_TEE_CHAR',
    'ZZzzzzZz': 'TOP_TEE_CHAR',
    'ZZzzzzZZ': 'LEFT_TEE_CHAR',
    'ZZzzzZzz': 'HORIZONTAL_BAR_CHAR',
    'ZZzzzZzZ': 'CROSS_CHAR',
    'ZZzzzZZz': 'TILDE_LOWER_a_CHAR',
    'ZZzzzZZZ': 'TILDE_UPPER_A_CHAR',
    'ZZzzZzzz': 'BOTTOM_LEFT_DOUBLE_CORNER_CHAR',
    'ZZzzZzzZ': 'TOP_LEFT_DOUBLE_CORNER_CHAR',
    'ZZzzZzZz': 'BOTTOM_DOUBLE_TEE_CHAR',
    'ZZzzZzZZ': 'TOP_DOUBLE_TEE_CHAR',
    'ZZzzZZzz': 'RIGHT_DOUBLE_TEE_CHAR',
    'ZZzzZZzZ': 'DOUBLE_HORIZONTAL_BAR_CHAR',
    'ZZzzZZZz': 'CROSS_DOUBLE_LINES_CHAR',
    'ZZzzZZZZ': 'CURRENCY_SIGN_CHAR',
    'ZZzZzzzz': 'ETH_LOWER_CHAR',
    'ZZzZzzzZ': 'ETH_UPPER_CHAR',
    'ZZzZzzZz': 'CIRCUMFLEX_UPPER_E_CHAR',
    'ZZzZzzZZ': 'UMLAUT_UPPER_E_CHAR',
    'ZZzZzZzz': 'GRAVE_UPPER_E_CHAR',
    'ZZzZzZzZ': 'DOTLESS_LOWER_I_CHAR',
    'ZZzZzZZz': 'ACUTE_UPPER_I_CHAR',
    'ZZzZzZZZ': 'CIRCUMFLEX_UPPER_I_CHAR',
    'ZZzZZzzz': 'UMLAUT_UPPER_I_CHAR',
    'ZZzZZzzZ': 'BOTTOM_RIGHT_CORNER_CHAR',
    'ZZzZZzZz': 'TOP_LEFT_CORNER_SIMPLE_CHAR',
    'ZZzZZzZZ': 'FULL_BLOCK_CHAR',
    'ZZzZZZzz': 'LOW_HALF_BLOCK_CHAR',
    'ZZzZZZzZ': 'BROKEN_BAR_CHAR',
    'ZZzZZZZz': 'GRAVE_UPPER_I_CHAR',
    'ZZzZZZZZ': 'UPPER_HALF_BLOCK_CHAR',
    'ZZZzzzzz': 'ACUTE_UPPER_O_CHAR',
    'ZZZzzzzZ': 'ESZETT_CHAR',
    'ZZZzzzZz': 'CIRCUMFLEX_UPPER_O_CHAR',
    'ZZZzzzZZ': 'GRAVE_UPPER_O_CHAR',
    'ZZZzzZzz': 'TILDE_LOWER_o_CHAR',
    'ZZZzzZzZ': 'TILDE_UPPER_O_CHAR',
    'ZZZzzZZz': 'MICRO_SIGN_CHAR',
    'ZZZzzZZZ': 'THORN_LOWER_CHAR',
    'ZZZzZzzz': 'THORN_UPPER_CHAR',
    'ZZZzZzzZ': 'ACUTE_UPPER_U_CHAR',
    'ZZZzZzZz': 'CIRCUMFLEX_UPPER_U_CHAR',
    'ZZZzZzZZ': 'GRAVE_UPPER_U_CHAR',
    'ZZZzZZzz': 'ACUTE_LOWER_y_CHAR',
    'ZZZzZZzZ': 'ACUTE_UPPER_Y_CHAR',
    'ZZZzZZZz': 'MACRON_CHAR',
    'ZZZzZZZZ': 'ACUTE_SIGN_CHAR',
    'ZZZZzzzz': 'CONGRUENCE_SIGN_CHAR',
    'ZZZZzzzZ': 'PLUS_MINUS_SIGN_CHAR',
    'ZZZZzzZz': 'DOUBLE_LOW_LINE_CHAR',
    'ZZZZzzZZ': 'THREE_QUARTERS_CHAR',
    'ZZZZzZzz': 'PILCROW_SIGN_CHAR',
    'ZZZZzZzZ': 'SECTION_SIGN_CHAR',
    'ZZZZzZZz': 'DIVISION_SIGN_CHAR',
    'ZZZZzZZZ': 'CEDILLA_SIGN_CHAR',
    'ZZZZZzzz': 'DEGREE_SIGN_CHAR',
    'ZZZZZzzZ': 'DIAERESIS_SIGN_CHAR',
    'ZZZZZzZz': 'MIDDLE_DOT_CHAR',
    'ZZZZZzZZ': 'SUPERSCRIPT_ONE_CHAR',
    'ZZZZZZzz': 'SUPERSCRIPT_THREE_CHAR',
    'ZZZZZZzZ': 'SUPERSCRIPT_TWO_CHAR',
    'ZZZZZZZz': 'BLACK_SQUARE_CHAR',
    'ZZZZZZZZ': 'NO_BREAK_SPACE_CHAR'
}


specialSymbol_lexemes = {
    '(': 'LPAREN_SPEC',
    ')': 'RPAREN_SPEC',
    ';': 'SEMICOLON_SPEC',
    '{': 'LBRACE_SPEC',
    '}': 'RBRACE_SPEC',
    '[': 'LBRACKET_SPEC',
    ']': 'RBRACKET_SPEC',
}

# Función para analizar desde un archivo
def analyze_file(file_path, output_path="tokens_output.py"):
    with open(file_path, 'r') as f:
        content = f.read()
    lexer.input(content)
    with open(output_path, 'w') as out:
        for token in lexer:
            out.write(f"{token}\n")
    print(f"Tokens escritos en {output_path}")