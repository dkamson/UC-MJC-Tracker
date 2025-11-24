COURSE_REQUIREMENTS = {

    "cal_getc": [
        {
            "id": "CAL_GETC_1A",
            "label": "Area 1A: English Composition (1 course)"
        },
        {
            "id": "CAL_GETC_1B",
            "label": "Area 1B: Critical Thinking (1 course)"
        },
        {
            "id": "CAL_GETC_1C",
            "label": "Area 1C: Oral Communication (1 course)"
        },
        {
            "id": "CAL_GETC_2",
            "label": "Area 2: Quantitative Reasoning (1 course)"
        },
        {
            "id": "CAL_GETC_3A",
            "label": "Area 3A: Arts (1 course)"
        },
        {
            "id": "CAL_GETC_3B",
            "label": "Area 3B: Humanities (1 course)"
        },
        {
            "id": "CAL_GETC_4A",
            "label": "Area 4: Social Sciences (1 of 2)"
        },
        {
            "id": "CAL_GETC_4B",
            "label": "Area 4: Social Sciences (2 of 2)"
        },
        {
            "id": "CAL_GETC_5A",
            "label": "Area 5A: Physical Science (1 course)"
        },
        {
            "id": "CAL_GETC_5B",
            "label": "Area 5B: Biological Science (1 course)"
        },
        {
            "id": "CAL_GETC_5C",
            "label": "Area 5C: Laboratory (1 course)"
        },
        {
            "id": "CAL_GETC_6",
            "label": "Area 6: Ethnic Studies (1 course)"
        }
    ],
    # These are the specific, required courses for the major.
    "uc_davis_cs_prep": [
        # --- CS Courses (MJC -> UCD) ---
        {
            "id": "CSCI 204",
            "label": "CSCI 204 - Discrete Structures (for UCD ECS 020)"
        },
        {
            "id": "CSCI 271",
            "label": "CSCI 271 - Problem Solving/Prog 1 (for UCD ECS 036A)"
        },
        {
            "id": "CSCI 272",
            "label": "CSCI 272 - Problem Solving/Prog 2 (for UCD ECS 036B)"
        },
        {
            "id": "CSCI 273",
            "label": "CSCI 273 - Assembly Language (for UCD ECS 050)"
        },
        
        # --- Math Courses (MJC -> UCD) ---
        {
            "id": "MATH 171",
            "label": "MATH 171 - Calculus I (for UCD MAT 021A)"
        },
        {
            "id": "MATH 172",
            "label": "MATH 172 - Calculus II (for UCD MAT 021B)"
        },
        {
            "id": "MATH 173",
            "label": "MATH 173 - Calculus III (for UCD MAT 021C)"
        },
        {
            "id": "MATH 191",
            "label": "MATH 191 - Linear Algebra (for UCD MAT 022A)"
        },
        
        # --- UCD-Only Requirement ---
        {
            "id": "UCD_ECS_036C",
            "label": "ECS 036C - Data Structures (Adv) (*Take at UCD*)"
        }
    ]
}

# --- Helper function ---

def get_all_courses():
    """Returns a flat list of all course objects."""
    all_courses = (
        COURSE_REQUIREMENTS["cal_getc"] +
        COURSE_REQUIREMENTS["uc_davis_cs_prep"]
    )
    return all_courses

def get_total_course_count():
    """Returns the total number of unique courses to track."""
    # We subtract 1 because 'UCD_ECS_036C' is for display only
    # and isn't a course you can "complete" at MJC.
    return len(get_all_courses()) - 1