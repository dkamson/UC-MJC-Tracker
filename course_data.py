GE_IGETC = [
    {"type": "single", "id": "IGETC_1A", "label": "Area 1A: English Composition (1 course)"},
    {"type": "single", "id": "IGETC_1B", "label": "Area 1B: Critical Thinking (1 course)"},
    {"type": "single", "id": "IGETC_1C_CSU", "label": "Area 1C: Oral Communication (CSU Only)"},
    {"type": "single", "id": "IGETC_2A", "label": "Area 2A: Mathematical Concepts (1 course)"},
    {"type": "single", "id": "IGETC_3A", "label": "Area 3A: Arts (1 course)"},
    {"type": "single", "id": "IGETC_3B", "label": "Area 3B: Humanities (1 course)"},
    
    # We model "3 courses" as 3 separate, logical checkboxes.
    {"type": "single", "id": "IGETC_4_1", "label": "Area 4: Social Science (1 of 3)"},
    {"type": "single", "id": "IGETC_4_2", "label": "Area 4: Social Science (2 of 3)"},
    {"type": "single", "id": "IGETC_4_3", "label": "Area 4: Social Science (3 of 3)"},
    
    {"type": "single", "id": "IGETC_5A", "label": "Area 5A: Physical Science (1 course)"},
    {"type": "single", "id": "IGETC_5B", "label": "Area 5B: Biological Science (1 course)"},
    {"type": "single", "id": "IGETC_5C", "label": "Area 5C: Laboratory (1 course)"},
    {"type": "single", "id": "IGETC_6A", "label": "Area 6A: Language Other Than English"},
    {"type": "single", "id": "IGETC_7_CSU", "label": "Area 7: Ethnic Studies (CSU Only)"} # UC requires this via Area 4
]

GE_CAL_GETC = [
    {"type": "single", "id": "CAL_GETC_1A", "label": "Area 1A: English Composition (1 course)"},
    {"type": "single", "id": "CAL_GETC_1B", "label": "Area 1B: Critical Thinking (1 course)"},
    {"type": "single", "id": "CAL_GETC_1C", "label": "Area 1C: Oral Communication (1 course)"},
    {"type": "single", "id": "CAL_GETC_2", "label": "Area 2: Quantitative Reasoning (1 course)"},
    {"type": "single", "id": "CAL_GETC_3A", "label": "Area 3A: Arts (1 course)"},
    {"type": "single", "id": "CAL_GETC_3B", "label": "Area 3B: Humanities (1 course)"},
    
    # We model "2 courses" as 2 separate, logical checkboxes.
    {"type": "single", "id": "CAL_GETC_4_1", "label": "Area 4: Social Sciences (1 of 2)"},
    {"type": "single", "id": "CAL_GETC_4_2", "label": "Area 4: Social Sciences (2 of 2)"},
    
    {"type": "single", "id": "CAL_GETC_5A", "label": "Area 5A: Physical Science (1 course)"},
    {"type": "single", "id": "CAL_GETC_5B", "label": "Area 5B: Biological Science (1 course)"},
    {"type": "single", "id": "CAL_GETC_5C", "label": "Area 5C: Laboratory (1 course)"},
    {"type": "single", "id": "CAL_GETC_6", "label": "Area 6: Ethnic Studies (1 course)"}
]

# --- MAJOR PREP LISTS ---
# NOTE: IDs are suffixed with _[UNI] to ensure they are unique in st.session_state

# --- 1. UC Davis ---
MAJOR_PREP_UCD = [
    {"type": "single", "id": "CSCI 204_UCD", "label": "CSCI 204 - Discrete Structures (for UCD ECS 020)"},
    {"type": "single", "id": "CSCI 271_UCD", "label": "CSCI 271 - Problem Solving/Prog 1 (for UCD ECS 036A)"},
    {"type": "single", "id": "CSCI 272_UCD", "label": "CSCI 272 - Problem Solving/Prog 2 (for UCD ECS 036B)"},
    {"type": "single", "id": "CSCI 273_UCD", "label": "CSCI 273 - Assembly Language (for UCD ECS 050)"},
    {"type": "single", "id": "MATH 171_UCD", "label": "MATH 171 - Calculus I (for UCD MAT 021A)"},
    {"type": "single", "id": "MATH 172_UCD", "label": "MATH 172 - Calculus II (for UCD MAT 021B)"},
    {"type": "single", "id": "MATH 173_UCD", "label": "MATH 173 - Calculus III (for UCD MAT 021C)"},
    {"type": "single", "id": "MATH 191_UCD", "label": "MATH 191 - Linear Algebra (for UCD MAT 022A)"},
    {"type": "single", "id": "UCD_ECS_036C", "label": "ECS 036C - Data Structures (Adv) (*Take at UCD*)"}
]

