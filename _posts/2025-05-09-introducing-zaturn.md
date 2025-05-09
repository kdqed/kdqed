---
cover_image: zaturn.webp
title: "Introducing Zaturn: Data Analysis With Vibes"
permalink: zaturn
schema_type: NewsArticle
---
The concept of vibe coding (using AI to generate code) has been doing the rounds online lately. I gave it a try but, to be honest, I wasn't happy with the output. The first problem is hallucination: AI uses libraries that don't even exist and generates hundreds of lines of code using those libraries. It all looks neat until you run it. Second, the code is very verbose and lengthy, often including features I didn't ask for. As a human owning the generated code, it would be me who has to understand, review, maintain, and update the code, and be responsible for its actions. Every line of code is a liability and only the useful functionalities are assets. And it is very important to consciously avoid tech debt from day zero. While all of this is completely achievable with AI, it takes time. For someone who knows programming and sees it as a language to instruct a computer, hiring an AI translator feels redundant.

However, I did not notice one use-case for vibe coding where I'd liberally use it: small scripts that will be used one time, with immediate output. In these cases, the verbosity or elegance of the code does not matter. The code just needs to work, and if it doesn't I will know immediately and ask AI to rewrite it. Now, what are these use-cases? Scraping, resizing my photos, writing SQL queries to work with data, data visualizations and so on.

At this point, I was also tinkering the concept of MCP Servers. They're like plugins to your AI chatbots, i.e., a set of tools AI can use on your behalf. For example, there is a WhatsApp MCP and now you can ask Claude to reply to your ex, if you don't want to. And for those like me who passionately hate the graphical user interfaces of popular consumer services like Instagram or Google Maps, a chat based interface opens up so many possibilities.

With data, I've used tools like Metabase which allow linking multiple data sources to instantly view some tables and charts from the data sources. But what if I could link multiple data sources to an AI chatbot and just have the AI talk to my data? With MCP, this was simple. I made an MCP called [Zaturn](https://github.com/kdqed/zaturn) which essentially equips the AI with the following tools:

- View linked data sources and the table structures in them
- Run SQL queries on these sources
- Make visualizations with the query results

Now, AI can just use these tools to explore your dataset. Anybody can analyze their data with just vibes:

- Who is my most valuable customer?
- Why are my users churning?
- In Bangalore, what time of the day is it most likely to rain in June?
- Visualize the correlation between strength and legendary status in the Pokemon dataset.

Chatbots with Zaturn will take these kind of questions, use SQL to get answers from the linked datasets, and give you answers with numbers and plots. The possibilities are now limited only by the data you can procure. Here's a brief video demo:

<iframe width="560" height="315" src="https://www.youtube.com/embed/au2uBfrqlec?si=7uko6SdLVX0Y9_iN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


What next?

- More data sources
- More visualizations
- Native UI for Zaturn
- Predictive analysis

[Try Zaturn Today](https://github.com/zaturn/kdqed)
