"""
Grace Crowder
Class: CS 521 - Fall
Date: 12/7/22
Final Project
Description of Problem (just a 1-2 line summary!):  A code for spam detection.
My code counts for variables I find through research that often suggest
something is spam or not.
"""


class Email:
    def __init__(self, text_analysis, sus_sender1, spam_phrases):
        self.text_analysis = text_analysis
        self.sus_sender = sus_sender1
        self.spam_phrases = spam_phrases

    def repr(self):
        return self.text_analysis + " " + self.sus_sender + " " + \
               self.text_analysis

    def spam_in_subject(self):
        """
        This function will test if the subject line within the email is likely
        to be spam.
        """
    SPAM_PHRASES = ['save', 'details inside' 'make money', 'buy now', 'click ',
                    'here', 'click link', 'additional income', 'cash bonus',
                    'double', 'earn more', 'once in a lifetime']
    print('Welcome to the Basic Python Spam checker. Before we begin, copy and'
          'paste the body of the email to the file body.txt that you would '
          'like to scan')
    print('After you have done that, move on to Step 2.')
    print('Step 2: Test the Subject')
    subject = input("Enter the subject of the e-mail you would like to scan "
                    "(if there is not a subject, type N/A): ")

    for phrase in SPAM_PHRASES:
        if phrase in subject:
            subject = str(False)
            print('Test 1 failed the Spam checker. Further analysis needed.')
        elif "N/A" in subject:
            print('Test 1 is not applicable as there is no subject.')
        else:
            subject = str(True)
            print('Test 1 Passed the Spam checker. Further analysis is still '
                  'necessary.')
        continue

    @staticmethod
    def spam_in_body():
        """
        This function will test if the body text within the email is likely to
        be spam.
        """
        bad_phrases = ['save', 'details inside' 'make money', 'buy now',
                       'click ', 'here', 'click link', 'additional income',
                       'cash bonus', 'double', 'earn more', 'once in a '
                                                            'lifetime']
        body_text = open("body.txt", "r")
        for phrases in bad_phrases:
            if phrases in body_text:
                body_text = str(False)
                print('Test 2 failed the Spam checker. Further analysis needed'
                      '.')
            else:
                body_text = str(True)
                print('Test 2 Passed the Spam checker. Further analysis is '
                      'still necessary.')
            continue

    @staticmethod
    def spam_sender():
        """
        This function will test if the sender of the email is likely to be
        spam.
        """
        print(input("Enter the email address of the sender: "))
        sus_sender = ['noreply', '-']
        for phrases in sus_sender:
            if phrases in sus_sender:
                print('Do you personally know this individual or organization?'
                      '')
                choice = input("Y or N: ")
                if choice == 'N' or 'n':
                    sus_sender = False
                    print('Test 3 failed the Spam checker.')
                elif choice == 'Y' or 'y':
                    sus_sender = True
                    print('Test 3 Passed the Spam checker.')
                else:
                    print('Error: You did not type Y or N.')
            continue

    @staticmethod
    def final_consideration():
        print('After consideration we have found: ')
        if subject and body_text and sus_sender is True:
            print('The spam checker has decided this email is NOT SPAM.')
        elif subject and body_text is True and sus_sender is False:
            print("The spam checker believes this email is PROBABLY NOT SPAM.")
        elif subject is True and body_text and sus_sender is False:
            print("The spam checker believes this email is PROBABLY SPAM.")
        elif subject is False and body_text and sus_sender is True:
            print("The spam checker believes this email is PROBABLY NOT SPAM.")
        elif subject and body_text and sus_sender is False:
            print("The spam checker believes this email is SPAM.")


if __name__ == '__main__':
    print('The Spam check is complete')