# --- 2. UC Berkeley ---
MAJOR_PREP_UCB = [
    {"type": "single", "id": "MATH 171_UCB", "label": "MATH 171 - Calculus: First Course (for UCB MATH 51)"},
    {"type": "single", "id": "MATH 172_UCB", "label": "MATH 172 - Calculus: Second Course (for UCB MATH 52)"},
    
    {"type": "group", "id": "UCB_MATH_B_GROUP(Choose 1)", "label": "Linear Algebra/Diff Eq (for UCB MATH 54/MATH 56)", "courses_needed": 1, "options": [
        {"id": "MATH 191_UCB", "label": "MATH 191 - Linear Algebra"},
        {"id": "MATH 193_UCB AND MATH_191", "label": "MATH 193 - Ordinary Differential Equations and MATH 191 - Linear Algebra"},
    ]},
    
    {"type": "single", "id": "UCB_CS_61A", "label": "COMPSCI 61A (*Take at UCB - No MJC Articulation*)"},
    
    # Per your global rule, we are articulating 61B (Data Structures)
    {"type": "single", "id": "CSCI 272_UCB_61B", "label": "CSCI 272 - Data Structures (Placeholder for UCB COMPSCI 61B)"},
    
    {"type": "single", "id": "UCB_CS_61C", "label": "COMPSCI 61C (*Take at UCB - No MJC Articulation*)"},
    
    # Per your global rule, this MUST be taken at UC, so we do not articulate it.
    {"type": "single", "id": "UCB_CS_70", "label": "COMPSCI 70 (*Take at UCB - Per ASSIST*)"},
]

# --- 3. UC Irvine ---
MAJOR_PREP_UCI = [
    {"type": "group", "id": "UCI_PROG_SERIES", "label": "Programming Series (for UCI I&C SCI 31-33)", "courses_needed": 2, "options": [
        {"id": "CSCI 271_UCI_PROG", "label": "CSCI 271 - Problem Solving/Prog 1"},
        {"id": "CSCI 272_UCI_PROG", "label": "CSCI 272 - Problem Solving/Prog 2"},
    ]},
    {"type": "group", "id": "UCI_CPP_REQ", "label": "C++ Programming (for UCI I&C SCI 45C)", "courses_needed": 2, "options": [
        {"id": "CSCI 271_UCI_CPP", "label": "CSCI 271 - Problem Solving/Prog 1"},
        {"id": "CSCI 272_UCI_CPP", "label": "CSCI 272 - Problem Solving/Prog 2"},
    ]},
    {"type": "single", "id": "MATH 171_UCI", "label": "MATH 171 - Calculus: First Course (for UCI MATH 2A)"},
    {"type": "single", "id": "MATH 172_UCI", "label": "MATH 172 - Calculus: Second Course (for UCI MATH 2B)"},
    {"type": "group", "id": "UCI_LINEAR_ALG_REQ", "label": "Linear Algebra Requirement (Choose 1)", "courses_needed": 1, "options": [
        {"id": "MATH 191_UCI", "label": "MATH 191 - Linear Algebra (for UCI MATH 3A)"},
        {"id": "UCI_ICS_6N", "label": "I&C SCI 6N - (*Take at UCI - No MJC Articulation*)"}
    ]},
    {"type": "single", "id": "CSCI 204_UCI", "label": "CSCI 204 - Discrete Structures (for UCI I&C SCI 6B/6D)"},
    {"type": "single", "id": "CSCI 273_UCI", "label": "CSCI 273 - Assembly Language (Placeholder for UCI I&C SCI 51)"},
    {"type": "single", "id": "UCI_IN4MATX_43", "label": "IN4MATX 43 - Software Eng (*Take at UCI - Verify w/ Counselor*)"},
    {"type": "single", "id": "UCI_ICS_53", "label": "I&C SCI 53 - System Design (*Take at UCI - Verify w/ Counselor*)"},
    {"type": "single", "id": "UCI_STATS_67", "label": "STATS 67 - Statistics (*Take at UCI - Verify w/ Counselor*)"},
]

