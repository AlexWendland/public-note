---
aliases: 
checked: false
created: 2025-06-29
last_edited: 2025-06-29
draft: true
tags:
  - finance
  - work
  - philosophy
type: blog
---
# How I think about work

A couple things in life have prompted me to think about work
- I am doing a masters and working a job at the same time - which is stressing me out,
- I read the [The 4-Hour Work Week](https://fourhourworkweek.com/),
- I have been reading a couple books on philosophy,
- I got turned down for a promotion last year - without much explanation,
- I realized when my manager asks if I want to do a project or not I don't have a system to think about my response,
- I am hopefully moving to the US soon, and
- I spoke to a friend who asked what I wanted in a job.

So I think it is time to do some verbal vomit on a page and see what comes out!

My real take away from the 4-hour work week was the following statement

>[!important] Work is the solution to a problem
> The problem work solves is not having enough money to do the things we want to in life. When we face a problem, we need to solve the problem and not fixating too much on the solution. So lets first frame the problem correctly so we can look at solutions.

So in this ramble I want to get a picture that will aid me in making decisions when considering different actions I can take like:

- Do I want to work at this job,
- Do I want to do a start up,
- Should I say yes to this promotion, or
- Should I agree to work on this project.

## What do I want to do and what do I need to do it?

My hobbies are fairly cheap:
- Running,
- Programming,
- Board games, and
- Learning.
The main substantial activity I have in life is visiting my wife Janet in the US and traveling with her. I wouldn't say traveling is a hobby of mine but I like seeing different cultures and love seeing Janet happy.

I live in London which is EXPENSIVE, I have tried to keep life inflation down but my expenses have gone up since I was a student. So lets get to the numbers:

>[!note] I am keeping costs per month - that is just how I think

| Activity            | Cost per month (£) |
| ------------------- | ------------------ |
| Rent                | 750                |
| Day to day expenses | 1500               |
| Holiday fund        | 250                |
| **Total**           | **2500**           |

My day to day is quite large - this is mainly as I am lazy. I pay for a meal service and eat lunches out that costs about £700 in itself. Tbh I am not 100% sure what the rest is ... that is most probably a blog post in itself - I do have the data!

Ok so financially I need £2500 per month after tax to live like I do at the moment .... well do I?

I did a PhD so I am going to consider time before 25 just sunk time that our lovely government or parents pay for. Between 25 - 65 I am going to assume I work 90% of the time giving me 36 years of work. I am going to be optimistic and assume I live till 85. So I need to earn (85-25 = 60 * 12 * 2500) post tax income using 36 years of work.

Lets break that down to a per month post tax number to keep it simple, this is:
$$2500 * 60 / 36 = 4166.66.. \sim 4200$$ 
>[!note] FIRE people
>For the Financially Independent Retire Early people you can shorten the time horizon by just reducing the number of years you work.

## Work is a cost?

Ok so work is the solution but I am not going to pretend all work is made equal. It is perfectly possible to do work you love, so when thinking about work as a 'cost' I think that is a little harsh.

Instead lets use a metric called 'Hours not enjoyed per week'. This is a gross simplification but please entertain me for a little bit.

I am a developer, I love just being in my room working on code that does something cool. But being a developer isn't that ... it is a lot of other stuff some of which I like - some of which I don't. You can roughly map hours of these times of behavior to roughly some number between 0 and 1 on hours you like or not. E.g.

- No time pressure coding on something I am proud of: 0
	- Love it
- Pair programming with a big brain who is happy to mentor me: 0
	- If it could go negative ... I would let it.
- Mentoring a junior engineer who is receptive to learning: 0.1
	- I am not good with people but I find it very rewarding.
- No time pressure coding in a rats nest of a code base: 0.3
	- Ok .. not fun but I like moaning also.
- Coding reviewing someone who does not care about their code: 1
	- Urghh the worst.
- Writing ADR/RFC's researching code: 0.2
	- I know a lot of people don't like it but I love putting my detective hat on.
- Debugging: 0.8
	- Controversial, I know some people love it - too much information for me, and normally too much at stake.
- Meetings, syncs, project planning: 1
	- mouth talking, ears listening, eyes drooping
- Slack: 1
	- Urghhh ping ping ping ... please stop

I think you get the point, you can look at a job or project and roughly work out for you how much time spent not enjoying yourself you are going to do.

>[!Example] Flow state
>I think a pretty good judge of whether you like something or not is how time passes whilst your doing it. If it is effortless action for you, you like it - whether you want to or not. Try to be honest with yourself.

Ok so ideally we keep the 'Hours not enjoyed per week' to a bare minimum. 

If you are shouting at the screen right now saying life isn't this simple, I have other commitments like child care, looking after relatives, doing university, or some other commitment. Then say every hour you have to work instead of doing the commitments is an hour you don't enjoy yourself - or simpler still just use the amount of hours you need to work.

If you are shouting at the screen, what about purpose? I don't enjoy my work but I feel like a great person for doing it. Then factor it in, having purpose in your role is super meaningful and it makes the days go faster as you achieve something great. Therefore the hours you work are a little less ... terrible. 

## Idea for a graph

Ok so we have post tax monthly income which is my goal, enough to fund my hobbies and life style. We have the cost of work which is hours spent not enjoying myself. Then lastly I need to judge how I feel about being in that situation which I will call a rating, i.e. we have a function

$$
f: \mbox{post-tax monthly-income} \times \mbox{sad hours per week} \rightarrow \mbox{rating}.
$$

>[!note] I use hours per week as that is how I think
>I know it is not consistent with the pay unit ... unlucky punk.

This will materialize as a 2D graph with some contours on if for how I feel about being in that situation. 

![[Life graph basic.excalidraw]]

## Where I am right now

### Pay

To know where you want to go, it is good to know where you are. Lets start simple, money.

I get paid £91,500 a year base. Then last year I got a discretionary bonus of 50% of my salary. I also get 5% pension paid by my company. This comes out in the wash as:

| Key points                        | Post-tax monthly income |
| --------------------------------- | ----------------------- |
| Current baseline (need)           | 2,500                   |
| UK average income (reference)     | 3,250                   |
| 36 years of work (need)           | 4,200                   |
| London average income (reference) | 4,350                   |
| Pay with pension (now)            | 5,200                   |
| Pay with pension + bonus (now)    | 7,500                   |

>[!note] References
>I donate 10% of my income to charity which is subtracted.
>I actually buy holiday which is subtracted from my pay with some other benefits.
>Average salaries were taken from [plumplot](https://www.plumplot.co.uk/London-salary-and-unemployment.html), I used [income tax calculator](https://www.gov.uk/estimate-income-tax) to account for tax, and added 5% pension match by the company.

### Hours spent not enjoying myself

I work 9-6 with a 1 hour lunch break. That is 8 hours a day (assuming I enjoy talking to work people), I then work 5 days a week but luckily very rarely work over time. So 40 hours not enjoying myself?

Well lets first talk about holiday, I get 25 days a year base, then I buy 8 days and my company gives me 12 days off for uni. Meaning that 9 out 52 weeks I am on holiday. That means I only work $40*43/52 = 33$ hours a week.

How much I enjoy work? This is hard and very project dependent. If I am writing code I am normally pretty content but that depends on the project. Right now I would say I am at about 0.7 for work hours with no real justification. So that makes the total: 23.5 but it is variable.

![[Life graph.excalidraw]]

## Where do I want to go

Ok I think up until now maybe I haven't said anything really that insightful - I hope the next bit is. As I said before we want to write the function $f$ that means at each point on this graph you need to judge how happy you are in that situation.

I am going to do it for 4 mental states:
- Life is just about bearable but I don't think fun is being had.
- Life is just fine.
- Life is good, could coast most of my life like this.
- I have essentially made it at this point.

![[Life graph contors.excalidraw]]

>[!warning] These are just gut feels
>I really do wonder if someone offered me the made it line if I would take it ... I think I would but I think you only know when the chips are down.

Some things I intuitively think should be true about the lines ... even if I am not sure if they are:
- If you are paid more for the same amount of bad hours that is better.
- If you spend less hours not enjoying yourself for the same pay that is better.
- The gradient should increase, as you get slammed with more unhappiness each additional extra hour of unhappiness should come at a higher price.

Some things that are maybe just true for me.
- I think I have a cut off at about 45 hours of unhappiness. At that point no more money really makes that much of a difference.
- If I don't have to work but still get an income, I could really cut down on life expenses.
- If I don't have to work, I don't think it will take that much money to make me happy.
- If I halved my pay but also halved the amount I had to do stuff I didn't enjoy.
- I am doing pretty good right now ... I should not stress and chill out a bit.

## What does this tell me

I think there are two main things I'll take away from this:
1. If taking a promotion gives me an extra 1k post-tax monthly income but I need to do another 5 hours of work that suck ... don't do it. It is not worth it. Similarly, if a project is really high profile so the bonus is good but is going to mean working with a team that suck ... don't do it.
2. When I am retired I don't need that much money. Not having to work, means my hobbies are cheap and I can cut down the life expenses.

## Rant about FIRE

I like the idea of FIRE but I think the book 4-hour work week has a better idea. Instead of burning all the time when you are young, relatively responsibility free, and have energy to earn money for the old you. Why not instead take breaks and spend that money when you are younger? Doesn't a year doing what you want sound good? What did old you (who you don't even know will be around) do that makes them deserve so much money?

When people used to not save at all for retirement - I agree it was an issue. But now retirement is so baked into most salaried work, I don't think the old guy deserves so much.
