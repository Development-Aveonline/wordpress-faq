import zipfile
import xml.etree.ElementTree as ET
import json
import os
import re

FAQ_DIR = "faq"
OUTPUT = "faq.json"

def get_paragraphs(path):
    with zipfile.ZipFile(path) as z:
        xml_content = z.read("word/document.xml")
    root = ET.fromstring(xml_content)
    body = root.find("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}body")
    paras = []
    for p in body.findall("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"):
        texts = []
        for t in p.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"):
            if t.text:
                texts.append(t.text)
        line = "".join(texts).strip()
        if line:
            paras.append(line)
    return paras

def is_section_header(line):
    # Skip decorative/structural lines
    if re.match(r'^[═=]{5,}$', line):
        return True
    if re.match(r'^SECCI[OÓ]N\s+\d+', line, re.IGNORECASE):
        return True
    if re.match(r'^NOTAS\s+IMPORTANTES', line, re.IGNORECASE):
        return True
    if re.match(r'^\[INSTRUCCIONES:', line):
        return True
    if re.match(r'^Ejemplo:', line):
        return True
    if re.match(r'^PREGUNTAS\s+FRECUENTES', line, re.IGNORECASE):
        return True
    if re.match(r'^FAQs?\s+OPTIMIZADAS', line, re.IGNORECASE):
        return True
    # Skip known section titles
    known_titles = [
        "Automatización Shopify",
        "Plugin WooCommerce",
        "Envíos nacionales",
    ]
    if line.strip() in known_titles:
        return True
    # Skip single-word/short headers
    if re.match(r'^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\s*(nacionales|internacionales)?$', line):
        if len(line) < 30 and '?' not in line:
            return True
    return False

def is_question_line(line):
    # Pattern 1: "N. ¿...?" or "N. ...?" (numbered question)
    if re.match(r'^\d+\.\s+[¿¡]?', line) and line.rstrip().endswith('?'):
        return True
    # Pattern 2: "Pregunta N: ...?" (with optional space after colon, may have ¿)
    if re.match(r'^Pregunta\s*\d+\s*:\s*', line, re.IGNORECASE):
        if line.rstrip().endswith('?'):
            return True
        if '¿' in line:
            return True
    # Pattern 3: Line starts with ¿ and ends with ?
    if line.startswith('¿') and line.rstrip().endswith('?'):
        return True
    # Pattern 4: Inline Q&A — line starts with ¿ and contains ? mid-line (Q&A in same paragraph)
    if line.startswith('¿') and '?' in line and not line.rstrip().endswith('?'):
        return True
    return False

def split_inline_qa(line):
    """Split a line like '¿Pregunta? Respuesta...' into (question, answer) or return None."""
    if line.startswith('¿') and '?' in line:
        idx = line.index('?') + 1
        q = line[:idx].strip()
        a = line[idx:].strip()
        # Clean up zero-width spaces and leading garbage
        a = a.lstrip('\u200b').strip()
        if a:
            return q, a
    return None, None

def is_answer_line(line):
    return re.match(r'^Respuesta\s*:', line, re.IGNORECASE)

def is_pregunta_header(line):
    # Matches "Pregunta N:" where the question text might be on the same line or next
    return re.match(r'^Pregunta\s+\d+\s*:\s*$', line, re.IGNORECASE)