# --- 4. UC Merced ---
MAJOR_PREP_UCM = [
    {"type": "single", "id": "CSCI 271_UCM", "label": "CSCI 271 - Problem Solving/Prog 1 (for UCM CSE 022)"},
    {"type": "single", "id": "CSCI 272_UCM", "label": "CSCI 272 - Data Structures (for UCM CSE 030)"},
    {"type": "single", "id": "MATH 171_UCM", "label": "MATH 171 - Calculus I (for UCM MATH 021)"},
    {"type": "single", "id": "MATH 172_UCM", "label": "MATH 172 - Calculus II (for UCM MATH 022)"},
    {"type": "single", "id": "MATH 173_UCM", "label": "MATH 173 - Vector Calculus (for UCM MATH 023)"},
    {"type": "group", "id": "UCM_MATH_024_GROUP", "label": "Lin Alg/Diff Eq (for UCM MATH 024)", "courses_needed": 2, "options": [
        {"id": "MATH 191_UCM", "label": "MATH 191 - Linear Algebra"},
        {"id": "MATH 193_UCM", "label": "MATH 193 - Ordinary Differential Equations"}
    ]},
    {"type": "single", "id": "PHYS 101_UCM", "label": "PHYS 101 - Gen Physics: Mechanics (for UCM PHYS 008)"},
    {"type": "group", "id": "UCM_PHYS_009_GROUP", "label": "Physics II (for UCM PHYS 009)", "courses_needed": 2, "options": [
        {"id": "PHYS 102_UCM", "label": "PHYS 102 - Waves, Thermo, & Optics"},
        {"id": "PHYS 103_UCM", "label": "PHYS 103 - Electricity, Magnetism, & Modern"}
    ]},
    {"type": "single", "id": "CSCI 204_UCM_REC", "label": "CSCI 204 - Discrete Structures (Recommended)"},
    {"type": "single", "id": "CSCI 273_UCM_REC", "label": "CSCI 273 - Assembly Language (Recommended)"},
    {"type": "group", "id": "UCM_ENGR_065_GROUP_REC", "label": "Circuit Theory (Recommended)", "courses_needed": 2, "options": [
        {"id": "ENGR 141_UCM", "label": "ENGR 141 - Intro to Circuit Analysis"},
        {"id": "MATH 193_UCM_REC", "label": "MATH 193 - Ordinary Differential Equations"}
    ]}
]

