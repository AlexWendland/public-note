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

Several things in life have prompted me to think more deliberately about work:

- I am doing a master's degree and working a job at the same time - which is stressing me out
- I read [The 4-Hour Work Week](https://fourhourworkweek.com/)
- I have been reading several books on philosophy
- I got turned down for a promotion last year - without much explanation
- I realized when my manager asks if I want to do a project or not, I don't have a system to think about my response
- I am hopefully moving to the US soon
- I spoke to a friend who asked what I wanted in a job

So I think it's time to do some thinking on paper and see what comes out!

My real takeaway from the 4-hour work week was the following statement:

>[!important] Work is the solution to a problem
> The problem work solves is not having enough money to do the things we want in life. When we face a problem, we need to solve the problem and not fixate too much on the solution. So let's first frame the problem correctly so we can look at solutions.

So in this exploration I want to develop a framework that will aid me in making decisions when considering different actions I can take like:

- Do I want to work at this job?
- Do I want to do a startup?
- Should I say yes to this promotion?
- Should I agree to work on this project?

## What do I want to do and what do I need to do it?

My hobbies are fairly cheap:
- Running
- Programming
- Board games
- Learning

The main substantial activity I have in life is visiting my wife Janet in the US and traveling with her. I wouldn't say traveling is a hobby of mine, but I like seeing different cultures and love seeing Janet happy.

I live in London, which is EXPENSIVE. I have tried to keep lifestyle inflation down, but my expenses have gone up since I was a student. So let's get to the numbers:

>[!note] I am keeping costs per month - that is just how I think

| Activity            | Cost per month (£) |
| ------------------- | ------------------ |
| Rent                | 750                |
| Day to day expenses | 1500               |
| Holiday fund        | 250                |
| **Total**           | **2500**           |

My day-to-day expenses are quite large - this is mainly because I am lazy. I pay for a meal service and eat lunches out, which costs about £700 by itself. To be honest, I am not 100% sure what the rest is... that is most probably a blog post in itself - I do have the data!

OK, so financially I need £2,500 per month after tax to live like I do at the moment... well, do I?

I did a PhD, so I am going to consider time before 25 just sunk time that our lovely government or parents pay for. Between 25-65 I am going to assume I work 90% of the time, giving me 36 years of work. I am going to be optimistic and assume I live until 85. So I need to earn (85-25 = 60 × 12 × 2500) post-tax income using 36 years of work.

Let's break that down to a per-month post-tax number to keep it simple. This is:
$$2500 × 60 ÷ 36 = 4166.66... ≈ 4200$$ 

>[!note] FIRE people
>For the Financially Independent Retire Early people, you can shorten the time horizon by just reducing the number of years you work.

## Work is a cost?

OK, so work is the solution, but I am not going to pretend all work is created equal. It is perfectly possible to do work you love, so when thinking about work as a 'cost' I think that is a little harsh.

Instead, let's use a metric called 'Hours not enjoyed per week'. This is a gross simplification, but please entertain me for a little bit.

I am a developer. I love just being in my room working on code that does something cool. But being a developer isn't just that... it is a lot of other stuff, some of which I like - some of which I don't. You can roughly map hours of these different activities to some number between 0 and 1 based on how much you like or don't like them. For example:

- **No time pressure coding on something I am proud of: 0**
	- Love it
- **Pair programming with a brilliant mentor: 0**
	- If it could go negative... I would let it
- **Mentoring a junior engineer who is receptive to learning: 0.1**
	- I am not good with people, but I find it very rewarding
- **No time pressure coding in a rat's nest of a codebase: 0.3**
	- OK... not fun, but I like complaining also
- **Code reviewing someone who doesn't care about their code: 1**
	- Ugh, the worst
- **Writing ADRs/RFCs, researching code: 0.2**
	- I know a lot of people don't like it, but I love putting my detective hat on
- **Debugging: 0.8**
	- Controversial, I know some people love it - too much information for me, and normally too much at stake
- **Meetings, syncs, project planning: 1**
	- Mouth talking, ears listening, eyes drooping
- **Slack: 1**
	- Ugh, ping ping ping... please stop

I think you get the point - you can look at a job or project and roughly work out how much time you'll spend not enjoying yourself.

>[!Example] Flow state
>I think a pretty good judge of whether you like something or not is how time passes while you're doing it. If it is effortless action for you, you like it - whether you want to or not. Try to be honest with yourself.

OK, so ideally we keep the 'Hours not enjoyed per week' to a bare minimum. 

If you are shouting at the screen right now saying "life isn't this simple, I have other commitments like childcare, looking after relatives, doing university, or some other commitment" - then say every hour you have to work instead of doing those commitments is an hour you don't enjoy yourself, or simpler still, just use the total amount of hours you need to work.

If you are shouting at the screen, "what about purpose? I don't enjoy my work but I feel like a great person for doing it" - then factor it in. Having purpose in your role is super meaningful and it makes the days go faster as you achieve something great. Therefore, the hours you work are a little less... terrible. 

## The Framework: A Visual Approach

OK, so we have:
1. **Post-tax monthly income** - my goal, enough to fund my hobbies and lifestyle
2. **The cost of work** - hours spent not enjoying myself  
3. **A rating** - how I feel about being in that situation

We can express this as a function:

$$
f: \text{post-tax monthly income} × \text{unhappy hours per week} → \text{rating}
$$

>[!note] I use hours per week as that is how I think
>I know it is not consistent with the pay unit... unlucky.

This will materialize as a 2D graph with contour lines showing how I feel about being in different situations. 

![[Life graph basic.excalidraw]]

## Where I am right now

### Current Financial Situation

To know where you want to go, it is good to know where you are. Let's start simple: money.

I get paid £91,500 a year base salary. Last year I received a discretionary bonus of 50% of my salary. I also get a 5% pension contribution paid by my company. This works out to:

| Scenario                          | Post-tax monthly income (£) |
| --------------------------------- | ---------------------------- |
| Current baseline (need)           | 2,500                        |
| UK average income (reference)     | 3,250                        |
| 36 years of work (need)           | 4,200                        |
| London average income (reference) | 4,350                        |
| My salary with pension            | 5,200                        |
| My salary with pension + bonus    | 7,500                        |

>[!note] References and assumptions
>- I donate 10% of my income to charity, which is subtracted from these figures
>- I buy additional holiday days, which is subtracted from my pay along with other benefits
>- Average salaries were taken from [plumplot](https://www.plumplot.co.uk/London-salary-and-unemployment.html)
>- I used the [government income tax calculator](https://www.gov.uk/estimate-income-tax) to account for tax
>- Added 5% pension match by the company to my figures

### Current Work Satisfaction

I work 9-6 with a 1-hour lunch break. That is 8 hours a day (assuming I enjoy talking to work people). I work 5 days a week and luckily very rarely work overtime. So 40 hours of potential unhappiness?

Well, let's first talk about holiday. I get 25 days a year base, then I buy 8 additional days, and my company gives me 12 days off for university study. This means that 9 out of 52 weeks I am on holiday. That means I only work 40 × 43 ÷ 52 = 33 hours per week on average.

How much do I enjoy work? This is hard and very project-dependent. If I am writing code, I am normally pretty content, but that depends on the project. Right now I would say I am at about 0.7 on the unhappiness scale for work hours (with no real justification). So that makes the total: 23.1 hours of unhappiness per week, but it is variable.

![[Life graph.excalidraw]]

## Where do I want to go

OK, I think up until now maybe I haven't said anything really insightful - I hope the next bit is. As I said before, we want to map the function f that judges how happy I am at each point on this graph.

I am going to define 4 satisfaction levels:
- **Barely bearable**: Life is just about bearable, but I don't think fun is being had
- **Just fine**: Life is acceptable, nothing special
- **Good life**: Life is good, could coast most of my life like this  
- **Made it**: I have essentially made it at this point

![[Life graph contors.excalidraw]]

>[!warning] These are just gut feelings
>I really do wonder if someone offered me the "made it" line if I would take it... I think I would, but I think you only know when the chips are down.

Some things I intuitively think should be true about these satisfaction curves:
- **More pay for same unhappiness = better**: If you are paid more for the same amount of unenjoyable hours, that is better
- **Less unhappiness for same pay = better**: If you spend fewer hours not enjoying yourself for the same pay, that is better  
- **Diminishing returns**: The gradient should increase - as you get hit with more unhappiness, each additional hour of unhappiness should command a higher price

Some things that are maybe just true for me:
- I think I have a cutoff at about 45 hours of unhappiness per week. At that point, no amount of additional money really makes much difference
- If I don't have to work but still get an income, I could really cut down on life expenses
- If I don't have to work, I don't think it will take much money to make me happy
- If I halved my pay but also halved the amount of stuff I don't enjoy doing, that might be worthwhile
- I am doing pretty well right now... I should probably not stress and chill out a bit

## What does this tell me

I think there are two main takeaways from this framework:

1. **Evaluate trade-offs carefully**: If taking a promotion gives me an extra £1k post-tax monthly income but requires another 5 hours per week of work that I hate... don't do it. It's not worth it. Similarly, if a project is really high-profile (so the bonus is good) but means working with a team that sucks... don't do it.

2. **Retirement doesn't require massive wealth**: When I am retired, I won't need that much money. Not having to work means my hobbies are cheap and I can cut down on lifestyle expenses.

## Thoughts on FIRE

I like the idea of FIRE (Financial Independence, Retire Early), but I think *The 4-Hour Work Week* has a better approach. Instead of grinding all your time when you are young, relatively responsibility-free, and have energy to earn money for your older self - why not take breaks and spend that money when you are younger? 

Doesn't a year doing what you want sound good? What did your older self (who you don't even know will be around) do to deserve so much money?

When people used to not save at all for retirement, I agree it was an issue. But now retirement savings are so baked into most salaried work that I don't think the old version of me deserves quite so much sacrifice from the current me.
