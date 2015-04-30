def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
    <h1 class="title">
        <h3 class="concepts">
            ''' + concept_title
    html_text_2 = '''
        </h3>
        <div class="text">
            ''' + concept_description
    html_text_3 = '''
        </div>
    </h1>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('CONCEPT:')
    end_location = concept.find('TEXT:')
    title = concept[start_location+8 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('TEXT:')
    description = concept[start_location+6 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('CONCEPT:')
        next_concept_end   = text.find('CONCEPT:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept
        

TEST_TEXT = """CONCEPT: Structured Data
TEXT: Lists are structured data because they contain defined positions. Strings are also structured, since their positions can also be queried.
CONCEPT: Mutability
TEXT: Lists are mutable, strings are not. Mutability means having the ability to change elements within the list, without creating a whole new list.
CONCEPT: Append vs +
TEXT: Appending a list to another list adds only one element to the initial list. This new element refers to the list that was appended. Therefore, changes to the appended list will be reflected in the list it was appended to. + works a lot like concatenate. If you concatenate two lists, each element in the appended list becomes a separate element in the list it was concatenated with.
CONCEPT: For Loops
TEXT: For Loops allow you to execute a piece of code multiple times (iterate), and are typically used when the number of iterations is known. Othwerwise, a While Loop could be used. For Loops iterate over a list or a string, in the order that they appear.
CONCEPT: How to Solve Problems
TEXT: 0. Don't Panic
      <br> 1. What are the <b>Inputs</b>?
      <br> 2. What are the <b>Outputs</b>?
      <br> 3. Work through some examples by hand.
      <br> 4. Simple mechanical solution.
      <br> 5. Develop incrementally and <u>test</u> as you go."""


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(TEST_TEXT)