# --- 5. UC San Diego ---
MAJOR_PREP_UCSD = [
    {"type": "single", "id": "MATH 171_UCSD", "label": "MATH 171 - Calculus I (for UCSD MATH 20A)"},
    {"type": "single", "id": "MATH 172_UCSD", "label": "MATH 172 - Calculus II (for UCSD MATH 20B)"},
    {"type": "single", "id": "MATH 173_UCSD", "label": "MATH 173 - Calculus III (for UCSD MATH 20C)"},
    {"type": "single", "id": "MATH 191_UCSD", "label": "MATH 191 - Linear Algebra (for UCSD MATH 18)"},
    {"type": "single", "id": "CSCI 272_UCSD", "label": "CSCI 272 - Data Structures (for UCSD CSE 12)"},
    {"type": "single", "id": "CSCI 271_UCSD", "label": "CSCI 271 - Intro to Prog (Placeholder for UCSD CSE 11)"},
    {"type": "single", "id": "CSCI 204_UCSD", "label": "CSCI 204 - Discrete Math (Placeholder for UCSD CSE 20)"},
    {"type": "group", "id": "UCSD_SCIENCE_GROUP", "label": "Science Requirement (Choose 1)", "courses_needed": 1, "options": [
        {"id": "PHYS 101_UCSD", "label": "PHYS 101 (for PHYS 2A)"},
        {"id": "PHYS 103_UCSD", "label": "PHYS 103 (for PHYS 2B)"},
        {"id": "CHEM 101_UCSD", "label": "CHEM 101 (for CHEM 6A)"},
        {"id": "UCSD_BILD_1_LOGICAL", "label": "BILD 1 (Reqs: BIO 101 + BOT 101 + ZOOL 101)"},
        {"id": "UCSD_BILD_2_LOGICAL", "label": "BILD 2 (Reqs: BIO 101 + BOT 101 + ZOOL 101)"},
        {"id": "UCSD_BILD_3_LOGICAL", "label": "BILD 3 (Reqs: BIO 101 + BOT 101 + ZOOL 101)"},
        {"id": "UCSD_CHEM_6B_LOGICAL", "label": "CHEM 6B (Reqs: CHEM 101 + CHEM 102)"},
        {"id": "UCSD_UNARTICULATED_SCI", "label": "Other options (e.g., COGS, SIO) must be taken at UCSD"}
    ]}
]

# --- 6. UC Riverside ---
MAJOR_PREP_UCR = [
    {"type": "single", "id": "CSCI 271_UCR", "label": "CSCI 271 - Intro to CS I (for UCR CS 10A)"},
    {"type": "single", "id": "MATH 171_UCR", "label": "MATH 171 - Calculus I (for UCR MATH 9A)"},
    {"type": "single", "id": "MATH 172_UCR", "label": "MATH 172 - Calculus II (for UCR MATH 9B)"},
    {"type": "single", "id": "PHYS 101_UCR", "label": "PHYS 101 - Gen Physics: Mechanics (for UCR PHYS 40A)"},
    {"type": "group", "id": "UCR_CS_10B_GROUP", "label": "Intro to CS II (for UCR CS 10B) (Choose 1)", "courses_needed": 1, "options": [
        {"id": "CSCI 272_UCR_10B", "label": "CSCI 272 - Problem Solving/Prog 2"},
        {"id": "CSCI 274_UCR", "label": "CSCI 274 - Windows Programming"}
    ]},
    {"type": "group", "id": "UCR_SELECT_3_GROUP", "label": "Required Group (Choose 3)", "courses_needed": 3, "options": [
        {"id": "CSCI 204_UCR_11", "label": "CSCI 204 - Discrete Structures (Placeholder for UCR CS 11)"},
        {"id": "CSCI 272_UCR_10C", "label": "CSCI 272 - Data Structures (Placeholder for UCR CS 10C)"},
        {"id": "CSCI 273_UCR_61", "label": "CSCI 273 - Assembly Language (for UCR CS 61)"},
        {"id": "MATH 173_UCR_10A", "label": "MATH 173 - Calculus III (for UCR MATH 10A)"},
        {"id": "UCR_PHYS_40B_LOGICAL", "label": "PHYS 40B (Reqs: PHYS 101 + PHYS 102)"},
        {"id": "PHYS 103_UCR_40C", "label": "PHYS 103 - Gen Physics: Electricity, Magnetism (for UCR PHYS 40C)"}
    ]},
    {"type": "group", "id": "UCR_RECOMMENDED_GROUP", "label": "Recommended (Choose 1)", "courses_needed": 1, "options": [
        {"id": "MATH 191_UCR_31", "label": "MATH 191 - Applied Linear Algebra (for UCR MATH 31)"},
        {"id": "UCR_EE_20B_LOGICAL", "label": "EE 20B - (*Take at UCR - No MJC Articulation*)"}
    ]}
]