def parse_faq(paras):
    items = []
    current_q = None
    current_a_parts = []
    i = 0

    while i < len(paras):
        line = paras[i]

        if is_section_header(line):
            i += 1
            continue

        # Check for "Pregunta N:" on its own line (question text follows)
        if re.match(r'^Pregunta\s*\d+\s*:\s*$', line, re.IGNORECASE):
            # Question text is likely on the next line
            if i + 1 < len(paras):
                next_line = paras[i + 1]
                if not is_answer_line(next_line) and not is_pregunta_header(next_line):
                    i += 1
                    line = next_line  # Use next line as the question
                else:
                    # "Respuesta:" follows directly, skip this
                    i += 1
                    continue

        # Check for inline numbered Q&A: "N. ¿Pregunta?Respuesta..." (no newline between Q and A)
        numbered_qa = re.match(r'^(\d+\.\s*)([¿¡].*?\?)(.+)$', line, re.DOTALL)
        if numbered_qa:
            num_prefix = numbered_qa.group(1)  # e.g. "10. "
            q_text = numbered_qa.group(2).strip()  # "¿Pregunta?"
            a_text = numbered_qa.group(3).strip()  # "Respuesta..."
            # Save previous Q&A
            if current_q is not None:
                answer = "\n".join(current_a_parts).strip()
                answer = re.sub(r'^Respuesta\s*:\s*', '', answer, flags=re.IGNORECASE).strip()
                if answer:
                    items.append({"question": current_q, "answer": answer})
            current_q = q_text
            current_a_parts = [a_text]
            i += 1
            continue

        # Check if line contains "Pregunta N:" mid-line (answer merged with next question)
        pregunta_match = re.search(r'(Pregunta\s*\d+\s*:\s*[¿¡]?)', line)
        if pregunta_match and pregunta_match.start() > 0:
            # Split the line at the "Pregunta N:" boundary
            split_pos = pregunta_match.start()
            answer_part = line[:split_pos].strip()
            question_part = line[split_pos:].strip()
            if answer_part and current_q is not None:
                current_a_parts.append(answer_part)
            # Process the question_part as a new question
            q = re.sub(r'^Pregunta\s+\d+:\s*', '', question_part, flags=re.IGNORECASE).strip()
            q = re.sub(r'^\d+\.\s+', '', q).strip()
            # Save previous Q&A
            if current_q is not None:
                answer = "\n".join(current_a_parts).strip()
                answer = re.sub(r'^Respuesta\s*:\s*', '', answer, flags=re.IGNORECASE).strip()
                if answer:
                    items.append({"question": current_q, "answer": answer})
            current_q = q
            current_a_parts = []
            i += 1
            continue

        # Now check if this line is a question
        if is_question_line(line):
            # Check for inline Q&A (question and answer in same paragraph)
            inline_q, inline_a = split_inline_qa(line)
            if inline_q and inline_a:
                # Save previous Q&A if exists
                if current_q is not None:
                    answer = "\n".join(current_a_parts).strip()
                    answer = re.sub(r'^Respuesta\s*:\s*', '', answer, flags=re.IGNORECASE).strip()
                    if answer:
                        items.append({"question": current_q, "answer": answer})
                current_q = inline_q
                current_a_parts = [inline_a]
                i += 1
                continue

            # Save previous Q&A if exists
            if current_q is not None:
                answer = "\n".join(current_a_parts).strip()
                # Clean up leading "Respuesta:" from answers
                answer = re.sub(r'^Respuesta\s*:\s*', '', answer, flags=re.IGNORECASE).strip()
                if answer:
                    items.append({"question": current_q, "answer": answer})

            # Extract clean question text
            q = line.strip()
            # If it starts with "Pregunta N: ", remove that prefix
            q = re.sub(r'^Pregunta\s*\d+\s*:\s*', '', q, flags=re.IGNORECASE).strip()
            # Remove leading numbering like "1. ", "10. "
            q = re.sub(r'^\d+\.\s+', '', q).strip()
            current_q = q
            current_a_parts = []
            i += 1
            continue

        # If it's an "Respuesta:" line, the rest of answer follows
        if is_answer_line(line):
            # Extract the part after "Respuesta:" if any
            answer_text = re.sub(r'^Respuesta\s*:\s*', '', line, flags=re.IGNORECASE).strip()
            if answer_text:
                current_a_parts.append(answer_text)
            # If no text after "Respuesta:", the answer is in subsequent paragraph(s)
            i += 1
            continue

        # Otherwise it's a continuation of the current answer
        if current_q is not None:
            current_a_parts.append(line)
        i += 1

    # Save last Q&A
    if current_q is not None:
        answer = "\n".join(current_a_parts).strip()
        answer = re.sub(r'^Respuesta\s*:\s*', '', answer, flags=re.IGNORECASE).strip()
        if answer:
            items.append({"question": current_q, "answer": answer})

    # Filter out items with questions that are clearly not real (like standalone "Pregunta N:")
    items = [item for item in items if not re.match(r'^Pregunta\s+\d+\s*$', item["question"], re.IGNORECASE)]

    return items


all_items = []
for fname in sorted(os.listdir(FAQ_DIR)):
    if not fname.endswith(".docx"):
        continue
    fpath = os.path.join(FAQ_DIR, fname)
    print(f"Processing {fname}...")
    paras = get_paragraphs(fpath)
    items = parse_faq(paras)
    print(f"  -> extracted {len(items)} Q&A pairs")
    all_items.extend(items)

# Remove potential duplicates based on question text
seen_questions = set()
unique_items = []
for item in all_items:
    q = item["question"].strip().lower()
    if q not in seen_questions:
        seen_questions.add(q)
        unique_items.append(item)

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(unique_items, f, ensure_ascii=False, indent=2)

print(f"\nDone! Generated {OUTPUT} with {len(unique_items)} total Q&A pairs (from {len(all_items)} raw, {len(all_items) - len(unique_items)} duplicates removed).")
