---
aliases: []
type: design document
publish: true
created: 2023-05-15
last_edited: 2023-05-15
tags: project
chatgpt: false
---
# Coffee Roulette Application

I am planning on writing a very simple application for setting up a coffee roulette. Something that matches participants with others on a schedule they decide, to meet up for a coffee. I used to run a couple of these off a google sheet when I worked for the civil service - however thought it would be fun to modernise it.

> What is the software application or feature?

The core functionality will
- Allow someone to set up a coffee roulette using an email.
	- This will give them a form they can give to people to sign up.
	- It will have a screen for them to manage the coffee roulette.
- It will allow people to sign up using their email.
	- It will have a screen for them to activate and deactive roulette subscriptions and tap out for a bit whilst they are on holiday.
- The core mechanics will:
	- On a specified schedule match people in the roulette so they meet someone new (if possible).
	- Send emails out to the people who have been matched.

> Who is it intended for?

This is aimed at civil servants. This is the audience I have the most exposure to and already people who are willing to use it. It will simplify their user experience of having to use the google sheet.

> What problem does it solve?

It allows people effortless meeting of new people to allow for networking and idea sharing. Civil servants tend to be less technologically enabled so it has to do this in a simple way.

> How is it going to work?

It will work through a simple web interface, it will try to minimise authentication hassle but just using email verification. To match people it will evaluate 'suitable fit' and then using linear programming to make an optimal match.

> What are the main concepts that are involved and how are they related?

- Front end development for the UI (this will be simple and clean)
- Back end database guarded with an API.
- Matching algorithms (linear programming).
- Email server and email verification.

1. First I can build the database with an API - I have done this before using Fast API.
2. I can write an email application that can send emails.
3. I can add in email verification to allow people to sign in.
4. I can write the matching algorithms to send the emails.
5. I can wrap this all in a nice UI.

> What are the main user stories?

## Creating a coffee roulette

1. Click on the website.
2. Make a coffee roulette using an email.
3. Verify the email using a code sent to the email address.
4. Configure the coffee roulette
	1. Set maximum frequency of meeting
	2. Set email that will be sent out
	3. Configure name
	4. Write message to appear on the form
5. Get sent a link for people to sign up using it

## Signing up for a coffee roulette

1. Go on the link provided by creator
2. Put in email
3. Verify it using a code
4. Get sent to a page to manage their coffee roulette and personal settings

## Booking holiday

1. Go to the website.
2. Sign in with email.
3. Verify email using code.
4. Get set to page to manage their coffee roulette.
5. Click dates they will be on holiday.

## Changing Emails

1. Go to the website.
2. Sign in with email.
3. Verify email using code.
4. Get set to page to manage their coffee roulette.
5. click add email.
6. Verify that through a code.

> What technical details need developers to know to develop the software or new feature?

- Databases - Most probably postgress?
- Micro processes - docker containers or AWS lambda functions.
- API - Most probably will use FastAPI a python library.

> Are there new tables to be added to the database? What fields?

## Users
id
name
bio
memorable_question_1
memorable_answer_1
memorable_question_2
memorable_answer_2
memorable_question_3
memorable_answer_3
default_frequency

## Emails
Email address
user_id

## Coffee Roulette
organiser_id
maximum frequency
roulette_id

## Subscriptions
User_id
roulette_id
frequency
last_matching

## Meetings
date
fist_user
second_user

## holidays
start_date
end_date
user_id

# Issues
1. Civil servants change emails lots - how do I account for this?
	1. Memorable question and answer?
2. How do I weed out people that do not reply to the emails?