# --- 7. UC Santa Barbara ---
MAJOR_PREP_UCSB = [
    {"type": "single", "id": "MATH 171_UCSB", "label": "MATH 171 - Calculus I (for UCSB MATH 3A)"},
    {"type": "single", "id": "MATH 172_UCSB", "label": "MATH 172 - Calculus II (for UCSB MATH 3B)"},
    {"type": "single", "id": "MATH 191_UCSB", "label": "MATH 191 - Linear Algebra (for UCSB MATH 4A)"},
    {"type": "single", "id": "MATH 193_UCSB", "label": "MATH 193 - Differential Equations (for UCSB MATH 4B)"},
    {"type": "single", "id": "CSCI 204_UCSB", "label": "CSCI 204 - Discrete Structures (for UCSB CMPSC 40)"},
    {"type": "single", "id": "CSCI 271_UCSB", "label": "CSCI 271 - Problem Solving I (Placeholder for UCSB CMPSC 16)"},
    {"type": "single", "id": "CSCI 272_UCSB_24", "label": "CSCI 272 - Problem Solving II (Placeholder for UCSB CMPSC 24)"},
    {"type": "single", "id": "CSCI 272_UCSB_32", "label": "CSCI 272 - Object Oriented Design (Placeholder for UCSB CMPSC 32)"},
    {"type": "single", "id": "CSCI 273_UCSB_64", "label": "CSCI 273 - Computer Organization (for UCSB CMPSC 64)"},
    {"type": "single", "id": "MATH 173_UCSB_6A", "label": "MATH 173 - Vector Calculus (for UCSB MATH 6A)"},
    {"type": "group", "id": "UCSB_SCIENCE_GROUP", "label": "Science Electives (Choose 2)", "courses_needed": 2, "options": [
        {"id": "UCSB_PHYS_1_LOGICAL", "label": "PHYS 101 (for PHYS 1, 2, or 7A)"},
        {"id": "UCSB_PHYS_7B_LOGICAL", "label": "PHYS 7B (Reqs: PHYS 101 + PHYS 102)"},
        {"id": "UCSB_PHYS_7C_LOGICAL", "label": "PHYS 7C/7D (Reqs: PHYS 102 + PHYS 103)"},
        {"id": "UCSB_PHYS_3_LOGICAL", "label": "PHYS 103 (for PHYS 3/3L)"},
        {"id": "UCSB_PHYS_6_LOGICAL", "label": "PHYS 6A/B/C (Reqs: PHYS 142 + PHYS 143)"},
        {"id": "UCSB_CHEM_1_LOGICAL", "label": "CHEM 1A/B/C (Reqs: CHEM 101 + CHEM 102)"},
        {"id": "UCSB_MCDB_1_LOGICAL", "label": "MCDB 1A/B (Reqs: BIO 101 + BOT 101 + ZOOL 101)"}
    ]}
]

# --- 8. UC Los Angeles ---
MAJOR_PREP_UCLA = [
    {"type": "single", "id": "CSCI 273_UCLA", "label": "CSCI 273 - Assembly Language (for UCLA COM SCI 33)"},
    {"type": "single", "id": "MATH 171_UCLA", "label": "MATH 171 - Calculus I (for UCLA MATH 31A)"},
    {"type": "single", "id": "MATH 172_UCLA", "label": "MATH 172 - Calculus II (for UCLA MATH 31B)"},
    {"type": "single", "id": "MATH 173_UCLA", "label": "MATH 173 - Calculus III (for UCLA MATH 32A/B)"},
    {"type": "single", "id": "MATH 191_UCLA", "label": "MATH 191 - Linear Algebra (for UCLA MATH 33A)"},
    {"type": "single", "id": "MATH 193_UCLA", "label": "MATH 193 - Differential Equations (for UCLA MATH 33B)"},
    {"type": "single", "id": "CSCI 204_UCLA", "label": "CSCI 204 - Discrete Structures (for UCLA MATH 61)"},
    {"type": "group", "id": "UCLA_PHYSICS_GROUP", "label": "Physics Series (for UCLA PHYSICS 1A/B/C)", "courses_needed": 3, "options": [
        {"id": "PHYS 101_UCLA", "label": "PHYS 101 - General Physics: Mechanics"},
        {"id": "PHYS 102_UCLA", "label": "PHYS 102 - Waves, Thermodynamics, & Optics"},
        {"id": "PHYS 103_UCLA", "label": "PHYS 103 - Electricity, Magnetism, & Modern"}
    ]},
    {"type": "group", "id": "UCLA_ENGCOMP_3_GROUP", "label": "English Composition (for UCLA ENGCOMP 3) (Choose 1)", "courses_needed": 1, "options": [
        {"id": "ENGL C1000_UCLA", "label": "ENGL C1000 - Academic Reading and Writing"},
        {"id": "ENGL 102_UCLA", "label": "ENGL 102 - Advanced Composition"},
        {"id": "PHILO 105_UCLA", "label": "PHILO 105 - Critical Reasoning"}
    ]},
    {"type": "single", "id": "CSCI 271_UCLA", "label": "CSCI 271 - Intro to CS I (Placeholder for UCLA COM SCI 31)"},
    {"type": "single", "id": "CSCI 272_UCLA", "label": "CSCI 272 - Intro to CS II (Placeholder for UCLA COM SCI 32)"},
    {"type": "single", "id": "UCLA_COM_SCI_35L", "label": "COM SCI 35L - Software Lab (*Take at UCLA - No MJC Articulation*)"},
    {"type": "single", "id": "UCLA_COM_SCI_M51A", "label": "COM SCI M51A - Logic Design (*Take at UCLA - No MJC Articulation*)"}
]

