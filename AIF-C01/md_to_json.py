import os
import re
import json

PAGES_DIR = os.path.join(os.path.dirname(__file__), 'pages')
OUTPUT_JSON = os.path.join(os.path.dirname(__file__), 'questions.json')

option_pattern = re.compile(r'^- ([A-Z])\. (.+)$')
answer_pattern = re.compile(r'^Correct Answer:?\s*(.*)$', re.IGNORECASE)
question_number_pattern = re.compile(r'Question\s*#(\d+)', re.IGNORECASE)

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
    questions.append({
        'id': qid,
        'question': question_md,
        'options': options,
        'answer': answer
    })

with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(sorted(questions, key=lambda q: q['id']), f, indent=2, ensure_ascii=False)
