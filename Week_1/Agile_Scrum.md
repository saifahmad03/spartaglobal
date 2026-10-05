# Agile & Scrum vs. Waterfall

## Waterfall

> The original, linear approach to full-scale projects. Involves heavy upfront planning to explore different strategies — once a direction is chosen, work proceeds step by step. Best suited to stable projects where customer needs can be identified early.

### Phases
`Requirements` → `Design` → `Implementation` → `Testing` → `Delivery`

| Advantages | Disadvantages |
|---|---|
| **Clear structure** — every phase has defined deliverables and milestones, making progress easy to track | **Inflexible to change** — late requirement changes are difficult and costly |
| **Predictable planning** — costs, timelines, and scope are estimated and locked in upfront | **Late testing** — bugs are found only after development finishes |
| **Strong documentation** — detailed records improve transparency and support long-term maintenance and compliance | **Delayed feedback** — stakeholders only see the final product at the end, risking misaligned expectations |

**Example use cases:** Construction and infrastructure · Enterprise software and regulated systems

---

## Agile & Scrum

> Agile is a flexible project management philosophy focused on continuous improvement and adapting quickly to change through collaboration. Scrum is a structured framework that puts Agile into practice using fixed, short work cycles (**sprints**) and defined team roles.

| Advantages | Disadvantages |
|---|---|
| **High flexibility** — adapts easily to changing market conditions or user requirements | **Less predictability** for final budgets, timelines, and launch dates |
| **Early risk detection** — issues are spotted and fixed during small, rapid iterations | **Higher risk of scope creep** — goals can constantly change |
| **Greater customer satisfaction** — continuous feedback and regular collaboration | |

---

## Quick comparison

| | Waterfall | Agile & Scrum |
|---|---|---|
| **Planning style** | Upfront, locked-in | Iterative, evolving |
| **Flexibility** | Low | High |
| **Feedback timing** | End of project | Every sprint |
| **Best for** | Stable, well-defined requirements | Changing or unclear requirements |
| **Risk** | Late-discovered bugs | Scope creep |


# Core Agile Values
- Individuals and interactions over processes and tools
- Working software over heavy paperwork
- Customer collaboration over strict contract talks
- Responding to change over following a rigid plan

---


<p align="center">
  <img src="https://scrumorg-website-prod.s3.amazonaws.com/drupal/inline-images/2023-09/scrum-framework-9.29.23.png" alt="Scrum sprint cycle diagram" width="600">
</p>


## The Scrum Cycle

1. **Refine the Product Backlog** — Keep a prioritized list of everything that could be built, guided by an overall Product Goal. Continually refine it so the top items stay clear and ready to work on.

2. **Sprint Planning** — At the start of a sprint, pull the highest-priority items off the Product Backlog and agree on a Sprint Goal: what the team intends to achieve by the end of this cycle.

3. **Build the Sprint Backlog** — Break the chosen work down into specific tasks needed to hit the Sprint Goal.

4. **Work the Sprint** — The Scrum Team (developers, a Scrum Master, and a Product Owner) does the actual work, syncing daily in a short Daily Scrum to check progress and clear blockers.

5. **Produce an Increment** — By the end of the sprint, the work should result in a usable Increment: a piece of the product that meets the team's Definition of Done.

6. **Sprint Review** — Show the Increment to stakeholders, gather feedback, and update the Product Backlog based on what was learned.

7. **Sprint Retrospective** — Before the next sprint, reflect on how the team worked together and agree on improvements to carry forward.

8. **Repeat** — Loop back into Sprint Planning. The cycle continues for the life of the project.

> It's a loop, not a straight line — each sprint's ending feeds directly into planning the next one.

## Scrum Team Roles

- **Product Owner** — Owns the Product Backlog and decides what gets built, prioritizing based on value to the business and customers.

- **Scrum Master** — Coaches the team on Scrum practices, removes blockers, and shields the team from outside distractions.

- **Developers** — The people doing the work of building the Increment each sprint, whatever their specific discipline (design, engineering, QA, etc.).

## The 3 Pillars of Scrum

- **Transparency** — Work and progress are visible to everyone involved, so decisions are made on shared, accurate information.

- **Inspection** — Progress toward the Sprint Goal and product quality are checked frequently, catching problems early.

- **Adaptation** — When inspection reveals something's off, the process or the product is adjusted quickly rather than waiting until it's too late.

## Functional vs. Non-Functional Requirements

- **Functional Requirements** — What the system should *do*. Specific features, actions, and behaviors (e.g. "users can reset their password," "the app sends a confirmation email").

- **Non-Functional Requirements** — How the system should *behave* while doing it. Qualities like speed, security, reliability, and usability (e.g. "the page must load in under 2 seconds," "the system must support 10,000 concurrent users"). Security, Reliability, Performance

**The simple difference:** functional requirements describe the *features*, non-functional requirements describe the *standards those features have to meet*.

## User Story Structure

A user story is a short, plain-language description of a feature from the end user's perspective. The standard template is:

> **As a** [type of user], **I want** [some goal], **so that** [some reason/benefit].

- **As a** — who is asking for the feature (the role or persona)
- **I want** — what they're trying to do (the goal)
- **so that** — why it matters to them (the value or motivation)

### Example

> **As a** returning customer, **I want** to save my payment details, **so that** I can check out faster next time.

### Often paired with Acceptance Criteria

These define when the story is "done" — the specific, testable conditions it must meet.

```
Given I am a logged-in customer
When I choose to save my card during checkout
Then my payment details are securely stored for future orders
```

## MoSCoW Prioritization

A simple way to sort requirements or backlog items into four priority buckets:

- **Must have** — Non-negotiable. Without this, the product doesn't work or fails to meet a critical need.

- **Should have** — Important, but not vital. The product still works without it, though it's a notable gap.

- **Could have** — Nice to have. Small improvements that add value but have low impact if left out.

- **Won't have (this time)** — Explicitly out of scope for now. Agreed to be excluded, but may be reconsidered later.

**The simple idea:** it forces hard conversations about trade-offs upfront, so "everything is a priority" doesn't happen.

## Definition of Ready vs. Definition of Done

- **Definition of Ready (DoR)** — The checklist a backlog item must meet *before* it's pulled into a sprint. Ensures the team isn't starting work on something vague, unclear, or missing key details (e.g. requirements are clear, acceptance criteria are defined, dependencies are identified).

- **Definition of Done (DoD)** — The checklist a piece of work must meet *before* it's considered complete. Ensures consistent quality across the team (e.g. code is tested, reviewed, documented, and deployed).

**The simple difference:** Definition of Ready is the entry gate into a sprint; Definition of Done is the exit gate out of it.