# --- 9. UC Santa Cruz ---
MAJOR_PREP_UCSC = [
    {"type": "single", "id": "CSCI 273_UCSC", "label": "CSCI 273 - Assembly Language (for UCSC CSE 12)"},
    {"type": "single", "id": "CSCI 204_UCSC", "label": "CSCI 204 - Discrete Structures (for UCSC CSE 16)"},
    {"type": "single", "id": "CSCI 272_UCSC", "label": "CSCI 272 - Programming Abstractions (for UCSC CSE 30)"},
    {"type": "single", "id": "MATH 171_UCSC", "label": "MATH 171 - Calculus I (for UCSC MATH 19A)"},
    {"type": "single", "id": "MATH 172_UCSC", "label": "MATH 172 - Calculus II (for UCSC MATH 19B)"},
    {"type": "group", "id": "UCSC_LIN_ALG_GROUP", "label": "Linear Algebra (Recommended) (Choose 1)", "courses_needed": 1, "options": [
        {"id": "MATH 191_UCSC", "label": "MATH 191 - Linear Algebra (for UCSC AM 10 or MATH 21)"}
    ]},
    {"type": "group", "id": "UCSC_VEC_CALC_GROUP", "label": "Vector Calculus (Recommended) (Choose 1)", "courses_needed": 1, "options": [
        {"id": "MATH 173_UCSC", "label": "MATH 173 - Calculus III (for UCSC AM 30 or MATH 23A)"}
    ]}
]


