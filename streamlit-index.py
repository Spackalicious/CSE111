import streamlit as st

"""
# Begin writing your story!
Start with your characters and setting: 
"""
story = ""
title = "Your Story:"
with st.sidebar: 
    st.title(f'{title}')

location = st.selectbox(
    'Where does your story take place? ',
    ('city', 'mountains', 'forest', 'canyon', 'hills', 'alleys'), key=9)
main_character = st.text_input('Enter the name of your main character: ')
best_friend = st.text_input('Enter the name of the best friend: ')
villain = st.text_input('Enter the name of the villain in your story: ')

def fork5(main_character, best_friend, villain, story):
    fork5_opt1 = f"\n{villain} got in a deadly shot and wounded {main_character} right in the heart. {best_friend} ran to kneel down beside {main_character} and looked up, accusingly, at {villain}. \"Look what you've done!\" {best_friend} exclaimed angrily. {villain} sneered disdainfully and pointed accusingly at {best_friend}, while shouting, \"Now you know what it's like to feel extreme pain!\" The two engaged in a deadly duel, which ended with both of them fatally injured. At the end of the day, all three lay dying in the road with no one to help them. \n\nThe End. "
    fork5_opt2 = f"{villain} got in a deadly shot and wounded {main_character} right in the shoulder. {best_friend} ran to kneel down beside {main_character} and looked up, accusingly, at {villain}. \"Look what you've done!\" {best_friend} exclaimed angrily. {villain} looked shocked to see so much crimson blood, and then guiltily dismayed when {main_character} let out a faint moan. {villain} whispered, \"Do you think a doctor could fix this?\" At the next whimper, {best_friend} declared \"If anybody is going to fix anything, we'd better move quickly!\" \n\nThe two previous enemies carefully escorted {main_character} to the nearest emergency room, and then prayed together that things would be alright. The medical staff were able to work miracles, and {main_character} made a full recovery! This led to forgiveness all around. "
    selection5 = st.selectbox('Option4',        
        ('What will happen next? ', fork5_opt1, fork5_opt2), key=5, label_visibility = "collapsed")

    if selection5 == fork5_opt1:
        story += selection5
        st.write("Bravo! You've just successfully written a tragedy.")
        title = st.text_input('What would you like to call your story? ')
        author = st.text_input('What is the author\'s name? ')
        with st.sidebar: 
            st.title(f'{title}')
            if author: 
                st.subheader(f'by {author}')
    elif selection5 == fork5_opt2: 
        story += selection5 + fork4(main_character, best_friend, villain, story)   
    return story

def fork4(main_character, best_friend, villain, story):
    fork4_opt1 = f"{main_character}, {best_friend}, and {villain} were so happy to have things good among them, that they decided to go over some grassy hills, cross a plain, and canoe over a lake in order to visit a nearby town and do some touristy things together. \n\nAfterwards, they all lived happily ever after. \n\nThe end. "
    fork4_opt2 = f"{main_character}, {best_friend}, and {villain} were so happy to have things good among them, that they decided to go to the beach one town over and go swimming together. \n\nAfter their swim, they all lived happily ever after. \n\nThe end. "
    selection4 = st.selectbox('Option3',        
        ('What should happen now? ', fork4_opt1, fork4_opt2), key=4, label_visibility = "collapsed")

    if selection4 == fork4_opt1 or selection4 == fork4_opt2:
        story += selection4
        st.write("Congratulations! You've written a happy tale!")
        title = st.text_input('What would you like to call your story? ')
        author = st.text_input('What is the author\'s name? ')
        with st.sidebar: 
            st.title(f'{title}')
            if author: 
                st.subheader(f'by {author}')
    return story

def fork3(main_character, best_friend, villain, story):
    fork3_opt1 = f"{villain} was surprised at their kind reaction. \"Wow! Hello! I'm so sorry for the things that happened before!\" {villain} said, and asked for forgiveness. {main_character} and {best_friend} were happy to see that {villain} was sincere. \n\nThey were able to have a wonderful conversation about old times and good friends. "
    fork3_opt2 = f"However, {villain} drew a weapon, crying \"What foul trick is this?\" and so {main_character} and {best_friend} drew their weapons in response, and a vicious battle ensued! "
    selection3 = st.selectbox('Option2',        
        ('What a tale! Do go on! ',fork3_opt1, fork3_opt2), key=3, label_visibility = "collapsed")

    if selection3 == fork3_opt1: 
        story += selection3 + fork4(main_character, best_friend, villain, story)
    elif selection3 == fork3_opt2: 
        story += selection3 + fork5(main_character, best_friend, villain, story) 
    return story

def fork2(main_character, best_friend, villain, story):
    fork2_opt1 = f"{villain} immediately stepped back with hands raised. \"Whoa! Please! Let me speak! I'm so sorry for the things that happened before!\" {villain} cried. {main_character} and {best_friend} cautiously lowered their weapons, but then decided that {villain} was sincere. \nThey were able to have a wonderful conversation about old times and good friends. "
    fork2_opt2 = f"{villain} drew their weapon also, and a vicious battle ensued! "
    selection2 = st.selectbox('Option2',        
        ('What happens next? ', fork2_opt1, fork2_opt2), key=2, label_visibility = "collapsed")

    if selection2 == fork2_opt1: 
        story += selection2 + fork4(main_character, best_friend, villain, story)
    elif selection2 == fork2_opt2: 
        story += selection2 + fork5(main_character, best_friend, villain, story) 
    return story

def fork1(main_character, best_friend, villain, story):
    st.write('Continue writing your story!')
    fork1_opt1 = f'{main_character} and {best_friend} immediately drew their weapons. "What are you doing here?" they demanded. '
    fork1_opt2 = f'{main_character} and {best_friend} smiled at {villain}. "Wow! Long time no see! How have you been?" they asked. '
    selection1 = st.selectbox( 'Option1',
        ('How will your story continue?', fork1_opt1, fork1_opt2), key=1, label_visibility = "collapsed")

    if selection1 == fork1_opt1: 
        story += selection1 + fork2(main_character, best_friend, villain, story)        
    elif selection1 == fork1_opt2: 
        story += selection1 + fork3(main_character, best_friend, villain, story)        
    return story

def opener(main_character, best_friend, villain, location):
    opening_line = f"Once upon a time, {main_character} and {best_friend} were walking through the {location} when they met their old enemy, {villain}. "
    return opening_line

if main_character and best_friend and villain and location:
    story += opener(main_character, best_friend, villain, location) + fork1(main_character, best_friend, villain, story)
        # the other forks are determined within each fork function


st.sidebar.write(f'{story}')