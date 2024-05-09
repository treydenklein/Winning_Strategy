# Introduction

The Monty Hall Problem is a famous probability puzzle named after Monty Hall, the original host of the game show "Let's Make a Deal". The problem can be described as follows:

**1.** You are a contestant on a game show, and you are presented with three doors 🚪🚪🚪.

**2.** Behind one of the doors is a prize (like a car 🚗), and behind the other two are "zonks" (like donkeys 🫏).

**3.** You choose one of the doors, let's say Door 1.

**4.** The host, who knows where the prize is, then opens another door, let's say Door 3, which reveals a zonk (a donkey).

**5.** Now, you are given a choice: stick with your original choice (Door 1), or switch to the remaining unopened door (Door 2).

**Now, the question is: what should you do to maximize your chances of winning the prize?**

# Solution

The correct answer is that you should **accept the offer and switch doors...**

- Making the switch gives you a **66.667%** chance of winning
- Sticking with your original choice leaves you with a **33.333%** chance

Although it might seem counterintuitive at first, the reason behind this solution is that when you switch, you benefit from the information provided by the host's action of opening a door with a zonk.

Essentially, switching allows you to "double" your chances of winning.

# Explanations

### 1. Simple Explanation

Below are all possible arrangements of having one prize and two donkeys behind three doors, and the result of staying or switching after initially picking Door #1 in each case:

<div align='center'>

|  Door #1  |  Door #2  |  Door #3  | Result from Staying | Result from Switching |
| :-------: | :-------: | :-------: | :-----------------: | :-------------------: |
|  Donkey   |  Donkey   | **Prize** |     Win Donkey      |     **Win Prize**     |
|  Donkey   | **Prize** |  Donkey   |     Win Donkey      |     **Win Prize**     |
| **Prize** |  Donkey   |  Donkey   |    **Win Prize**    |      Win Donkey       |

</div>

A player who sticks with their original choice wins in just one of three equally probable scenarios, while a player who switches wins in two out of three cases.

If the contestant initially picks a donkey (2 of 3 doors), the contestant **_will_** win the prize by switching because the other donkey can no longer be picked, as the host had to reveal its location. However, if the contestant initially chooses the prize (1 of 3 doors), they **_will not_** win by switching.

So, by using the strategy to always make the switch, winning or losing **only** depends on whether the contestant has initially chosen a donkey ($\frac{2}{3}$ probability) or the prize ($\frac{1}{3}$ probability).

The fact that the host subsequently reveals a donkey behind one of the unchosen doors changes nothing about the initial probability.

### 2. Bayes' Theorem and Conditional Probability

**Conditional Probability** is a measure of the probability that an event occurs, given that another event has also occurred. This can be calculated using the formula:

<div align='center'>

$\huge{P(A \mid B) = \frac{P(A \cap B)}{P(B)}}$

</div>

where:

- $P(A \mid B)$ is the probability of event $A$ occurring given that event $B$ has occurred.
- $P(A \cap B)$ is the probability of both $A$ and $B$ occurring.
- $P(B)$ is the probability of event $B$ occurring.
- $P(B)$ is assumed to **not** be zero, as division by zero is undefined.