# --- LEVEL 1: MASTER DICTIONARY (THE "FILING CABINET ROOM") ---
ALL_DATA = {
    # --- LEVEL 2: University (The "Filing Cabinet") ---
    "ucd": {
        "name": "UC Davis",
        "plans": {
            # --- LEVEL 3: Plan (The "Drawer") ---
            "igetc": {
                "name": "IGETC (Started before Fall 2025)",
                "requirements": {
                    "ge": GE_IGETC, 
                    "major_prep": MAJOR_PREP_UCD 
                }
            },
            "cal_getc": {
                "name": "Cal-GETC (Started Fall 2025)",
                "requirements": {
                    "ge": GE_CAL_GETC, 
                    "major_prep": MAJOR_PREP_UCD
                }
            }
        }
    },
    
    "ucb": {
        "name": "UC Berkeley",
        "plans": {
            "igetc": {
                "name":"IGETC (Started before Fall 2025)",
                "requirements": {
                    "ge": GE_IGETC,
                    "major_prep": MAJOR_PREP_UCB
                }
            },
            "cal_getc": {
                "name": "Cal-GETC (Started Fall 2025+)",
                "requirements": {
                    "ge": GE_CAL_GETC,
                    "major_prep": MAJOR_PREP_UCB
                }
            }
        }
    },
    
    "uci": {
        "name": "UC Irvine",
        "plans": {
            "igetc": {
                "name": "IGETC (Started before Fall 2025)",
                "requirements": {
                    "ge": GE_IGETC,
                    "major_prep": MAJOR_PREP_UCI
                }
            },
            "cal_getc": {
                "name": "Cal-GETC (Started Fall 2025+)",
                "requirements": {
                    "ge": GE_CAL_GETC, 
                    "major_prep": MAJOR_PREP_UCI
                }
            }
        }
    },
    
    "ucm": {
        "name": "UC Merced",
        "plans": {
            "igetc": {
                "name": "IGETC (Started before Fall 2025)",
                "requirements": {
                    "ge": GE_IGETC,
                    "major_prep": MAJOR_PREP_UCM
                }
            },
            "cal_getc": {
                "name": "Cal-GETC (Started Fall 2025+)",
                "requirements": {
                    "ge": GE_CAL_GETC,
                    "major_prep": MAJOR_PREP_UCM
                }
            }
        }
    },
    
    "ucsd": {
        "name": "UC San Diego",
        "plans": {
            "igetc": {
                "name": "IGETC (Started before Fall 2025)",
                "requirements": {
                    "ge": GE_IGETC,
                    "major_prep": MAJOR_PREP_UCSD
                }
            },
            "cal_getc": {
                "name": "Cal-GETC (Started Fall 2025+)",
                "requirements": {
                    "ge": GE_CAL_GETC,
                    "major_prep": MAJOR_PREP_UCSD
                }
            }
        }
    },
    
    "ucr": {
        "name": "UC Riverside",
        "plans": {
            "igetc": {
                "name": "IGETC (Started before Fall 2025)",
                "requirements": {
                    "ge": GE_IGETC,
                    "major_prep": MAJOR_PREP_UCR
                }
            },
            "cal_getc": {
                "name": "Cal-GETC (Started Fall 2025+)",
                "requirements": {
                    "ge": GE_CAL_GETC,
                    "major_prep": MAJOR_PREP_UCR
                }
            }
        }
    },
    
    "ucsb": {
        "name": "UC Santa Barbara",
        "plans": {
            "igetc": {
                "name": "IGETC (Started before Fall 2025)",
                "requirements": {
                    "ge": GE_IGETC,
                    "major_prep": MAJOR_PREP_UCSB
                }
            },
            "cal_getc": {
                "name": "Cal-GETC (Started Fall 2025+)",
                "requirements": {
                    "ge": GE_CAL_GETC,
                    "major_prep": MAJOR_PREP_UCSB
                }
            }
        }
    },
    
    "ucla": {
        "name": "UC Los Angeles",
        "plans": {
            "igetc": {
                "name": "IGETC (Started before Fall 2025)",
                "requirements": {
                    "ge": GE_IGETC,
                    "major_prep": MAJOR_PREP_UCLA
                }
            },
            "cal_getc": {
                "name": "Cal-GETC (Started Fall 2025+)",
                "requirements": {
                    "ge": GE_CAL_GETC,
                    "major_prep": MAJOR_PREP_UCLA
                }
            }
        }
    },
    
    "ucsc": {
        "name": "UC Santa Cruz",
        "plans": {
            "igetc": {
                "name": "IGETC (Started before Fall 2025)",
                "requirements": {
                    "ge": GE_IGETC,
                    "major_prep": MAJOR_PREP_UCSC
                }
            },
            "cal_getc": {
                "name": "Cal-GETC (Started Fall 2025+)",
                "requirements": {
                    "ge": GE_CAL_GETC,
                    "major_prep": MAJOR_PREP_UCSC
                }
            }
        }
    }
    
    # --- Our "database" is now complete with all 9 UC campuses! ---
}


# --- Helper Functions (BROKEN - DO NOT USE) ---
# --- (We will fix these in the NEXT step when we build app.py) ---

def get_all_courses(plan_data):
    """
    (This function is now BROKEN and will need to be refactored
    to handle the new 'type' structure.)
    """
    # This old logic will CRASH because it doesn't understand 'type'.
    return []

def get_total_course_count(plan_data):
    """
    (This function is now BROKEN and will need to be refactored
    to handle the new 'type' structure.)
    """
    # This old logic will CRASH.
    return 