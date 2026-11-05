feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

additional_feedbacks = int(input("How many more feedbacks do you want to add? "))

for i in range(additional_feedbacks):
    name = input("Enter name: ")
    text = input("Enter feedback: ")
    valid = False
    while valid == False:
        rating = int(input("Enter rating (1-5): "))
        if rating < 1:
            print("Rating is too low. Please enter 1 to 5.")
        elif rating > 5:
            print("Rating is too high. Please enter 1 to 5.")
        else:
            valid = True
    feedback_data['S_No'].append(len(feedback_data['S_No']) + 1)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(text)
    feedback_data['Rating'].append(rating)

for i in range(len(feedback_data['Feedback'])):
    text = feedback_data['Feedback'][i]
    for p in ['.', ',', '!', '?']:
        text = text.replace(p, '')
    text = ' '.join(text.split()).lower()
    feedback_data['Feedback'][i] = text


def count_word_in_feedbacks(word):
    word = word.lower()
    count = 0
    for text in feedback_data['Feedback']:
        if word in text.split():
            count += 1
    return count


print("Word Count Insights")
print("Feedbacks containing 'good':", count_word_in_feedbacks("good"))
print("Feedbacks containing 'poor':", count_word_in_feedbacks("poor"))
print("Feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))

print("Final Cleaned Feedback Data")
print(feedback_data)

print("Final Summary and Insights")
average = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print("Average rating:", average)

longest_text = ""
longest_count = 0
for text in feedback_data['Feedback']:
    if len(text.split()) > longest_count:
        longest_count = len(text.split())
        longest_text = text
print("Longest feedback:", longest_text)

unique_words = set()
for text in feedback_data['Feedback']:
    for w in text.split():
        unique_words.add(w)
print("Unique words:", unique_words)

print("Feedbacks Sorted by Rating (Highest to Lowest)")
for r in [5, 4, 3, 2, 1]:
    for i in range(len(feedback_data['Rating'])):
        if feedback_data['Rating'][i] == r:
            print(feedback_data['S_No'][i], feedback_data['Name'][i], feedback_data['Feedback'][i], feedback_data['Rating'][i])
