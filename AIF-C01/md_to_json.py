import os
import re
import json

PAGES_DIR = os.path.join(os.path.dirname(__file__), 'pages')
OUTPUT_JSON = os.path.join(os.path.dirname(__file__), 'questions.json')

option_pattern = re.compile(r'^- ([A-Z])\. (.+)$')
answer_pattern = re.compile(r'^Correct Answer:?\s*(.*)$', re.IGNORECASE)
question_number_pattern = re.compile(r'Question\s*#(\d+)', re.IGNORECASE)


def determine_question_type(question_text, options):
    """
    Determine the question type based on the content.
    Returns: 'single_select', 'multi_select', or 'hotspot_dropdown'
    """
    question_lower = question_text.lower()
    
    # Check for hotspot questions
    if "hotspot" in question_lower:
        return "hotspot_dropdown"
    
    # Check for multi-select: if there's option "E" then this is multi_select
    if "E" in options:
        return "multi_select"
    
    # Default to single select
    return "single_select"


# Load existing questions if the file exists
existing_questions = {}
if os.path.exists(OUTPUT_JSON):
    try:
        with open(OUTPUT_JSON, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
            # Convert to dict with id as key for easier lookup
            existing_questions = {q['id']: q for q in existing_data}
        print(f"Loaded {len(existing_questions)} existing questions from {OUTPUT_JSON}")
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error loading existing questions: {e}. Starting fresh.")
        existing_questions = {}

questions = []

for filename in sorted(os.listdir(PAGES_DIR)):
    if not filename.endswith('.md'):
        continue
    with open(os.path.join(PAGES_DIR, filename), encoding='utf-8') as f:
        lines = f.read().splitlines()
    qtext = []
    options = {}
    answer = None
    qid = None
    skip_next = False
    for idx, line in enumerate(lines):
        if skip_next:
            skip_next = False
            continue
        opt_match = option_pattern.match(line)
        ans_match = answer_pattern.match(line)
        qnum_match = question_number_pattern.search(line)
        if qnum_match and qid is None:
            qid = int(qnum_match.group(1))
        if opt_match:
            options[opt_match.group(1)] = opt_match.group(2)
        elif ans_match:
            # If the next line exists, use all chars before the first space as the answer
            if idx + 1 < len(lines):
                next_line = lines[idx + 1].strip()
                if next_line:
                    answer_str = next_line.split(' ', 1)[0]
                    if ',' in answer_str:
                        answer = [a.strip() for a in answer_str.split(',') if a.strip()]
                    else:
                        answer = answer_str
                    skip_next = True
            # Otherwise, fallback to previous logic
            else:
                ans_val = ans_match.group(1).strip()
                if ',' in ans_val:
                    answer = [a.strip() for a in ans_val.split(',') if a.strip()]
                elif ans_val:
                    answer = ans_val
        else:
            qtext.append(line)
    # Remove trailing empty lines
    while qtext and not qtext[-1].strip():
        qtext.pop()
    question_md = '\n'.join(qtext)
    
    # Determine question type
    question_type = determine_question_type(question_md, options)
    
    # Create new question data
    new_question = {
        'id': qid,
        'question': question_md,
        'question_type': question_type,
        'options': options,
        'answer': answer
    }
    
    # Check if this question already exists
    if qid in existing_questions:
        # Update existing question with new data
        existing_questions[qid].update(new_question)
        print(f"Updated existing question #{qid}")
    else:
        # Add new question
        existing_questions[qid] = new_question
        print(f"Added new question #{qid}")
    
    questions.append(new_question)

# Convert back to list and sort by id
final_questions = sorted(existing_questions.values(), key=lambda q: q['id'])

with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(final_questions, f, indent=2, ensure_ascii=False)

print(f"Successfully saved {len(final_questions)} questions to {OUTPUT_JSON}")
